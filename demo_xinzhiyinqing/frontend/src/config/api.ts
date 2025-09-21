// API配置
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const API_ENDPOINTS = {
  VALIDATE_API_KEY: `${API_BASE_URL}/validate-api-key`,
  CHAT: `${API_BASE_URL}/chat`,
  HEALTH: `${API_BASE_URL}/health`,
} as const;

export default API_BASE_URL;
