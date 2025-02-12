import Image from "next/image";
import { Search, Heart, User, LogIn, MapPin } from 'lucide-react';
import SearchBar from "./SearchBar"; // Componente client-side
import FavoritesButton from "./FavoriteButton"; // Componente client-side
import LoginButton from "./LoginButton"; // Componente client-side
import { FiltroPesquisa } from "./FiltroPesquisa";

export default function Navbar() {
  return (
    <nav className="bg-[#FFCF00] shadow-md">
      <div className="container mx-auto flex justify-between items-center py-4">
        {/* Logo */}
        <div className="flex items-center space-x-2">
          <Image src="/Logo.png" alt="Logo" width={174} height={0} className="m-4" />
        </div>
        
        {/* Search Bar */}
        <FiltroPesquisa/>
        
        {/* Icons */}
        <div className="flex items-center space-x-4">
          <FavoritesButton />
          <LoginButton />
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