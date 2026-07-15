import api from "./api";

export async function generateRoadmap(
  resumeData: any,
  targetRole: string
) {

  const response = await api.post(
    "/roadmap/generate",
    {
      resume_data: resumeData,
      target_role: targetRole,
    }
  );

  return response.data;

}