import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

export default function MetricGrid({
  children,
}: Props) {
  return (
    <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
      {children}
    </div>
  );
}