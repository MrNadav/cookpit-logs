import React from 'react';

function Dashboard({ counts, setFilter }) {
  return (
    <div className="dashboard">
      <h2>System Overview</h2>
      <div className="summary-boxes">
        <div className="box normal" onClick={() => setFilter('normal')}>
          <h3>Normal</h3>
          <div className="count">{counts.normal}</div>
        </div>
        <div className="box warning" onClick={() => setFilter('warning')}>
          <h3>Warning</h3>
          <div className="count">{counts.warning}</div>
        </div>
        <div className="box critical" onClick={() => setFilter('critical')}>
          <h3>Critical</h3>
          <div className="count">{counts.critical}</div>
        </div>
        <div className="box alerts" onClick={() => setFilter('all')}>
          <h3>Total Alerts</h3>
          <div className="count">{counts.total_alerts}</div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
