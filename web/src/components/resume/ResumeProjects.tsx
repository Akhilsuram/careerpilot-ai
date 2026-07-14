interface Props {
  projects: any[];
}

export default function ResumeProjects({
  projects,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        Projects
      </h2>

      <div className="grid gap-5">

        {projects?.length ? (
          projects.map((project, index) => (
            <div
              key={index}
              className="rounded-xl border p-5"
            >
              <h3 className="text-xl font-semibold">
                {project.name}
              </h3>

              <p className="mt-3">
                {project.description}
              </p>

              <div className="mt-4 flex flex-wrap gap-2">

                {project.technologies?.map((tech: string) => (
                  <span
                    key={tech}
                    className="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-700"
                  >
                    {tech}
                  </span>
                ))}

              </div>

            </div>
          ))
        ) : (
          <p className="text-gray-500">
            No projects found.
          </p>
        )}

      </div>

    </div>
  );
}