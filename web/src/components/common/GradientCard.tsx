import { ReactNode } from "react";

interface Props {
  title: string;
  children: ReactNode;
}

export default function GradientCard({
  title,
  children,
}: Props) {
  return (
    <div className="rounded-3xl bg-gradient-to-r from-indigo-600 to-purple-600 p-8 text-white shadow-lg">

      <h2 className="mb-6 text-2xl font-bold">
        {title}
      </h2>

      {children}

    </div>
  );
}