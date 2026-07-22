"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef } from "react";

import {
  LayoutDashboard,
  Sparkles,
  FileText,
  BarChart3,
  Briefcase,
  Mic,
  Route,
  Activity,
  History,
  Cpu,
  Database,
  Bot,
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
    name: "AI Report",
    href: "/report",
    icon: Sparkles,
  },
  {
    name: "History",
    href: "/history",
    icon: History,
  },
];

interface SidebarProps {
  open: boolean;
  onClose: () => void;
}

export default function Sidebar({
  open,
  onClose,
}: SidebarProps) {

  const pathname = usePathname();
  const sidebarRef = useRef<HTMLDivElement>(null);

  useEffect(() => {

    const saved = sessionStorage.getItem(
      "careerpilot-sidebar-scroll"
    );

    if (saved && sidebarRef.current) {
      sidebarRef.current.scrollTop = Number(saved);
    }

  }, []);

  return (
    <>

      {/* Mobile Overlay */}

      {open && (

        <div
          className="fixed inset-0 z-40 bg-black/40 lg:hidden"
          onClick={() => onClose()}
        />

      )}

      {/* Sidebar */}

      <aside
        className={`
          fixed left-0 top-0 z-50 flex h-screen w-72 flex-col
          border-r border-slate-200 bg-white/95 backdrop-blur-md shadow-xl
          transition-transform duration-300
          ${open ? "translate-x-0" : "-translate-x-full"}
          lg:translate-x-0
        `}
      >

        {/* Logo */}

        <div className="border-b border-slate-200 p-7">

          <Link
            href="/dashboard"
            className="flex items-center gap-3"
          >

            <div className="flex h-12 w-12 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-600 to-purple-600 text-white shadow-lg">
              🤖
            </div>

            <div>

              <h1 className="text-2xl font-bold text-slate-900">
                CareerPilot AI
              </h1>

              <p className="text-sm text-slate-500">
                Multi-Agent Career Copilot
              </p>

            </div>

          </Link>

        </div>

        {/* Navigation */}

        <nav
          ref={sidebarRef}
          className="flex-1 space-y-2 overflow-y-auto p-5"
          onScroll={(e) =>
            sessionStorage.setItem(
              "careerpilot-sidebar-scroll",
              e.currentTarget.scrollTop.toString()
            )
          }
        >

          {menu.map((item) => {

            const Icon = item.icon;

            const active = pathname === item.href;

            return (

              <Link
                key={item.href}
                href={item.href}
                onClick={() => onClose()}
                className={`group flex items-center gap-4 rounded-2xl px-5 py-3 font-medium transition-all duration-200 ${
                  active
                    ? "bg-gradient-to-r from-indigo-600 to-purple-600 text-white shadow-lg"
                    : "text-slate-600 hover:bg-slate-100 hover:text-slate-900"
                }`}
              >

                <Icon size={20} />

                <span>{item.name}</span>

              </Link>

            );

          })}

        </nav>

        {/* System Status */}

        <div className="border-t border-slate-200 p-6">

          <h3 className="mb-4 text-sm font-semibold text-gray-500">
            SYSTEM STATUS
          </h3>

          <div className="space-y-3">

            <div className="flex items-center gap-3">

              <Bot
                size={18}
                className="text-emerald-500"
              />

              <span className="text-sm text-slate-700">
                AI Agents Online
              </span>

            </div>

            <div className="flex items-center gap-3">

              <Database
                size={18}
                className="text-emerald-500"
              />

              <span className="text-sm text-slate-700">
                SQLite Connected
              </span>

            </div>

            <div className="flex items-center gap-3">

              <Cpu
                size={18}
                className="text-emerald-500"
              />

              <span className="text-sm text-slate-700">
                Groq Ready
              </span>

            </div>

          </div>

          <div className="mt-8 rounded-2xl border border-slate-200 bg-gradient-to-r from-slate-50 to-indigo-50 p-5">

            <p className="font-semibold text-slate-900">
              👤 Akhil
            </p>

            <p className="text-sm text-gray-500">
              AI Engineer
            </p>

          </div>

        </div>

      </aside>

    </>
  );

}