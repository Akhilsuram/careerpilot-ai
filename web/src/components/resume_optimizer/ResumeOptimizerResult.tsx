interface Props {
  result: any;
}

export default function ResumeOptimizerResult({
  result,
}: Props) {
  const recommendations =
    result.recommendations ??
    result.resume_optimizer?.recommendations ??
    [];

  const strengths =
    result.strengths ??
    result.final_report?.strengths ??
    [];

  const improvements =
    result.improvements ??
    result.weaknesses ??
    result.final_report?.weaknesses ??
    [];

  return (
    <div className="space-y-6">
      {/* Suggestions */}
      <div className="rounded-3xl bg-white p-8 shadow">
        <h2 className="text-2xl font-bold">
          AI Suggestions
        </h2>

        <div className="mt-6 space-y-3">
          {recommendations.length > 0 ? (
            recommendations.map((item: string) => (
              <div
                key={item}
                className="rounded-xl border p-4"
              >
                ✅ {item}
              </div>
            ))
          ) : (
            <p className="text-gray-500">
              No suggestions available.
            </p>
          )}
        </div>
      </div>

      {/* Strengths & Improvements */}
      <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
        <div className="rounded-3xl bg-white p-8 shadow">
          <h2 className="mb-4 text-xl font-bold">
            Strengths
          </h2>

          {strengths.length > 0 ? (
            <ul className="space-y-2">
              {strengths.map((item: string) => (
                <li key={item}>💪 {item}</li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500">
              No strengths available.
            </p>
          )}
        </div>

        <div className="rounded-3xl bg-white p-8 shadow">
          <h2 className="mb-4 text-xl font-bold">
            Improvements
          </h2>

          {improvements.length > 0 ? (
            <ul className="space-y-2">
              {improvements.map((item: string) => (
                <li key={item}>🚀 {item}</li>
              ))}
            </ul>
          ) : (
            <p className="text-gray-500">
              No improvements available.
            </p>
          )}
        </div>
      </div>
    </div>
  );
}