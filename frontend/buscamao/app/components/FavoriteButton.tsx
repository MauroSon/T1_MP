'use client';

import { Heart } from 'lucide-react';

export default function FavoritesButton() {
  return (
    <button className="flex items-center space-x-2 text-gray-900">
      <Heart />
      <span>Favoritos</span>
    </button>
  );
}