export default function Header() {
  return (
    <header className="h-20 bg-white border-b flex items-center justify-between px-8">
      <div>
        <h2 className="text-3xl font-bold">
          Welcome Back 👋
        </h2>

        <p className="text-gray-500">
          Build your career with AI.
        </p>
      </div>

      <div className="flex items-center gap-4">
        <div className="h-12 w-12 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold">
          A
        </div>
      </div>
    </header>
  );
}