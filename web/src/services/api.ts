import axios from "axios";

const api = axios.create({
  baseURL:
    process.env.NEXT_PUBLIC_API_URL ??
    "http://127.0.0.1:8000",

  timeout: 180000, // 3 minutes

  headers: {
    "Content-Type": "application/json",
  },
});

export default api;