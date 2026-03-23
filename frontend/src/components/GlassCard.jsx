export default function GlassCard({ children }) {
  return (
    <div style={{
      background:"rgba(255,255,255,.08)",
      border:"1px solid rgba(255,255,255,.12)",
      borderRadius:22,
      padding:22,
      backdropFilter:"blur(16px)",
      boxShadow:"0 40px 80px rgba(0,0,0,.45)"
    }}>
      {children}
    </div>
  );
}
