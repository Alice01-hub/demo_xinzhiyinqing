import React, { useState } from 'react';
import { API_ENDPOINTS } from '../config/api';
import './ApiKeyConfig.css';

interface ApiKeyConfigProps {
  onConfigSuccess: (apiKey: string, appId: string) => void;
}

const ApiKeyConfig: React.FC<ApiKeyConfigProps> = ({ onConfigSuccess }) => {
  const [apiKey, setApiKey] = useState('');
  const [appId, setAppId] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setError('');

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
        onConfigSuccess(apiKey, appId);
      } else {
        setError(data.message || 'API密钥验证失败，请检查输入是否正确');
      }
    } catch (err) {
      setError('网络连接失败，请检查后端服务是否正常运行');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="api-key-config">
      <div className="config-container">
        <div className="config-header">
          <h2>🔑 API密钥配置</h2>
          <p>请输入您的阿里云百炼API密钥和App ID以开始使用</p>
        </div>
        
        <form onSubmit={handleSubmit} className="config-form">
          <div className="form-group">
            <label htmlFor="apiKey">API Key:</label>
            <input
              type="password"
              id="apiKey"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="请输入您的API Key"
              required
              disabled={isLoading}
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="appId">App ID:</label>
            <input
              type="text"
              id="appId"
              value={appId}
              onChange={(e) => setAppId(e.target.value)}
              placeholder="请输入您的App ID"
              required
              disabled={isLoading}
            />
          </div>
          
          {error && (
            <div className="error-message">
              ❌ {error}
            </div>
          )}
          
          <button 
            type="submit" 
            className="submit-button"
            disabled={isLoading || !apiKey || !appId}
          >
            {isLoading ? '验证中...' : '验证并开始使用'}
          </button>
        </form>
        
        <div className="config-help">
          <h3>如何获取API密钥？</h3>
          <ol>
            <li>访问 <a href="https://bailian.console.aliyun.com/" target="_blank" rel="noopener noreferrer">阿里云百炼控制台</a></li>
            <li>创建应用并获取API Key和App ID</li>
            <li>将获取的密钥信息填入上方表单</li>
          </ol>
        </div>
      </div>
    </div>
  );
};

export default ApiKeyConfig;
