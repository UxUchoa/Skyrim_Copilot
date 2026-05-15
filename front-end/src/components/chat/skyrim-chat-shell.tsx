import { type FormEvent, useEffect, useRef, useState } from 'react'
import { HugeiconsIcon } from '@hugeicons/react'
import {
  AiMagicIcon,
  BookOpen02Icon,
  ImageUploadIcon,
  Menu03Icon,
  QuillWrite01Icon,
  ScrollIcon,
  SentIcon,
  SparklesIcon,
  Sword02Icon,
} from '@hugeicons/core-free-icons'

import { Button } from '@/components/ui/button'
import { Card } from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { ScrollArea } from '@/components/ui/scroll-area'
import { streamChat, type ChatFilePayload, type UploadedFileResponse, uploadImage } from '@/lib/skyrim-api'
import { cn } from '@/lib/utils'

const chats = [
  'Dwemer ruins and tonal locks',
  'Best herbs near Whiterun',
  'Daedric artifacts index',
  'College of Winterhold lore',
]

type ChatMessage = {
  id: string
  role: 'assistant' | 'user'
  title: string
  content: string
  files?: UploadedFileResponse[]
  status?: 'streaming' | 'error'
}

const INITIAL_MESSAGES: ChatMessage[] = [
  {
    id: 'welcome',
    role: 'assistant',
    title: 'Skyrim Codex',
    content:
      'Ask about factions, quests, alchemy, artifacts, regions, or obscure book lore. I will answer like a living archive of Tamrielic knowledge.',
  },
]

const CHAT_USER = 'lucas'

