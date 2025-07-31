import React from 'react';

const LoadingSpinner = ({ message = "Carregando..." }) => {
  return (
    <div className="loading-container">
      <div className="loading-spinner">
        <div className="spinner"></div>
        <div className="loading-text">
          <span className="label">{message}</span>
        </div>
      </div>
      
      <style jsx>{`
        .loading-container {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background-color: var(--color-background);
        }
        
        .loading-spinner {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 24px;
        }
        
        .spinner {
          width: 40px;
          height: 40px;
          border: 2px solid var(--border-light);
          border-top: 2px solid var(--accent-primary);
          border-radius: 50%;
          animation: spin 1s linear infinite;
        }
        
        .loading-text {
          text-align: center;
        }
        
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
};

export default LoadingSpinner;