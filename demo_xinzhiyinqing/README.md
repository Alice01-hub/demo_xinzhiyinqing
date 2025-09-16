# 面试智能助手

一个基于React和阿里云百炼智能体的现代化法律知识问答系统，采用罗翔老师风格的专业法律咨询。

## 🌟 项目特色

- 🤖 **智能AI助手** - 集成阿里云百炼智能体，提供专业法律建议
- 📝 **Markdown渲染** - 支持结构化内容展示，阅读体验更佳
- 💡 **预设问题** - 提供常见法律问题快速入口
- 🎨 **现代化界面** - 仿照主流AI助手的界面设计
- 🔄 **对话重置** - 一键清空对话历史，重新开始交互
- 📱 **响应式设计** - 完美适配桌面端和移动端

## 🏗️ 项目结构

```
面试智能助手/
├── frontend/                 # React前端应用
│   ├── src/
│   │   ├── components/       # React组件
│   │   │   ├── ChatInterface.tsx
│   │   │   └── ChatInterface.css
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── public/
│   ├── package.json
│   └── tsconfig.json
├── backend/                  # Python后端服务
│   ├── main.py              # FastAPI主服务
│   ├── config.py            # 配置文件
│   ├── setup_env.py         # 环境设置
│   └── requirements.txt     # Python依赖
├── .gitignore
└── README.md
```

## 🚀 快速开始

### 环境要求

- Node.js 16+ 
- Python 3.8+
- 阿里云百炼API密钥

### 1. 克隆项目

```bash
git clone https://github.com/YOUR_USERNAME/面试智能助手.git
cd 面试智能助手
```

### 2. 启动后端服务

```bash
cd backend
pip install -r requirements.txt

# 配置环境变量
# 创建 .env 文件并添加：
# DASHSCOPE_API_KEY=your_api_key_here
# APP_ID=your_app_id_here

python main.py
```

后端服务运行在 http://localhost:8000

### 3. 启动前端服务

```bash
cd frontend
npm install
npm start
```

前端服务运行在 http://localhost:3000

## 🔧 环境配置

### 获取API密钥

1. 访问 [阿里云百炼](https://bailian.console.aliyun.com/)
2. 创建应用并获取API Key和App ID
3. 在 `backend/.env` 文件中配置：

```env
DASHSCOPE_API_KEY=your_api_key_here
APP_ID=your_app_id_here
```

### 前端API配置

在 `frontend/src/components/ChatInterface.tsx` 中修改API地址：

```typescript
const API_BASE_URL = 'http://localhost:8000'; // 开发环境
// 生产环境请修改为实际的后端地址
```

## 📖 使用说明

1. 打开应用后，会看到罗翔老师法律知识顾问的欢迎界面
2. 点击预设问题或输入自定义法律问题
3. AI会提供专业的法律建议和解答
4. 支持多轮对话，可随时重新开始

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

## 🚀 部署

### GitHub Pages 部署

1. 推送代码到GitHub
2. 在仓库设置中启用GitHub Pages
3. 配置GitHub Actions自动构建和部署

详细部署说明请参考 [DEPLOYMENT.md](./DEPLOYMENT.md)

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📞 联系方式

如有问题，请通过GitHub Issues联系。
