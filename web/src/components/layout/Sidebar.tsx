export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-screen w-72 bg-slate-900 text-white p-8">

      <h1 className="text-3xl font-bold mb-10">
        🚀 CareerPilot AI
      </h1>

      <nav className="space-y-4">

        <p className="hover:text-indigo-300 cursor-pointer">
          Dashboard
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Resume
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          ATS
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Jobs
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Interview
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Roadmap
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Analytics
        </p>

        <p className="hover:text-indigo-300 cursor-pointer">
          Settings
        </p>

      </nav>

    </aside>
  );
}