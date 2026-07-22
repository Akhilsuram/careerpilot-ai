"use client";

import { useState } from "react";
import { Mic } from "lucide-react";

import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";
import Button from "@/components/ui/Button";
import toast from "react-hot-toast";

import { generateInterview } from "@/services/interview";

interface Props {
  onComplete: (questions: any[]) => void;
}

export default function InterviewForm({
  onComplete,
}: Props) {
  const [role, setRole] = useState("");
  const [jd, setJD] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem("careerpilot_resume");

    if (!stored) {
      toast.error("Upload resume first.");
      return;
    }

    if (!role.trim()) {
      alert("Please enter a target role.");
      return;
    }

    const resume = JSON.parse(stored);

    setLoading(true);

    try {
      const result = await generateInterview(
        resume.data,
        role,
        jd
      );

      onComplete(result.data.questions);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>

      <PageHeader
        title="AI Interview Preparation"
        subtitle="Generate personalized interview questions based on your resume."
      />

      <div className="mt-8 rounded-3xl border-2 border-dashed border-indigo-300 bg-gradient-to-br from-indigo-50 to-cyan-50 p-8">

        <div className="mb-6 flex items-center gap-3">

          <Mic
            size={28}
            className="text-indigo-600"
          />

          <h2 className="text-xl font-semibold">
            Interview Settings
          </h2>

        </div>

        <div className="space-y-5">

          <input
            className="w-full rounded-2xl border border-slate-200 p-4 outline-none focus:border-indigo-500"
            placeholder="Target Role"
            value={role}
            onChange={(e) => setRole(e.target.value)}
          />

          <textarea
            rows={8}
            className="w-full rounded-2xl border border-slate-200 p-4 outline-none focus:border-indigo-500"
            placeholder="Paste Job Description (Optional)"
            value={jd}
            onChange={(e) => setJD(e.target.value)}
          />

        </div>

        <div className="mt-8">

          <Button
            loading={loading}
            onClick={run}
          >
            Generate Questions
          </Button>

        </div>

      </div>

    </Card>
  );
}