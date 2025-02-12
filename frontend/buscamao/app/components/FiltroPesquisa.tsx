"use client"

import { useState } from "react"
import { Search } from "lucide-react"

const produto = ["produto 1", "produto 2"]

export function FiltroPesquisa() {
  const [buscaProduto, setbuscaProduto] = useState("")

  const produtoFiltrado = produto.filter((prod) => prod.toLowerCase().includes(buscaProduto.toLowerCase()))

  return (
    <div className="w-2/5 my-4 mx-auto relative bg-white rounded-lg">
      <div className="rounded-lg p-4 mb-1 flex items-center">
        <input
          className="w-full placeholder:text-opacity-50 placeholder:text-gray-500 focus:outline-none pr-8"
          type="text"
          placeholder="Digite sua busca..."
          value={buscaProduto}
          onChange={(env) => setbuscaProduto(env.target.value)}
        />
        <Search className="absolute right-6 text-gray-400" size={20} />
      </div>

      {buscaProduto && produtoFiltrado.length > 0 && (
        <ul className="absolute w-full bg-white z-10 border rounded-lg shadow-lg">
          {produtoFiltrado.map((produto) => (
            <li className="px-4 py-2 hover:bg-gray-100" key={produto}>
              {produto}
            </li>
          ))}
        </ul>
      )}
    </div>
  )
}

