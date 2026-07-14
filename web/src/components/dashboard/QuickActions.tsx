export default function QuickActions() {
  const buttons = [
    "Analyze Resume",
    "ATS Score",
    "Find Jobs",
    "Interview",
  ];

  return (
    <div className="flex gap-4 flex-wrap">
      {buttons.map((button) => (
        <button
          key={button}
          className="rounded-xl bg-indigo-600 px-6 py-3 text-white transition hover:bg-indigo-700"
        >
          {button}
        </button>
      ))}
    </div>
  );
}