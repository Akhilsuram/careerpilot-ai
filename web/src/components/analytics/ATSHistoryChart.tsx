"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

interface Props {
  history: any[];
}

export default function ATSHistoryChart({
  history,
}: Props) {

  return (

    <Card>

      <PageHeader
        title="ATS Score Trend"
        subtitle="Track your ATS improvement over time."
      />

      <div className="mt-8 h-96">

        <ResponsiveContainer
          width="100%"
          height="100%"
        >

          <LineChart
            data={history}
          >

            <CartesianGrid
              strokeDasharray="3 3"
            />

            <XAxis
              dataKey="id"
            />

            <YAxis />

            <Tooltip />

            <Line
              type="monotone"
              dataKey="score"
              stroke="#6366f1"
              strokeWidth={4}
            />

          </LineChart>

        </ResponsiveContainer>

      </div>

    </Card>

  );

}