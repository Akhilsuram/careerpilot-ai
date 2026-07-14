interface Props {
  skills: string[];
}

export default function ResumeSkills({
  skills,
}: Props) {

  return (

    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">

        Skills

      </h2>

      <div className="flex flex-wrap gap-3">

        {skills?.map((skill) => (

          <span

            key={skill}

            className="rounded-full bg-indigo-100 px-4 py-2 text-indigo-700"

          >

            {skill}

          </span>

        ))}

      </div>

    </div>

  );

}