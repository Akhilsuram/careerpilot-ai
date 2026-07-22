"use client";

import { ButtonHTMLAttributes } from "react";
import { Loader2 } from "lucide-react";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  loading?: boolean;
  variant?: "primary" | "secondary" | "success" | "danger";
}

export default function Button({
  children,
  loading = false,
  variant = "primary",
  className = "",
  ...props
}: ButtonProps) {
  const variants = {
    primary:
      "bg-indigo-600 hover:bg-indigo-700 text-white",

    secondary:
      "bg-slate-100 hover:bg-slate-200 text-slate-800",

    success:
      "bg-emerald-600 hover:bg-emerald-700 text-white",

    danger:
      "bg-rose-600 hover:bg-rose-700 text-white",
  };

  return (
    <button
      {...props}
      disabled={loading || props.disabled}
      className={`
        inline-flex
        items-center
        justify-center
        gap-2
        rounded-2xl
        px-6
        py-3
        font-semibold
        transition-all
        duration-200
        shadow-md
        hover:shadow-xl
        disabled:opacity-60
        disabled:cursor-not-allowed
        active:scale-95
        ${variants[variant]}
        ${className}
      `}
    >
      {loading && (
        <Loader2
          size={18}
          className="animate-spin"
        />
      )}

      {children}
    </button>
  );
}