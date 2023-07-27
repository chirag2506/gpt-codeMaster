import AuthContext from "./authContext";
import { useEffect, useState } from "react";
import axios from "../api/axios";

const AuthState = (props) => {
    const [auth, setAuth] = useState(null);
    const [user, setUser] = useState(null);

    useEffect(() => {
        const isAuth = async () => {
            try {
                const res = await axios.get('/getUser');
                setUser(res.data);
            } catch (error) {
                setUser(null);
            };
        };

        isAuth();
    }, [auth]);

    return (
        <AuthContext.Provider value={{ auth, setAuth, user}}>
            {props.children}
        </AuthContext.Provider>
    )
}

export default AuthState