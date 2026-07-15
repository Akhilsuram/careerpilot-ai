"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";
import JobSearchForm from "@/components/jobs/JobSearchForm";
import JobResults from "@/components/jobs/JobResults";

export default function JobsPage() {

  const [jobs, setJobs] = useState<any>(null);

  return (
    <MainLayout>
      <div className="space-y-8">

        <JobSearchForm
          onComplete={setJobs}
        />

        {jobs && (
          <JobResults
            jobs={jobs}
          />
        )}

      </div>
    </MainLayout>
  );

}