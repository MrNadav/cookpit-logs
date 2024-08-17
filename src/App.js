import React, { useState, useEffect } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import LogSection from './components/LogSection';
import ServiceSection from './components/ServiceSection';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [filter, setFilter] = useState('all'); // Added filter state

  useEffect(() => {
    fetch(process.env.REACT_APP_API_URL || 'http://192.168.1.250:5000/api/data')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => setData(data))
      .catch(e => {
        console.error("Fetching error:", e);
        setError(e.message);
      });
  }, []);

  if (error) return <div className="error">Error: {error}</div>;
  if (!data) return <div>Loading...</div>;

  // Filter logs and services based on selected filter
  const filteredLogs = filter === 'all' ? data.logs : data.logs.filter(log => log.category === filter);
  const filteredServices = filter === 'all' ? data.services : data.services.filter(service => service.category === filter);

  return (
    <div className="App">
      <h1>Custom Cockpit</h1>
      <Dashboard counts={data.counts} setFilter={setFilter} /> {/* Pass setFilter as a prop */}
      <LogSection logs={filteredLogs} />
      <ServiceSection services={filteredServices} />
    </div>
  );
}

export default App;
