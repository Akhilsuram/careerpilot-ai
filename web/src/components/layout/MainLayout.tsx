"use client";

import Sidebar from "./Sidebar";
import Header from "./Header";

interface Props {
  children: React.ReactNode;
}

export default function MainLayout({
  children,
}: Props) {

  return (

    <div className="min-h-screen bg-slate-50">

      <Sidebar />

      <div className="min-h-screen ml-72">

        <Header />

        <main className="px-10 py-8">

          {children}

        </main>

      </div>

    </div>

  );

}