import React from 'react';
import './App.css';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <div className="App">
      <div className="page-header">
        <h1>法律是道德的最低标准</h1>
      </div>
      <ChatInterface />
    </div>
  );
}

export default App;