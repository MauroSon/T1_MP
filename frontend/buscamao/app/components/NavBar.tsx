'use client';

import Link from "next/link"
import Image from "next/image";
import { Search, Heart, User, LogIn, MapPin } from 'lucide-react';

export default function Navbar() {
  return (
    <nav className="bg-[#FFCF00] shadow-md">
      <div className="container mx-auto flex justify-between items-center py-4">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <Image src="/Logo.png" alt="Logo" width={174} height={0} className="m-4" />
        </div>
        
        {/* Search Bar */}
        <div className="flex items-center bg-white px-4 py-2 rounded-lg w-1/4">
          <input type="text" placeholder="Digite sua busca..." className="flex-grow outline-none text-gray-600" />
          <Search className="text-gray-500" />
        </div>
        
        {/* Icons */}
        <div className="flex items-center space-x-4">
          <button className="flex items-center space-x-2 text-gray-900">
            <Heart />
            <span>Favoritos</span>
          </button>
          <button className="flex items-center space-x-2 bg-white px-4 py-2 rounded-xl shadow-md">
            <Link className="flex" href="/login" >
            <User />
              <span className="flex">Entrar </span>
            <LogIn className="ml-1" />
            </Link>
          </button>
        </div>
      </div>
      
      {/* Secondary Menu */}
      <div className="bg-[#E9BD00] px-4 py-2 text-white flex text-sm w-full">
        <div className="flex items-center space-x-2">
          <MapPin />
          <span>00000-000</span>
        </div>
        <div className="flex items-center space-x-4">
          <span>Categorias</span>
          <span>Mais vendidos</span>
          <span>Ofertas do dia</span>
          <span>Menor preço</span>
          <span>Mais desejados</span>
        </div>
      </div>
    </nav>
  );
}