import { SelectHTMLAttributes } from "react";

interface Props
  extends SelectHTMLAttributes<HTMLSelectElement> {}

export default function Select({
  className = "",
  children,
  ...props
}: Props) {
  return (
    <select
      {...props}
      className={`
        w-full
        rounded-2xl
        border
        border-slate-300
        bg-white
        px-5
        py-3
        outline-none
        transition-all
        duration-200
        focus:border-indigo-500
        focus:ring-4
        focus:ring-indigo-100
        ${className}
      `}
    >
      {children}
    </select>
  );
}