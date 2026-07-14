"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";


import {
  LayoutDashboard,
  FileText,
  BarChart3,
  Briefcase,
  Mic,
  Route,
  Activity,
  History,
  Settings,
  Cpu,
  Database,
  Bot,
  Sparkles,
} from "lucide-react";
const menu = [
  {
    name: "Dashboard",
    href: "/dashboard",
    icon: LayoutDashboard,
  },
  {
    name: "Resume",
    href: "/resume",
    icon: FileText,
  },
  {
    name: "ATS Analysis",
    href: "/ats",
    icon: BarChart3,
  },
  {
    name: "Resume Optimizer",
    href: "/resume-optimizer",
    icon: Sparkles,
  },
  {
    name: "Jobs",
    href: "/jobs",
    icon: Briefcase,
  },
  {
    name: "Interview",
    href: "/interview",
    icon: Mic,
  },
  {
    name: "Roadmap",
    href: "/roadmap",
    icon: Route,
  },
  {
    name: "Analytics",
    href: "/analytics",
    icon: Activity,
  },
  {
    name: "History",
    href: "/history",
    icon: History,
  },
  {
    name: "Settings",
    href: "/settings",
    icon: Settings,
  },
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 flex h-screen w-72 flex-col border-r bg-white shadow-sm">

      <div className="border-b p-6">

        <h1 className="text-3xl font-bold text-indigo-600">
          CareerPilot AI
        </h1>

        <p className="mt-1 text-sm text-gray-500">
          Multi-Agent Career Copilot
        </p>

      </div>

      <nav className="flex-1 space-y-2 overflow-y-auto p-5">

        {menu.map((item) => {

          const Icon = item.icon;

          const active = pathname === item.href;

          return (
            <Link
              key={item.href}
              href={item.href}
              className={`flex items-center gap-4 rounded-xl px-4 py-3 transition-all ${
                active
                  ? "bg-indigo-600 text-white shadow-lg"
                  : "text-gray-600 hover:bg-gray-100"
              }`}
            >
              <Icon size={20} />

              <span>{item.name}</span>

            </Link>
          );
        })}

      </nav>

      <div className="border-t p-5">

        <h3 className="mb-4 text-sm font-semibold text-gray-500">
          SYSTEM STATUS
        </h3>

        <div className="space-y-3">

          <div className="flex items-center gap-3">
            <Bot size={18} className="text-green-500" />
            <span className="text-sm">AI Agents Online</span>
          </div>

          <div className="flex items-center gap-3">
            <Database size={18} className="text-green-500" />
            <span className="text-sm">SQLite Connected</span>
          </div>

          <div className="flex items-center gap-3">
            <Cpu size={18} className="text-green-500" />
            <span className="text-sm">Groq Ready</span>
          </div>

        </div>

        <div className="mt-8 rounded-xl bg-slate-100 p-4">

          <p className="font-semibold">
            👤 Akhil
          </p>

          <p className="text-sm text-gray-500">
            AI Engineer
          </p>

        </div>

      </div>

    </aside>
  );
}