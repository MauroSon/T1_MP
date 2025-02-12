export default function ProductForm() {
    return (
      <div className="h-screen flex items-center justify-center bg-gray-100">
        <div className="w-1/3 border border-gray-400 shadow-lg p-6 rounded-lg bg-white">
          <form className="space-y-4">
            <div className="justify-center items-center flex">
                Cadastre Seu Produto!!
            </div>
            <div>
              <label htmlFor="nome_produto" className="block text-sm font-medium text-gray-700">
                Nome do Produto
              </label>
              <input
                type="text"
                id="nome_produto"
                name="nome_produto"
                required
                className="mt-1 block w-full bg-gray-50 border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </div>
  
            <div>
              <label htmlFor="categoria_produto" className="block text-sm font-medium text-gray-700">
                Categoria do Produto
              </label>
              <input
                type="text"
                id="categoria_produto"
                name="categoria_produto"
                required
                className="mt-1 block w-full bg-gray-50 border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </div>
  
            <div>
              <label htmlFor="loja_id" className="block text-sm font-medium text-gray-700">
                ID da Loja
              </label>
              <input
                type="text"
                id="loja_id"
                name="loja_id"
                required
                className="mt-1 block w-full bg-gray-50 border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </div>
  
            <div>
              <label htmlFor="preco" className="block text-sm font-medium text-gray-700">
                Preço
              </label>
              <input
                type="number"
                id="preco"
                name="preco"
                required
                step="0.01"
                min="0"
                className="mt-1 block w-full bg-gray-50 border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              />
            </div>
  
            <div>
              <label htmlFor="descricao_produto" className="block text-sm font-medium text-gray-700">
                Descrição do Produto
              </label>
              <textarea
                id="descricao_produto"
                name="descricao_produto"
                required
                rows={3}
                className="mt-1 block w-full bg-gray-50 border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              ></textarea>
            </div>
  
            <div>
              <button
                type="submit"
                className="w-full py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-black bg-yellow-400 hover:bg-yellow-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                Salvar Produto
              </button>
            </div>
          </form>
        </div>
      </div>
    )
  }
  