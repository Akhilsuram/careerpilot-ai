import JobCard from "./JobCard";
interface Props {
  jobs: any[];
}

export default function JobResults({ jobs }: Props) {

  if (!Array.isArray(jobs) || jobs.length === 0) {
    return (
      <div className="rounded-3xl bg-white p-8 shadow">
        No matching jobs found.
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {jobs.map((job, index) => (
        <JobCard
          key={index}
          job={job}
        />
      ))}
    </div>
  );
}