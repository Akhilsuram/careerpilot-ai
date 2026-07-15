"use client";

import { useState } from "react";

import PrimaryButton from "@/components/common/PrimaryButton";

import { generateInterview } from "@/services/interview";

interface Props{

    onComplete:(questions:any[])=>void;

}

export default function InterviewForm({

    onComplete

}:Props){

    const [role,setRole]=useState("");

    const [jd,setJD]=useState("");

    const [loading,setLoading]=useState(false);

    async function run(){

        const stored=localStorage.getItem("careerpilot_resume");

        if(!stored){

            alert("Upload resume first.");

            return;

        }

        const resume=JSON.parse(stored);

        setLoading(true);

        try{

            try {
    const result = await generateInterview(
        resume.data,
        role,
        jd
    );

    console.log("Interview Response:", result);

    onComplete(result.data.questions);

} catch (error: any) {
    console.error("Interview Error:", error);

    if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);
    }

    throw error;
}

        }

        finally{

            setLoading(false);

        }

    }

    return(

        <div className="rounded-3xl bg-white p-8 shadow">

            <h1 className="text-3xl font-bold">

                AI Interview Preparation

            </h1>

            <div className="mt-6 space-y-4">

                <input

                    className="w-full rounded-xl border p-4"

                    placeholder="Target Role"

                    value={role}

                    onChange={(e)=>setRole(e.target.value)}

                />

                <textarea

                    className="w-full rounded-xl border p-4"

                    rows={5}

                    placeholder="Job Description (Optional)"

                    value={jd}

                    onChange={(e)=>setJD(e.target.value)}

                />

            </div>

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

                        "Generate Questions"

                    }

                </PrimaryButton>

            </div>

        </div>

    );

}