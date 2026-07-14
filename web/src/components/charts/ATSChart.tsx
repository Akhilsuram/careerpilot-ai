type ATSChartProps = {
  data: any[];
};

export default function ATSChart({
  data,
}: ATSChartProps) {
  return (
    <div className="rounded-xl bg-white p-6 shadow">
      <h2 className="text-xl font-semibold mb-4">
        ATS Score Trend
      </h2>

      {data.length === 0 ? (
        <p className="text-gray-500">
          No ATS history available.
        </p>
      ) : (
        <pre className="text-sm overflow-auto">
          {JSON.stringify(data, null, 2)}
        </pre>
      )}
    </div>
  );
}