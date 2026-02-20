import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { NhostProvider } from "@nhost/react";
import { nhost } from "./lib/nhost";

ReactDOM.createRoot(document.getElementById("root")).render(
  <NhostProvider nhost={nhost}>
    <App />
  </NhostProvider>
);