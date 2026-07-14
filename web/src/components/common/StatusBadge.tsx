interface Props {
  text: string;
}

export default function StatusBadge({
  text,
}: Props) {
  return (
    <span className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700">
      {text}
    </span>
  );
}