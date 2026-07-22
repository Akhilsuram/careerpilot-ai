"use client";

import { useState } from "react";
import { Briefcase } from "lucide-react";
import toast from "react-hot-toast";

import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";
import Button from "@/components/ui/Button";

import { searchJobs } from "@/services/jobs";

interface Props {
  onComplete: (jobs: any[]) => void;
}

export default function JobSearchForm({
  onComplete,
}: Props) {
  const [targetRole, setTargetRole] = useState("");
  const [location, setLocation] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem("careerpilot_resume");

    if (!stored) {
      toast.error("Upload resume first.");
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

      onComplete(result.data.jobs);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>

      <PageHeader
        title="AI Job Matching"
        subtitle="Discover jobs that best match your resume."
      />

      <div className="mt-8 rounded-3xl border-2 border-dashed border-indigo-300 bg-gradient-to-br from-indigo-50 to-cyan-50 p-8">

        <div className="mb-6 flex items-center gap-3">

          <Briefcase
            size={28}
            className="text-indigo-600"
          />

          <h2 className="text-xl font-semibold">
            Search Criteria
          </h2>

        </div>

        <div className="space-y-5">

          <input
            className="w-full rounded-2xl border border-slate-200 p-4 outline-none focus:border-indigo-500"
            placeholder="Target Role (AI Engineer)"
            value={targetRole}
            onChange={(e) => setTargetRole(e.target.value)}
          />

          <input
            className="w-full rounded-2xl border border-slate-200 p-4 outline-none focus:border-indigo-500"
            placeholder="Location (Optional)"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />

        </div>

        <div className="mt-8">

          <Button
            loading={loading}
            onClick={run}
          >
            Find Matching Jobs
          </Button>

        </div>

      </div>

    </Card>
  );
}