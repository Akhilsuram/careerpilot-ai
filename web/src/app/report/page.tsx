"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";
import { runCareerCopilot } from "@/services/careerCopilot";
import CareerReport from "@/components/report/CareerReport";

export default function ReportPage() {
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState<any>(null);
  const [targetRole, setTargetRole] = useState("");

  async function generateReport() {
    try {
      const stored = localStorage.getItem("careerpilot_resume");

      if (!stored) {
        alert("Please upload a resume first.");
        return;
      }

      if (!targetRole.trim()) {
        alert("Please enter a target role.");
        return;
      }

      setLoading(true);

      const resume = JSON.parse(stored);

      const response = await runCareerCopilot({
        resume_data: resume.data,
        target_role: targetRole,
      });

      console.log(response);

      setReport(response.data);

    } catch (err) {
      console.error(err);
      alert("Failed to generate report");
    } finally {
      setLoading(false);
    }
  }

  return (
    <MainLayout>
      <div className="space-y-6">

        <div className="flex items-center justify-between gap-8">

          <div className="flex-1 space-y-4">

            <div>
              <h1 className="text-4xl font-bold">
                AI Career Report
              </h1>

              <p className="mt-2 text-gray-500">
                Complete Multi-Agent Career Analysis
              </p>
            </div>

            <input
              className="w-full rounded-xl border p-4"
              placeholder="Enter Target Role (Example: Software Engineer)"
              value={targetRole}
              onChange={(e) => setTargetRole(e.target.value)}
            />

          </div>

          <button
            onClick={generateReport}
            disabled={loading}
            className="rounded-xl bg-violet-600 px-6 py-3 text-white hover:bg-violet-700 disabled:opacity-50"
          >
            {loading ? "Generating..." : "Generate Report"}
          </button>

        </div>

        {report && (
          <div className="rounded-2xl border bg-white p-6 shadow">
            <CareerReport report={report} />
          </div>
        )}

      </div>
    </MainLayout>
  );
}