export function SkyrimChatShell() {
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [messages, setMessages] = useState<ChatMessage[]>(INITIAL_MESSAGES)
  const [input, setInput] = useState('')
  const [conversationId, setConversationId] = useState<string | null>(null)
  const [uploadedFiles, setUploadedFiles] = useState<UploadedFileResponse[]>([])
  const [isSending, setIsSending] = useState(false)
  const [isUploading, setIsUploading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const fileInputRef = useRef<HTMLInputElement | null>(null)
  const messagesEndRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth', block: 'end' })
  }, [messages])

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()

    const query = input.trim()
    if (!query || isSending || isUploading) return

    const filesForRequest = uploadedFiles.map(toChatFilePayload)
    const userMessageId = crypto.randomUUID()
    const assistantMessageId = crypto.randomUUID()

    setError(null)
    setInput('')
    setUploadedFiles([])
    setIsSending(true)
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        id: userMessageId,
        role: 'user',
        title: 'Dragonborn',
        content: query,
        files: uploadedFiles,
      },
      {
        id: assistantMessageId,
        role: 'assistant',
        title: 'Skyrim Codex',
        content: '',
        status: 'streaming',
      },
    ])

    try {
      await streamChat(
        {
          query,
          conversation_id: conversationId,
          user: CHAT_USER,
          files: filesForRequest,
        },
        {
          onConversationId: (nextConversationId) => {
            setConversationId(nextConversationId)
          },
          onMessage: (chunk, nextConversationId) => {
            if (nextConversationId) {
              setConversationId(nextConversationId)
            }

            setMessages((currentMessages) =>
              currentMessages.map((message) =>
                message.id === assistantMessageId
                  ? { ...message, content: message.content + chunk }
                  : message,
              ),
            )
          },
          onEnd: (nextConversationId) => {
            if (nextConversationId) {
              setConversationId(nextConversationId)
            }
          },
        },
      )

      setMessages((currentMessages) =>
        currentMessages.map((message) =>
          message.id === assistantMessageId
            ? {
                ...message,
                content: message.content || 'No answer was returned by the archive.',
                status: undefined,
              }
            : message,
        ),
      )
    } catch (streamError) {
      const message = streamError instanceof Error ? streamError.message : 'Chat stream failed.'
      setError(message)
      setMessages((currentMessages) =>
        currentMessages.map((chatMessage) =>
          chatMessage.id === assistantMessageId
            ? {
                ...chatMessage,
                content: message,
                status: 'error',
              }
            : chatMessage,
        ),
      )
    } finally {
      setIsSending(false)
    }
  }

  async function handleFileSelected(file: File | undefined) {
    if (!file) return

    if (!file.type.startsWith('image/')) {
      setError('Only image uploads are supported.')
      return
    }

    setError(null)
    setIsUploading(true)

    try {
      const uploaded = await uploadImage(file, CHAT_USER)
      setUploadedFiles((currentFiles) => [...currentFiles, uploaded])
    } catch (uploadError) {
      setError(uploadError instanceof Error ? uploadError.message : 'Image upload failed.')
    } finally {
      setIsUploading(false)
      if (fileInputRef.current) {
        fileInputRef.current.value = ''
      }
    }
  }

  function clearConversation() {
    setMessages(INITIAL_MESSAGES)
    setInput('')
    setConversationId(null)
    setUploadedFiles([])
    setError(null)
  }

  return (
    <main className="min-h-dvh overflow-hidden bg-background text-foreground">
      <div className="flex h-dvh bg-[radial-gradient(circle_at_top,oklch(0.84_0.055_82_/_0.55),transparent_34%),linear-gradient(135deg,oklch(0.25_0.025_68),oklch(0.15_0.011_72)_42%,oklch(0.22_0.028_42))] p-2 text-left sm:p-4">
        <aside
          className={cn(
            'hidden shrink-0 overflow-hidden rounded-2xl border border-sidebar-border bg-sidebar text-sidebar-foreground shadow-2xl shadow-black/35 transition-all duration-300 md:flex md:flex-col',
            sidebarOpen ? 'w-80' : 'w-20',
          )}
        >
          <div className="flex items-center gap-3 border-b border-sidebar-border p-4">
            <div className="grid size-11 place-items-center rounded-xl border border-primary/35 bg-primary/15 text-primary">
              <HugeiconsIcon icon={Sword02Icon} size={24} strokeWidth={1.8} />
            </div>
            {sidebarOpen && (
              <div>
                <p className="font-heading text-lg tracking-[0.18em] text-sidebar-foreground uppercase">
                  Skyrim AI
                </p>
                <p className="text-xs text-sidebar-foreground/60">Archive of the north</p>
              </div>
            )}
          </div>

          <div className="p-3">
            <Button
              className="h-11 w-full justify-start gap-3 border-primary/25 bg-primary/15 text-primary hover:bg-primary/25"
              onClick={clearConversation}
              type="button"
              variant="outline"
            >
              <HugeiconsIcon icon={ScrollIcon} size={19} />
              {sidebarOpen && <span>New scroll</span>}
            </Button>
          </div>

          <ScrollArea className="min-h-0 flex-1 px-3 pb-4">
            <div className="space-y-2">
              {chats.map((chat) => (
                <button
                  className="flex w-full items-center gap-3 rounded-xl border border-transparent px-3 py-3 text-left text-sm text-sidebar-foreground/72 transition hover:border-sidebar-border hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
                  key={chat}
                  type="button"
                >
                  <HugeiconsIcon className="shrink-0" icon={BookOpen02Icon} size={18} />
                  {sidebarOpen && <span className="truncate">{chat}</span>}
                </button>
              ))}
            </div>
          </ScrollArea>
        </aside>

        <section className="flex min-w-0 flex-1 flex-col rounded-2xl border border-border bg-background/95 shadow-2xl shadow-black/35 backdrop-blur">
          <header className="flex items-center justify-between border-b border-border bg-card/80 px-4 py-3 sm:px-6">
            <div className="flex items-center gap-3">
              <Button
                aria-label="Toggle chat history"
                aria-pressed={sidebarOpen}
                className="text-muted-foreground hover:text-foreground"
                onClick={() => setSidebarOpen((open) => !open)}
                size="icon"
                type="button"
                variant="ghost"
              >
                <HugeiconsIcon icon={Menu03Icon} size={22} />
              </Button>
              <div>
                <p className="font-heading text-xl tracking-[0.08em] text-foreground uppercase sm:text-2xl">
                  The Elder Codex
                </p>
                <p className="text-xs text-muted-foreground sm:text-sm">
                  Skyrim wiki knowledge base interface
                </p>
              </div>
            </div>
            <div className="hidden items-center gap-2 rounded-full border border-border bg-muted px-3 py-1 text-xs text-muted-foreground sm:flex">
              <HugeiconsIcon icon={AiMagicIcon} size={16} />
              {conversationId ? 'Context linked' : 'New conversation'}
            </div>
          </header>

          <ScrollArea className="min-h-0 flex-1">
            <div className="mx-auto flex w-full max-w-4xl flex-col gap-5 px-4 py-6 sm:px-8 lg:py-10">
              <Card className="border-primary/20 bg-card/75 p-5 shadow-lg shadow-primary/5 sm:p-7">
                <div className="flex gap-4">
                  <div className="grid size-12 shrink-0 place-items-center rounded-2xl border border-primary/25 bg-primary/15 text-primary">
                    <HugeiconsIcon icon={SparklesIcon} size={25} />
                  </div>
                  <div>
                    <h1 className="font-heading text-3xl leading-tight tracking-[0.08em] uppercase sm:text-5xl">
                      Ask the Greybeard Archive
                    </h1>
                    <p className="mt-3 max-w-2xl text-sm leading-7 text-muted-foreground sm:text-base">
                      A parchment-styled ChatGPT layout for exploring Skyrim lore, item details,
                      quest hints, creatures, and historical records.
                    </p>
                  </div>
                </div>
              </Card>

              {messages.map((message) => (
                <article
                  className={cn(
                    'flex gap-3 sm:gap-4',
                    message.role === 'user' && 'flex-row-reverse',
                  )}
                  key={message.id}
                >
                  <div
                    className={cn(
                      'grid size-10 shrink-0 place-items-center rounded-xl border',
                      message.role === 'user'
                        ? 'border-primary/30 bg-primary text-primary-foreground'
                        : 'border-border bg-muted text-muted-foreground',
                    )}
                  >
                    <HugeiconsIcon
                      icon={message.role === 'user' ? QuillWrite01Icon : ScrollIcon}
                      size={20}
                    />
                  </div>
                  <Card
                    className={cn(
                      'max-w-[78ch] border p-4 leading-7 shadow-sm sm:p-5',
                      message.role === 'user'
                        ? 'border-primary/25 bg-primary/10'
                        : 'border-border bg-card/90',
                    )}
                  >
                    <p className="font-heading text-sm tracking-[0.12em] text-foreground uppercase">
                      {message.title}
                    </p>
                    {message.files?.length ? (
                      <div className="mt-3 flex flex-wrap gap-2">
                        {message.files.map((file) => (
                          <span
                            className="rounded-lg border border-primary/20 bg-primary/10 px-2.5 py-1 text-xs text-primary"
                            key={file.upload_file_id}
                          >
                            {file.name ?? 'Uploaded image'}
                          </span>
                        ))}
                      </div>
                    ) : null}
                    <p
                      className={cn(
                        'mt-2 whitespace-pre-wrap text-sm text-muted-foreground sm:text-base',
                        message.status === 'error' && 'text-destructive',
                      )}
                    >
                      {message.content}
                      {message.status === 'streaming' && (
                        <span className="ml-1 inline-block animate-pulse text-primary">|</span>
                      )}
                    </p>
                  </Card>
                </article>
              ))}
              <div ref={messagesEndRef} />
            </div>
          </ScrollArea>

          <footer className="border-t border-border bg-card/90 p-3 sm:p-5">
            <div className="mx-auto max-w-4xl">
              <Card className="overflow-hidden border-primary/20 bg-background/85 p-3 shadow-xl shadow-black/10">
                <button
                  className="mb-3 flex w-full items-center gap-3 rounded-xl border border-dashed border-primary/35 bg-primary/10 px-4 py-3 text-left text-primary transition hover:bg-primary/15 disabled:cursor-not-allowed disabled:opacity-70"
                  disabled={isSending || isUploading}
                  onClick={() => fileInputRef.current?.click()}
                  type="button"
                >
                  <HugeiconsIcon icon={ImageUploadIcon} size={22} />
                  <div className="min-w-0">
                    <p className="text-sm font-medium">
                      {isUploading
                        ? 'Uploading image...'
                        : uploadedFiles.length
                          ? `${uploadedFiles.length} image${uploadedFiles.length > 1 ? 's' : ''} attached`
                          : 'Attach image'}
                    </p>
                    <p className="truncate text-xs text-primary/75">
                      {uploadedFiles.map((file) => file.name ?? 'Uploaded image').join(', ') ||
                        'Screenshots are uploaded before the next message.'}
                    </p>
                  </div>
                </button>
                <input
                  accept="image/*"
                  className="hidden"
                  onChange={(event) => handleFileSelected(event.target.files?.[0])}
                  ref={fileInputRef}
                  type="file"
                />
                <form className="flex items-center gap-2" onSubmit={handleSubmit}>
                  <Input
                    aria-label="Ask about Skyrim"
                    className="h-12 border-border bg-muted/60 px-4 text-base placeholder:text-muted-foreground/70"
                    disabled={isSending}
                    onChange={(event) => setInput(event.target.value)}
                    placeholder="Ask about a quest, hold, artifact, creature, or book..."
                    value={input}
                  />
                  <Button
                    className="h-12 gap-2 bg-primary px-4 text-primary-foreground hover:bg-primary/90 sm:px-5"
                    disabled={!input.trim() || isSending || isUploading}
                    type="submit"
                  >
                    <HugeiconsIcon icon={SentIcon} size={20} />
                    <span className="hidden sm:inline">{isSending ? 'Sending' : 'Send'}</span>
                  </Button>
                </form>
                {error && <p className="mt-3 text-sm text-destructive">{error}</p>}
              </Card>
            </div>
          </footer>
        </section>
      </div>
    </main>
  )
}

function toChatFilePayload(file: UploadedFileResponse): ChatFilePayload {
  return {
    upload_file_id: file.upload_file_id,
    type: 'image',
    transfer_method: 'local_file',
  }
}
