import React, { useState } from 'react';
import './App.css';

function App() {
  const [emailText, setEmailText] = useState('');
  const [prediction, setPrediction] = useState('');

  const handleSubmit = async () => {
    // Dummy 3000 features (you can connect this to actual model input)
    const features = Array(3000).fill(0);

    const response = await fetch('http://127.0.0.1:8000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ features }),
    });

    const data = await response.json();
    setPrediction(data.prediction);
  };

  return (
    <div className="App">
      <h1>Email Spam Classifier</h1>
      <textarea
        rows="6"
        cols="60"
        value={emailText}
        onChange={(e) => setEmailText(e.target.value)}
        placeholder="Paste your email here..."
      />
      <br />
      <button onClick={handleSubmit}>Check</button>
      {prediction && <h2>Result: {prediction}</h2>}
    </div>
  );
}

export default App;
