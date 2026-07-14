"use client";

import { useState } from "react";

import PrimaryButton from "@/components/common/PrimaryButton";

import { analyzeATS } from "@/services/ats";

interface Props {

    onComplete:(data:any)=>void;

}

export default function ATSInput({

    onComplete,

}:Props){

    const [jobDescription,setJobDescription]=useState("");

    const [loading,setLoading]=useState(false);

    async function run(){

        const stored=localStorage.getItem(
            "careerpilot_resume"
        );

        if(!stored){

            alert("Please upload resume first.");

            return;

        }

        const resume=JSON.parse(stored);

        setLoading(true);

        try{

            const result=await analyzeATS(

                resume.data,

                jobDescription,

            );

            onComplete(result.data);

        }

        finally{

            setLoading(false);

        }

    }

    return(

<div className="rounded-3xl bg-white p-8 shadow">

<h1 className="text-3xl font-bold">

ATS Analysis

</h1>

<textarea

className="mt-6 h-64 w-full rounded-xl border p-4"

placeholder="Paste Job Description"

value={jobDescription}

onChange={(e)=>setJobDescription(e.target.value)}

/>

<div className="mt-6">

<PrimaryButton

onClick={run}

disabled={loading}

>

{loading?"Analyzing...":"Analyze ATS"}

</PrimaryButton>

</div>

</div>

    )

}