interface Props {
  title: string;
  items?: any[];
}

export default function ReportSection({
  title,
  items = [],
}: Props) {
  if (!items.length) return null;

  function renderItem(item: any) {
    // Simple strings
    if (typeof item === "string") {
      return <p>{item}</p>;
    }

    // --------------------
    // Job Matches
    // --------------------
    if (
      item.company &&
      item.role &&
      item.match_score !== undefined
    ) {
      return (
        <div className="space-y-3">
          <div className="flex items-center justify-between">
            <h3 className="text-xl font-bold text-violet-700">
              {item.company}
            </h3>

            <span className="rounded-full bg-violet-100 px-3 py-1 text-sm font-semibold text-violet-700">
              ⭐ {item.match_score}/10
            </span>
          </div>

          <p>
            <strong>Role:</strong> {item.role}
          </p>

          <p>
            <strong>Location:</strong> {item.location}
          </p>

          <div>
            <strong>Required Skills</strong>

            <ul className="ml-6 mt-2 list-disc">
              {item.required_skills?.map(
                (skill: string) => (
                  <li key={skill}>{skill}</li>
                )
              )}
            </ul>
          </div>

          <div>
            <strong>Missing Skills</strong>

            <ul className="ml-6 mt-2 list-disc text-red-600">
              {item.missing_skills?.map(
                (skill: string) => (
                  <li key={skill}>{skill}</li>
                )
              )}
            </ul>
          </div>

          <div className="rounded-xl bg-slate-50 p-4">
            <strong>Reason</strong>

            <p className="mt-2 text-gray-700">
              {item.reason}
            </p>
          </div>
        </div>
      );
    }

    // --------------------
    // Interview Questions
    // --------------------
    if (
      item.question &&
      item.answer
    ) {
      return (
        <div className="space-y-4">

          <div className="flex gap-3">

            <span className="rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
              {item.category}
            </span>

            <span className="rounded-full bg-green-100 px-3 py-1 text-sm font-medium text-green-700">
              {item.difficulty}
            </span>

          </div>

          <div>

            <h3 className="font-bold">
              Question
            </h3>

            <p className="mt-2">
              {item.question}
            </p>

          </div>

          <div>

            <h3 className="font-bold">
              Answer
            </h3>

            <p className="mt-2 whitespace-pre-wrap text-gray-700">
              {item.answer}
            </p>

          </div>

        </div>
      );
    }

    // --------------------
    // Generic Object
    // --------------------
    return (
      <div className="space-y-2">
        {Object.entries(item).map(([key, value]) => (
          <div key={key}>
            <strong className="capitalize">
              {key.replace(/_/g, " ")}:
            </strong>{" "}
            {Array.isArray(value)
              ? value.join(", ")
              : String(value)}
          </div>
        ))}
      </div>
    );
  }

  return (
    <div className="rounded-2xl border bg-white p-6 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        {title}
      </h2>

      <div className="space-y-5">

        {items.map((item, index) => (
          <div
            key={index}
            className="rounded-xl border p-5"
          >
            {renderItem(item)}
          </div>
        ))}

      </div>

    </div>
  );
}