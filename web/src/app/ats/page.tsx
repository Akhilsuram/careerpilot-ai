"use client";

import { useState } from "react";

import MainLayout from "@/components/layout/MainLayout";

import ATSInput from "@/components/ats/ATSInput";
import ATSResult from "@/components/ats/ATSResult";

export default function ATSPage() {

  const [result, setResult] = useState<any>(null);

  return (

    <MainLayout>

      <div className="space-y-8">

        <ATSInput
          onComplete={setResult}
        />

        {result && (

          <ATSResult
            result={result}
          />

        )}

      </div>

    </MainLayout>

  );

}