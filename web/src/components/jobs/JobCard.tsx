interface Props {
  job: any;
}

export default function JobCard({
  job,
}: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">

      <div className="flex items-center justify-between">

        <div>

          <h2 className="text-2xl font-bold">
            {job.role}
          </h2>

          <p className="text-slate-500">
            {job.company}
          </p>

        </div>

        {/* Recommendation Badge */}

        <div className="rounded-full bg-emerald-100 px-4 py-2 font-semibold text-emerald-700">
          ⭐ AI Recommended
        </div>

      </div>

      <div className="mt-6 grid gap-4 lg:grid-cols-2">

        <div>

          <h3 className="font-semibold">
            Required Skills
          </h3>

          <div className="mt-3 flex flex-wrap gap-2">

            {job.required_skills?.map((skill: string) => (
              <span
                key={skill}
                className="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-700"
              >
                {skill}
              </span>
            ))}

          </div>

        </div>

        <div>

          <h3 className="font-semibold">
            Missing Skills
          </h3>

          <div className="mt-3 flex flex-wrap gap-2">

            {job.missing_skills?.map((skill: string) => (
              <span
                key={skill}
                className="rounded-full bg-red-100 px-3 py-1 text-sm text-red-700"
              >
                {skill}
              </span>
            ))}

          </div>

        </div>

      </div>

      <div className="mt-6 rounded-2xl bg-slate-50 p-4">

        <h3 className="mb-2 font-semibold text-slate-900">
          Why this job?
        </h3>

        <p className="text-slate-600">
          {job.reason}
        </p>

      </div>

    </div>
  );
}