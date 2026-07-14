interface Props {
  certifications: any[];
}

export default function ResumeCertifications({
  certifications,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">

      <h2 className="mb-6 text-2xl font-bold">
        Certifications
      </h2>

      <div className="space-y-4">

        {certifications?.length ? (
          certifications.map((cert, index) => (
            <div
              key={index}
              className="rounded-xl border p-5"
            >
              <h3 className="font-semibold">
                {cert.name}
              </h3>

              <p className="text-gray-500">
                {cert.organization}
              </p>
            </div>
          ))
        ) : (
          <p className="text-gray-500">
            No certifications available.
          </p>
        )}

      </div>

    </div>
  );
}