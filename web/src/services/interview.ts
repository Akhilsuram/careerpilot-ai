import api from "./api";

export async function generateInterview(

    resumeData:any,
    targetRole:string,
    jobDescription:string

){

    const response = await api.post(

        "/interview/generate",

        {

            resume_data:resumeData,

            target_role:targetRole,

            job_description:jobDescription

        }

    );

    return response.data;

}