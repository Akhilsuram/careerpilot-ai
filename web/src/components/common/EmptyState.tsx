interface Props {
  title: string;
  description: string;
}

export default function EmptyState({
  title,
  description,
}: Props) {
  return (
    <div className="rounded-3xl border-2 border-dashed border-gray-300 p-10 text-center">

      <h3 className="text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-2 text-gray-500">
        {description}
      </p>

    </div>
  );
}