'use client';

import Link from "next/link";
import { User, LogIn } from 'lucide-react';

export default function LoginButton() {
  return (
    <button className="flex items-center space-x-2 bg-white px-4 py-2 rounded-xl shadow-md">
      <Link className="flex" href="/login">
        <User />
        <span className="flex">Entrar</span>
        <LogIn className="ml-1" />
      </Link>
    </button>
  );
}