"use client"; // Adicione esta linha no topo do arquivo

import Image from "next/image";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

export default function CreateAccount() {
  const [userType, setUserType] = useState<"varejista" | "cliente" | null>(null);
  const [formData, setFormData] = useState({
    nome: "",
    email: "",
    password: "",
    identificador: "",
  });
  const [profileImg, setProfileImg] = useState(null);
  const [message, setMessage] = useState("");

  // Atualiza os campos do formulário
  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setFormData({ ...formData, [id]: value });
  };

  // Atualiza a imagem de perfil
  const handleFileChange = (e) => {
    setProfileImg(e.target.files[0]);
  };

  // Envia os dados para a API Flask
  const handleSubmit = async (e) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append("email", formData.email);
    formDataToSend.append("password", formData.password);
    formDataToSend.append("nome", formData.nome);
    formDataToSend.append("administrador", false); // Sempre falso
    formDataToSend.append("feirante", userType === "varejista"); // True apenas para "varejista"
    formDataToSend.append("identificador", formData.identificador);
    
    if (profileImg) {
      formDataToSend.append("foto_perfil", profileImg);
    }

    try {
      const response = await fetch("http://localhost:5000/auth/signup", {
        method: "POST",
        body: formDataToSend,
        headers: {
          "Accept": "application/json"
        },
      });

      const data = await response.json();

      if (response.ok) {
        setMessage("Cadastro realizado com sucesso!");
      } else {
        setMessage(`Erro: ${data.msg}`);
      }
    } catch (error) {
      setMessage("Erro ao conectar com o servidor.");
    }
  };

  const renderForm = () => {
    if (userType) {
      return (
        <div>
          <div className="font-bold"> Passo 2: </div>
          <div className="mb-4"> Digite suas informações: </div>
          <form className="space-y-4" onSubmit={handleSubmit} encType="multipart/form-data">
            <div>
              <Label htmlFor="nome">Nome</Label>
              <Input id="nome" type="text" placeholder="Digite seu nome" value={formData.nome} onChange={handleInputChange} />
            </div>
            <div>
              <Label htmlFor="email">Email</Label>
              <Input id="email" type="email" placeholder="Digite o email" value={formData.email} onChange={handleInputChange} />
            </div>
            <div>
              <Label htmlFor="password">Senha</Label>
              <Input id="password" type="password" placeholder="Digite a senha" value={formData.password} onChange={handleInputChange} />
            </div>
            <div>
              <Label htmlFor="identificador">{userType === "varejista" ? "CNPJ" : "CPF"}</Label>
              <Input id="identificador" type="text" placeholder={`Digite seu ${userType === "varejista" ? "CNPJ" : "CPF"}`} value={formData.identificador} onChange={handleInputChange} />
            </div>
            <div>
              <Label htmlFor="foto_perfil">Foto de Perfil</Label>
              <Input id="foto_perfil" type="file" accept="image/*" onChange={handleFileChange} />
            </div>
            <Button type="submit" className="w-full rounded-2xl border-black border-2">Cadastrar</Button>
          </form>
          {message && <p className="mt-4 text-center text-red-500">{message}</p>}
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
        <Image src="/Logo.png" alt="logo" width={174} height={0} className="m-4"></Image>
        <Card className="mt-4 rounded-xl border-black self-center">
          <CardHeader className="flex items-center">
            <CardTitle>Criar conta</CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col">
            <div className="font-bold"> Passo 1: </div>
            <div> Você deseja se cadastrar como: </div>
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
