import { ButtonHTMLAttributes } from "react";

interface Props extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

export default function PrimaryButton({
  children,
  ...props
}: Props) {
  return (
    <button
      {...props}
      className="rounded-xl bg-indigo-600 px-6 py-3 font-medium text-white transition hover:bg-indigo-700 disabled:opacity-50"
    >
      {children}
    </button>
  );
}