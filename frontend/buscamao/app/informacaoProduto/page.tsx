import React from 'react';
import {Footer} from '@/app/components/Footer'
import { Heart } from 'lucide-react';
import { useState, useEffect } from 'react';
//
import { FiltroPesquisa } from '../components/FiltroPesquisa';

export default function infoProd() {
  return (
    <main>
      {/* testando filtro de FiltroPesquisa */}
      <FiltroPesquisa/>
    <div className="max-w-2xl mx-auto p-4 space-y-6">
      

      {/* cartela do produto*/}
      <div className="border border-black p-4">
        <div className="flex justify-between items-start">
          <div className="flex gap-4">
            {/* imagem do produto */}
            <div className="w-32 h-32 bg-gray-200"> imagem </div>
            
            <div>
              <h2 className="text-lg font-semibold">Título do produto com alguns detalhes</h2>
              <p className="text-lg font-bold mt-2">R$ 0000,00</p>
              <div className="flex items-center gap-2 mt-2">
                <span>0.0</span>
                <div className="flex">
                  {'★'.repeat(0)}
                  {'☆'.repeat(5)}
                </div>
                <span className="text-gray-500">(000)</span>
              </div>
            </div>
          </div>
          
          <button className="text-gray-400 hover:text-red-500">
            <Heart size={24} />
          </button>
        </div>
      </div>

      {/* comnentarios */}
      <div className="p-4">
        <h3 className=" text-">Comentários</h3>
        <div className="bg-gray-50 p-4">
          Aqui vem os comentários
        </div>
      </div>
    </div>
    <Footer/>
    </main>
  );
}
