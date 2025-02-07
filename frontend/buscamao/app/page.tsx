import React from "react";
import { Footer } from "./_components/Footer_/footer";

export default function Home() {
  

  return (
    <main className=" bg-white">
      <div className="container w-screen h-screen px-4 flex">
        {/* Div que ocupa 3/5 da largura e toda a altura */}
        <div className="w-3/5 h-screen">
          <img 
            src="buscamao.png" 
            alt="Foto de um cara gente boa" 
            className="w-full h-full object-cover"
          />
        </div>

        {/* Div restante com 2/5 da largura */}
        <div className="w-2/5 h-screen bg-gray-200">
          {/* Conteúdo adicional aqui */}
        </div>
      </div>



       
      
      
    </main>
  );
}
