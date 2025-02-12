import Footer from "./components/Footer"
import Navbar from "./components/NavBar"
import { FiltroComponent } from "./components/FiltroComponent"
import {ProductCard} from "./components/ProductCard"
import { BannerCarousel } from "./components/Banner"

export default function Home() {
  // Array de produtos de exemplo
  const products = [
    { id: 1, name: "Teclado Gamer", description: "Teclado gamer", price: 99.99, src: "download1.jpeg", distancia: "15km" },
    { id: 2, name: "Gabinete warrior", description: "Melhor gabinete da região", price: 149.99, src: "download2.jpeg", distancia: "10km" },
    { id: 3, name: "Gabinete usual", description: "Gabinete custo-beneficio", price: 79.99, src: "download3.jpeg", distancia: "15km" },
    { id: 4, name: "New era ed thug life", description: "bone estiloso", price: 199.99, src: "4.jpeg", distancia: "2km" },
    { id: 5, name: "New era boné", description: "boné normal", price: 129.99, src: "5.jpeg", distancia: "200km" },
    { id: 6, name: "New era blitz", description: "boné top", price: 89.99, src: "6.jpeg", distancia: "2km" },
    { id: 7, name: "tenis vans", description: "Tenis casual", price: 159.99, src: "7.jpeg" , distancia: "1km"},
    { id: 8, name: "tenis adidas", description: "Tenis corrida", price: 109.99, src: "8.jpeg" , distancia: "1km"},
  ];

  const mockBannerImages = [
    {
      src: "/pato.jpeg",
      alt: "Banner promocional",
    },
    {
      src: "/pato2.png",
      alt: "Banner promocional",
    },
    {
      src: "/images.jpeg",
      alt:"cerveja gelada",
    }
  ]

  return (
    <div>
      <Navbar />
      <BannerCarousel images={mockBannerImages} />
      <div className="container mx-auto px-4 my-8">
        <div className="w-full">
        <h1 className="m-10 w-3/5 text- text-right text-2xl font-bold">
            Os items mais vendidos na sua região!!
          </h1>
        </div>
        <div className="flex flex-col md:flex-row gap-8">
          
          <div className="w-full md:w-1/4">
            <FiltroComponent />
          </div>
          <div className="w-full md:w-3/4">
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              
              {products.map((product) => (
                <ProductCard key={product.id} name={product.name} description={product.description} price={product.price.toString()} image={product.src} distancia={product.distancia} />
              ))}
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  )
}

