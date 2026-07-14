interface Props {
  resume: any;
}

export default function ResumeMetadata({
  resume,
}: Props) {
  return (
    <div className="rounded-3xl bg-white p-8 shadow">
      <h2 className="mb-6 text-2xl font-bold">
        Analysis Details
      </h2>

      <div className="grid grid-cols-2 gap-6">

        <div>
          <p className="text-gray-500">Provider</p>
          <p className="font-semibold">{resume.provider}</p>
        </div>

        <div>
          <p className="text-gray-500">Model</p>
          <p className="font-semibold">{resume.model}</p>
        </div>

        <div>
          <p className="text-gray-500">Status</p>
          <p className="font-semibold text-green-600">
            {resume.status}
          </p>
        </div>

        <div>
          <p className="text-gray-500">Processing Time</p>
          <p className="font-semibold">
            {resume.processing_time}s
          </p>
        </div>

      </div>
    </div>
  );
}