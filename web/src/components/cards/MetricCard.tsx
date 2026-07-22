interface Props {
  title: string;
  value: string | number;
}

export default function MetricCard({
  title,
  value,
}: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">

      <p className="text-sm font-medium text-slate-500">
        {title}
      </p>

      <h2 className="mt-4 text-4xl font-bold text-indigo-600">
        {value}
      </h2>

    </div>
  );
}