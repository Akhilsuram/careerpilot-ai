interface Props {
  education: any[];
}

export default function ResumeEducation({
  education,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        Education
      </h2>

      <div className="space-y-5">

        {education?.length ? (
          education.map((item, index) => (
            <div
              key={index}
              className="rounded-xl border p-5"
            >
              <h3 className="text-xl font-semibold">
                {item.degree}
              </h3>

              <p className="text-gray-600">
                {item.institution}
              </p>

              <p className="text-gray-500">
                {item.year}
              </p>

              {item.cgpa && (
                <p className="mt-2 text-indigo-600 font-medium">
                  CGPA: {item.cgpa}
                </p>
              )}
            </div>
          ))
        ) : (
          <p className="text-gray-500">
            No education information available.
          </p>
        )}

      </div>

    </div>
  );
}