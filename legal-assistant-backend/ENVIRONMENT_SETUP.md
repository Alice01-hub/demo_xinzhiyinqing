# 环境变量配置指南

## ✅ 环境变量配置完成！

程序已成功修改为使用 `os.getenv()` 方式管理API密钥，更加安全和灵活。

## 🔧 配置方式

### 方式一：自动配置（推荐）

程序会自动从 `../api-key.txt` 文件读取配置并设置环境变量：

```bash
# 启动API服务
python main.py

# 启动聊天程序
python chat_cli.py
```

### 方式二：使用批处理文件（Windows）

```bash
# 启动API服务
start_server.bat

# 启动聊天程序
start_chat.bat
```

### 方式三：手动设置环境变量

**Windows:**
```cmd
set DASHSCOPE_API_KEY=your_api_key
set APP_ID=your_app_id
python main.py
```

**Linux/Mac:**
```bash
export DASHSCOPE_API_KEY=your_api_key
export APP_ID=your_app_id
python main.py
```

## 📁 文件结构

```
legal-assistant-backend/
├── main.py              # 主API服务
├── chat_cli.py          # 聊天程序
├── config.py            # 配置管理（使用环境变量）
├── setup_env.py         # 环境变量设置脚本
├── setup_env.bat        # Windows批处理文件
├── start_server.bat     # 启动API服务
├── start_chat.bat       # 启动聊天程序
└── ../api-key.txt       # API密钥文件
```

## 🔒 安全特性

1. **环境变量隔离**：API密钥存储在环境变量中，不会硬编码在代码里
2. **自动配置**：程序启动时自动从文件读取并设置环境变量
3. **错误检查**：启动时检查环境变量是否正确设置
4. **灵活配置**：支持多种配置方式

## 🚀 使用步骤

1. **确保api-key.txt文件存在**：
   ```
   API_KEY=your_dashscope_api_key
   APP_ID=your_app_id
   ```

2. **启动程序**：
   ```bash
   python main.py
   ```

3. **查看输出**：
   ```
   🔧 设置环境变量...
   ✅ API Key: sk-9c8db66...
   ✅ App ID: 1bf4a3d9135f46d184163505fdb5b41d
   ✅ 环境变量设置成功!
   INFO:     Started server process [xxxx]
   INFO:     Uvicorn running on http://0.0.0.0:8000
   ```

## 🐛 故障排除

### 环境变量设置失败
- 检查 `../api-key.txt` 文件是否存在
- 确认文件格式正确（API_KEY=xxx, APP_ID=xxx）
- 查看错误提示信息

### API调用失败
- 确认环境变量已正确设置
- 检查API密钥是否有效
- 查看控制台输出

## ✨ 优势

1. **更安全**：API密钥不直接写在代码中
2. **更灵活**：支持多种配置方式
3. **更易维护**：配置集中管理
4. **更易部署**：支持容器化部署

现在您的程序已经使用环境变量管理API密钥了！🎉
