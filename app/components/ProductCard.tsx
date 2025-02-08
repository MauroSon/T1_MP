import Image from "next/image";

type ProductProps = {
  name: string;
  description: string;
  price: string;
  image: string;
};

export default function ProductCard({ name, description, price, image }: ProductProps) {
  return (
    <div className="border rounded-lg p-4 shadow-md max-w-xs">
      <Image src={`/${image}`} alt={name} width={200} height={200} className="rounded" />
      <h2 className="text-lg font-bold mt-2">{name}</h2>
      <p className="text-gray-600">{description}</p>
      <p className="text-green-600 font-semibold mt-2">R$ {price}</p>
      <button className="mt-3 bg-blue-500 text-white py-1 px-4 rounded">Comprar</button>
    </div>
  );
}