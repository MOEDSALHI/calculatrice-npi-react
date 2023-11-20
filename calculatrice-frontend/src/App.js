import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

import './App.css';

function App() {
  const [expression, setExpression] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:8000/calculer/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression })
      });
      const data = await response.json();
      console.log(data); 
      setResult(`Résultat: ${data.resultat}`);
      console.log(data);
    } catch (error) {
      console.error('Erreur lors de l\'envoi de l\'expression:', error);
    }
  };
  
  const exportCsv = async () => {
    try {
      const response = await fetch('http://localhost:8000/export/');
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'historique.csv';
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Erreur lors de l\'exportation:', error);
    }
  };

  
  return (
    // <div className="App">
    //   <form onSubmit={handleSubmit}>
    //     <input 
    //       type="text" 
    //       value={expression} 
    //       onChange={(e) => setExpression(e.target.value)}
    //       placeholder="Entrez l'expression NPI"
    //     />
    //     <button type="submit">Calculer</button>
    //   </form>
    //   <div>{result}</div>
    //   <button type="button" onClick={exportCsv}>Export CSV</button>
    // </div>
    <div className="App container mt-5">
  <form onSubmit={handleSubmit} className="mb-3">
    <div className="form-group">
      <input 
        type="text" 
        value={expression} 
        onChange={(e) => setExpression(e.target.value)}
        placeholder="Entrez l'expression NPI"
        className="form-control"
      />
    </div>
    <button type="submit" className="btn btn-primary">Calculer</button>
  </form>
  {result && <div className="alert alert-success">{result}</div>}
  <button type="button" onClick={exportCsv} className="btn btn-secondary">Export CSV</button>
</div>

  );
}

export default App;
