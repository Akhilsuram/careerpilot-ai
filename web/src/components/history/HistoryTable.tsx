import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

import HistoryRow from "./HistoryRow";

interface Props {
  history: any[];
}

export default function HistoryTable({
  history,
}: Props) {
  return (
    <Card>

      <PageHeader
        title="Career History"
        subtitle={`${history.length} saved reports`}
      />

      <div className="mt-8 overflow-x-auto">

        <table className="w-full">

          <thead>

            <tr className="border-b">

              <th className="p-4 text-left">
                Goal
              </th>

              <th className="p-4 text-left">
                ATS
              </th>

              <th className="p-4 text-left">
                Date
              </th>

            </tr>

          </thead>

          <tbody>

            {history.map((item) => (

              <HistoryRow
                key={item.id}
                item={item}
              />

            ))}

          </tbody>

        </table>

      </div>

    </Card>
  );
}