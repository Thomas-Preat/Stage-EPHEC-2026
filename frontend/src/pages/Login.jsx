import { useState } from "react";
import { useSignInEmailPassword } from "@nhost/react";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { signInEmailPassword, isLoading, isSuccess, isError, error } = useSignInEmailPassword();

  const handleSubmit = (e) => {
    e.preventDefault();
    signInEmailPassword(email, password);
  };

  return (
    <div className="container">
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        /><br/>
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        /><br/>
        <button type="submit" disabled={isLoading}>Login</button>
      </form>
      {isError && <p style={{color:"red"}}>{error.message}</p>}
      {isSuccess && <p style={{color:"green"}}>Logged in!</p>}
    </div>
  );
}

export default Login;