import ScoreCircle from "@/components/common/ScoreCircle";

interface Props{

result:any;

}

export default function ATSResult({

result,

}:Props){

return(

<div className="space-y-8">

<div className="rounded-3xl bg-white p-8 shadow">

<div className="flex items-center gap-10">

<ScoreCircle
score={result.overall_score}
/>

<div>

<h2 className="text-3xl font-bold">

ATS Analysis Complete

</h2>

<p className="text-gray-500">

Overall Resume Compatibility

</p>

</div>

</div>

</div>

<div className="grid grid-cols-2 gap-6">

<div className="rounded-3xl bg-white p-8 shadow">

<h2 className="mb-6 text-2xl font-bold">

Strengths

</h2>

<ul className="space-y-3">

{result.strengths.map((item:string)=>(

<li key={item}>

✅ {item}

</li>

))}

</ul>

</div>

<div className="rounded-3xl bg-white p-8 shadow">

<h2 className="mb-6 text-2xl font-bold">

Weaknesses

</h2>

<ul className="space-y-3">

{result.weaknesses.map((item:string)=>(

<li key={item}>

❌ {item}

</li>

))}

</ul>

</div>

</div>

<div className="rounded-3xl bg-white p-8 shadow">

<h2 className="mb-6 text-2xl font-bold">

Recommendations

</h2>

<ul className="space-y-3">

{result.recommendations.map((item:string)=>(

<li key={item}>

⭐ {item}

</li>

))}

</ul>

</div>

</div>

)

}