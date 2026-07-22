"use client";

import { useState } from "react";
import toast from "react-hot-toast";
import PrimaryButton from "@/components/common/PrimaryButton";
import { optimizeResume } from "@/services/resumeOptimizer";

interface Props {
  onComplete: (data: any) => void;
}

export default function ResumeOptimizerInput({
  onComplete,
}: Props) {
  const [role, setRole] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem("careerpilot_resume");

    if (!stored) {
      toast.error("Upload resume first.");
      return;
    }

    if (!role.trim()) {
      alert("Enter a target role.");
      return;
    }

    const resume = JSON.parse(stored);

    setLoading(true);

    try {
      const result = await optimizeResume(
        resume.data,
        role
      );
      console.log("========== RESPONSE ==========");
      console.log(result);
      console.log(result.data);

      onComplete(result.data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="rounded-3xl bg-white p-8 shadow">
      <h1 className="text-3xl font-bold">
        Resume Optimizer
      </h1>

      <input
        className="mt-6 w-full rounded-xl border p-4"
        placeholder="Target Role (Example: AI Engineer)"
        value={role}
        onChange={(e) => setRole(e.target.value)}
      />

      <div className="mt-6">
        <PrimaryButton
          onClick={run}
          disabled={loading}
        >
          {loading
            ? "Optimizing..."
            : "Optimize Resume"}
        </PrimaryButton>
      </div>
    </div>
  );
}