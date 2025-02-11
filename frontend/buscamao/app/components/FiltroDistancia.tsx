import React from "react";
import { useState,useEffect } from "react";


export function filtroDistancia(){
    const produto = [
        { nome: "telefone", dist: 36 },
        { nome: "tablet", dist: 120 },
        { nome: "notebook", dist: 2500 },
        { nome: "fones", dist: 80 },
        { nome: "mouse", dist: 45 }
    ]; 
    
    const [buscaProduto, setbuscaProduto] = useState('')

    const produtoFiltrado = produto.filter((prod) => prod.includes(buscaProduto.toLowerCase()));



    return(
        <div>
            <h1>Valor Máximo de preço</h1>
            <input
          className="w-full placeholder:text-opacity-50 placeholder:text-gray-500 focus:outline-none"
          type="text"
          placeholder="Digite o Preço"
          value={buscaProduto}
          onChange={(env) => setbuscaProduto(env.target.value)}
        />            

        </div>
    )
}