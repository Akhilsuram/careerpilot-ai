import ATSChart from "../charts/ATSChart";

import ActivityTimeline from "./ActivityTimeline";
import RecommendedJobs from "./RecommendedJobs";
import WeeklyGoals from "./WeeklyGoals";
import UpcomingTasks from "./UpcomingTasks";
import AIAssistant from "./AIAssistant";

export default function DashboardGrid() {
  return (
    <div className="space-y-6">

      <div className="grid grid-cols-3 gap-6">

        <div className="col-span-2">

          <ATSChart />

        </div>

        <ActivityTimeline />

      </div>

      <div className="grid grid-cols-2 gap-6">

        <RecommendedJobs />

        <AIAssistant />

      </div>

      <div className="grid grid-cols-2 gap-6">

        <WeeklyGoals />

        <UpcomingTasks />

      </div>

    </div>
  );
}