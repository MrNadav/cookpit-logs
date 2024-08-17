import React, { useState } from 'react';

function LogSection({ logs }) {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSection = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="log-section">
      <h2 onClick={toggleSection} style={{ cursor: 'pointer' }}>
        System Logs {isOpen ? '▼' : '▲'}
      </h2>
      {isOpen && (
        <div className="logs">
          {logs.map((log, index) => (
            <div key={index} className={`log ${log.category}`}>
              {log.text}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default LogSection;
