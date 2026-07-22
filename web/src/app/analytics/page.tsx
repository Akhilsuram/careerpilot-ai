"use client";

import { useEffect, useState } from "react";

import MainLayout from "@/components/layout/MainLayout";

import AnalyticsCards from "@/components/analytics/AnalyticsCards";
import ATSHistoryChart from "@/components/analytics/ATSHistoryChart";

import {
  getAnalytics,
  getATSHistory,
} from "@/services/dashboard";

export default function AnalyticsPage() {

  const [analytics, setAnalytics] = useState<any>(null);
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {

    async function load() {

      const analyticsData = await getAnalytics();
      const historyData = await getATSHistory();

      setAnalytics(analyticsData);
      setHistory(historyData);

    }

    load();

  }, []);

  if (!analytics)
    return (
      <MainLayout>
        Loading...
      </MainLayout>
    );

  return (

    <MainLayout>

      <div className="space-y-8">

        <AnalyticsCards
          analytics={analytics}
        />

        <ATSHistoryChart
          history={history}
        />

      </div>

    </MainLayout>

  );

}