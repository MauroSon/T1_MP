'use client'
import { useState } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"
import Image from "next/image"


import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"


export default function Login() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState("")
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    setError("")

    try {
      const response = await fetch("http://127.0.0.1:5000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      })

      const data = await response.json()

      if (response.ok) {
        // Armazena o token no localStorage
        localStorage.setItem("token", data.access_token)
        // Redireciona para a página principal ou dashboard
        router.push("/")
      } else {
        setError(data.msg) // Exibe a mensagem de erro do backend
      }
    } catch (error) {
      setError("Erro ao conectar ao servidor.")
    }
  }
  return (
<div className="flex h-screen">
      {/* Lado esquerdo com a imagem */}
      <div className="relative w-3/4 h-full flex justify-center bg-[#FFCF00]">
        <Image src="/Frame5.jpg" alt="imagem" width={800} height={600} className="object-cover" />
      </div>

      {/* Lado direito com o formulário */}
      <main className="w-1/4 flex flex-col justify-center items-center">
        <Image src="/Logo.png" alt="logo" width={174} height={100} className="m-4" />
        
        <Card className="mt-4 rounded-xl border-black self-center">
          <CardHeader className="flex items-center">
            <CardTitle>Fazer Login</CardTitle>
          </CardHeader>

          <CardContent>
            <form onSubmit={handleSubmit}>
              <div>
                <Label htmlFor="email">Email:</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="JohnDoe@email.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="mt-2 mb-2"
                />
              </div>
              <div>
                <Label htmlFor="password">Senha:</Label>
                <Input
                  id="password"
                  type="password"
                  placeholder="****"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="mt-2 mb-2"
                />
              </div>

              {error && <p className="text-red-500 text-sm">{error}</p>}

              <p className="mt-2">
                Não possui uma conta? <Link className="underline" href="/create_account">Cadastre-se!</Link>
              </p>

              <CardFooter className="flex items-center justify-center mt-4">
                <Button type="submit" className="rounded-2xl border-black border-2">
                  Logar
                </Button>
              </CardFooter>
            </form>
          </CardContent>
        </Card>
      </main>
    </div>
  )
}