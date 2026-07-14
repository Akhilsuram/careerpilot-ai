"use client";

import { motion } from "framer-motion";
import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}

export default function AnimatedCard({
  children,
}: Props) {
  return (
    <motion.div
      initial={{
        opacity: 0,
        y: 20,
      }}
      animate={{
        opacity: 1,
        y: 0,
      }}
      transition={{
        duration: 0.4,
      }}
      whileHover={{
        y: -4,
      }}
      className="rounded-3xl bg-white p-8 shadow-md"
    >
      {children}
    </motion.div>
  );
}