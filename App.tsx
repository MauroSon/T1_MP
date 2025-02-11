import React from "react";
import Comment from "./components/Comment";

const App: React.FC = () => {
  return (
    <div>
      <h2>Comentários</h2>
      <Comment 
        usuario="João Silva"
        data="11/02/2025"
        texto="Ótimo produto, recomendo!"
        estrelas={5}
        alerta={false} 
      />

      <Comment 
        usuario="Maria Oliveira"
        data="10/02/2025"
        texto="Veio com um pequeno defeito, mas funciona bem."
        estrelas={3}
        alerta={true} 
      />
    </div>
  );
};

export default App;
