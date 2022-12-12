import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import { BrowserRouter, HashRouter } from "react-router-dom";
//import reportWebVitals from './reportWebVitals';
//import * as Sentry from "@sentry/react";
//import { BrowserTracing } from "@sentry/tracing";

import * as atatus from 'atatus-spa';
 atatus.config('9ffae19639324580a8440ff2b8058355').install();
 atatus.notify(new Error('Test Atatus Setup'));

// process.env.NODE_ENV === "production" &&
//Sentry.init({
 // dsn: "https://9dbafcca75694db4873f27d071e27863@o4504281252233216.ingest.sentry.io/4504281257476096",
  //integrations: [new BrowserTracing()],

  // Set tracesSampleRate to 1.0 to capture 100%
  // of transactions for performance monitoring.
  // We recommend adjusting this value in production
  //tracesSampleRate: 1.0,
//});

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
