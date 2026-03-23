import { apiFetch } from "./http";

export async function login(email, password){
  return apiFetch("/auth/login", { method:"POST", json:{ email, password } });
}

export async function register(name, email, password){
  return apiFetch("/auth/register", { method:"POST", json:{ name, email, password } });
}
