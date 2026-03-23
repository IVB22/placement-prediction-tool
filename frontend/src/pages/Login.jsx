import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import GlassCard from "../components/GlassCard";
import { login } from "../api/auth";
import { setAuth } from "../store/authStore";

export default function Login(){
  const nav = useNavigate();
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [err,setErr] = useState("");
  const [loading,setLoading] = useState(false);

  async function onSubmit(e){
    e.preventDefault();
    setErr(""); setLoading(true);
    try{
      const res = await login(email,password);
      setAuth(res.token, res.user);
      nav("/dashboard");
    }catch(ex){
      setErr(ex.message);
    }finally{
      setLoading(false);
    }
  }

  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>Login</h2>
      <p className="small">Access your placement predictions and history.</p>

      <form onSubmit={onSubmit} className="grid">
        <div style={{ gridColumn:"1/-1" }}>
          <label className="small">Email</label>
          <input value={email} onChange={e=>setEmail(e.target.value)} />
        </div>
        <div style={{ gridColumn:"1/-1" }}>
          <label className="small">Password</label>
          <input type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        </div>

        {err && <div className="badge" style={{ gridColumn:"1/-1", borderColor:"rgba(255,80,80,.5)" }}>{err}</div>}

        <button className="btn" disabled={loading} style={{ gridColumn:"1/-1" }}>
          {loading ? "Signing in..." : "Login"}
        </button>
      </form>

      <p className="small" style={{ marginTop:12 }}>
        New user? <Link to="/register" className="badge">Create account</Link>
      </p>
    </GlassCard>
  );
}
