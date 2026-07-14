interface Props {
  message: string;
}

export default function ErrorCard({
  message,
}: Props) {
  return (
    <div className="rounded-3xl border border-red-200 bg-red-50 p-6">
      <p className="font-medium text-red-600">
        {message}
      </p>
    </div>
  );
}