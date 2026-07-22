import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

interface Props {
  roadmap: any[];
}

export default function RoadmapTimeline({
  roadmap,
}: Props) {
  return (

    <Card>

      <PageHeader
        title="Learning Timeline"
        subtitle={`${roadmap.length} Weeks`}
      />

      <div className="mt-8 space-y-8">

        {roadmap.map((week: any) => (

          <div
            key={week.week}
            className="relative border-l-4 border-indigo-500 pl-8"
          >

            <div className="absolute -left-4 top-0 flex h-8 w-8 items-center justify-center rounded-full bg-indigo-600 text-white">

              {week.week}

            </div>

            <h2 className="text-xl font-bold">

              Week {week.week}

            </h2>

            <div className="mt-5">

              <h3 className="font-semibold">

                Topics

              </h3>

              <div className="mt-3 flex flex-wrap gap-2">

                {week.topics.map((topic: string) => (

                  <span
                    key={topic}
                    className="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-700"
                  >

                    {topic}

                  </span>

                ))}

              </div>

            </div>

            <div className="mt-5">

              <h3 className="font-semibold">

                Goals

              </h3>

              <ul className="mt-3 space-y-2">

                {week.goals.map((goal: string) => (

                  <li key={goal}>

                    ✅ {goal}

                  </li>

                ))}

              </ul>

            </div>

          </div>

        ))}

      </div>

    </Card>

  );
}