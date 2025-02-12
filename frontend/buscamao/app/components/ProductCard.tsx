import Image from "next/image";

type ProductProps = {
  name: string;
  description: string;
  price: string;
  image: string;
  distancia: string;
};

export function ProductCard({ name, description, price, image , distancia }: ProductProps) {
  return (
    <div className="border rounded-lg p-4 shadow-md max-w-xs">
      <Image src={`/${image}`} alt={name} width={200} height={200} className="rounded" />
      <h2 className="text-lg font-bold mt-2">{name}</h2>
      <p className="text-gray-600">{description}</p>
      <p className="text-green-600 font-semibold mt-2">R$ {price}</p>
      <p className="mt-3 bg-orange-100 text-center text-black py-1 rounded">Distancia: {distancia}</p>
    </div>
  );
}