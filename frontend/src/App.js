import './App.css';
import Navbar from "./components/Navbar";
import Footer from "./components/Footer"
import Home from "./components/Home";
import About from "./components/About";
import Login from "./components/Login";
import AuthState from './context/AuthState';
import CodeGeneration from './components/CodeGeneration';
import CommentGeneration from './components/CommentGeneration';
import UserHistory from './components/UserHistory';
import ProtectedRoute from './components/ProtectedRoute';
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
          <Route path="/about" element={<About />} />
          <Route path="/login" element={<Login />} />
          <Route element={<ProtectedRoute />}>
            <Route path="/commentGeneration" element={<CommentGeneration />} />
            <Route path="/codeGeneration" element={<CodeGeneration />} />
            <Route path="/history" element={<UserHistory />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </AuthState>
  )
}

export default App;
