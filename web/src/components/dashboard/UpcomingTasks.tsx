export default function UpcomingTasks() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md">

      <h2 className="text-xl font-semibold">
        Upcoming Tasks
      </h2>

      <div className="mt-5 space-y-3">

        <div className="rounded-lg border p-3">
          📄 Update Resume
        </div>

        <div className="rounded-lg border p-3">
          💼 Apply to Microsoft
        </div>

        <div className="rounded-lg border p-3">
          🎤 Mock Interview
        </div>

        <div className="rounded-lg border p-3">
          📚 Finish Roadmap Week 3
        </div>

      </div>

    </div>
  );
}