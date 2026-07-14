export default function AIAssistant() {
  return (
    <div className="rounded-2xl bg-gradient-to-br from-indigo-600 to-purple-600 p-6 text-white shadow-lg">

      <h2 className="text-2xl font-bold">
        🤖 AI Career Assistant
      </h2>

      <p className="mt-3 opacity-90">
        Based on your resume and recent activity,
        here's what I recommend today.
      </p>

      <ul className="mt-6 space-y-3">

        <li>✅ Improve Docker skills</li>

        <li>📚 Solve 2 DSA questions</li>

        <li>💼 Apply to 5 internships</li>

        <li>🎤 Practice SQL Interview</li>

      </ul>

    </div>
  );
}