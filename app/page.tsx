import ProductCard from "./components/ProductCard";

export default function Home() {
  const product = {
    name: "Tênis Nike Air",
    description: "Confortável e estiloso.",
    price: "51 000,00",
    image: "Air Jordan.png", 
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <ProductCard {...product} />
    </div>
  );
}
