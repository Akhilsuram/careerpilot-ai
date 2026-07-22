"use client";

import { useEffect, useState } from "react";
import { getCareerHistory } from "@/services/dashboard";

export default function ActivityTimeline() {
  const [activities, setActivities] = useState<any[]>([]);

  useEffect(() => {
    loadActivities();
  }, []);

  async function loadActivities() {
    try {
      const data = await getCareerHistory();
      setActivities(data ?? []);
    } catch (err) {
      console.error(err);
    }
  }

  return (
    <div className="rounded-2xl bg-white p-6 shadow-md h-[370px] flex flex-col">

      <h2 className="mb-5 text-xl font-semibold">
        Recent Activity
      </h2>

      <div className="space-y-4 overflow-y-auto pr-2 flex-1 scrollbar-thin scrollbar-thumb-slate-300 scrollbar-track-transparent">

        {activities.length ? (
          activities.map((item: any, index: number) => (
            <div
              key={index}
              className="rounded-lg border p-4"
            >
              <div className="space-y-1">

                <p className="font-semibold">
                  Career Report Generated
                </p>

                <p className="text-sm text-gray-600">
                  🎯 Goal: {item.goal}
                </p>

                <p className="text-sm text-gray-600">
                  📊 ATS Score: {item.ats_score}
                </p>

                <p className="text-xs text-gray-400">
                  {new Date(item.created_at).toLocaleString()}
                </p>

              </div>
            </div>
          ))
        ) : (
          <div className="rounded-lg border p-3 text-gray-500">
            No recent activity
          </div>
        )}

      </div>

    </div>
  );
}