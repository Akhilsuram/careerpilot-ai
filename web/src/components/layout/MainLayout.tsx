"use client";

import { useState } from "react";

import Sidebar from "./Sidebar";
import Header from "./Header";

interface Props {
  children: React.ReactNode;
}

export default function MainLayout({
  children,
}: Props) {

  const [sidebarOpen, setSidebarOpen] = useState(false);
  console.log("sidebarOpen =", sidebarOpen);
  return (

    <div className="min-h-screen bg-slate-50">

      <Sidebar
        open={sidebarOpen}
        onClose={() => setSidebarOpen(false)}
      />

      <div className="min-h-screen lg:ml-72">

        <Header
          onMenuClick={() => {
            console.log("Opening sidebar");
            setSidebarOpen(true);
          }}
        />

        <main className="px-4 py-6 lg:px-10 lg:py-8">

          {children}

        </main>

      </div>

    </div>

  );

}