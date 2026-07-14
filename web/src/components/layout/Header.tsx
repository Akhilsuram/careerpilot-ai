import {
  Bell,
  Search,
} from "lucide-react";

export default function Header() {
  return (
    <header className="flex h-20 items-center justify-between border-b bg-white px-10">

      <div>

        <h2 className="text-3xl font-bold">
          Dashboard
        </h2>

        <p className="text-gray-500">
          Welcome back, Akhil 👋
        </p>

      </div>

      <div className="flex items-center gap-5">

        <div className="flex items-center rounded-xl border bg-slate-50 px-4 py-2">

          <Search size={18} />

          <input
            placeholder="Search..."
            className="ml-2 bg-transparent outline-none"
          />

        </div>

        <button className="rounded-xl bg-slate-100 p-3">

          <Bell size={20} />

        </button>

      </div>

    </header>
  );
}