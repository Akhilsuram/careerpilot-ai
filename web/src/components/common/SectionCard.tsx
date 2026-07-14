import { ReactNode } from "react";

interface Props {
  title?: string;
  children: ReactNode;
}

export default function SectionCard({
  title,
  children,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow-md">

      {title && (
        <h2 className="mb-6 text-2xl font-bold">
          {title}
        </h2>
      )}

      {children}

    </div>
  );
}