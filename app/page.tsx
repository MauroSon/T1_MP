import Comment from "@/components/Comment"; // Importando o componente

export default function Home() {
  return (
    <main className="p-8">
      <h1 className="text-2xl font-bold">Comentários</h1>
      <Comment 
        usuario="João Silva"
        data="11/02/2025"
        texto="Ótimo produto, recomendo!"
        estrelas={5}
        alerta={true} 
      />
    </main>
  );
}
