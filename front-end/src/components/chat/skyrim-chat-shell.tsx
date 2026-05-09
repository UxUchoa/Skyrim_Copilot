import { useState } from 'react'
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
import { cn } from '@/lib/utils'

const chats = [
  'Dwemer ruins and tonal locks',
  'Best herbs near Whiterun',
  'Daedric artifacts index',
  'College of Winterhold lore',
]

const messages = [
  {
    role: 'assistant',
    title: 'Skyrim Codex',
    content:
      'Ask about factions, quests, alchemy, artifacts, regions, or obscure book lore. I will answer like a living archive of Tamrielic knowledge.',
  },
  {
    role: 'user',
    title: 'Dragonborn',
    content: 'What should I know before entering Blackreach for the first time?',
  },
  {
    role: 'assistant',
    title: 'Skyrim Codex',
    content:
      'Carry cure disease potions, resist poison, and a strong light source. Blackreach is vast, vertical, and rich with Falmer paths, crimson nirnroot, and hidden Dwemer machinery.',
  },
]

export function SkyrimChatShell() {
  const [sidebarOpen, setSidebarOpen] = useState(true)

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
              UI prototype only
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
                  key={`${message.role}-${message.content}`}
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
                    <p className="mt-2 text-sm text-muted-foreground sm:text-base">{message.content}</p>
                  </Card>
                </article>
              ))}
            </div>
          </ScrollArea>

          <footer className="border-t border-border bg-card/90 p-3 sm:p-5">
            <div className="mx-auto max-w-4xl">
              <Card className="overflow-hidden border-primary/20 bg-background/85 p-3 shadow-xl shadow-black/10">
                <div className="mb-3 flex items-center gap-3 rounded-xl border border-dashed border-primary/35 bg-primary/10 px-4 py-3 text-primary">
                  <HugeiconsIcon icon={ImageUploadIcon} size={22} />
                  <div className="min-w-0">
                    <p className="text-sm font-medium">Image-ready prompt space</p>
                    <p className="truncate text-xs text-primary/75">
                      Drag and drop screenshots, paste images, or attach references later.
                    </p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <Input
                    aria-label="Ask about Skyrim"
                    className="h-12 border-border bg-muted/60 px-4 text-base placeholder:text-muted-foreground/70"
                    placeholder="Ask about a quest, hold, artifact, creature, or book..."
                  />
                  <Button className="h-12 gap-2 bg-primary px-4 text-primary-foreground hover:bg-primary/90 sm:px-5">
                    <HugeiconsIcon icon={SentIcon} size={20} />
                    <span className="hidden sm:inline">Send</span>
                  </Button>
                </div>
              </Card>
            </div>
          </footer>
        </section>
      </div>
    </main>
  )
}
