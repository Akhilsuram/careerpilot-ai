interface Props {
  title: string;
  value: string;
  subtitle: string;
}

export default function StatCard({
  title,
  value,
  subtitle,
}: Props) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-md hover:shadow-xl transition-all">
      <p className="text-gray-500 text-sm">{title}</p>

      <h2 className="mt-3 text-4xl font-bold text-indigo-600">
        {value}
      </h2>

      <p className="mt-3 text-gray-400 text-sm">
        {subtitle}
      </p>
    </div>
  );
}