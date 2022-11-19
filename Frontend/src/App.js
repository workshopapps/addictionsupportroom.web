import "./App.css";
import NavBar from "./Components/navbar/NavBar";
import Footer from "./Components/footer/Footer";
import CreateRoute from "./Routes/CreateRoute";

function App() {
  return (
    <div className="App">
      <NavBar />
      <CreateRoute />
      <Footer />
    </div>
  );
}

export default App;
