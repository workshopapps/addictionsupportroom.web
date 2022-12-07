import "./App.css";
import NavBar from "./Components/navbar/NavBar";
import Footer from "./Components/footer/Footer";
import CreateRoute from "./Routes/CreateRoute";
import * as Sentry from "@sentry/react";

function App() {
  return (
    <div className="App">
      <NavBar />
      <CreateRoute />
      <Footer />
    </div>
  );
}

// export default App;
export default Sentry.withProfiler(App);
