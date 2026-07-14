import MainLayout from "@/components/layout/MainLayout";

import ATSOverview from "@/components/ats/ATSOverview";
import ATSBreakdown from "@/components/ats/ATSBreakdown";
import ATSSuggestions from "@/components/ats/ATSSuggestions";
import ATSHistory from "@/components/ats/ATSHistory";

export default function ATSPage() {
  return (
    <MainLayout>
      <div className="space-y-8">

        <ATSOverview />

        <ATSBreakdown />

        <ATSSuggestions />

        <ATSHistory />

      </div>
    </MainLayout>
  );
}