import React, { useState } from 'react'
import axios from '../api/axios';

export default function UserHistory() {

    const [history, setHistory] = useState("")

    const getHistory = async (e) => {
        e.preventDefault();
        try {
            const resp = await axios.get('/database/getHistory');
            setHistory(JSON.stringify(resp.data))
        } catch (err) {
            console.log('Error In Logging in:', err)
        }
    }

    return (
        <div className='px-3 py-3'>
            <h3>History</h3>
            <div>
                <button className="btn btn-lg btn-primary btn-block" type="submit" onClick={getHistory}>Check</button>
            </div>
            {history}
        </div>
    )
}
