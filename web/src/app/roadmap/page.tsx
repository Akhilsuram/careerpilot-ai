"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";
import RoadmapForm from "@/components/roadmap/RoadmapForm";
import RoadmapTimeline from "@/components/roadmap/RoadmapTimeline";

export default function RoadmapPage() {

  const [roadmap, setRoadmap] = useState<any[]>([]);

  return (

    <MainLayout>

      <div className="space-y-8">

        <RoadmapForm
          onComplete={setRoadmap}
        />

        {roadmap.length > 0 && (

          <RoadmapTimeline
            roadmap={roadmap}
          />

        )}

      </div>

    </MainLayout>

  );

}