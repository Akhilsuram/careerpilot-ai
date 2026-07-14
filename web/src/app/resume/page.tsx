import MainLayout from "@/components/layout/MainLayout";

import ResumeUploader from "@/components/resume/ResumeUploader";
import ResumeViewer from "@/components/resume/ResumeViewer";

export default function ResumePage() {
  return (
    <MainLayout>
      <div className="space-y-8">

        <ResumeUploader />

        <ResumeViewer />

      </div>
    </MainLayout>
  );
}