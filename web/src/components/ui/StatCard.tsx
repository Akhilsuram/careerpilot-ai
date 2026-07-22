import { ReactNode } from "react";

interface Props {
  title: string;
  value: string | number;
  icon?: ReactNode;
  color?: string;
}

export default function StatCard({
  title,
  value,
  icon,
  color = "text-indigo-600",
}: Props) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-xl">

      <div className="flex items-center justify-between">

        <div>

          <p className="text-sm text-slate-500">
            {title}
          </p>

          <h2 className={`mt-3 text-4xl font-bold ${color}`}>
            {value}
          </h2>

        </div>

        {icon && (
          <div className="rounded-2xl bg-slate-100 p-4">
            {icon}
          </div>
        )}

      </div>

    </div>
  );
}