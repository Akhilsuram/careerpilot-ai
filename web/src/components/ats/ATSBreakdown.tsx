const sections = [
  ["Keywords", 92],
  ["Formatting", 95],
  ["Skills", 88],
  ["Experience", 81],
  ["Projects", 90],
];

export default function ATSBreakdown() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-8 text-2xl font-bold">
        Section Breakdown
      </h2>

      <div className="space-y-6">

        {sections.map(([name, score]) => (

          <div key={name}>

            <div className="mb-2 flex justify-between">

              <span>{name}</span>

              <span>{score}%</span>

            </div>

            <div className="h-3 rounded-full bg-gray-200">

              <div
                className="h-3 rounded-full bg-emerald-500"
                style={{
                  width: `${score}%`,
                }}
              />

            </div>

          </div>

        ))}

      </div>

    </div>
  );
}