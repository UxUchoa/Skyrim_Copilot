export type ChatFilePayload = {
  upload_file_id: string
  type: 'image'
  transfer_method: 'local_file'
}

export type UploadedFileResponse = {
  upload_file_id: string
  name: string | null
  size: number | null
  mime_type: string | null
}

type StreamChatPayload = {
  query: string
  conversation_id: string | null
  user: string
  files: ChatFilePayload[]
}

type StreamChatHandlers = {
  onConversationId?: (conversationId: string) => void
  onMessage?: (chunk: string, conversationId?: string | null) => void
  onEnd?: (conversationId?: string | null) => void
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000'

export async function uploadImage(file: File, user: string): Promise<UploadedFileResponse> {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('user', user)

  const response = await fetch(`${API_BASE_URL}/api/files/upload`, {
    method: 'POST',
    body: formData,
  })

  if (!response.ok) {
    throw new Error(await readApiError(response, 'Image upload failed.'))
  }

  return response.json()
}

export async function streamChat(
  payload: StreamChatPayload,
  handlers: StreamChatHandlers,
): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/api/chat/stream`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Accept: 'text/event-stream',
    },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    throw new Error(await readApiError(response, 'Chat request failed.'))
  }

  if (!response.body) {
    throw new Error('Streaming is not supported in this browser.')
  }

  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffer = ''

  while (true) {
    const { done, value } = await reader.read()
    if (done) break

    buffer += decoder.decode(value, { stream: true })
    const rawEvents = buffer.split('\n\n')
    buffer = rawEvents.pop() ?? ''

    for (const rawEvent of rawEvents) {
      handleSseEvent(rawEvent, handlers)
    }
  }

  if (buffer.trim()) {
    handleSseEvent(buffer, handlers)
  }
}

function handleSseEvent(rawEvent: string, handlers: StreamChatHandlers) {
  const lines = rawEvent.split('\n')
  const eventLine = lines.find((line) => line.startsWith('event: '))
  const dataLine = lines.find((line) => line.startsWith('data: '))

  if (!eventLine || !dataLine) return

  const eventName = eventLine.replace('event: ', '').trim()
  const payload = JSON.parse(dataLine.replace('data: ', ''))

  if (eventName === 'conversation_id' && payload.conversation_id) {
    handlers.onConversationId?.(payload.conversation_id)
    return
  }

  if (eventName === 'agent_message') {
    handlers.onMessage?.(payload.answer ?? '', payload.conversation_id)
    return
  }

  if (eventName === 'message_end') {
    handlers.onEnd?.(payload.conversation_id)
    return
  }

  if (eventName === 'error') {
    throw new Error(payload.message ?? 'Dify stream error.')
  }
}

async function readApiError(response: Response, fallback: string): Promise<string> {
  const text = await response.text()
  if (!text) return fallback

  try {
    const payload = JSON.parse(text)
    return payload.detail ?? payload.message ?? fallback
  } catch {
    return text
  }
}
