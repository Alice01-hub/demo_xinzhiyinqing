# 法律知识助手

一个基于React和阿里云百炼智能体的现代化法律知识问答系统，采用罗翔老师风格的专业法律咨询。

## 🌟 项目特色

- 🤖 **智能AI助手** - 集成阿里云百炼智能体，提供专业法律建议
- 🔑 **动态API密钥配置** - 用户可自行输入API密钥，无需预配置
- 📝 **Markdown渲染** - 支持结构化内容展示，阅读体验更佳
- 💡 **预设问题** - 提供常见法律问题快速入口
- 🎨 **现代化界面** - 仿照主流AI助手的界面设计
- 🔄 **对话重置** - 一键清空对话历史，重新开始交互
- 📱 **响应式设计** - 完美适配桌面端和移动端

## 🏗️ 项目结构

```
心知引擎/
├── frontend/                 # React前端应用
│   ├── src/
│   │   ├── components/       # React组件
│   │   │   ├── ApiKeyConfig.tsx    # API密钥配置组件
│   │   │   ├── ApiKeyConfig.css
│   │   │   ├── ChatInterface.tsx   # 聊天界面组件
│   │   │   └── ChatInterface.css
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── index.tsx
│   │   └── index.css
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
├── backend/                  # Python后端服务
│   ├── main.py              # FastAPI主服务
│   ├── config_manager.py    # 配置管理器
│   └── requirements.txt     # Python依赖
├── api-key.txt.example      # API密钥配置示例
├── .gitignore              # Git忽略文件
├── README.md               # 项目说明
└── SECURITY_GUIDE.md       # 安全配置指南
```

## 🚀 快速开始

### 环境要求

- Node.js 16+ 
- Python 3.8+
- 阿里云百炼API密钥

### 📝 最新更新

- ✅ 已更新为使用官方推荐的 `Application.call()` API
- ✅ 优化了API调用方式，提高兼容性
- ✅ 更新了依赖版本，确保稳定性

### 1. 启动后端服务

```bash
cd backend
pip install -r requirements.txt
python main.py
```

后端服务运行在 http://localhost:8000

**可选配置**：
```bash
# 自定义主机和端口
export HOST=0.0.0.0
export PORT=8080
python main.py
```

### 2. 启动前端服务

```bash
cd frontend
npm install
npm start
```

前端服务运行在 http://localhost:3000

**可选配置**：
```bash
# 自定义API服务器地址
export REACT_APP_API_BASE_URL=http://your-api-server:8080
npm start
```

### 3. 配置API密钥

1. 打开浏览器访问 http://localhost:3000
2. 在API密钥配置页面输入您的阿里云百炼API密钥和App ID
3. 点击"验证并开始使用"按钮
4. 验证成功后即可开始使用法律知识助手

## 🔧 获取API密钥

### 如何获取API密钥？

1. 访问 [阿里云百炼控制台](https://bailian.console.aliyun.com/)
2. 创建应用并获取API Key和App ID
3. 将获取的密钥信息填入配置页面

### 🔐 安全配置（重要！）

**请务必阅读 [安全配置指南](SECURITY_GUIDE.md) 了解如何安全地配置API密钥！**

#### 配置方法：

**方法一：使用配置文件（推荐）**
```bash
# 1. 复制示例配置文件
copy api-key.txt.example api-key.txt

# 2. 编辑配置文件，填入您的真实密钥
# API_KEY=your_real_api_key_here
# APP_ID=your_real_app_id_here
```

**方法二：设置环境变量**
```bash
# Windows PowerShell
$env:DASHSCOPE_API_KEY="your_api_key_here"
$env:APP_ID="your_app_id_here"

# Linux/Mac
export DASHSCOPE_API_KEY="your_api_key_here"
export APP_ID="your_app_id_here"
```

**方法三：使用配置管理器**
```bash
cd backend
python config_manager.py
```

⚠️ **重要提醒**：请勿将真实的API密钥提交到版本控制系统！

## 📖 使用说明

1. 首次使用需要配置API密钥
2. 配置成功后，可以点击预设问题或输入自定义法律问题
3. AI会提供专业的法律建议和解答
4. 支持多轮对话，可随时重新开始
5. 可以点击"重新配置"按钮更换API密钥

## 🛠️ 技术栈

### 前端
- **React 18** - 前端框架
- **TypeScript** - 类型安全
- **React Markdown** - Markdown渲染
- **CSS3** - 样式设计

### 后端
- **Python 3.8+** - 后端语言
- **FastAPI** - Web框架
- **阿里云百炼** - AI智能体服务
- **dashscope** - 阿里云百炼Python SDK (使用Application.call API)

## 🔒 安全特性

- ✅ **无硬编码密钥** - 代码中不包含任何敏感信息
- ✅ **多种配置方式** - 支持环境变量、配置文件、用户输入
- ✅ **自动安全检查** - 启动时自动验证配置完整性
- ✅ **Git安全** - 敏感文件已加入.gitignore
- ✅ **配置管理** - 提供专门的配置管理工具
- ✅ **API密钥验证** - 支持API密钥验证，确保输入正确
- ✅ **本地存储** - API密钥仅在本地存储，不会上传到服务器
- ✅ **随时更换** - 支持随时更换API密钥

## 🚀 部署

### 本地部署

1. 按照上述步骤启动前后端服务
2. 访问 http://localhost:3000 即可使用

### 生产环境部署

1. 构建前端：`npm run build`
2. 部署后端到服务器
3. 配置反向代理指向后端API
4. 部署前端静态文件

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

如有问题，请通过GitHub Issues联系。
