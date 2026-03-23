const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:5000/api";

export function getToken(){
  return localStorage.getItem("fp_token") || "";
}

export async function apiFetch(path, { method="GET", json, formData } = {}) {
  const headers = {};
  const token = getToken();
  if (token) headers["Authorization"] = `Bearer ${token}`;

  let body;
  if (formData) {
    body = formData;
  } else if (json) {
    headers["Content-Type"] = "application/json";
    body = JSON.stringify(json);
  }

  const res = await fetch(`${API_BASE}${path}`, { method, headers, body });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || "Request failed");
  return data;
}
