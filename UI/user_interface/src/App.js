import React, { useState } from 'react';
import axios from 'axios';

import GetDroneData from './components/drone_data.js';

function App() {
  const [data, setData] = useState('');

  const handleClick = (command) => {
    axios.post('http://192.168.88.15:8000/command/', {type: command} )
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div className="container">
      <h1>Drone Control Interface</h1>
      <div className="buttons_container">
        <button class="button-24" onClick={() => handleClick(1)}>ARM</button>
        <button class="button-24" onClick={() => handleClick(2)}>DISARM</button>
        <br></br>
        <button class="button-24" onClick={() => handleClick(3)}>TAKEOFF Mode</button>
        <button class="button-24" onClick={() => handleClick(4)}>LAND Mode</button>
        <br></br>
        <button class="button-24" onClick={() => handleClick(7)}>MISSION Mode</button>
        <button class="button-24" onClick={() => handleClick(8)}>RETURN Mode</button>

      </div>
      <div>
        <GetDroneData/>
      </div>
    </div>
  );
}

export default App;