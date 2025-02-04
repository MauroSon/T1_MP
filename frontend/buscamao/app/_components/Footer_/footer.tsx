import { Button } from "@/components/ui/button"
import { Facebook, Instagram, Youtube } from "lucide-react"
import { Twitter } from "lucide-react"
import Link from "next/link"

export function Footer() {
  return (
    <footer className="w-full bg-black text-white py-8 my-16">
      <div className="container mx-auto px-4 max-w-5xl">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 justify-items-start">
          {/* Destaques Column */}
          <div>
            <h2 className="font-bold mb-4 text-yellow-400">Destaques</h2>
            <ul className="space-y-2">
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Celulares
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Ar-Condicionado
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  TVs
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Notebooks
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Geladeiras
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Todas as categorias
                </Link>
              </li>
            </ul>
          </div>

          {/* O Buscamão Column */}
          <div>
            <h2 className="font-bold mb-4 text-yellow-400">O Buscamão</h2>
            <ul className="space-y-2">
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Sua privacidade
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Trabalhe conosco
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Imprensa
                </Link>
              </li>
              <li>
                <Link href="#" className="hover:text-yellow-400">
                  Ética e Integridade
                </Link>
              </li>
              <li>
                <h3 className="font-bold mb-2 mt-4 text-yellow-400">Marcas e lojas</h3>
                <Link href="#" className="hover:text-yellow-400">
                  Área do anunciante
                </Link>
              </li>
            </ul>
          </div>

          {/* Precisa de ajuda Column */}
          <div>
            <h2 className="font-bold mb-4 text-yellow-400">Precisa de ajuda?</h2>
            <Button variant="outline" className="text-white border-white hover:bg-white hover:text-black">
              Fale conosco
            </Button>
          </div>
        </div>

        {/* Social Media Links */}
        <div className="mt-8 pt-8 border-t border-gray-800">
          <div className="flex space-x-6 justify-center">
            <Link href="#" className="hover:text-yellow-400">
              <Facebook className="h-6 w-6" />
              <span className="sr-only">Facebook</span>
            </Link>
            <Link href="#" className="hover:text-yellow-400">
              <Twitter className="h-6 w-6" />
              <span className="sr-only">Twitter</span>
            </Link>
            <Link href="#" className="hover:text-yellow-400">
              <Youtube className="h-6 w-6" />
              <span className="sr-only">YouTube</span>
            </Link>
            <Link href="#" className="hover:text-yellow-400">
              <Instagram className="h-6 w-6" />
              <span className="sr-only">Instagram</span>
            </Link>
          </div>

          {/* Legal Text */}
          <p className="text-xs text-gray-400 mt-6 text-center">
            O uso deste site está sujeito aos termos e condições dos Termos de Uso e Política de Privacidade.
            <br />
            Qualquer semelhança com outras marcas e empresas é mera coincidência.
          </p>
        </div>
      </div>
    </footer>
  )
}

