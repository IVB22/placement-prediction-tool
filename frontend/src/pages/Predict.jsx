import { useState } from "react";
import { useNavigate } from "react-router-dom";
import GlassCard from "../components/GlassCard";
import { apiFetch } from "../api/http";

export default function Predict(){
  const nav = useNavigate();
  const [loading,setLoading] = useState(false);
  const [err,setErr] = useState("");

  const [form, setForm] = useState({
    gender:"M",
    ssc_p:75,
    hsc_p:70,
    hsc_s:"Science",
    degree_p:72,
    degree_t:"Sci&Tech",
    workex:"No",
    etest_p:65,
    specialisation:"Mkt&Fin",
    mba_p:68,
    company:"",
    role:"",
    resume_text:"",
  });

  const [pdfFile, setPdfFile] = useState(null);

  function setField(k,v){ setForm(prev=>({ ...prev, [k]: v })); }

  async function onSubmit(e){
    e.preventDefault();
    setErr(""); setLoading(true);

    try{
      const fd = new FormData();
      fd.append("profile_json", JSON.stringify({
        gender: form.gender,
        ssc_p: Number(form.ssc_p),
        hsc_p: Number(form.hsc_p),
        hsc_s: form.hsc_s,
        degree_p: Number(form.degree_p),
        degree_t: form.degree_t,
        workex: form.workex,
        etest_p: Number(form.etest_p),
        specialisation: form.specialisation,
        mba_p: Number(form.mba_p),
      }));
      fd.append("company", form.company.trim());
      fd.append("role", form.role.trim());
      fd.append("resume_text", form.resume_text || "");
      if (pdfFile) fd.append("resume_pdf", pdfFile);

      const res = await apiFetch("/match/run", { method:"POST", formData: fd });
      localStorage.setItem("fp_last_result", JSON.stringify(res));
      nav("/result");
    }catch(ex){
      setErr(ex.message);
    }finally{
      setLoading(false);
    }
  }

  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>Predict</h2>
      <p className="small">
        Mode A: Company+Role • Mode B: empty • Mode C: Role only
      </p>

      <form onSubmit={onSubmit} className="grid">
        <div>
          <label className="small">Gender</label>
          <select value={form.gender} onChange={e=>setField("gender", e.target.value)}>
            <option value="M">M</option><option value="F">F</option>
          </select>
        </div>

        <div>
          <label className="small">WorkEx</label>
          <select value={form.workex} onChange={e=>setField("workex", e.target.value)}>
            <option value="No">No</option><option value="Yes">Yes</option>
          </select>
        </div>

        <div>
          <label className="small">SSC % (ssc_p)</label>
          <input type="number" step="0.01" value={form.ssc_p} onChange={e=>setField("ssc_p", e.target.value)} />
        </div>

        <div>
          <label className="small">HSC % (hsc_p)</label>
          <input type="number" step="0.01" value={form.hsc_p} onChange={e=>setField("hsc_p", e.target.value)} />
        </div>

        <div>
          <label className="small">HSC Stream (hsc_s)</label>
          <select value={form.hsc_s} onChange={e=>setField("hsc_s", e.target.value)}>
            <option>Science</option><option>Commerce</option><option>Arts</option>
          </select>
        </div>

        <div>
          <label className="small">Degree % (degree_p)</label>
          <input type="number" step="0.01" value={form.degree_p} onChange={e=>setField("degree_p", e.target.value)} />
        </div>

        <div>
          <label className="small">Degree Type (degree_t)</label>
          <select value={form.degree_t} onChange={e=>setField("degree_t", e.target.value)}>
            <option>Sci&Tech</option><option>Comm&Mgmt</option><option>Others</option>
          </select>
        </div>

        <div>
          <label className="small">E-test % (etest_p)</label>
          <input type="number" step="0.01" value={form.etest_p} onChange={e=>setField("etest_p", e.target.value)} />
        </div>

        <div>
          <label className="small">Specialisation</label>
          <select value={form.specialisation} onChange={e=>setField("specialisation", e.target.value)}>
            <option>Mkt&Fin</option><option>Mkt&HR</option>
          </select>
        </div>

        <div>
          <label className="small">MBA % (mba_p)</label>
          <input type="number" step="0.01" value={form.mba_p} onChange={e=>setField("mba_p", e.target.value)} />
        </div>

        <div>
          <label className="small">Target Company (optional)</label>
          <input value={form.company} onChange={e=>setField("company", e.target.value)} />
        </div>

        <div>
          <label className="small">Target Role (optional)</label>
          <input value={form.role} onChange={e=>setField("role", e.target.value)} />
        </div>

        <div style={{ gridColumn:"1/-1" }}>
          <label className="small">Resume PDF (optional)</label>
          <input type="file" accept="application/pdf" onChange={e=>setPdfFile(e.target.files?.[0] || null)} />
        </div>

        <div style={{ gridColumn:"1/-1" }}>
          <label className="small">Resume Text (optional)</label>
          <textarea value={form.resume_text} onChange={e=>setField("resume_text", e.target.value)} />
        </div>

        {err && <div className="badge" style={{ gridColumn:"1/-1", borderColor:"rgba(255,80,80,.5)" }}>{err}</div>}

        <button className="btn" disabled={loading} style={{ gridColumn:"1/-1" }}>
          {loading ? "Analyzing..." : "Analyze & Save to MongoDB"}
        </button>
      </form>
    </GlassCard>
  );
}
