interface Props {
  report: any;
}
import ReportSection from "./ReportSection";
export default function CareerReport({ report }: Props) {
  if (!report) return null;

  const cards = [
    {
      title: "🧠 Planner",
      value: report.planner?.target_role || "-",
      subtitle: report.planner?.location || "",
    },
    {
      title: "🎯 ATS Score",
      value:
        report.ats?.overall_score !== undefined
          ? `${
              report.ats.overall_score <= 1
                ? Math.round(report.ats.overall_score * 100)
                : Math.round(report.ats.overall_score)
            }%`
          : "-",
      subtitle: "ATS Analysis",
    },
    {
      title: "📄 Resume Score",
      value:
        report.resume_optimizer?.resume_score ??
        "-",
      subtitle: "Optimized Resume",
    },
    {
      title: "📚 Missing Skills",
      value:
        report.skill_gap?.missing_skills?.length ??
        0,
      subtitle: "Skill Gap",
    },
    {
      title: "💼 Job Matches",
      value:
        report.job_match?.jobs?.length ??
        0,
      subtitle: "Matching Jobs",
    },
    {
      title: "🎤 Interview",
      value:
        report.interview?.questions?.length ??
        0,
      subtitle: "Questions Generated",
    },
    {
      title: "🛣 Roadmap",
      value:
        report.roadmap?.estimated_duration ??
        "-",
      subtitle: "Learning Plan",
    },
    {
      title: "🤖 Final Report",
      value: "Ready",
      subtitle: "Completed",
    },
  ];

  return (
    <div className="space-y-8">

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-4">

        {cards.map((card) => (

            <div
            key={card.title}
            className="rounded-2xl border bg-white p-6 shadow"
            >
            <h3 className="text-lg font-semibold">
                {card.title}
            </h3>

            <p className="mt-4 text-3xl font-bold text-violet-600">
                {card.value}
            </p>

            <p className="mt-2 text-gray-500">
                {card.subtitle}
            </p>

            </div>

        ))}

        </div>

        <ReportSection
        title="Missing Skills"
        items={report.skill_gap?.missing_skills}
        />

        <ReportSection
        title="Recommendations"
        items={report.resume_optimizer?.recommendations}
        />

        <ReportSection
        title="Job Matches"
        items={report.job_match?.jobs}
        />

        <ReportSection
        title="Interview Questions"
        items={report.interview?.questions}
        />

    </div>
    );
}