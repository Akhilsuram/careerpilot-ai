import RoadmapWeekCard from "./RoadmapWeekCard";

interface Props{
    roadmap:any[];
}

export default function RoadmapTimeline({
    roadmap,
}:Props){

    if(!Array.isArray(roadmap)){

        return null;

    }

    return(

        <div className="space-y-6">

            {

                roadmap.map(

                    (week,index)=>(

                        <RoadmapWeekCard

                            key={index}

                            week={week}

                        />

                    )

                )

            }

        </div>

    );

}