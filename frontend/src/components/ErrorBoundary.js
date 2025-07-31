import React from 'react';
import { AlertTriangle, RefreshCw, Wifi, WifiOff } from 'lucide-react';

const ErrorMessage = ({ error, isOnline, onRetry }) => {
  return (
    <div className="error-container">
      <div className="error-content">
        <div className="error-icon">
          {isOnline ? <AlertTriangle size={48} /> : <WifiOff size={48} />}
        </div>
        
        <div className="error-message">
          <h2 className="text-regular">
            {isOnline ? 'Erro de Conexão' : 'Modo Offline'}
          </h2>
          <p className="text-body">
            {isOnline 
              ? 'Não foi possível conectar com o servidor. Usando dados locais.'
              : 'Backend não disponível. Exibindo dados de demonstração.'
            }
          </p>
          {error && (
            <details className="error-details">
              <summary className="label-small">Detalhes técnicos</summary>
              <p className="error-text">{error}</p>
            </details>
          )}
        </div>
        
        {onRetry && (
          <button className="btn-accent retry-button" onClick={onRetry}>
            <RefreshCw size={16} />
            <span>TENTAR NOVAMENTE</span>
          </button>
        )}
        
        <div className="connection-status">
          {isOnline ? (
            <div className="status-online">
              <Wifi size={16} />
              <span className="label-small">ONLINE - DADOS LOCAIS</span>
            </div>
          ) : (
            <div className="status-offline">
              <WifiOff size={16} />
              <span className="label-small">OFFLINE - MODO DEMO</span>
            </div>
          )}
        </div>
      </div>
      
      <style jsx>{`
        .error-container {
          position: fixed;
          top: 80px;
          right: 24px;
          background: var(--bg-white);
          border: 1px solid var(--border-light);
          padding: 24px;
          max-width: 400px;
          z-index: 1001;
          box-shadow: 0 4px 20px var(--border-light);
        }
        
        .error-content {
          display: flex;
          flex-direction: column;
          gap: 16px;
          align-items: center;
          text-align: center;
        }
        
        .error-icon {
          color: var(--color-warning);
        }
        
        .error-message h2 {
          margin-bottom: 8px;
          color: var(--text-primary);
        }
        
        .error-message p {
          margin-bottom: 16px;
          opacity: 0.8;
        }
        
        .error-details {
          width: 100%;
          text-align: left;
        }
        
        .error-details summary {
          margin-bottom: 8px;
          cursor: pointer;
          color: var(--text-secondary);
        }
        
        .error-text {
          font-family: 'Inter', monospace;
          font-size: 12px;
          background: var(--border-light);
          padding: 8px;
          border-radius: 4px;
          color: var(--text-secondary);
          word-break: break-word;
        }
        
        .retry-button {
          display: flex;
          align-items: center;
          gap: 8px;
        }
        
        .connection-status {
          width: 100%;
          padding: 12px;
          border: 1px solid var(--border-light);
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
        }
        
        .status-online {
          display: flex;
          align-items: center;
          gap: 8px;
          color: var(--accent-primary);
        }
        
        .status-offline {
          display: flex;
          align-items: center;
          gap: 8px;
          color: var(--color-warning);
        }
        
        @media (max-width: 768px) {
          .error-container {
            right: 16px;
            left: 16px;
            max-width: none;
          }
        }
      `}</style>
    </div>
  );
};

export default ErrorMessage;