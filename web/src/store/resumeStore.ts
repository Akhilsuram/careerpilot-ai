import { create } from "zustand";

interface ResumeStore {
  resume: any;
  setResume: (resume: any) => void;
  clearResume: () => void;
}

export const useResumeStore = create<ResumeStore>((set) => ({
  resume: null,

  setResume: (resume) =>
    set({
      resume,
    }),

  clearResume: () =>
    set({
      resume: null,
    }),
}));