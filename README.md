# Skyrim Copilot

Chat local sobre o universo de Skyrim usando **Frontend React**, **Backend
FastAPI**, **Dify** e **Ollama**.

O frontend nunca conversa direto com o Dify. Ele chama o backend local em
`http://localhost:8000`, e o backend repassa a mensagem para o Dify usando a
API key guardada no `.env`.

## Arquitetura

```text
React/Vite (front-end)
  -> FastAPI (backend/api)
  -> Dify (infra/dify/docker)
  -> Ollama no Windows host
```

Servicos locais:

- **Frontend:** `http://localhost:5173`
- **Backend:** `http://localhost:8000`
- **Backend Swagger:** `http://localhost:8000/docs`
- **Dify UI:** `http://localhost`
- **Ollama:** `http://localhost:11434`

## Pre-requisitos

Instale uma vez:

- Docker Desktop com WSL 2 backend.
- Python 3.11+.
- Node.js 20+ com `npm`.
- Ollama.

## Setup Inicial

Execute na raiz do projeto.

### 1. Criar ambiente Python

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Se o PowerShell bloquear o activate:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois tente ativar de novo.

### 2. Instalar dependencias do frontend

```powershell
cd front-end
npm install
cd ..
```

### 3. Configurar `.env`

Copie `.env.example` para `.env` e preencha `DIFY_API_KEY` depois de criar o
app no Dify.

Valores principais:

```env
API_CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
DIFY_BASE_URL=http://localhost:80
DIFY_API_KEY=app-sua-chave-do-dify
DIFY_DEFAULT_USER=skyrim-copilot-local
DIFY_LLM_PROVIDER=ollama
DIFY_LLM_MODEL=qwen3:8b
DIFY_EMBEDDING_PROVIDER=ollama
DIFY_EMBEDDING_MODEL=bge-m3
```

Importante: `DIFY_LLM_MODEL` aparece no `GET /api/health`, mas quem escolhe o
modelo real do chat e o app dentro do Dify. Se o Dify estiver configurado com
`qwen3:14b`, ele vai chamar o 14b mesmo que o `.env` diga `qwen3:8b`.

### 4. Baixar os modelos no Ollama

```powershell
ollama pull qwen3:8b
ollama pull bge-m3
```

Recomendado para evitar descarregar modelo a cada poucos minutos:

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_KEEP_ALIVE", "-1", "User")
```

Reinicie o Ollama pelo tray depois disso.

### 5. Configurar Flash Attention para o embedding

O `bge-m3` pode falhar no Ollama com Flash Attention ligado. Configure uma vez:

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_FLASH_ATTENTION", "0", "User")
```

Depois encerre o Ollama pelo tray e abra de novo.

## Configurando o Dify

Suba o Dify primeiro:

```powershell
docker compose -f infra/dify/docker/docker-compose.yaml up -d
```

Abra:

```text
http://localhost
```

### 1. Criar conta admin

Na primeira vez, abra:

```text
http://localhost/install
```

Crie a conta admin.

### 2. Cadastrar Ollama no Dify

No Dify:

```text
Settings -> Model Providers -> Ollama
```

Configure:

- LLM: `qwen3:8b`
- Text Embedding: `bge-m3`
- Base URL dos dois: `http://host.docker.internal:11434`

Para caber melhor em VRAM, edite o `qwen3:8b` e use:

- **Model context size:** `4096` ou `8192`
- **Upper bound for max tokens:** `2048`

Depois confirme:

```powershell
ollama ps
```

O ideal e aparecer `qwen3:8b` como `100% GPU`. Se aparecer CPU/GPU dividido,
reduza o context size para `4096`.

### 3. Criar ou selecionar a Knowledge

No Dify:

```text
Knowledge -> Create Knowledge
```

Importe os arquivos de conhecimento do projeto, aguarde a indexacao terminar e
confirme que os documentos ficaram como **Disponivel**.

### 4. Criar o app de chat

No Dify:

```text
Studio -> Create App -> Chatbot (Basic)
```

Nome sugerido:

```text
Skyrim Copilot
```

Dentro do app:

1. No seletor de modelo do canto superior direito, escolha `qwen3:8b`.
2. Em **Knowledge**, clique em **+ Add** e selecione a Knowledge criada.
3. Em **Instructions**, cole:

   ```text
   /no_think

   You are a Skyrim lore expert. Answer using ONLY the provided knowledge base,
   in the same language the user writes. If you don't know, say so. Do not
   invent details outside the context.
   ```

4. Clique em **Publish -> Update**.

`/no_think` e importante porque o `qwen3` pode responder primeiro com
`<think>...</think>`. Com essa flag, a resposta fica limpa para o frontend.

