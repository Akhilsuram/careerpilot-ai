"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";
import InterviewForm from "@/components/interview/InterviewForm";
import InterviewQuestions from "@/components/interview/InterviewQuestions";

export default function InterviewPage() {

  const [questions, setQuestions] = useState<any[]>([]);

  return (

    <MainLayout>

      <div className="space-y-8">

        <InterviewForm
          onComplete={setQuestions}
        />

        {questions.length > 0 && (

          <InterviewQuestions
            questions={questions}
          />

        )}

      </div>

    </MainLayout>

  );

}