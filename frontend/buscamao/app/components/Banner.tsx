"use client"

import { useState } from "react"
import Image from "next/image"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { Button } from "@/components/ui/button"

interface BannerImage {
  src: string
  alt: string
}

interface BannerCarouselProps {
  images: BannerImage[]
}

export function BannerCarousel({ images }: BannerCarouselProps) {
  const [currentIndex, setCurrentIndex] = useState(0)

  const nextSlide = () => {
    setCurrentIndex((current) => (current + 1) % images.length)
  }

  const previousSlide = () => {
    setCurrentIndex((current) => (current - 1 + images.length) % images.length)
  }

  return (
    <div className="relative w-full max-w-[1200px] mx-auto mb-6">
      <div className="relative h-[140px] overflow-hidden">
        <Image
          src={images[currentIndex].src || "/placeholder.svg"}
          alt={images[currentIndex].alt}
          fill
          className="object-cover"
          priority
        />
        <div className="absolute inset-0 flex items-center justify-between">
          <Button variant="ghost" size="icon" className="h-8 w-8 ml-2" onClick={previousSlide}>
            <ChevronLeft className="h-6 w-6" />
          </Button>
          <Button variant="ghost" size="icon" className="h-8 w-8 mr-2" onClick={nextSlide}>
            <ChevronRight className="h-6 w-6" />
          </Button>
        </div>
      </div>
      <div className="absolute bottom-2 left-0 right-0 flex justify-center gap-1">
        {images.map((_, index) => (
          <button
            key={index}
            className={`h-1.5 w-1.5 rounded-full ${index === currentIndex ? "bg-primary" : "bg-primary/30"}`}
            onClick={() => setCurrentIndex(index)}
          />
        ))}
      </div>
    </div>
  )
}

