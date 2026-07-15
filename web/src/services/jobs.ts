import api from "./api";

export async function searchJobs(
  resumeData: any,
  targetRole: string,
  location: string
) {

  const response = await api.post(
    "/job-match/search",
    {
      resume_data: resumeData,
      target_role: targetRole,
      location,
    }
  );

  return response.data;

}