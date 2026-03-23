import { Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/Navbar";
import ProtectedRoute from "./components/ProtectedRoute";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Predict from "./pages/Predict";
import Result from "./pages/Result";
import History from "./pages/History";

export default function App(){
  return (
    <>
      <Navbar />
      <div className="container" style={{ paddingTop: 18 }}>
        <Routes>
          <Route path="/" element={<Navigate to="/dashboard" replace />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route path="/dashboard" element={<ProtectedRoute><Dashboard/></ProtectedRoute>} />
          <Route path="/predict" element={<ProtectedRoute><Predict/></ProtectedRoute>} />
          <Route path="/result" element={<ProtectedRoute><Result/></ProtectedRoute>} />
          <Route path="/history" element={<ProtectedRoute><History/></ProtectedRoute>} />

          <Route path="*" element={<Navigate to="/dashboard" replace />} />
        </Routes>
      </div>
    </>
  );
}
