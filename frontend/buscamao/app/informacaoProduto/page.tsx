"use client"

import type React from "react"
import { useState } from "react"
import Image from "next/image"
import Footer from "@/app/components/Footer"
import { Heart, Send } from "lucide-react"
import Navbar from "../components/NavBar"

interface Comment {
  id: number
  author: string
  text: string
  date: string
}

export default function InfoProd() {
  const [comments, setComments] = useState<Comment[]>([
    { id: 1, author: "João Silva", text: "Ótimo produto!", date: "2023-06-01" },
    { id: 2, author: "Maria Santos", text: "Recomendo muito.", date: "2023-06-02" },
  ])
  const [newComment, setNewComment] = useState("")

  const handleCommentSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (newComment.trim()) {
      const comment: Comment = {
        id: comments.length + 1,
        author: "Usuário Atual", // You might want to replace this with actual user data
        text: newComment.trim(),
        date: new Date().toISOString().split("T")[0],
      }
      setComments([...comments, comment])
      setNewComment("")
    }
  }

  return (
    <main>
      <Navbar />

      <div className="max-w-2xl mx-auto p-4 space-y-6">
        {/* cartela do produto*/}
        <div className="border border-black p-4 rounded-lg">
          <div className="flex justify-between items-start">
            <div className="flex gap-4">
              {/* imagem do produto */}
              <div className="w-32 h-32 relative">
                <Image
                  src="/placeholder.svg"
                  alt="Imagem do produto"
                  layout="fill"
                  objectFit="cover"
                  className="rounded-md"
                />
              </div>

              <div>
                <h2 className="text-lg font-semibold">Título do produto com alguns detalhes</h2>
                <p className="text-lg font-bold mt-2">R$ 0000,00</p>
                <div className="flex items-center gap-2 mt-2">
                  <span>0.0</span>
                  <div className="flex">
                    {"★".repeat(0)}
                    {"☆".repeat(5)}
                  </div>
                  <span className="text-gray-500">(000)</span>
                </div>
              </div>
            </div>

            <button className="text-gray-400 hover:text-red-500">
              <Heart size={24} />
            </button>
          </div>
        </div>

        {/* comentarios */}
        <div className="p-4 border border-gray-200 rounded-lg">
          <h3 className="text-lg font-semibold mb-4">Comentários</h3>

          {/* Lista de comentários */}
          <div className="space-y-4 mb-4">
            {comments.map((comment) => (
              <div key={comment.id} className="bg-gray-50 p-3 rounded-md">
                <div className="flex justify-between items-center mb-2">
                  <span className="font-semibold">{comment.author}</span>
                  <span className="text-sm text-gray-500">{comment.date}</span>
                </div>
                <p>{comment.text}</p>
              </div>
            ))}
          </div>

          {/* Formulário de novo comentário */}
          <form onSubmit={handleCommentSubmit} className="mt-4">
            <div className="flex items-center">
              <input
                type="text"
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
                placeholder="Escreva um comentário..."
                className="flex-grow p-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <button
                type="submit"
                className="bg-blue-500 text-white p-2 rounded-r-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <Send size={20} />
              </button>
            </div>
          </form>
        </div>
      </div>
      <Footer />
    </main>
  )
}

