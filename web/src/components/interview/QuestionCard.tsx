interface Props {
  question: any;
}

export default function QuestionCard({
  question,
}: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">

      <div className="mb-5 flex items-center justify-between">

        <span className="rounded-full bg-indigo-100 px-4 py-2 text-sm font-semibold text-indigo-700">
          {question.category}
        </span>

        <span className="rounded-full bg-slate-100 px-4 py-2 text-sm">
          {question.difficulty}
        </span>

      </div>

      <h2 className="text-xl font-bold">
        {question.question}
      </h2>

      <div className="mt-6 rounded-2xl bg-slate-50 p-5">

        <h3 className="mb-3 font-semibold">
          Model Answer
        </h3>

        <p className="leading-8 text-slate-600">
          {question.answer}
        </p>

      </div>

    </div>
  );
}