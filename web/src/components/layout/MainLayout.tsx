import Sidebar from "./Sidebar";
import Header from "./Header";

export default function MainLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen bg-slate-100">
      <Sidebar />

      <main className="ml-72 flex-1">
        <Header />

        <div className="p-8">{children}</div>
      </main>
    </div>
  );
}