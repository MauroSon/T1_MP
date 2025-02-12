"use client"

import { Slider } from "@/components/ui/slider"
import { Filter } from "lucide-react"
import { useState } from "react"

export function FiltroComponent() {
  const [priceRange, setPriceRange] = useState([0, 2000])
  const [distanceRange, setDistanceRange] = useState([0, 100])

  return (
    <div className="w-72 border rounded-lg p-4 bg-white">
      <div className="flex items-center gap-2 mb-6">
        <Filter className="w-5 h-5" />
        <h2 className="font-medium">Filtrar</h2>
      </div>

      <div className="space-y-6">
        {/* Price Range */}
        <div className="space-y-4">
          <div className="flex justify-between text-sm">
            <span>R$ Min.</span>
            <span>R$ Máx.</span>
          </div>
          <div className="flex justify-between text-sm text-muted-foreground mb-2">
            <span>R$ {priceRange[0].toFixed(2)}</span>
            <span>R$ {priceRange[1].toFixed(2)}</span>
          </div>
          <Slider min={0} max={2000} step={10} value={priceRange} onValueChange={setPriceRange} className="my-4" />
        </div>

        {/* Distance Range */}
        <div className="space-y-4">
          <div className="flex justify-between text-sm">
            <span>Dist. Min.</span>
            <span>Dist. Máx.</span>
          </div>
          <div className="flex justify-between text-sm text-muted-foreground mb-2">
            <span>{distanceRange[0]} km</span>
            <span>{distanceRange[1]} km</span>
          </div>
          <Slider min={0} max={100} step={1} value={distanceRange} onValueChange={setDistanceRange} className="my-4" />
        </div>

        {/* Types */}
        <div className="space-y-2">
          <h3 className="font-medium">Tipos</h3>
          <ul className="space-y-1">
            {["Tecnologia", "Moda", "Alimentação", "Móveis", "Livros"].map((tipo) => (
              <li key={tipo} className="flex items-center gap-2">
                <input type="checkbox" id={tipo} className="rounded border-gray-300" />
                <label htmlFor={tipo} className="text-sm">
                  {tipo}
                </label>
              </li>
            ))}
          </ul>
        </div>

        {/* Price Order */}
        <div className="space-y-2">
          <h3 className="font-medium">Preço</h3>
          <ul className="space-y-1">
            {["Mais Baratos", "Mais Caros"].map((opcao) => (
              <li key={opcao} className="flex items-center gap-2">
                <input type="radio" name="preco" id={opcao} className="border-gray-300" />
                <label htmlFor={opcao} className="text-sm">
                  {opcao}
                </label>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  )
}

