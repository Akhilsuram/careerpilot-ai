import StatCard from "../cards/StatCard";

export default function DashboardStats() {
  return (
    <div className="grid grid-cols-4 gap-6">
      <StatCard
        title="ATS Score"
        value="87%"
        subtitle="Excellent Resume"
      />

      <StatCard
        title="Job Matches"
        value="42"
        subtitle="Available Today"
      />

      <StatCard
        title="Interview Score"
        value="91%"
        subtitle="Practice Ready"
      />

      <StatCard
        title="Roadmap"
        value="75%"
        subtitle="Progress"
      />
    </div>
  );
}