import { Navigate, Outlet } from 'react-router-dom'
import authContext from '../context/authContext';
import { useContext } from 'react';

export default function ProtectedRoute() {

    const auth = useContext(authContext);

    return (
        (auth.auth ? <Outlet/> : <Navigate to={'/login'}/>)
    )
}
