import { useEffect, useState } from "react";
import GlassCard from "../components/GlassCard";
import { apiFetch } from "../api/http";

export default function History(){
  const [runs, setRuns] = useState([]);
  const [err, setErr] = useState("");

  useEffect(() => {
    (async () => {
      try{
        const res = await apiFetch("/history?limit=20");
        setRuns(res.runs || []);
      }catch(ex){
        setErr(ex.message);
      }
    })();
  }, []);

  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>History</h2>
      {err && <div className="badge" style={{ borderColor:"rgba(255,80,80,.5)" }}>{err}</div>}

      <table className="table" style={{ marginTop: 10 }}>
        <thead><tr><th>Time</th><th>Mode</th><th>Placement %</th><th>Target</th></tr></thead>
        <tbody>
          {runs.map((r)=>(
            <tr key={r.id}>
              <td>{r.created_at}</td>
              <td>{r.response?.mode}</td>
              <td>{r.response?.placement_probability}</td>
              <td>
                {r.request?.company ? `${r.request.company} / ` : ""}
                {r.request?.role || "-"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <p className="small" style={{ marginTop: 10 }}>
        Full resume text is stored in history under request.resume_text as requested.
      </p>
    </GlassCard>
  );
}
