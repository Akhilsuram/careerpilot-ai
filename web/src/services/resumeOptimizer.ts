import api from "./api";

export async function optimizeResume(
  resumeData: any,
  targetRole: string
) {
  const response = await api.post(
    "/resume-optimizer/optimize",
    {
      resume_data: resumeData,
      target_role: targetRole,
    }
  );

  return response.data;
}