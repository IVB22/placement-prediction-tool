import GlassCard from "../components/GlassCard";

export default function Result(){
  const data = JSON.parse(localStorage.getItem("fp_last_result") || "{}");

  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>Result</h2>

      <div className="row">
        <span className="badge">Mode: {data.mode || "-"}</span>
        <span className="badge">Placement: {data.placement_probability ?? "-"}%</span>
      </div>

      {data.mode === "A" && (
        <>
          <div className="row" style={{ marginTop:12 }}>
            <span className="badge">Role Fit: {data.role_fit_score ?? "-"}</span>
            <span className="badge">ATS: {data.resume_ats_score ?? "-"}</span>
          </div>

          <h3 style={{ marginBottom:6 }}>Missing Skills</h3>
          <ul className="small">
            {(data.missing_skills || []).slice(0,10).map((s,i)=><li key={i}>{s}</li>)}
          </ul>

          <h3 style={{ marginBottom:6 }}>Suggestions</h3>
          <ul className="small">
            {(data.suggestions || []).map((s,i)=><li key={i}>{s}</li>)}
          </ul>
        </>
      )}

      {data.mode !== "A" && (
        <>
          <h3 style={{ marginBottom:6, marginTop:12 }}>Top Matches</h3>
          <table className="table">
            <thead><tr><th>Company</th><th>Role</th><th>Fit</th><th>Role Fit</th><th>ATS</th></tr></thead>
            <tbody>
              {(data.matches || []).slice(0,15).map((r, i)=>(
                <tr key={i}>
                  <td>{r.company}</td><td>{r.role}</td><td>{r.fit_score}</td><td>{r.role_fit}</td><td>{r.ats}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {data.note && <p className="small">{data.note}</p>}
        </>
      )}
    </GlassCard>
  );
}
