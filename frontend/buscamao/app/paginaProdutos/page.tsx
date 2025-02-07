import React from 'react';
import {Footer} from '@/app/components/Footer'
import { BannerCarousel } from "@/app/components/Banner"

export default function Prod() {
    const mockBannerImages = [
        {
          src: "/buscamao.png",
          alt: "Banner promocional",
        },
      ]

  return (
    <main>
        <BannerCarousel images={mockBannerImages} />

    
    <Footer/>
    </main>
  );
}
