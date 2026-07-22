interface ErrorStateProps {
  message?: string;
}

export default function ErrorState({
  message = "Something went wrong.",
}: ErrorStateProps) {
  return (
    <div className="rounded-xl border border-red-200 bg-red-50 p-6 text-center">
      <h3 className="text-lg font-semibold text-red-700">
        Error
      </h3>

      <p className="mt-2 text-red-600">
        {message}
      </p>
    </div>
  );
}