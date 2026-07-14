const suggestions = [
  "Add Docker skills.",
  "Mention AWS experience.",
  "Increase quantified achievements.",
  "Improve leadership keywords.",
];

export default function ATSSuggestions() {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        AI Suggestions
      </h2>

      <div className="space-y-4">

        {suggestions.map((item) => (

          <div
            key={item}
            className="rounded-xl border p-4"
          >

            ✅ {item}

          </div>

        ))}

      </div>

    </div>
  );
}