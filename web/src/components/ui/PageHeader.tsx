import { ReactNode } from "react";

interface Props {
  title: string;
  subtitle?: string;
  action?: ReactNode;
}

export default function PageHeader({
  title,
  subtitle,
  action,
}: Props) {
  return (
    <div className="mb-8 flex items-center justify-between">

      <div>

        <h1 className="text-4xl font-bold tracking-tight text-slate-900">
          {title}
        </h1>

        {subtitle && (
          <p className="mt-2 text-slate-500">
            {subtitle}
          </p>
        )}

      </div>

      {action && (
        <div>
          {action}
        </div>
      )}

    </div>
  );
}