import './App.css';
import Navbar from "./components/navbar";
import Footer from "./components/footer"
import Home from "./components/home";
import Login from "./components/login";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Navbar title="CodeMaster" />
      <Routes>
        <Route path="/" element={
          <div className='holder'>
            <Home />
            <Footer />
          </div>
        } />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
