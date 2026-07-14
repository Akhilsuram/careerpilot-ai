"use client";

import { useEffect, useState } from "react";
import { analyzeATS } from "@/services/ats";

export default function ATSOverview() {
  const [ats, setATS] = useState<any>(null);

  useEffect(() => {
    async function load() {
      const stored = localStorage.getItem("careerpilot_resume");

      if (!stored) return;

      const resume = JSON.parse(stored);

      const result = await analyzeATS(
        resume.data
      );

      setATS(result.data);
    }

    load();
  }, []);

  if (!ats) {
    return (
      <div className="rounded-3xl bg-white p-8 shadow">
        Loading ATS...
      </div>
    );
  }

  return (
    <div className="rounded-3xl bg-gradient-to-r from-emerald-500 to-green-600 p-8 text-white shadow-lg">

      <h1 className="text-3xl font-bold">
        ATS Score
      </h1>

      <div className="mt-8 flex items-center gap-10">

        <div className="text-7xl font-bold">
          {ats.overall_score}%
        </div>

        <div>
          <p className="text-lg">
            Resume ATS Analysis
          </p>

          <p className="mt-2">
            {ats.strengths?.length || 0} strengths found
          </p>

          <p>
            {ats.weaknesses?.length || 0} weaknesses found
          </p>

        </div>

      </div>

    </div>
  );
}