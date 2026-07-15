interface Props {
  job: any;
}

export default function JobCard({ job }: Props) {
  return (
    <div className="rounded-3xl bg-white p-6 shadow">

      <div className="flex justify-between">

        <div>

          <h2 className="text-2xl font-bold">

            {job.role}

          </h2>

          <p className="text-gray-500">

            {job.company}

          </p>

          <p className="text-sm text-gray-400 mt-1">

            {job.location}

          </p>

        </div>

        <div className="text-right">

          <div className="text-3xl font-bold text-indigo-600">

            {job.match_score}%

          </div>

          <div className="text-sm">

            Match

          </div>

        </div>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold">

          Why matched?

        </h3>

        <p className="mt-2 text-gray-600">

          {job.reason}

        </p>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold">

          Required Skills

        </h3>

        <div className="mt-3 flex flex-wrap gap-2">

          {job.required_skills.map((skill: string) => (

            <span
              key={skill}
              className="rounded-full bg-indigo-100 px-3 py-1 text-sm"
            >
              {skill}
            </span>

          ))}

        </div>

      </div>

      <div className="mt-6">

        <h3 className="font-semibold text-red-600">

          Missing Skills

        </h3>

        <div className="mt-3 flex flex-wrap gap-2">

          {job.missing_skills.map((skill: string) => (

            <span
              key={skill}
              className="rounded-full bg-red-100 px-3 py-1 text-sm"
            >
              {skill}
            </span>

          ))}

        </div>

      </div>

    </div>
  );
}