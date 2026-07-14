interface Props {
  resume: any;
}

export default function ResumeStats({
  resume,
}: Props) {
  const skills = resume.skills?.length || 0;
  const projects = resume.projects?.length || 0;
  const experience = resume.experience?.length || 0;
  const certifications = resume.certifications?.length || 0;

  return (
    <div className="grid grid-cols-4 gap-6">

      <div className="rounded-2xl bg-white p-6 shadow">
        <p className="text-gray-500">Skills</p>
        <h2 className="text-3xl font-bold text-indigo-600">
          {skills}
        </h2>
      </div>

      <div className="rounded-2xl bg-white p-6 shadow">
        <p className="text-gray-500">Projects</p>
        <h2 className="text-3xl font-bold text-indigo-600">
          {projects}
        </h2>
      </div>

      <div className="rounded-2xl bg-white p-6 shadow">
        <p className="text-gray-500">Experience</p>
        <h2 className="text-3xl font-bold text-indigo-600">
          {experience}
        </h2>
      </div>

      <div className="rounded-2xl bg-white p-6 shadow">
        <p className="text-gray-500">Certificates</p>
        <h2 className="text-3xl font-bold text-indigo-600">
          {certifications}
        </h2>
      </div>

    </div>
  );
}