import api from "./api";

export async function getDashboard() {
  const response = await api.get("/analytics/");
  return response.data;
}

// Compatibility alias
export async function getAnalytics() {
  return getDashboard();
}

export async function getATSHistory() {
  const response = await api.get("/analytics-history/");
  return response.data;
}

export async function getCareerHistory() {
  const response = await api.get("/career-history/");
  return response.data.data;
}