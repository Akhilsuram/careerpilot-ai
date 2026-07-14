"use client";

import { useRef, useState } from "react";
import { Upload } from "lucide-react";

import { analyzeResume } from "@/services/resume";

export default function ResumeUploader() {

  const inputRef = useRef<HTMLInputElement>(null);

  const [loading, setLoading] = useState(false);

  async function upload(file: File) {

    try {

      setLoading(true);

    const result = await analyzeResume(file);

    // Save the complete backend response
    localStorage.setItem(
    "careerpilot_resume",
    JSON.stringify(result)
    );

    console.log(result);

    alert("Resume analyzed successfully.");

    window.dispatchEvent(
    new Event("resume-updated")
    );

    } catch (err) {

      console.error(err);

      alert("Resume upload failed.");

    } finally {

      setLoading(false);

    }

  }

  return (

    <div className="rounded-3xl bg-white p-8 shadow-md">

      <h1 className="text-3xl font-bold">
        Resume Analysis
      </h1>

      <p className="mt-2 text-gray-500">
        Upload your latest resume.
      </p>

      <div
        className="mt-8 rounded-2xl border-2 border-dashed border-indigo-300 bg-indigo-50 p-12 text-center"
      >

        <Upload
          className="mx-auto text-indigo-600"
          size={60}
        />

        <h2 className="mt-6 text-2xl font-semibold">

          Drag & Drop Resume

        </h2>

        <p className="mt-3 text-gray-500">

          PDF • DOCX

        </p>

        <button

          onClick={() => inputRef.current?.click()}

          disabled={loading}

          className="mt-8 rounded-xl bg-indigo-600 px-8 py-3 text-white"

        >

          {loading
            ? "Analyzing..."
            : "Choose Resume"}

        </button>

        <input

          ref={inputRef}

          hidden

          type="file"

          accept=".pdf"

          onChange={(e) => {

            const file = e.target.files?.[0];

            if (file)
              upload(file);

          }}

        />

      </div>

    </div>

  );

}