import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import rehypeHighlight from 'rehype-highlight';
import './ChatInterface.css';

interface Message {
  id: number;
  text: string;
  isUser: boolean;
  timestamp: Date;
}

interface ChatRequest {
  message: string;
  user_id: string;
}

interface ChatResponse {
  success: boolean;
  message: string;
  response: string;
  request_id: string;
}

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [conversationHistory, setConversationHistory] = useState<Message[]>([]);
  const [showWelcome, setShowWelcome] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  
  // 预设问题
  const presetQuestions = [
    "我同事在微信群里说我偷东西，其实根本没有的事，现在大家都用异样眼光看我。我能告他吗？",
    "我在街上看到一个老人摔倒，想扶又怕被讹，你说我该怎么办？",
    "我不想卷了，打算辞职躺平，天天打游戏，靠父母养着。这违法吗？"
  ];
  
  // 相关预设问题（在AI回复后显示）
  const contextualQuestions = [
    "如何收集证据？",
    "诽谤罪的构成要件是什么？",
    "起诉流程是怎样的？"
  ];
  
  // 后端API地址
  const API_BASE_URL = 'http://localhost:8000';

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // 调用后端API
  const callBackendAPI = async (message: string): Promise<string> => {
    try {
      const requestData: ChatRequest = {
        message: message,
        user_id: 'web_user'
      };

      const response = await fetch(`${API_BASE_URL}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ChatResponse = await response.json();
      
      if (data.success) {
        return data.response;
      } else {
        throw new Error(data.message || 'API调用失败');
      }
    } catch (error) {
      console.error('API调用错误:', error);
      return `抱歉，服务暂时不可用。错误信息：${error instanceof Error ? error.message : '未知错误'}`;
    }
  };

  const handleSendMessage = async (customInput?: string) => {
    const messageText = customInput || inputText;
    if (!messageText.trim()) return;

    setShowWelcome(false); // 隐藏欢迎界面

    const userMessage: Message = {
      id: Date.now(),
      text: messageText,
      isUser: true,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setConversationHistory(prev => [...prev, userMessage]);
    setInputText('');
    setIsLoading(true);

    try {
      // 调用后端API获取真实回复
      const aiResponseText = await callBackendAPI(messageText);
      
      const aiResponse: Message = {
        id: Date.now() + 1,
        text: aiResponseText,
        isUser: false,
        timestamp: new Date()
      };
      
      setMessages(prev => [...prev, aiResponse]);
      setConversationHistory(prev => [...prev, aiResponse]);
    } catch (error) {
      console.error('发送消息失败:', error);
      const errorMessage: Message = {
        id: Date.now() + 1,
        text: '抱歉，发送消息时出现错误，请稍后重试。',
        isUser: false,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };


  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  // 重置对话功能
  const handleResetConversation = () => {
    setMessages([]);
    setConversationHistory([]);
    setInputText('');
    setIsLoading(false);
    setShowWelcome(true);
  };

  // 处理预设问题点击
  const handlePresetQuestion = async (question: string) => {
    setShowWelcome(false);
    setInputText(question);
    await handleSendMessage(question);
  };

  // 处理相关预设问题点击
  const handleContextualQuestion = async (question: string) => {
    setInputText(question);
    await handleSendMessage(question);
  };

  // 重新生成消息
  const handleRegenerateMessage = async (messageId: number) => {
    // 找到要重新生成的消息
    const messageIndex = messages.findIndex(msg => msg.id === messageId);
    if (messageIndex === -1) return;
    
    const message = messages[messageIndex];
    if (message.isUser) return; // 只重新生成AI消息
    
    // 找到对应的用户消息
    const userMessageIndex = messageIndex - 1;
    if (userMessageIndex < 0) return;
    
    const userMessage = messages[userMessageIndex];
    if (userMessage.isUser) {
      // 移除当前AI消息
      setMessages(prev => prev.filter(msg => msg.id !== messageId));
      setIsLoading(true);
      
      try {
        // 重新调用API
        const aiResponseText = await callBackendAPI(userMessage.text);
        
        const newAiResponse: Message = {
          id: Date.now(),
          text: aiResponseText,
          isUser: false,
          timestamp: new Date()
        };
        
        setMessages(prev => [...prev, newAiResponse]);
      } catch (error) {
        console.error('重新生成消息失败:', error);
        // 恢复原消息
        setMessages(prev => [...prev, message]);
      } finally {
        setIsLoading(false);
      }
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {showWelcome && (
          <div className="welcome-screen">
            <div className="ai-avatar">
              <div className="avatar-icon">罗</div>
            </div>
            <h2 className="ai-title">罗老师法律知识顾问</h2>
            <p className="ai-description">我是一位专业的法律顾问，也是一名刑法学教师，我可以解答你的一切法律问题，也可以和你探讨哲学问题。</p>
            
            <div className="preset-questions">
              {presetQuestions.map((question, index) => (
                <button
                  key={index}
                  className="preset-question-btn"
                  onClick={() => handlePresetQuestion(question)}
                >
                  <span className="question-icon">💎</span>
                  <span className="question-text">{question}</span>
                  <span className="question-arrow">→</span>
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((message) => (
          <div
            key={message.id}
            className={`message ${message.isUser ? 'user-message' : 'ai-message'}`}
          >
            <div className="message-content">
              {message.isUser ? (
                message.text
              ) : (
                <div className="markdown-content">
                  <ReactMarkdown
                    remarkPlugins={[remarkGfm]}
                    rehypePlugins={[rehypeHighlight]}
                  >
                    {message.text}
                  </ReactMarkdown>
                </div>
              )}
            </div>
            <div className="message-footer">
              <div className="message-time">
                {message.timestamp.toLocaleTimeString()}
              </div>
              {!message.isUser && (
                <div className="message-actions">
                  <button 
                    className="action-btn" 
                    title="复制"
                    onClick={() => navigator.clipboard.writeText(message.text)}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                      <rect x="9" y="9" width="13" height="13" rx="2" ry="2" stroke="currentColor" strokeWidth="2"/>
                      <path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1" stroke="currentColor" strokeWidth="2"/>
                    </svg>
                  </button>
                  <button 
                    className="action-btn" 
                    title="重新生成"
                    onClick={() => handleRegenerateMessage(message.id)}
                  >
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                      <path d="M3 12a9 9 0 019-9 9.75 9.75 0 016.74 2.74L21 8" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      <path d="M21 3v5h-5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      <path d="M21 12a9 9 0 01-9 9 9.75 9.75 0 01-6.74-2.74L3 16" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                      <path d="M3 21v-5h5" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                    </svg>
                  </button>
                </div>
              )}
            </div>
          </div>
        ))}
        
        {messages.length > 0 && !isLoading && (
          <div className="contextual-questions">
            {contextualQuestions.map((question, index) => (
              <button
                key={index}
                className="contextual-question-btn"
                onClick={() => handleContextualQuestion(question)}
              >
                {question}
              </button>
            ))}
          </div>
        )}
        
        {isLoading && (
          <div className="message ai-message">
            <div className="message-content">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-container">
        <div className="input-area">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="遇事莫慌，罗老师在此"
            className="chat-input"
            rows={1}
          />
          
          <div className="input-footer">
            <div className="footer-left">
              <button className="input-icon-btn" title="附件">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M21.44 11.05l-9.19 9.19a6 6 0 01-8.49-8.49l9.19-9.19a4 4 0 015.66 5.66L9.64 16.2a2 2 0 01-2.83-2.83l8.49-8.49" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
              <button className="input-icon-btn" title="图片">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <rect x="3" y="3" width="18" height="18" rx="2" ry="2" stroke="currentColor" strokeWidth="2"/>
                  <circle cx="8.5" cy="8.5" r="1.5" fill="currentColor"/>
                  <path d="M21 15l-5-5L5 21" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
              <button className="input-icon-btn" title="展开">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M8 3H5a2 2 0 00-2 2v3m18 0V5a2 2 0 00-2-2h-3m0 18h3a2 2 0 002-2v-3M3 16v3a2 2 0 002 2h3" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
              <button 
                className="input-icon-btn reset-icon" 
                title="重新开始对话"
                onClick={handleResetConversation}
              >
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
                  <path d="M4 12a8 8 0 018-8V2.5L16 6l-4 3.5V8a6 6 0 00-6 6c0 1.657.672 3.157 1.757 4.243L6.343 20.343A8 8 0 014 12z" fill="currentColor"/>
                </svg>
              </button>
            </div>
            
            <div className="footer-right">
              <button
                onClick={() => handleSendMessage()}
                disabled={!inputText.trim() || isLoading}
                className="send-button"
              >
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                  <path d="M12 19V5M5 12l7-7 7 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>
        
        <div className="disclaimer">
          内容由AI生成，仅供参考
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;
