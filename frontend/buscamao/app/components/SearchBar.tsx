'use client';

import { Search } from 'lucide-react';

export default function SearchBar() {
  return (
    <div className="flex items-center bg-white px-4 py-2 rounded-lg w-1/4">
      <input
        type="text"
        placeholder="Digite sua busca..."
        className="flex-grow outline-none text-gray-600"
      />
      <Search className="text-gray-500" />
    </div>
  );
}