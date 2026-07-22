import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

import ScoreCircle from "@/components/common/ScoreCircle";

interface Props {
  result: any;
}

export default function ATSResult({
  result,
}: Props) {
  return (
    <div className="space-y-8">

      <Card>

        <PageHeader
          title="ATS Report"
          subtitle="AI-powered evaluation of your resume."
        />

        <div className="mt-8 flex flex-col items-center gap-8 lg:flex-row">

          <ScoreCircle
            score={result.overall_score}
          />

          <div>

            <h2 className="text-3xl font-bold text-slate-900">

              {result.overall_score}% Match

            </h2>

            <p className="mt-2 text-slate-500">

              Overall ATS Compatibility

            </p>

          </div>

        </div>

      </Card>

      <div className="grid gap-6 lg:grid-cols-2">

        <Card>

          <h2 className="mb-5 text-2xl font-bold">

            ✅ Strengths

          </h2>

          <div className="space-y-3">

            {result.strengths.map(
              (item: string) => (

                <div
                  key={item}
                  className="rounded-xl bg-emerald-50 p-4 text-emerald-700"
                >
                  {item}
                </div>

              )
            )}

          </div>

        </Card>

        <Card>

          <h2 className="mb-5 text-2xl font-bold">

            ❌ Weaknesses

          </h2>

          <div className="space-y-3">

            {result.weaknesses.map(
              (item: string) => (

                <div
                  key={item}
                  className="rounded-xl bg-red-50 p-4 text-red-700"
                >
                  {item}
                </div>

              )
            )}

          </div>

        </Card>

      </div>

      <Card>

        <h2 className="mb-6 text-2xl font-bold">

          💡 Recommendations

        </h2>

        <div className="space-y-3">

          {result.recommendations.map(
            (item: string) => (

              <div
                key={item}
                className="rounded-xl bg-indigo-50 p-4 text-indigo-700"
              >
                {item}
              </div>

            )
          )}

        </div>

      </Card>

    </div>
  );
}