import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from '../api/axios';
import authContext from '../context/authContext';
import { useContext } from 'react';

export default function NavbarAuth(props) {

    const auth = useContext(authContext);
    const navigate = useNavigate();

    const logout = async (e) => {
        try {
            const resp = await axios.post('/logout');
            auth.setAuth(false);
            console.log(resp.data);
            navigate('/')
        } catch (err) {
            console.log('Error In Logging out:', err)
        }
    }

    return (
        <div>
            <nav className="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
                <div className="container-fluid">
                    <Link className="navbar-brand" to="/">{props.title}</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className="nav-link active" to="/about">About</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link active" to="/commentGeneration">CommentGeneration</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link active" to="/codeGeneration">CodeGeneration</Link>
                            </li>
                            <li className="nav-item dropdown">
                                <Link className="nav-link dropdown-toggle active" to="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    {props.userName}
                                </Link>
                                <ul className="dropdown-menu">
                                    <li>
                                        <Link className="dropdown-item" onClick={logout}>Logout</Link>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    )
}
