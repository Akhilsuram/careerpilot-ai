interface Props {
  summary?: string;
}

export default function ResumeSummary({
  summary,
}: Props) {
  return (
    <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-purple-600 p-8 text-white shadow-lg">
      <h2 className="text-2xl font-bold">
        🧠 AI Resume Summary
      </h2>

      <p className="mt-5 leading-8">
        {summary ||
          "No AI summary is available yet. Once the backend returns a professional summary, it will appear here."}
      </p>
    </div>
  );
}