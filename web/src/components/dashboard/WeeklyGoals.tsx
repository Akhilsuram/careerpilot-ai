export default function WeeklyGoals() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md">

      <h2 className="text-xl font-semibold">
        Weekly Goals
      </h2>

      <div className="mt-6">

        <div className="mb-4">

          <p>Resume Improvements</p>

          <progress
            value="80"
            max="100"
            className="w-full"
          />

        </div>

        <div className="mb-4">

          <p>Job Applications</p>

          <progress
            value="45"
            max="100"
            className="w-full"
          />

        </div>

        <div>

          <p>Interview Practice</p>

          <progress
            value="60"
            max="100"
            className="w-full"
          />

        </div>

      </div>

    </div>
  );
}