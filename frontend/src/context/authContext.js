import { createContext } from "react";

const authContext = createContext(
    {
        auth: null,
        setAuth: () => { },
        user: null,
    }
);

export default authContext;