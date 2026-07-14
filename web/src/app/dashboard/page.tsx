import MainLayout from "@/components/layout/MainLayout";

export default function Dashboard() {
  return (
    <MainLayout>
      <h1 className="text-4xl font-bold">
        Dashboard
      </h1>

      <p className="mt-2 text-gray-500">
        Welcome to CareerPilot AI.
      </p>
    </MainLayout>
  );
}