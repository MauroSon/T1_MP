'use client'
import { useState, useEffect } from "react";
import Footer from "./components/Footer";
import Navbar from "./components/NavBar";
import { FiltroComponent } from "./components/FiltroComponent";
import { ProductCard } from "./components/ProductCard";
import { BannerCarousel } from "./components/Banner";

export default function Home() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [jwtToken, setJwtToken] = useState<string | null>(null);
  useEffect(() => {
    if (typeof window !== "undefined") {
      setJwtToken(localStorage.getItem("token")); // Agora só acessa localStorage no cliente
    }
  }, []);
  useEffect(() => {
    if (typeof window !== "undefined") {
      setJwtToken(localStorage.getItem("token")); // Agora só acessa localStorage no cliente
    }
  }, []);

  useEffect(() => {
    const fetchProducts = async () => {
      if (!jwtToken) return; // Aguarda o token ser carregado

      setLoading(true);

      try {
        const response = await fetch("http://localhost:5000/produto/all/", {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${jwtToken}`,
            "Content-Type": "application/json",
          },
        });

        if (!response.ok) {
          throw new Error(`Erro ao buscar produtos: ${response.status}`);
        }

        const data = await response.json();
        setProducts(data.data || []); // Garante que o estado será sempre um array
        console.log("Produtos carregados:", data);
      } catch (error) {
        console.error("Erro na requisição:", error);
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProducts();
  }, [jwtToken]); // Só faz a requisição quando o token estiver disponível


  const mockBannerImages = [
    { src: "/pato.jpeg", alt: "Banner promocional" },
    { src: "/pato2.png", alt: "Banner promocional" },
    { src: "/images.jpeg", alt: "Cerveja gelada" },
  ];

  return (
    <div>
      <Navbar />
      <BannerCarousel images={mockBannerImages} />
      <div className="container mx-auto px-4 my-8">
        <div className="w-full">
          <h1 className="m-10 w-3/5 text-right text-2xl font-bold">
            Os itens mais vendidos na sua região!!
          </h1>
        </div>
        <div className="flex flex-col md:flex-row gap-8">
          <div className="w-full md:w-1/4">
            <FiltroComponent />
          </div>
          <div className="w-full md:w-3/4">
            {loading ? (
              <p>Carregando produtos...</p>
            ) : error ? (
              <p className="text-red-500">Erro: {error}</p>
            ) : products.length === 0 ? (
              <p className="text-gray-500">Nenhum produto disponível.</p>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {products.map((product) => (
                  <ProductCard
                    key={product.produto_id}
                    name={product.nome_produto}
                    description={product.descricao_produto}
                    price={product.preco.toString()}
                    image={product.foto_produto ? (
                      <img src={`data:image/jpeg;base64,${product.foto_produto}`} alt="Produto" className="w-full h-auto"/>
                    ) : (
                      <img src="/6.jpeg" alt="Imagem padrão" className="w-full h-auto"/>
                    )}
                    distancia={product.localizacao}
                  />
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}
