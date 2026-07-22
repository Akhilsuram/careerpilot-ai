"use client";

import { useEffect, useState } from "react";

import MainLayout from "@/components/layout/MainLayout";

import HistoryTable from "@/components/history/HistoryTable";

import { getCareerHistory } from "@/services/history";

export default function HistoryPage() {

    const [history, setHistory] = useState<any[]>([]);

    useEffect(() => {

        async function load() {

            const result = await getCareerHistory();

            setHistory(result.data);

        }

        load();

    }, []);

    return (

        <MainLayout>

            <div className="space-y-8">

                <HistoryTable
                    history={history}
                />

            </div>

        </MainLayout>

    );

}