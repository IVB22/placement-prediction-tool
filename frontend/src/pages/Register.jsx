import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import GlassCard from "../components/GlassCard";
import { register } from "../api/auth";

export default function Register(){
  const nav = useNavigate();
  const [name,setName] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [err,setErr] = useState("");
  const [loading,setLoading] = useState(false);

  async function onSubmit(e){
    e.preventDefault();
    setErr(""); setLoading(true);
    try{
      await register(name,email,password);
      nav("/login");
    }catch(ex){
      setErr(ex.message);
    }finally{
      setLoading(false);
    }
  }

  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>Create Account</h2>
      <p className="small">Professional login + MongoDB storage.</p>

      <form onSubmit={onSubmit} className="grid">
        <div style={{ gridColumn:"1/-1" }}>
          <label className="small">Name</label>
          <input value={name} onChange={e=>setName(e.target.value)} />
        </div>
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
          {loading ? "Creating..." : "Register"}
        </button>
      </form>

      <p className="small" style={{ marginTop:12 }}>
        Already have an account? <Link to="/login" className="badge">Login</Link>
      </p>
    </GlassCard>
  );
}
