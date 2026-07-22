import {
  BarChart3,
  Trophy,
  FileText,
  Activity,
} from "lucide-react";

import MetricGrid from "@/components/shared/MetricGrid";
import StatCard from "@/components/ui/StatCard";

interface Props {
  analytics: any;
}

export default function AnalyticsCards({
  analytics,
}: Props) {
  return (
    <MetricGrid>

      <StatCard
        title="Reports"
        value={analytics.total_reports}
        icon={<FileText size={22} />}
      />

      <StatCard
        title="Average ATS"
        value={`${analytics.average_ats_score}%`}
        icon={<BarChart3 size={22} />}
        color="text-emerald-600"
      />

      <StatCard
        title="Highest ATS"
        value={`${analytics.highest_ats_score}%`}
        icon={<Trophy size={22} />}
        color="text-amber-600"
      />

      <StatCard
        title="Resume Versions"
        value={analytics.total_resume_versions}
        icon={<Activity size={22} />}
        color="text-cyan-600"
      />

    </MetricGrid>
  );
}