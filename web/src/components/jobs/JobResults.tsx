import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

import JobCard from "./JobCard";

interface Props {
  jobs: any[];
}

export default function JobResults({
  jobs,
}: Props) {
  return (
    <Card>

      <PageHeader
        title="Matching Jobs"
        subtitle={`${jobs.length} opportunities matched to your profile`}
      />

      <div className="mt-8 space-y-6">

        {jobs.map((job, index) => (
          <JobCard
            key={index}
            job={job}
          />
        ))}

      </div>

    </Card>
  );
}