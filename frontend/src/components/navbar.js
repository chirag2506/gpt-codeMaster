import React from 'react';
import NavbarAuth from './navbarAuth';
import NavbarNoAuth from './navbarNoAuth';
import { useContext } from 'react';
import authContext from '../context/authContext';

export default function Navbar() {

    const auth = useContext(authContext)

    return (
        <>
            {auth.auth ? <NavbarAuth title= "CodeMaster" userName= {auth?.user?.user} /> : <NavbarNoAuth title="CodeMaster" />}
        </>
    )
}
