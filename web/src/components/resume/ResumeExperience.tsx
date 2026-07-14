interface Props {
  experience: any[];
}

export default function ResumeExperience({
  experience,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        Experience
      </h2>

      <div className="space-y-5">

        {experience?.length ? (
          experience.map((item, index) => (
            <div
              key={index}
              className="rounded-xl border-l-4 border-indigo-600 bg-slate-50 p-5"
            >
              <h3 className="text-xl font-semibold">
                {item.role}
              </h3>

              <p className="text-indigo-600">
                {item.company}
              </p>

              <p className="text-gray-500">
                {item.duration}
              </p>

              <p className="mt-3">
                {item.description}
              </p>
            </div>
          ))
        ) : (
          <p className="text-gray-500">
            No experience available.
          </p>
        )}

      </div>

    </div>
  );
}