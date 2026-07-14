"use client";

import { useEffect, useState } from "react";

import ResumeProfile from "./ResumeProfile";
import ResumeSkills from "./ResumeSkills";

export default function ResumeViewer() {

  const [resume, setResume] = useState<any>(null);

  function loadResume() {

    const data = localStorage.getItem(
      "careerpilot_resume"
    );

    if (!data) return;

    setResume(JSON.parse(data));

  }

  useEffect(() => {

    loadResume();

    window.addEventListener(
      "resume-updated",
      loadResume
    );

    return () =>

      window.removeEventListener(
        "resume-updated",
        loadResume
      );

  }, []);

  if (!resume)

    return null;

  return (

    <div className="space-y-6">

      <ResumeProfile
        resume={resume.data}
      />

      <ResumeSkills
        skills={resume.data.skills}
      />

    </div>

  );

}