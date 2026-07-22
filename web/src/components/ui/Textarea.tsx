import { TextareaHTMLAttributes } from "react";

interface Props
  extends TextareaHTMLAttributes<HTMLTextAreaElement> {}

export default function Textarea({
  className = "",
  ...props
}: Props) {
  return (
    <textarea
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
    />
  );
}