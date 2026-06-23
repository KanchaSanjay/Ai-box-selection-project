import { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [products, setProducts] = useState('1,2');
  const [result, setResult] = useState('');
  const [error, setError] = useState('');

  const submitData = async () => {
    try {
      const ids = products
        .split(',')
        .map((value) => Number(value.trim()))
        .filter((value) => Number.isInteger(value));

      const response = await axios.post('/api/recommend-box/', {
        products: ids,
      });

      setResult(JSON.stringify(response.data, null, 2));
      setError('');
    } catch (err) {
      setError(err.response?.data?.detail || err.message);
      setResult('');
    }
  };

  return (
    <div className="app-container">
      <h1>AI Box Selection</h1>
      <p>Enter product IDs and request a box recommendation.</p>
      <input
        type="text"
        value={products}
        onChange={(e) => setProducts(e.target.value)}
        placeholder="1,2"
      />
      <button onClick={submitData}>Recommend Box</button>
      {error && <div className="error">{error}</div>}
      {result && (
        <pre className="result">
          {result}
        </pre>
      )}
    </div>
  );
}

export default App;
