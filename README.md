# Skyrim Copilot

Backend e engenharia de dados para construir uma base RAG/LLM sobre o universo de
Skyrim. A Fase 1 coleta conteúdo da UESP, limpa o HTML da wiki, estrutura o texto
em Markdown e gera arquivos prontos para importação no Dify.

O frontend está fora deste repositório por enquanto. Este projeto foca em dados,
scraping, sanitização e preparação de corpus.

## Setup

Requer Python 3.11+.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
```

Copie `.env.example` para `.env` se quiser alterar limites e caminhos padrão.

## Como Rodar

Smoke test amplo, usando hubs curados, API MediaWiki e links:

```powershell
python -m backend.pipeline.build_uesp_corpus --discovery hybrid --scope all --max-pages 25 --max-depth 1
```

Corpus maior, recomendado para alimentar a base do Dify:

```powershell
python -m backend.pipeline.build_uesp_corpus --discovery api --scope all --max-pages 1000 --delay-seconds 1.0
```

Modo antigo, partindo de uma seed e navegando por links:

```powershell
python -m backend.pipeline.build_uesp_corpus --discovery crawl --seed "https://en.uesp.net/wiki/Skyrim:Skyrim" --max-pages 10
```

Use `--no-raw` para não salvar HTML bruto. Use `--resume` para continuar uma
execução sem reprocessar URLs que já aparecem no manifest.

## Modos de Descoberta

- `--discovery api`: usa a API MediaWiki para descobrir páginas por categoria.
- `--discovery hybrid`: combina hubs curados, API MediaWiki e links internos.
- `--discovery crawl`: apenas segue links a partir das seeds informadas.

Escopos disponíveis:

- `--scope skyrim`: somente páginas `Skyrim:`.
- `--scope all`: páginas `Skyrim:` e `Lore:`, cobrindo gameplay e lore amplo.

## Estrutura do Projeto

`backend/ingest/` contém a camada de ingestão da UESP.

- `mediawiki_client.py`: consulta a API MediaWiki e pagina resultados de categorias.
- `uesp_seed_catalog.py`: define hubs e categorias importantes, como quests, armas,
  armaduras, NPCs, locais, livros, spells, factions e lore.
- `uesp_scraper.py`: baixa HTML com delay, retries, filtros de URL e suporte a
  namespaces como `Skyrim:` e `Lore:`.
- `uesp_parser.py`: remove ruído da wiki e transforma o conteúdo principal em
  documentos semânticos.

`backend/rag/` contém a preparação para RAG/Dify.

- `documents.py`: modelos internos como `RagDocument` e `RagSection`.
- `chunker.py`: divide documentos grandes em chunks por seção.
- `markdown_exporter.py`: gera Markdown final e `manifest.jsonl`.

`backend/pipeline/` contém a orquestração.

- `build_uesp_corpus.py`: comando principal que descobre URLs, baixa páginas,
  parseia, chunkifica e exporta o corpus.

`tests/` contém os testes unitários do scraper, parser, API, chunker e pipeline.

## Arquivos Gerados

- `data/raw/uesp/`: snapshots HTML brutos, úteis para depuração.
- `data/processed/url_plan.jsonl`: plano auditável de URLs descobertas.
- `data/processed/dify_markdown/`: um arquivo Markdown por página/entidade.
- `data/processed/manifest.jsonl`: metadados, chunks, URLs e caminhos exportados.

Os arquivos em `data/` são gerados localmente e não devem ser versionados.

## Fluxo do Pipeline

1. Descobre URLs por API MediaWiki, hubs curados ou crawl.
2. Baixa o HTML das páginas aceitas.
3. Remove menus, navegação, scripts, seções de baixo valor e ruído visual.
4. Converte o conteúdo principal para Markdown.
5. Infere metadados como `namespace` e `entity_type`.
6. Divide o documento em chunks.
7. Exporta Markdown e manifest para importação no Dify.

## Testes

```powershell
python -m pytest
```
