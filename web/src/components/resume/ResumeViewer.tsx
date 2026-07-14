"use client";

import { useEffect, useState } from "react";

import ResumeProfile from "./ResumeProfile";
import ResumeSkills from "./ResumeSkills";
import ResumeEducation from "./ResumeEducation";
import ResumeExperience from "./ResumeExperience";
import ResumeProjects from "./ResumeProjects";
import ResumeCertifications from "./ResumeCertifications";
import ResumeSummary from "./ResumeSummary";
import ResumeMetadata from "./ResumeMetadata";
import ResumeStats from "./ResumeStats";

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
      <ResumeStats resume={resume.data} />

<ResumeSummary
  summary={resume.data.summary}
/>

<ResumeMetadata
  resume={resume}
/>

      <ResumeSkills
        skills={resume.data.skills}
      />

      <ResumeEducation
  education={resume.data.education}
/>

<ResumeExperience
  experience={resume.data.experience}
/>

<ResumeProjects
  projects={resume.data.projects}
/>

<ResumeCertifications
  certifications={resume.data.certifications}
/>

    </div>

  );

}