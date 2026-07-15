"use client";

import { useState } from "react";
import PrimaryButton from "@/components/common/PrimaryButton";
import { searchJobs } from "@/services/jobs";

interface Props {
  onComplete: (jobs: any[]) => void;
}

export default function JobSearchForm({ onComplete }: Props) {
  const [targetRole, setTargetRole] = useState("");
  const [location, setLocation] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem("careerpilot_resume");

    if (!stored) {
      alert("Please upload your resume first.");
      return;
    }

    if (!targetRole.trim()) {
      alert("Please enter a target role.");
      return;
    }

    const resume = JSON.parse(stored);

    setLoading(true);

    try {
      const result = await searchJobs(
        resume.data,
        targetRole,
        location
      );
      console.log(result);
      
      onComplete(result.data.jobs);

    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h1 className="text-3xl font-bold">
        AI Job Match
      </h1>

      <div className="mt-6 space-y-4">

        <input
          className="w-full rounded-xl border p-4"
          placeholder="Target Role"
          value={targetRole}
          onChange={(e) => setTargetRole(e.target.value)}
        />

        <input
          className="w-full rounded-xl border p-4"
          placeholder="Location (Optional)"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
        />

      </div>

      <div className="mt-6">
        <PrimaryButton
          onClick={run}
          disabled={loading}
        >
          {loading ? "Searching..." : "Find Jobs"}
        </PrimaryButton>
      </div>

    </div>
  );
}