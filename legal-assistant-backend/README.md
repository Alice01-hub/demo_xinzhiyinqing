# 法律助手终端对话程序

基于阿里云百炼智能体的法律知识助手终端对话程序，支持多轮对话和短期记忆。

## 功能特点

- 🤖 **百炼智能体集成** - 接入阿里云百炼平台自定义智能体
- 💬 **多轮对话** - 支持连续对话，保持上下文
- 🧠 **短期记忆** - 记住最近5轮对话内容
- 🏛️ **法律专业** - 专门针对法律问题优化
- 🎯 **简单易用** - 终端界面，操作简单
- 🔒 **API密钥管理** - 安全的API密钥配置

## 技术栈

- **DashScope** - 阿里云百炼智能体SDK
- **Python 3.7+** - 编程语言
- **datetime** - 时间处理
- **sys** - 系统交互

## 项目结构

```
legal-assistant-backend/
├── chat_cli.py          # 终端对话程序
├── start_chat.py        # 快速启动脚本
├── main.py              # FastAPI服务（可选）
├── config.py            # 配置文件
├── requirements.txt     # 依赖包列表
└── README.md           # 项目说明
```

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置API密钥

确保在项目根目录有 `api-key.txt` 文件，包含以下内容：
```
API_KEY=your_dashscope_api_key
APP_ID=your_app_id
```

### 3. 启动程序

**方式一：使用批处理文件（Windows推荐）**
```bash
# 启动聊天程序
start_chat.bat

# 启动API服务
start_server.bat
```

**方式二：使用Python脚本**
```bash
# 启动聊天程序
python start_chat.py

# 启动API服务
python main.py
```

**方式三：手动设置环境变量**
```bash
# Windows
set DASHSCOPE_API_KEY=your_api_key
set APP_ID=your_app_id

# Linux/Mac
export DASHSCOPE_API_KEY=your_api_key
export APP_ID=your_app_id
```

## 使用说明

### 基本操作

1. **开始对话**：程序启动后，直接输入您的问题
2. **多轮对话**：可以连续提问，AI会记住最近5轮对话
3. **特殊命令**：
   - 输入 `quit` 或 `exit` 退出程序
   - 输入 `clear` 清空对话历史
   - 输入 `history` 查看对话历史

### 对话示例

```
👤 您：什么是合同法？
🤖 罗老师：合同法是指调整平等主体之间合同关系的法律规范...

👤 您：合同的基本要素有哪些？
🤖 罗老师：根据我们刚才讨论的合同法，合同的基本要素包括...
```

### 记忆功能

- 程序会记住最近5轮对话内容
- 超过5轮的对话会被自动清除
- 每次对话都会包含历史上下文

## 环境变量

可以通过环境变量配置API密钥：

```bash
export DASHSCOPE_API_KEY="your_api_key"
export APP_ID="your_app_id"
```

## 错误处理

程序包含完整的错误处理机制：

- API调用失败时的友好提示
- 网络连接问题的处理
- 用户输入验证
- 程序异常的安全退出

## 开发说明

### 修改记忆大小

在 `chat_cli.py` 中修改 `memory_size` 参数：

```python
assistant = LegalAssistant(memory_size=5)  # 改为你想要的轮数
```

### 自定义提示词

在 `build_context_prompt` 方法中修改提示词模板。

### 修改配置

在 `config.py` 中修改相关配置，支持环境变量和文件配置两种方式。

## 许可证

MIT License
