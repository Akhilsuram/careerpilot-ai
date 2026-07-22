import { ReactNode } from "react";

interface Props {
  title: string;
  description: string;
  icon?: ReactNode;
}

export default function FeatureCard({
  title,
  description,
  icon,
}: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-lg">

      {icon && (
        <div className="mb-4">
          {icon}
        </div>
      )}

      <h3 className="text-xl font-semibold">
        {title}
      </h3>

      <p className="mt-3 text-slate-500">
        {description}
      </p>

    </div>
  );
}