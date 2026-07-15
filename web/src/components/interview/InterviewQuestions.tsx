import QuestionCard from "./QuestionCard";

interface Props{

    questions:any[];

}

export default function InterviewQuestions({

    questions

}:Props){

    if(!Array.isArray(questions))

        return null;

    return(

        <div className="space-y-6">

            {

                questions.map(

                    (q,index)=>(

                        <QuestionCard

                            key={index}

                            question={q}

                        />

                    )

                )

            }

        </div>

    );

}