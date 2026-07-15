interface Props{

    question:any;

}

export default function QuestionCard({

    question

}:Props){

    return(

        <div className="rounded-3xl bg-white p-8 shadow">

            <div className="flex justify-between">

                <span className="rounded-full bg-indigo-100 px-4 py-1">

                    {question.category}

                </span>

                <span>

                    {question.difficulty}

                </span>

            </div>

            <h2 className="mt-6 text-2xl font-bold">

                {question.question}

            </h2>

            <div className="mt-6 rounded-xl bg-slate-100 p-5">

                <h3 className="font-semibold">

                    Suggested Answer

                </h3>

                <p className="mt-3 whitespace-pre-wrap">

                    {question.answer}

                </p>

            </div>

        </div>

    );

}