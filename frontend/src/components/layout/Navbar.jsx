import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#2c3e50" }}>
      <Link to="/" style={{ marginRight: "1rem", color: "white" }}>
        Dashboard
      </Link>
      <Link to="/inventory" style={{ marginRight: "1rem", color: "white" }}>
        Inventaire
      </Link>
      <Link to="/login" style={{ color: "white" }}>
        Login
      </Link>
    </nav>
  );
}

export default Navbar;