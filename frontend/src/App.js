import React, { useState } from 'react';

function App() {
  const [time, setTime] = useState('');

  // Function to fetch current time from the backend
  const getTime = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5001/time');
      const data = await response.json();
      setTime(data.time);  // Update the state with the time
    } catch (error) {
      console.error('Error fetching time:', error);
    }
  };

  return (
    <div>
      <h1>Get Current Time</h1>
      <button onClick={getTime}>Get Time</button>
      {/* Display the time below the button */}
      {time && <p>Current time: {time}</p>}
    </div>
  );
}

export default App;