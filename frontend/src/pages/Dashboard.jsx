import GlassCard from "../components/GlassCard";

export default function Dashboard(){
  return (
    <GlassCard>
      <h2 style={{ marginTop:0 }}>Dashboard</h2>
      <div className="row">
        <span className="badge">Enterprise Modular Backend</span>
        <span className="badge">MongoDB</span>
        <span className="badge">JWT Auth</span>
        <span className="badge">Placement + Role Fit</span>
      </div>
      <p className="small" style={{ marginTop:12 }}>
        Go to Predict to run Mode A/B/C. Your runs are saved in MongoDB and visible in History.
      </p>
    </GlassCard>
  );
}
