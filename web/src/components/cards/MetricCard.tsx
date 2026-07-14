interface Props {
  title: string;
  value: string;
}

export default function MetricCard({
  title,
  value,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow transition hover:-translate-y-1 hover:shadow-xl">
      <p className="text-sm text-gray-500">
        {title}
      </p>

      <h2 className="mt-3 text-3xl font-bold text-indigo-600">
        {value}
      </h2>
    </div>
  );
}