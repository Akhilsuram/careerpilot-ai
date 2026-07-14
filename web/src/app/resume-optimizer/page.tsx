"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";
import ResumeOptimizerInput from "@/components/resume_optimizer/ResumeOptimizerInput";
import ResumeOptimizerResult from "@/components/resume_optimizer/ResumeOptimizerResult";

export default function ResumeOptimizerPage() {
  const [result, setResult] = useState<any>(null);

  return (
    <MainLayout>
      <div className="space-y-8">
        <ResumeOptimizerInput onComplete={setResult} />

        {result && (
          <ResumeOptimizerResult result={result} />
        )}
      </div>
    </MainLayout>
  );
}