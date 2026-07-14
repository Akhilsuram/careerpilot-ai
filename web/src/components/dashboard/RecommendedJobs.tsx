import { recommendedJobs } from "@/lib/dashboard-data";

export default function RecommendedJobs() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md">

      <h2 className="mb-5 text-xl font-semibold">
        Recommended Jobs
      </h2>

      <div className="space-y-4">

        {recommendedJobs.map((job) => (
          <div
            key={job.company}
            className="rounded-xl border p-4"
          >
            <h3 className="font-semibold">
              {job.role}
            </h3>

            <p className="text-gray-500">
              {job.company}
            </p>

            <p className="mt-2 text-indigo-600 font-semibold">
              Match: {job.match}%
            </p>
          </div>
        ))}

      </div>

    </div>
  );
}