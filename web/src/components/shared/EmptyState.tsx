interface Props {
  title: string;
  subtitle: string;
}

export default function EmptyState({
  title,
  subtitle,
}: Props) {
  return (
    <div className="rounded-3xl border-2 border-dashed border-slate-300 p-16 text-center">

      <h2 className="text-2xl font-bold">
        {title}
      </h2>

      <p className="mt-3 text-slate-500">
        {subtitle}
      </p>

    </div>
  );
}