### 5. Gerar API key do app

No app:

```text
API Access -> API Key -> Create secret key
```

Copie a chave que comeca com `app-` e cole no `.env`:

```env
DIFY_API_KEY=app-sua-chave-aqui
```

Reinicie o backend depois de editar `.env`.

## Rodando o Projeto

Use 3 terminais.

### Terminal 1: Dify

Abra o Docker Desktop e espere ficar rodando. Depois:

```powershell
docker compose -f infra/dify/docker/docker-compose.yaml start
```

Se for a primeira vez ou se voce deu `down` antes:

```powershell
docker compose -f infra/dify/docker/docker-compose.yaml up -d
```

### Terminal 2: Backend

```powershell
.\.venv\Scripts\Activate.ps1
python -m uvicorn backend.api.main:app --reload --env-file .env
```

Teste:

```text
http://localhost:8000/api/health
```

Resposta esperada:

```json
{
  "status": "ok",
  "dify_configured": true,
  "dify_base_url": "http://localhost:80",
  "dify_llm_model": "qwen3:8b",
  "dify_embedding_model": "bge-m3"
}
```

Se `dify_configured` vier `false`, falta `DIFY_API_KEY` no `.env`.

### Terminal 3: Frontend

```powershell
cd front-end
npm run dev
```

Abra:

```text
http://localhost:5173
```

## Como o Frontend Deve Chamar o Backend

O frontend deve chamar somente o backend FastAPI:

```text
http://localhost:8000
```

Nao coloque a API key do Dify no frontend.

### Health

```http
GET /api/health
```

Uso:

```ts
const response = await fetch('http://localhost:8000/api/health')
const data = await response.json()
```

### Chat streaming

Endpoint:

```http
POST /api/chat/stream
```

Body da primeira mensagem:

```json
{
  "query": "Quem sao os Greybeards em Skyrim?",
  "conversation_id": null,
  "user": "lucas",
  "files": []
}
```

Regras:

- Na primeira mensagem, envie `conversation_id: null`.
- Nas proximas mensagens, reuse o `conversation_id` retornado pelo backend.
- Nunca envie `"conversation_id": "string"`.
- `files` pode ficar como `[]` enquanto upload nao estiver sendo usado.

O retorno e SSE:

```text
event: conversation_id
data: {"conversation_id":"..."}

event: agent_message
data: {"answer":"Os Greybeards","conversation_id":"...","message_id":"..."}

event: agent_message
data: {"answer":" sao mestres","conversation_id":"...","message_id":"..."}

event: message_end
data: {"conversation_id":"...","message_id":"...","metadata":{...}}
```

O frontend precisa concatenar cada `data.answer` dos eventos
`agent_message` para montar a resposta final.

Exemplo simples de consumo no browser:

```ts
const response = await fetch('http://localhost:8000/api/chat/stream', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    Accept: 'text/event-stream',
  },
  body: JSON.stringify({
    query: 'Quem sao os Greybeards em Skyrim?',
    conversation_id: null,
    user: 'lucas',
    files: [],
  }),
})

if (!response.body) {
  throw new Error('Streaming nao suportado neste browser.')
}

const reader = response.body.getReader()
const decoder = new TextDecoder()
let buffer = ''
let answer = ''
let conversationId: string | null = null

while (true) {
  const { done, value } = await reader.read()
  if (done) break

  buffer += decoder.decode(value, { stream: true })
  const events = buffer.split('\n\n')
  buffer = events.pop() ?? ''

  for (const rawEvent of events) {
    const eventLine = rawEvent.split('\n').find((line) => line.startsWith('event: '))
    const dataLine = rawEvent.split('\n').find((line) => line.startsWith('data: '))
    if (!eventLine || !dataLine) continue

    const eventName = eventLine.replace('event: ', '').trim()
    const payload = JSON.parse(dataLine.replace('data: ', ''))

    if (eventName === 'conversation_id') {
      conversationId = payload.conversation_id
    }

    if (eventName === 'agent_message') {
      answer += payload.answer ?? ''
      // Atualize o estado React aqui:
      // setAssistantMessage(answer)
    }

    if (eventName === 'error') {
      throw new Error(payload.message)
    }
  }
}
```

### Continuar uma conversa

Depois da primeira chamada, salve o `conversation_id`:

```json
{
  "query": "E qual o papel deles na historia principal?",
  "conversation_id": "4b624ea4-f786-4d9e-baa3-44a214d22c44",
  "user": "lucas",
  "files": []
}
```

### Upload de imagem

Endpoint:

```http
POST /api/files/upload
```

Formato:

- `multipart/form-data`
- Campo `file`: imagem
- Campo `user`: opcional

Resposta:

