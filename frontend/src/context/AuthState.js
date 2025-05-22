import AuthContext from "./authContext";
import { useEffect, useState } from "react";
import axios from "../api/axios";

const AuthState = (props) => {

    useEffect(() => {(async () => {
            try {
                const res = await axios.get('/getUser');
                if(res.status === 200 && res?.data?.user){
                    setUser(res.data.user);
                    setAuth(true);
                }
                console.log("USER IS: "+ res.data?.user);
            } catch (error) {
                console.log(`Error in getting user:\n${error}`);
            };
        })();
    }, []);

    const [auth, setAuth] = useState(null);
    const [user, setUser] = useState(null);

    useEffect(() => {
        const isAuth = async () => {
            try {
                const res = await axios.get('/getUser');
                setUser(res.data);
            } catch (error) {
                console.log(`Error in getting user:\n${error}`);
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