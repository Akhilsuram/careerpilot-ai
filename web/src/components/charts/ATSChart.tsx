"use client";

import {
  LineChart,
  Line,
  XAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import { atsHistory } from "@/lib/dashboard-data";

export default function ATSChart() {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md">

      <h2 className="mb-6 text-xl font-semibold">
        ATS Score Trend
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >
        <LineChart data={atsHistory}>
          <XAxis dataKey="month" />
          <Tooltip />
          <Line
            dataKey="score"
            stroke="#4F46E5"
            strokeWidth={4}
          />
        </LineChart>
      </ResponsiveContainer>

    </div>
  );
}