import {
  Sparkles,
  TrendingUp,
} from "lucide-react";

export default function Hero() {

  return (

    <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-indigo-600 via-purple-600 to-cyan-600 p-10 text-white shadow-xl">

      <div className="absolute right-0 top-0 h-56 w-56 rounded-full bg-white/10 blur-3xl" />

      <div className="relative">

        <div className="flex items-center gap-3">

          <Sparkles size={30} />

          <h1 className="text-4xl font-bold">

            Welcome back 👋

          </h1>

        </div>

        <p className="mt-4 max-w-2xl text-lg text-indigo-100">

          Your AI-powered career copilot is ready.
          Continue improving your resume,
          interview skills and job readiness.

        </p>

        <div className="mt-8 inline-flex items-center gap-2 rounded-full bg-white/20 px-5 py-3">

          <TrendingUp size={18} />

          Career Progress Improving

        </div>

      </div>

    </div>

  );

}