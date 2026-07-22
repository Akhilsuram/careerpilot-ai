import Card from "@/components/ui/Card";

type Props = {
  data?: any[];
};

export default function ATSChart({
  data = [],
}: Props) {
  return (
    <Card className="h-[370px] flex flex-col">

      <h2 className="mb-6 text-2xl font-bold">
        ATS Score History
      </h2>

      {data.length === 0 ? (

        <p className="text-gray-500">
          No ATS history available yet.
        </p>

      ) : (

        <div className="space-y-4 overflow-y-auto flex-1 pr-2">

          {[...data].reverse().map((item) => (

            <div
              key={item.id}
              className="flex items-center justify-between rounded-2xl border p-4"
            >

              <div>

                <p className="font-medium">
                  ATS Analysis
                </p>

                <p className="text-sm text-gray-500">
                  {new Date(item.created_at).toLocaleString()}
                </p>

              </div>

              <span className="text-lg font-bold text-indigo-600">
                {Math.round(item.score)}%
              </span>

            </div>

          ))}

        </div>

      )}

    </Card>
  );
}