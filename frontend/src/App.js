import './App.css';
import Navbar from "./components/navbar";
import Footer from "./components/footer"
import Home from "./components/home";
import About from "./components/about";
import Login from "./components/login";
import AuthState from './context/AuthState';
import CodeGeneration from './components/codeGeneration';
import CommentGeneration from './components/commentGeneration';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {

  return (
    <AuthState>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route path="/" element={
            <div className='holder'>
              <Home />
              <Footer />
            </div>
          } />
          <Route path="/login" element={<Login />} />
          <Route path="/about" element={<About />} />
          <Route path="/commentGeneration" element={<CommentGeneration />} />
          <Route path="/codeGeneration" element={<CodeGeneration />} />
        </Routes>
      </BrowserRouter>
    </AuthState>
  )
}

export default App;
