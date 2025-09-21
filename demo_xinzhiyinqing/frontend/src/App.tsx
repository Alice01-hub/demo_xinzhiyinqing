import React, { useState, useEffect } from 'react';
import ApiKeyConfig from './components/ApiKeyConfig';
import ChatInterface from './components/ChatInterface';
import { API_ENDPOINTS } from './config/api';
import './App.css';

interface ApiCredentials {
  apiKey: string;
  appId: string;
}

const App: React.FC = () => {
  const [credentials, setCredentials] = useState<ApiCredentials | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // 检查本地存储中是否有保存的API密钥
    const savedApiKey = localStorage.getItem('apiKey');
    const savedAppId = localStorage.getItem('appId');
    
    if (savedApiKey && savedAppId) {
      // 验证保存的密钥是否仍然有效
      validateCredentials(savedApiKey, savedAppId);
    } else {
      setIsLoading(false);
    }
  }, []);

  const validateCredentials = async (apiKey: string, appId: string) => {
    try {
      const response = await fetch(API_ENDPOINTS.VALIDATE_API_KEY, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          api_key: apiKey,
          app_id: appId,
        }),
      });

      const data = await response.json();

      if (data.success) {
        setCredentials({ apiKey, appId });
        localStorage.setItem('apiKey', apiKey);
        localStorage.setItem('appId', appId);
      } else {
        // 清除无效的密钥
        localStorage.removeItem('apiKey');
        localStorage.removeItem('appId');
      }
    } catch (error) {
      console.error('验证API密钥失败:', error);
      // 清除无效的密钥
      localStorage.removeItem('apiKey');
      localStorage.removeItem('appId');
    } finally {
      setIsLoading(false);
    }
  };

  const handleConfigSuccess = (apiKey: string, appId: string) => {
    setCredentials({ apiKey, appId });
    localStorage.setItem('apiKey', apiKey);
    localStorage.setItem('appId', appId);
  };

  const handleLogout = () => {
    setCredentials(null);
    localStorage.removeItem('apiKey');
    localStorage.removeItem('appId');
  };

  if (isLoading) {
    return (
      <div className="app-loading">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>正在验证API密钥...</p>
        </div>
      </div>
    );
  }

  if (!credentials) {
    return <ApiKeyConfig onConfigSuccess={handleConfigSuccess} />;
  }

  return (
    <div className="app">
      <div className="app-header">
        <h1>🤖 法律知识助手</h1>
        <button onClick={handleLogout} className="logout-button">
          🔄 重新配置
        </button>
      </div>
      <ChatInterface apiKey={credentials.apiKey} appId={credentials.appId} />
    </div>
  );
};

export default App;
