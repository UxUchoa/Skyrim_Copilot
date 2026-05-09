import { useEffect, useRef, useState, type ClipboardEvent, type DragEvent } from 'react'
import { HugeiconsIcon } from '@hugeicons/react'
import {
  Add01Icon,
  AiMagicIcon,
  BookOpen02Icon,
  Cancel01Icon,
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

type PreviewOverlayProps = {
  activePreviewIndex: number
  attachedImages: File[]
  imageUrls: string[]
  isClosing: boolean
  onClose: () => void
  onAddImages: () => void
  onRemoveImage: (index: number) => void
  onSelectImage: (index: number) => void
  onSend: () => void
}

function PreviewOverlay({
  activePreviewIndex,
  attachedImages,
  imageUrls,
  isClosing,
  onAddImages,
  onClose,
  onRemoveImage,
  onSelectImage,
  onSend,
}: PreviewOverlayProps) {
  const activeImage = attachedImages[activePreviewIndex]
  const activeImageUrl = imageUrls[activePreviewIndex]

  return (
    <div
      className={cn(
        'absolute inset-0 z-20 flex flex-col overflow-hidden rounded-b-2xl border-t border-primary/20 bg-[radial-gradient(circle_at_center,oklch(0.43_0.04_75_/_0.35),transparent_58%),linear-gradient(135deg,oklch(0.18_0.014_72_/_0.96),oklch(0.12_0.01_68_/_0.98))] text-foreground shadow-2xl shadow-black/40 backdrop-blur-md transition-[opacity,transform,filter] duration-300 ease-out',
        isClosing ? 'scale-[0.985] opacity-0 blur-sm' : 'scale-100 opacity-100 blur-0',
      )}
    >
      <div className="pointer-events-none absolute inset-0 opacity-35 [background-image:linear-gradient(90deg,oklch(0.86_0.06_82_/_0.05)_1px,transparent_1px),linear-gradient(oklch(0.86_0.06_82_/_0.04)_1px,transparent_1px)] [background-size:18px_18px]" />

      <div className="relative flex items-center justify-center border-b border-primary/15 px-4 py-4 sm:px-6">
        <Button
          aria-label="Close image preview"
          className="absolute left-4 size-10 border-primary/25 bg-background/70 text-primary shadow-lg shadow-black/20 hover:bg-primary/15 sm:left-6"
          onClick={onClose}
          size="icon"
          type="button"
          variant="outline"
        >
          <HugeiconsIcon icon={Cancel01Icon} size={21} strokeWidth={1.9} />
        </Button>
        <p className="font-heading text-center text-sm tracking-[0.24em] text-primary uppercase sm:text-base">
          Present Image to the Codex
        </p>
      </div>

      <div className="relative flex min-h-0 flex-1 items-center justify-center p-5 sm:p-8">
        <div className="absolute inset-x-8 top-8 bottom-8 rounded-[2rem] border border-primary/10 bg-background/15 shadow-inner shadow-black/40" />
        {activeImage && activeImageUrl ? (
          <img
            alt={activeImage.name}
            className="relative max-h-full max-w-full rounded-2xl border border-primary/25 bg-card object-contain p-1 shadow-2xl shadow-black/45"
            src={activeImageUrl}
          />
        ) : (
          <div className="relative grid min-h-64 w-full max-w-2xl place-items-center rounded-2xl border border-dashed border-primary/35 bg-card/45 p-8 text-center shadow-2xl shadow-black/35">
            <div>
              <HugeiconsIcon className="mx-auto text-primary" icon={ImageUploadIcon} size={40} />
              <p className="mt-4 font-heading text-lg tracking-[0.18em] text-primary uppercase">
                Release Screenshot
              </p>
              <p className="mt-2 text-sm text-muted-foreground">
                The Codex will reveal the image preview when your browser provides the file.
              </p>
            </div>
          </div>
        )}
      </div>

      <div className="relative flex items-center justify-center gap-3 border-t border-primary/15 bg-card/70 px-4 py-4 backdrop-blur sm:px-6">
        <div className="flex max-w-full items-center gap-3 overflow-x-auto rounded-2xl border border-border bg-background/70 p-2 shadow-inner shadow-black/20">
          {attachedImages.map((image, index) => (
            <div
              className={cn(
                'group relative size-16 shrink-0 overflow-hidden rounded-xl border bg-card shadow-sm shadow-black/20 transition-all duration-300 ease-out',
                index === activePreviewIndex
                  ? 'border-primary ring-2 ring-primary/45'
                  : 'border-primary/30 hover:border-primary/70',
              )}
              key={`${image.name}-${image.lastModified}-${index}`}
            >
              <button
                aria-label={`Preview ${image.name}`}
                className="grid size-full place-items-center transition-transform duration-300 group-hover:scale-105"
                onClick={() => onSelectImage(index)}
                type="button"
              >
                {imageUrls[index] ? (
                  <img alt={image.name} className="size-full object-cover" src={imageUrls[index]} />
                ) : (
                  <HugeiconsIcon className="text-primary/75" icon={ImageUploadIcon} size={23} />
                )}
              </button>
              <button
                aria-label={`Remove ${image.name}`}
                className="absolute top-1 right-1 grid size-5 place-items-center rounded-full border border-primary/30 bg-background/90 text-primary opacity-90 shadow-sm shadow-black/25 transition duration-200 hover:border-destructive/70 hover:bg-destructive hover:text-destructive-foreground group-hover:scale-105"
                onClick={(event) => {
                  event.stopPropagation()
                  onRemoveImage(index)
                }}
                type="button"
              >
                <HugeiconsIcon icon={Cancel01Icon} size={13} strokeWidth={2.2} />
              </button>
            </div>
          ))}
          <button
            aria-label="Add more images"
            className="grid size-16 shrink-0 place-items-center rounded-xl border border-dashed border-primary/40 bg-primary/10 text-primary transition hover:border-primary hover:bg-primary/20"
            onClick={onAddImages}
            type="button"
          >
            <HugeiconsIcon icon={Add01Icon} size={24} strokeWidth={1.8} />
          </button>
        </div>

        <Button
          aria-label="Send image preview"
          className="size-12 shrink-0 rounded-full bg-primary text-primary-foreground shadow-lg shadow-primary/20 hover:bg-primary/90"
          disabled={attachedImages.length === 0}
          onClick={onSend}
          size="icon"
          type="button"
        >
          <HugeiconsIcon icon={QuillWrite01Icon} size={22} strokeWidth={1.9} />
        </Button>
      </div>
    </div>
  )
}

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
  const [prompt, setPrompt] = useState('')
  const [attachedImages, setAttachedImages] = useState<File[]>([])
  const [attachedImageUrls, setAttachedImageUrls] = useState<string[]>([])
  const [activePreviewIndex, setActivePreviewIndex] = useState(0)
  const [isOverlayVisible, setIsOverlayVisible] = useState(false)
  const [isOverlayClosing, setIsOverlayClosing] = useState(false)
  const fileInputRef = useRef<HTMLInputElement>(null)
  const attachedImageUrlsRef = useRef<string[]>([])
  const overlayCloseTimerRef = useRef<number | null>(null)

  useEffect(() => {
    return () => {
      if (overlayCloseTimerRef.current) {
        window.clearTimeout(overlayCloseTimerRef.current)
      }

      attachedImageUrlsRef.current.forEach((imageUrl) => URL.revokeObjectURL(imageUrl))
    }
  }, [])

  const clearAttachedImages = () => {
    attachedImageUrlsRef.current.forEach((imageUrl) => URL.revokeObjectURL(imageUrl))
    attachedImageUrlsRef.current = []
    setAttachedImages([])
    setAttachedImageUrls([])
    setActivePreviewIndex(0)
  }

  const closeImagePreview = () => {
    setIsOverlayClosing(true)

    if (overlayCloseTimerRef.current) {
      window.clearTimeout(overlayCloseTimerRef.current)
    }

    overlayCloseTimerRef.current = window.setTimeout(() => {
      clearAttachedImages()
      setIsOverlayVisible(false)
      setIsOverlayClosing(false)
      overlayCloseTimerRef.current = null
    }, 260)
  }

  const addImageFiles = (files: FileList | File[]) => {
    const imageFiles = Array.from(files).filter((file) => file.type.startsWith('image/'))

    if (imageFiles.length === 0) {
      return false
    }

    const nextImageUrls = imageFiles.map((file) => URL.createObjectURL(file))

    if (overlayCloseTimerRef.current) {
      window.clearTimeout(overlayCloseTimerRef.current)
      overlayCloseTimerRef.current = null
    }

    attachedImageUrlsRef.current = [...attachedImageUrlsRef.current, ...nextImageUrls]
    setAttachedImageUrls((currentImageUrls) => [...currentImageUrls, ...nextImageUrls])

    setAttachedImages((currentImages) => {
      const nextImages = [...currentImages, ...imageFiles]

      if (currentImages.length === 0) {
        setActivePreviewIndex(0)
      }

      return nextImages
    })
    setIsOverlayClosing(false)
    setIsOverlayVisible(true)
    return true
  }

  const removeAttachedImage = (imageIndex: number) => {
    const removedImageUrl = attachedImageUrlsRef.current[imageIndex]
    const nextImages = attachedImages.filter((_, index) => index !== imageIndex)
    const nextImageUrls = attachedImageUrlsRef.current.filter((_, index) => index !== imageIndex)

    if (removedImageUrl) {
      URL.revokeObjectURL(removedImageUrl)
    }

    attachedImageUrlsRef.current = nextImageUrls
    setAttachedImages(nextImages)
    setAttachedImageUrls(nextImageUrls)

    if (nextImages.length === 0) {
      closeImagePreview()
      return
    }

    if (imageIndex === activePreviewIndex) {
      setActivePreviewIndex(Math.min(imageIndex, nextImages.length - 1))
      return
    }

    if (imageIndex < activePreviewIndex) {
      setActivePreviewIndex(activePreviewIndex - 1)
    }
  }

  const handlePasteImages = (event: ClipboardEvent<HTMLInputElement | HTMLDivElement>) => {
    const imageFiles = Array.from(event.clipboardData.files).filter((file) =>
      file.type.startsWith('image/'),
    )

    if (imageFiles.length > 0) {
      addImageFiles(imageFiles)
    }
  }

  const handleMainChatDragOver = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault()

    if (event.dataTransfer.types.includes('Files')) {
      setIsOverlayVisible(true)
    }
  }

  const handleMainChatDragLeave = (event: DragEvent<HTMLDivElement>) => {
    const nextTarget = event.relatedTarget

    if (nextTarget instanceof Node && event.currentTarget.contains(nextTarget)) {
      return
    }

    if (attachedImages.length === 0) {
      closeImagePreview()
    }
  }

  const handleMainChatDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault()

    if (!addImageFiles(event.dataTransfer.files) && attachedImages.length === 0) {
      closeImagePreview()
    }
  }

  const handleSubmit = () => {
    setPrompt('')
  }

  const handleOverlaySend = () => {
    // Future backend submission will receive `attachedImages` after upload integration exists.
    void attachedImages
    closeImagePreview()
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

          <ScrollArea
            className="min-h-0 flex-1"
            onDragLeave={handleMainChatDragLeave}
            onDragOver={handleMainChatDragOver}
            onDrop={handleMainChatDrop}
            onPaste={handlePasteImages}
          >
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
            {isOverlayVisible && (
              <PreviewOverlay
                activePreviewIndex={activePreviewIndex}
                attachedImages={attachedImages}
                imageUrls={attachedImageUrls}
                isClosing={isOverlayClosing}
                onAddImages={() => fileInputRef.current?.click()}
                onClose={closeImagePreview}
                onRemoveImage={removeAttachedImage}
                onSelectImage={setActivePreviewIndex}
                onSend={handleOverlaySend}
              />
            )}
          </ScrollArea>

          <footer className="border-t border-border bg-card/90 p-3 sm:p-5">
            <div className="mx-auto max-w-4xl">
              <Card className="overflow-hidden border-primary/20 bg-background/85 p-3 shadow-xl shadow-black/10">
                <div className="flex items-center gap-2">
                  <input
                    accept="image/*"
                    className="sr-only"
                    multiple
                    onChange={(event) => {
                      if (event.target.files) {
                        addImageFiles(event.target.files)
                      }

                      event.target.value = ''
                    }}
                    ref={fileInputRef}
                    type="file"
                  />
                  <Button
                    aria-label="Attach screenshot"
                    className="h-12 border-primary/25 bg-primary/10 text-primary hover:bg-primary/20"
                    onClick={() => fileInputRef.current?.click()}
                    size="icon"
                    type="button"
                    variant="outline"
                  >
                    <HugeiconsIcon icon={ImageUploadIcon} size={21} />
                  </Button>
                  <Input
                    aria-label="Ask about Skyrim"
                    className="h-12 border-border bg-muted/60 px-4 text-base placeholder:text-muted-foreground/70"
                    onChange={(event) => setPrompt(event.target.value)}
                    onPaste={handlePasteImages}
                    placeholder="Ask about a quest, hold, artifact, creature, or book..."
                    value={prompt}
                  />
                  <Button
                    className="h-12 gap-2 bg-primary px-4 text-primary-foreground hover:bg-primary/90 sm:px-5"
                    onClick={handleSubmit}
                    type="button"
                  >
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
