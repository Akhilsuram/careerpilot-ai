"use client";

import { useState } from "react";
import { FileSearch } from "lucide-react";
import toast from "react-hot-toast";


import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";
import Button from "@/components/ui/Button";

import { analyzeATS } from "@/services/ats";

interface Props {
  onComplete: (data: any) => void;
}

export default function ATSInput({
  onComplete,
}: Props) {
  const [jobDescription, setJobDescription] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    const stored = localStorage.getItem(
      "careerpilot_resume"
    );

    if (!stored) {
      toast.error("Upload resume first.");
      return;
    }

    const resume = JSON.parse(stored);

    setLoading(true);

    try {
      const result = await analyzeATS(
        resume.data,
        jobDescription
      );

      onComplete(result.data);
    } finally {
      setLoading(false);
    }
  }

  return (
    <Card>

      <PageHeader
        title="ATS Analysis"
        subtitle="Compare your resume with a job description using AI."
      />

      <div className="mt-8 rounded-3xl border-2 border-dashed border-indigo-300 bg-gradient-to-br from-indigo-50 to-cyan-50 p-8">

        <div className="mb-6 flex items-center gap-3">

          <FileSearch
            className="text-indigo-600"
            size={28}
          />

          <h2 className="text-xl font-semibold">
            Job Description
          </h2>

        </div>

        <textarea
          rows={10}
          className="w-full rounded-2xl border border-slate-200 bg-white p-5 outline-none transition focus:border-indigo-500"
          placeholder="Paste the complete Job Description here..."
          value={jobDescription}
          onChange={(e) =>
            setJobDescription(e.target.value)
          }
        />

        <div className="mt-8">

          <Button
            loading={loading}
            onClick={run}
          >
            Analyze ATS
          </Button>

        </div>

      </div>

    </Card>
  );
}