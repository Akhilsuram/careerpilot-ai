interface Props {
  resume: any;
}

export default function ResumeProfile({
  resume,
}: Props) {

  return (

    <div className="rounded-3xl bg-white p-8 shadow">

      <div className="flex items-center gap-6">

        <div className="flex h-24 w-24 items-center justify-center rounded-full bg-indigo-600 text-4xl font-bold text-white">

          {resume.name?.charAt(0)}

        </div>

        <div>

          <h2 className="text-3xl font-bold">

            {resume.name}

          </h2>

          <p className="mt-2 text-gray-500">

            {resume.email}

          </p>

          <p className="mt-1 text-gray-500">

            {resume.phone}

          </p>

          <p className="mt-1 text-indigo-600">

            {resume.location}

          </p>

        </div>

      </div>

    </div>

  );

}