"use client"

// * Função: Filtro de Pesquisa de Produtos
// * Descrição
// * Filtra os produtos disponíveis de acordo com o texto de busca digitado
// * pelo usuário, considerando a busca sem diferenciação de maiúsculas ou
// * minúsculas.
// * Parâmetros
// * buscaProduto - string com o texto digitado pelo usuário para buscar
// *                 nos produtos disponíveis.
// * Valor retornado
// * Retorna uma lista de produtos cujos nomes contêm a string de busca, 
// * ignorando a diferenciação entre maiúsculas e minúsculas.
// * Assertiva de entrada
// * buscaProduto != NULL
// * buscaProduto é uma string válida (não vazia ou somente espaços)
// * Assertiva de saída
// * retorna uma lista de produtos filtrados (produtoFiltrado), que contém 
// * produtos cujos nomes incluem a string de busca.

import { useState } from "react"

const produto = ["produto 1", "produto 2"]



export function FiltroPesquisa() {
  const [buscaProduto, setbuscaProduto] = useState("");

  const produtoFiltrado = produto.filter((prod) => prod.toLowerCase().includes(buscaProduto.toLowerCase()));
  return (
    <div className="w-2/5 my-4 mx-auto relative">
      <div className="border rounded-lg p-4 mb-1">
        <input
          className="w-full placeholder:text-opacity-50 placeholder:text-gray-500 focus:outline-none"
          type="text"
          placeholder="Digite sua busca..."
          value={buscaProduto}
          onChange={(env) => setbuscaProduto(env.target.value)}
        />
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

