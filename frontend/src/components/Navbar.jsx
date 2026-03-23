import { Link, useNavigate } from "react-router-dom";
import { clearAuth, getUser, isAuthed } from "../store/authStore";

export default function Navbar(){
  const nav = useNavigate();
  const user = getUser();

  return (
    <div className="container" style={{ paddingTop:16 }}>
      <div className="row" style={{ justifyContent:"space-between" }}>
        <Link to="/" style={{ fontWeight:900, letterSpacing:0.3 }}></Link>

        <div className="row">
          {isAuthed() && <Link className="badge" to="/dashboard">Dashboard</Link>}
          {isAuthed() && <Link className="badge" to="/predict">Predict</Link>}
          {isAuthed() && <Link className="badge" to="/history">History</Link>}

          {!isAuthed() && <Link className="badge" to="/login">Login</Link>}
          {!isAuthed() && <Link className="badge" to="/register">Register</Link>}

          {isAuthed() && (
            <button
              className="badge"
              onClick={() => { clearAuth(); nav("/login"); }}
              style={{ cursor:"pointer", color:"#fff" }}
            >
              Logout{user?.name ? ` (${user.name})` : ""}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
