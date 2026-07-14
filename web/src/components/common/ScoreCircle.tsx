interface Props {
  score: number;
}

export default function ScoreCircle({
  score,
}: Props) {
  return (
    <div className="flex h-36 w-36 items-center justify-center rounded-full border-[10px] border-indigo-600 text-4xl font-bold text-indigo-600">
      {score}%
    </div>
  );
}