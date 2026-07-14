import Sidebar from "./Sidebar";
import Header from "./Header";

export default function MainLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex bg-slate-100">

      <Sidebar />

      <div className="ml-72 flex min-h-screen flex-1 flex-col">

        <Header />

        <main className="flex-1 p-8">

          {children}

        </main>

      </div>

    </div>
  );
}