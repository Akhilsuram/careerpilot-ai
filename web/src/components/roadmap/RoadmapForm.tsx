"use client";

import { useState } from "react";
import { Route } from "lucide-react";
import toast from "react-hot-toast";

import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";
import Button from "@/components/ui/Button";

import { generateRoadmap } from "@/services/roadmap";

interface Props {
  onComplete: (roadmap: any[]) => void;
}

export default function RoadmapForm({ onComplete }: Props) {
  const [role, setRole] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem("careerpilot_resume");

    if (!stored) {
      toast.error("Upload resume first.");
      return;
    }

    if (!role.trim()) {
      toast.error("Enter a target role.");
      return;
    }

    const resume = JSON.parse(stored);

    setLoading(true);

    try {
      const result = await generateRoadmap(
        resume.data,
        role
      );

      console.log("Roadmap API Response:", result);
      console.log("Roadmap Data:", result.data);
      console.log("Roadmap Array:", result.data?.roadmap);

      if (!result.success) {
        toast.error(result.message || "Failed to generate roadmap.");
        return;
      }

      onComplete(result.data.roadmap);

      toast.success("Roadmap generated successfully!");
    } catch (error) {
      console.error("Roadmap Error:", error);
      toast.error("Failed to generate roadmap.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>
      <PageHeader
        title="Career Roadmap"
        subtitle="Generate a personalized learning roadmap."
      />

      <div className="mt-8 rounded-3xl border-2 border-dashed border-indigo-300 bg-gradient-to-br from-indigo-50 to-cyan-50 p-8">
        <div className="mb-6 flex items-center gap-3">
          <Route
            size={28}
            className="text-indigo-600"
          />

          <h2 className="text-xl font-semibold">
            Target Role
          </h2>
        </div>

        <input
          className="w-full rounded-2xl border border-slate-200 p-4 outline-none focus:border-indigo-500"
          placeholder="AI Engineer"
          value={role}
          onChange={(e) => setRole(e.target.value)}
        />

        <div className="mt-8">
          <Button
            loading={loading}
            onClick={run}
          >
            Generate Roadmap
          </Button>
        </div>
      </div>
    </Card>
  );
}