"use client";

import { useEffect, useState } from "react";

import {
  Target,
  Briefcase,
  Mic,
  Route,
} from "lucide-react";

import StatCard from "@/components/ui/StatCard";
import { getDashboard } from "@/services/dashboard";

export default function DashboardStats() {
  const [loading, setLoading] = useState(true);
  const [dashboard, setDashboard] = useState<any>({});

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      const data = await getDashboard();
      setDashboard(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return (
      <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">
        {Array.from({ length: 4 }).map((_, i) => (
          <div
            key={i}
            className="h-32 animate-pulse rounded-xl bg-gray-200"
          />
        ))}
      </div>
    );
  }

  return (
    <div className="grid gap-6 sm:grid-cols-2 xl:grid-cols-4">

      <StatCard
        title="ATS Score"
        value={`${dashboard.ats_score ?? 0}%`}
        color="text-emerald-600"
        icon={<Target size={24} />}
      />

      <StatCard
        title="Resume Score"
        value={`${dashboard.resume_score ?? 0}`}
        color="text-indigo-600"
        icon={<Briefcase size={24} />}
      />

      <StatCard
        title="Interview Questions"
        value={`${dashboard.interview_questions ?? 0}`}
        color="text-purple-600"
        icon={<Mic size={24} />}
      />

      <StatCard
        title="Job Matches"
        value={`${dashboard.job_matches ?? 0}`}
        color="text-cyan-600"
        icon={<Route size={24} />}
      />

    </div>
  );
}