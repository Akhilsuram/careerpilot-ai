interface Props {
  result: any;
}

export default function ResumeOptimizerResult({
  result,
}: Props) {
  return (
    <div className="space-y-6">

      <div className="rounded-3xl bg-white p-8 shadow">
        <h2 className="text-2xl font-bold">
          AI Suggestions
        </h2>

        <div className="mt-6 space-y-3">
          {result.recommendations?.map((item: string) => (
            <div
              key={item}
              className="rounded-xl border p-4"
            >
              ✅ {item}
            </div>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-2 gap-6">

        <div className="rounded-3xl bg-white p-8 shadow">
          <h2 className="mb-4 text-xl font-bold">
            Strengths
          </h2>

          <ul className="space-y-2">
            {result.strengths?.map((item: string) => (
              <li key={item}>💪 {item}</li>
            ))}
          </ul>
        </div>

        <div className="rounded-3xl bg-white p-8 shadow">
          <h2 className="mb-4 text-xl font-bold">
            Improvements
          </h2>

          <ul className="space-y-2">
            {result.improvements?.map((item: string) => (
              <li key={item}>🚀 {item}</li>
            ))}
          </ul>
        </div>

      </div>
    </div>
  );
}