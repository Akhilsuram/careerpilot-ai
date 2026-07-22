import Card from "@/components/ui/Card";
import PageHeader from "@/components/ui/PageHeader";

import QuestionCard from "./QuestionCard";

interface Props {
  questions: any[];
}

export default function InterviewQuestions({
  questions,
}: Props) {
  return (
    <Card>

      <PageHeader
        title="Interview Questions"
        subtitle={`${questions.length} AI-generated interview questions`}
      />

      <div className="mt-8 space-y-6">

        {questions.map((question, index) => (
          <QuestionCard
            key={index}
            question={question}
          />
        ))}

      </div>

    </Card>
  );
}