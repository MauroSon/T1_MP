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
  return (
    <div className="flex h-screen">
      <div className="relative w-3/4 h-full flex justify-center bg-[#FFCF00]">
        <Image src="/Frame5.jpg" alt="teste" width={800} height={0} className="object-cover"></Image>
      </div>
      <main className="w-1/4 flex flex-col justify-center items-center">
        <Image src="/Logo.png" alt="logo" width={174} height={0} className="m-4" ></Image>
        <Card className="mt-4 rounded-xl border-black self-center">
          <CardHeader className="flex items-center">
            <CardTitle className=""> Fazer Login </CardTitle>
          </CardHeader>
          <CardContent className="">
            <form>
              <div className="">
                <div className="gap-4">
                  <Label htmlFor="email">Email: </Label>
                  <Input className="mt-2 mb-2" id="email" type="email" placeholder="JohnDoe@email.com"/>
                </div>
                <div className="gap-4">
                  <Label htmlFor="password"> Senha: </Label>
                  <Input className="mt-2 mb-2" id="password" type="password" placeholder="********"/>
                </div>
              </div>
              <div>
                <p>Não possui uma conta? <Link className="underline" href="/create_account">Cadastre-se!</Link></p>
              </div>
            </form>
          </CardContent>
          <CardFooter className="flex items-center justify-center">
            <Button className="rounded-2xl border-black border-2">Logar</Button>
          </CardFooter>
        </Card>
      </main>
    </div>
  )
}