```json
{
  "upload_file_id": "...",
  "name": "image.png",
  "size": 12345,
  "mime_type": "image/png"
}
```

Depois envie no chat:

```json
{
  "query": "Analise esta imagem no contexto de Skyrim.",
  "conversation_id": null,
  "user": "lucas",
  "files": [
    {
      "upload_file_id": "ID_DO_UPLOAD",
      "type": "image",
      "transfer_method": "local_file"
    }
  ]
}
```

## Testando a API Sem o Front

### Swagger

Abra:

```text
http://localhost:8000/docs
```

Use `POST /api/chat/stream`.

Observacao: o Swagger nao mostra SSE token a token; ele pode parecer loading
por bastante tempo e so exibir quando a resposta fechar.

### PowerShell

```powershell
curl.exe -N -X POST "http://localhost:8000/api/chat/stream" `
  -H "Content-Type: application/json" `
  -H "Accept: text/event-stream" `
  --data-binary "{\"query\":\"Quem sao os Greybeards?\",\"conversation_id\":null,\"user\":\"lucas\",\"files\":[]}"
```

### Insomnia

Mais seguro: crie a request importando cURL.

```bash
curl -N -X POST "http://localhost:8000/api/chat/stream" \
  -H "Content-Type: application/json" \
  -H "Accept: text/event-stream" \
  -d '{"query":"Quem sao os Greybeards?","conversation_id":null,"user":"lucas","files":[]}'
```

Se configurar manualmente:

- Method: `POST`
- URL: `http://localhost:8000/api/chat/stream`
- Body: `JSON`
- Header: `Accept: text/event-stream`
- Nao envie o JSON como string. O body precisa comecar direto com `{`.

## Estrutura

```text
backend/api/       FastAPI, rotas, schemas e cliente Dify
front-end/         React + Vite + Tailwind
infra/dify/docker/ Docker Compose do Dify
tests/             Testes do backend/API
```

## Scripts Uteis

Backend:

```powershell
python -m uvicorn backend.api.main:app --reload --env-file .env
python -m pytest
```

Frontend:

```powershell
cd front-end
npm run dev
npm run build
npm run lint
```

Infra:

```powershell
docker compose -f infra/dify/docker/docker-compose.yaml start
docker compose -f infra/dify/docker/docker-compose.yaml stop
docker ps --format "table {{.Names}}\t{{.Status}}"
ollama ps
```

## Desligando

1. Pare o frontend com `Ctrl+C`.
2. Pare o backend com `Ctrl+C`.
3. Pare o Dify:

   ```powershell
   docker compose -f infra/dify/docker/docker-compose.yaml stop
   ```

4. Se quiser liberar VRAM/RAM do Ollama:

   ```powershell
   ollama stop qwen3:8b
   ollama stop bge-m3
   ```

## Troubleshooting

### `Dify API error 401: Access token is invalid`

A chave do `.env` nao e a chave ativa do app.

Cheque:

- A chave precisa vir de **Studio -> Skyrim Copilot -> API Access**.
- Ela deve comecar com `app-`.
- Depois de editar `.env`, reinicie o `uvicorn`.
- Depois de mudar app/modelo/knowledge no Dify, clique em **Publish -> Update**.

### O backend mostra `qwen3:8b`, mas o Ollama carrega `qwen3:14b`

O `.env` nao manda no modelo real. Troque o modelo dentro do app no Dify e
publique:

```text
Studio -> Skyrim Copilot -> seletor de modelo -> qwen3:8b -> Publish -> Update
```

### Resposta vem com `<think>...</think>`

Adicione `/no_think` na primeira linha das Instructions do app no Dify e
publique de novo.

### `ollama ps` mostra CPU/GPU dividido

O contexto esta grande demais para sua VRAM.

No Dify, edite o modelo `qwen3:8b`:

- **Model context size:** `4096`
- **Upper bound for max tokens:** `2048`

Depois:

```powershell
ollama stop qwen3:8b
Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method POST `
  -ContentType "application/json" `
  -Body '{"model":"qwen3:8b","prompt":"hi","keep_alive":-1,"options":{"num_ctx":4096}}'
ollama ps
```

### Insomnia retorna `422 model_attributes_type`

O Insomnia esta mandando o body como string. Use **Body -> JSON** ou importe a
request via cURL.

### Swagger fica em loading

Normal para SSE. Teste via PowerShell ou no frontend para ver streaming em
tempo real.

### Frontend nao conecta no backend

Confirme:

- Backend rodando em `http://localhost:8000`.
- Frontend rodando em `http://localhost:5173`.
- `API_CORS_ORIGINS` no `.env` contem `http://localhost:5173`.
- O backend foi reiniciado depois de alterar `.env`.
