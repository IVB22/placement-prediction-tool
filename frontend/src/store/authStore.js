export function setAuth(token, user){
  localStorage.setItem("fp_token", token);
  localStorage.setItem("fp_user", JSON.stringify(user));
}

export function clearAuth(){
  localStorage.removeItem("fp_token");
  localStorage.removeItem("fp_user");
}

export function getUser(){
  try { return JSON.parse(localStorage.getItem("fp_user") || "null"); }
  catch { return null; }
}

export function isAuthed(){
  return Boolean(localStorage.getItem("fp_token"));
}
