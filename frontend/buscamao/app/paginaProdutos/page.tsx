import React from 'react';
import {Footer} from '@/app/_components/Footer_/footer'
import { BannerCarousel } from "@/app/_components/banners/page"

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
