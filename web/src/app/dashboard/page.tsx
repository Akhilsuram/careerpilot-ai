import MainLayout from "@/components/layout/MainLayout";
import Hero from "@/components/dashboard/Hero";
import DashboardStats from "@/components/dashboard/DashboardStats";
import DashboardGrid from "@/components/dashboard/DashboardGrid";

export default function DashboardPage() {
  return (
    <MainLayout>
      <div className="space-y-8">
        <Hero />
        <DashboardStats />
        <DashboardGrid />
      </div>
    </MainLayout>
  );
}