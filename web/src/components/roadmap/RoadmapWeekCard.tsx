interface Props{
    week:any;
}

export default function RoadmapWeekCard({
    week,
}:Props){

    return(

        <div className="rounded-3xl bg-white p-8 shadow">

            <div className="mb-6 flex items-center justify-between">

                <h2 className="text-2xl font-bold">

                    Week {week.week}

                </h2>

            </div>

            <h3 className="font-semibold">

                Topics

            </h3>

            <ul className="mt-3 space-y-2">

                {

                    week.topics.map((t:string)=>(

                        <li key={t}>

                            📘 {t}

                        </li>

                    ))

                }

            </ul>

            <h3 className="mt-6 font-semibold">

                Goals

            </h3>

            <ul className="mt-3 space-y-2">

                {

                    week.goals.map((g:string)=>(

                        <li key={g}>

                            ✅ {g}

                        </li>

                    ))

                }

            </ul>

        </div>

    );

}