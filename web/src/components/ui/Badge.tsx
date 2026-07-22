interface Props {
  children: React.ReactNode;
}

export default function Badge({
  children,
}: Props) {
  return (
    <span
      className="
        rounded-full
        bg-indigo-100
        px-4
        py-1
        text-sm
        font-medium
        text-indigo-700
      "
    >
      {children}
    </span>
  );
}