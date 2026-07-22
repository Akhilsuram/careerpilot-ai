import api from "./api";

export interface CareerCopilotRequest {
  resume_data: Record<string, unknown>;
  target_role: string;
}

export async function runCareerCopilot(
  data: CareerCopilotRequest
) {
  const response = await api.post(
    "/career-copilot/run",
    data
  );

  return response.data;
}