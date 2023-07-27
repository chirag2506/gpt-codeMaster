import React, { useState } from 'react';
import LogoImage from '../assets/logo.jpg';
import axios from '../api/axios';
import { useNavigate } from 'react-router-dom';
import { useContext } from 'react';
import authContext from '../context/authContext';


export default function Login() {

    const auth = useContext(authContext);
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const login = async (e) => {
        e.preventDefault();
        try {
            const body = JSON.stringify({ email: email, password: password});
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                }
            }
            const resp = await axios.post('/login', body, config);
            auth.setAuth(true);
            console.log(resp.data);
            navigate('/about');
        } catch (err) {
            console.log('Error In Logging in:', err)
        }
    }

    return (
        <div>
            <h2 className='py-3 px-3'>LOGIN</h2>
            <div className="text-center">
                <form onSubmit={login} className="form-signin">
                    <img className="mb-4" src={LogoImage} alt="" width="72" height="72" />
                    <h1 className="h3 mb-3 font-weight-normal">Sign In</h1>
                    <div className="mb-3">
                        <label htmlFor="inputEmail" className="sr-only">Email address</label>
                        <input type="email" id="inputEmail" value={email} onChange={(e) => setEmail(e.target.value)} className="form-control" placeholder="Email address" required />
                    </div><div className="mb-3">
                        <label htmlFor="inputPassword" className="sr-only">Password</label>
                        <input type="password" id="inputPassword" value={password} onChange={(e) => setPassword(e.target.value)} className="form-control" placeholder="Password" required />
                    </div><div className="checkbox mb-3">
                        <label>
                            <input type="checkbox" value="remember-me" /> Remember me
                        </label>
                    </div>
                    <button className="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
                </form>
            </div>
        </div>
    )
}
