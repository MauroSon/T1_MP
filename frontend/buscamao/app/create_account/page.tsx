"use client"; // Adicione esta linha no topo do arquivo

import Link from "next/link";
import Image from "next/image";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

export default function CreateAccount() {
  const [userType, setUserType] = useState<"varejista" | "cliente" | null>(null);

  const renderForm = () => {
    if (userType === "varejista") {
      return (
        <div>
          <div className="font-bold"> Passo 2: </div>
          <div className="mb-4"> Digite suas informações: </div>
          <form className="space-y-4">
          <div>
            <Label htmlFor="companyName">Nome da Empresa</Label>
            <Input id="companyName" type="text" placeholder="Digite o nome da empresa" />
          </div>
          <div>
            <Label htmlFor="cnpj">CNPJ</Label>
            <Input id="cnpj" type="text" placeholder="Digite o CNPJ" />
          </div>
          <div>
            <Label htmlFor="email">Email</Label>
            <Input id="email" type="email" placeholder="Digite o email" />
          </div>
          <div>
            <Label htmlFor="password">Senha</Label>
            <Input id="password" type="password" placeholder="Digite a senha" />
          </div>
          <Button type="submit" className="w-full rounded-2xl border-black border-2">Cadastrar</Button>
        </form>
        </div>
      );
    } else if (userType === "cliente") {
      return (
        <div>
          <div className="font-bold"> Passo 2: </div>
          <div className="mb-4"> Digite suas informações: </div>
          <form className="space-y-4 flex flex-col">
          <div>
            <Label htmlFor="fullName">Nome Completo: </Label>
            <Input id="fullName" type="text" placeholder="Digite seu nome completo" />
          </div>
          <div>
            <Label htmlFor="email">Email: </Label>
            <Input id="email" type="email" placeholder="Digite o email" />
          </div>
          <div>
            <Label htmlFor="password">Senha: </Label>
            <Input id="password" type="password" placeholder="Digite a senha" />
          </div>
          <Button type="submit" className="rounded-2xl border-black border-2 flex justify-center">Cadastrar</Button>
        </form>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="flex h-screen">
      <div className="relative w-3/4 h-full flex justify-center bg-[#FFCF00]">
        <Image src="/Frame5.jpg" alt="teste" width={800} height={0} className="object-cover"></Image>
      </div>
      <main className="w-1/4 flex flex-col justify-center items-center">
        <Image src="/Logo.png" alt="logo" width={174} height={0} className="m-4" ></Image>
        <Card className="mt-4 rounded-xl border-black self-center">
          <CardHeader className="flex items-center">
            <CardTitle>Criar conta</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col">
            <div className="font-bold"> Passo 1: </div>
            <div> Voce deseja se cadastrar como: </div>
            <div className="flex flex-col justify-around mb-4">
              <Button
                className="bg-[#FFCF00] gap-4 mt-4 mb-4" 
                onClick={() => setUserType("varejista")} 
                variant={userType === "varejista" ? "default" : "outline"}
              >
                Varejista
              </Button>
              <div className="flex justify-center"> ou </div>
              <Button
                className="mt-4 mb-4 gap-4" 
                onClick={() => setUserType("cliente")} 
                variant={userType === "cliente" ? "default" : "outline"}
              >
                Cliente
              </Button>
            </div>
            {renderForm()}
          </CardContent>
        </Card>
      </main>
    </div>
  );
} 