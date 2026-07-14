import { recentActivity } from "@/lib/dashboard-data";

export default function ActivityTimeline() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md">

      <h2 className="mb-5 text-xl font-semibold">
        Recent Activity
      </h2>

      <div className="space-y-4">

        {recentActivity.map((item, index) => (
          <div
            key={index}
            className="rounded-lg border p-3"
          >
            {item}
          </div>
        ))}

      </div>

    </div>
  );
}