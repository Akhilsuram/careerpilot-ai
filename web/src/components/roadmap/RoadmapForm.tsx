"use client";

import { useState } from "react";

import PrimaryButton from "@/components/common/PrimaryButton";

import { generateRoadmap } from "@/services/roadmap";

interface Props{
    onComplete:(roadmap:any[])=>void;
}

export default function RoadmapForm({
    onComplete,
}:Props){

    const [role,setRole]=useState("");
    const [loading,setLoading]=useState(false);

    async function run(){

        const stored=localStorage.getItem(
            "careerpilot_resume"
        );

        if(!stored){

            alert("Upload resume first.");
            return;

        }

        if(!role.trim()){

            alert("Enter target role.");
            return;

        }

        const resume=JSON.parse(stored);

        setLoading(true);

        try{

            const result=await generateRoadmap(
                resume.data,
                role
            );

            onComplete(result.data.roadmap);

        }finally{

            setLoading(false);

        }

    }

    return(

        <div className="rounded-3xl bg-white p-8 shadow">

            <h1 className="text-3xl font-bold">

                AI Career Roadmap

            </h1>

            <input

                className="mt-6 w-full rounded-xl border p-4"

                placeholder="Target Role"

                value={role}

                onChange={(e)=>setRole(e.target.value)}

            />

            <div className="mt-6">

                <PrimaryButton

                    onClick={run}

                    disabled={loading}

                >

                    {

                        loading

                        ?

                        "Generating..."

                        :

                        "Generate Roadmap"

                    }

                </PrimaryButton>

            </div>

        </div>

    );

}