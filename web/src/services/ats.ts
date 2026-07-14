import api from "./api";

export async function analyzeATS(
  resumeData: any,
  jobDescription = ""
) {
  const response = await api.post("/ats/analyze", {
    resume_data: resumeData,
    job_description: jobDescription,
  });

  return response.data;
}