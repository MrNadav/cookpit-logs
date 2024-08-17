import React, { useState } from 'react';

function ServiceSection({ services }) {
  const [isOpen, setIsOpen] = useState(true);

  const toggleSection = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="service-section">
      <h2 onClick={toggleSection} style={{ cursor: 'pointer' }}>
        Service Status {isOpen ? '▼' : '▲'}
      </h2>
      {isOpen && (
        <div className="services">
          {services.map((service, index) => (
            <div key={index} className={`service ${service.category}`}>
              {service.text}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ServiceSection;
