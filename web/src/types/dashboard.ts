export interface Analytics {
  total_reports: number;
  average_ats_score: number;
  highest_ats_score: number;
  total_resume_versions: number;
  total_interview_sessions: number;
}

export interface ATSHistory {
  id: number;
  score: number;
  created_at: string;
}