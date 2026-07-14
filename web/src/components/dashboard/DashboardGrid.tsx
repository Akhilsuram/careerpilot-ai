import QuickActions from "./QuickActions";

export default function DashboardGrid() {
  return (
    <div className="grid grid-cols-3 gap-6">
      <div className="col-span-2 rounded-2xl bg-white p-6 shadow">
        <h2 className="mb-4 text-2xl font-semibold">
          Dashboard Overview
        </h2>

        <QuickActions />

        <div className="mt-8 h-64 rounded-xl border-2 border-dashed border-gray-300 flex items-center justify-center text-gray-400">
          ATS Chart (Coming Next)
        </div>
      </div>

      <div className="rounded-2xl bg-white p-6 shadow">
        <h2 className="mb-4 text-xl font-semibold">
          AI Insights
        </h2>

        <ul className="space-y-3 text-gray-700">
          <li>✅ Resume is ATS friendly.</li>
          <li>📈 Add Docker & AWS to improve score.</li>
          <li>💼 42 matching jobs available.</li>
          <li>🎯 Practice SQL interview questions.</li>
        </ul>
      </div>
    </div>
  );
}