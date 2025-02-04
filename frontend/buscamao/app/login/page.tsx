import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"
import { Pencil } from "lucide-react"
import { Footer } from "../_components/Footer_/footer"

export default function login() {
  return (
    <main>
    <Card className="w-full max-w-md mx-auto shadow-lg">
      <CardContent className="pt-6">
        <div className="flex flex-col items-center space-y-6">
          {"avatar do versel"}
          <div className="w-16 h-16 bg-yellow-400 rounded-full flex items-center justify-center">
            <svg className="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" />
            </svg>
          </div>

          
          <div className="w-full space-y-4">
            
            <div className="flex items-center justify-between border-b pb-2">
              <div>
                <div className="text-sm text-gray-500">Nome de usuário</div>
                <div className="font-medium">JohnDoe@gmail.com</div>
              </div>
              <Button variant="ghost" size="icon" className="h-8 w-8 hover:bg-gray-100">
                <Pencil className="h-4 w-4" />
              </Button>
            </div>

           
            <div className="flex items-center justify-between border-b pb-2">
              <div>
                <div className="text-sm text-gray-500">Senha</div>
                <div className="font-medium">••••••••••</div>
              </div>
              <Button variant="ghost" size="icon" className="h-8 w-8 hover:bg-gray-100">
                <Pencil className="h-4 w-4" />
              </Button>
            </div>
          </div>

          
          <Button variant="destructive" className="w-full bg-red-500 hover:bg-red-600 text-white">
            Excluir conta
          </Button>
        </div>
      </CardContent>
    </Card>
    <Footer/>
    </main>
  )
}

