"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import toast from "react-hot-toast";

import {
  Bell,
  Search,
  Sparkles,
  Menu,
} from "lucide-react";

interface HeaderProps {
  onMenuClick: () => void;
}

export default function Header({
  onMenuClick,
}: HeaderProps) {

  const router = useRouter();

  const [search, setSearch] = useState("");

  const [showStatus, setShowStatus] = useState(false);

  const [showNotifications, setShowNotifications] = useState(false);

  const handleSearch = () => {

    const q = search.trim().toLowerCase();

    const routes: Record<string, string> = {
      dashboard: "/dashboard",
      report: "/report",
      ai: "/report",
      resume: "/resume",
      ats: "/ats",
      optimizer: "/resume-optimizer",
      "resume optimizer": "/resume-optimizer",
      jobs: "/jobs",
      interview: "/interview",
      roadmap: "/roadmap",
      analytics: "/analytics",
      history: "/history",
    };

    if (routes[q]) {

      router.push(routes[q]);

      setSearch("");

      return;

    }

    toast.error("No matching page found.");

  };

  return (

    <header className="sticky top-0 z-40 border-b border-slate-200 bg-white/80 backdrop-blur-xl">

      <div className="flex h-20 items-center justify-between px-4 lg:px-10">

        {/* Left */}

        <div className="flex items-center gap-4">

          <button
            onClick={() => {
              alert("clicked");
              console.log("clicked");
              onMenuClick();
            }}
            className="rounded-xl p-2 hover:bg-slate-100 lg:hidden"
          >
            <Menu size={24} />
          </button>

          <div>

            <h1 className="text-xl font-bold text-slate-900 lg:text-2xl">

              Welcome Back 👋

            </h1>

            <p className="hidden text-slate-500 md:block">

              Let's build your career today.

            </p>

          </div>

        </div>

        {/* Right */}

        <div className="flex items-center gap-2 lg:gap-5">

          {/* Search */}

          <div className="hidden items-center gap-3 rounded-2xl border border-slate-200 bg-slate-50 px-5 py-3 md:flex">

            <Search
              size={18}
              className="cursor-pointer text-slate-500"
              onClick={handleSearch}
            />

            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  handleSearch();
                }
              }}
              placeholder="Search pages..."
              className="w-full bg-transparent outline-none"
            />

          </div>

          {/* Notifications */}

          <div className="relative">

            <button
              onClick={() =>
                setShowNotifications(!showNotifications)
              }
              className="rounded-xl border bg-white p-3 shadow-sm transition hover:bg-slate-100"
            >

              <Bell size={20} />

            </button>

            {showNotifications && (

              <div className="absolute right-0 z-50 mt-3 w-80 rounded-2xl border bg-white p-5 shadow-xl">

                <h3 className="mb-4 font-bold">

                  Notifications

                </h3>

                <div className="space-y-3 text-sm">

                  <p>✅ Welcome to CareerPilot AI</p>

                  <p>✅ Resume analyzed successfully</p>

                  <p>✅ ATS analysis completed</p>

                  <p>✅ Career roadmap generated</p>

                </div>

              </div>

            )}

          </div>

          {/* AI Ready */}

          <div className="relative">

            <button
              onClick={() =>
                setShowStatus(!showStatus)
              }
              className="rounded-xl bg-gradient-to-r from-violet-600 to-fuchsia-600 px-4 py-3 font-semibold text-white shadow-lg lg:px-6"
            >

              <div className="flex items-center gap-2">

                <Sparkles size={18} />

                <span className="hidden sm:inline">

                  AI Ready

                </span>

              </div>

            </button>

            {showStatus && (

              <div className="absolute right-0 z-50 mt-3 w-72 rounded-2xl border bg-white p-5 shadow-xl">

                <h3 className="mb-4 font-bold">

                  System Status

                </h3>

                <div className="space-y-3 text-sm">

                  <p>🟢 Backend Connected</p>

                  <p>🟢 Groq Ready</p>

                  <p>🟢 SQLite Connected</p>

                  <p>🟢 AI Agents Online</p>

                </div>

              </div>

            )}

          </div>

        </div>

      </div>

    </header>

  );

}