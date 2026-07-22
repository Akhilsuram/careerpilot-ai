"use client";

import { useRef, useState } from "react";
import { Upload } from "lucide-react";
import toast from "react-hot-toast";

import { analyzeResume } from "@/services/resume";

import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import PageHeader from "@/components/ui/PageHeader";

export default function ResumeUploader() {

  const inputRef = useRef<HTMLInputElement>(null);

  const [loading, setLoading] = useState(false);

  async function upload(file: File) {

    try {

      setLoading(true);

      const result = await analyzeResume(file);

      localStorage.setItem(
        "careerpilot_resume",
        JSON.stringify(result)
      );

      console.log(result);

      toast.success("Resume analyzed successfully.");

      window.dispatchEvent(
        new Event("resume-updated")
      );

    } catch (err: any) {

      console.error(err);

      toast.error(
        err.response?.data?.detail ??
        "Resume upload failed. Please try again."
      );

    } finally {

      setLoading(false);

    }

  }

  return (

    <Card>

      <PageHeader
        title="Resume Analysis"
        subtitle="Upload your latest resume and let CareerPilot AI analyze it."
      />

      <div
        className="
        mt-8
        rounded-3xl
        border-2
        border-dashed
        border-indigo-300
        bg-gradient-to-br
        from-indigo-50
        to-cyan-50
        p-12
        text-center
        transition-all
        duration-300
        hover:border-indigo-500
        hover:shadow-lg
        "
      >

        <Upload
          className="mx-auto text-indigo-600"
          size={60}
        />

        <h2 className="mt-6 text-2xl font-semibold">
          Drag & Drop Resume
        </h2>

        <p className="mt-3 text-gray-500">
          PDF Resume (DOCX support coming soon)
        </p>

        <div className="mt-8 flex justify-center">

          <Button
            loading={loading}
            onClick={() => inputRef.current?.click()}
          >
            Choose Resume
          </Button>

        </div>

        <input
          ref={inputRef}
          hidden
          type="file"
          accept=".pdf"
          onChange={(e) => {

            const file = e.target.files?.[0];

            if (!file) return;

            if (file.type !== "application/pdf") {
              toast.error("Please select a PDF file.");
              return;
            }

            if (file.size > 5 * 1024 * 1024) {
              toast.error("Resume must be smaller than 5 MB.");
              return;
            }

            upload(file);

          }}
        />

      </div>

    </Card>

  );

}