import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

export default function SectionContainer({
  children,
}: Props) {
  return (
    <section className="mx-auto max-w-7xl space-y-8">
      {children}
    </section>
  );
}