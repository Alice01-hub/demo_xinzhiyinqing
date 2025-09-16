import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 从环境变量读取API配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
APP_ID = os.getenv("APP_ID")

# 检查环境变量是否设置
if not DASHSCOPE_API_KEY:
    print("❌ 错误: 未设置 DASHSCOPE_API_KEY 环境变量")
    print("请设置环境变量: export DASHSCOPE_API_KEY=your_api_key")
    exit(1)

if not APP_ID:
    print("❌ 错误: 未设置 APP_ID 环境变量")
    print("请设置环境变量: export APP_ID=your_app_id")
    exit(1)

print(f"✅ API Key: {DASHSCOPE_API_KEY[:10]}...")
print(f"✅ App ID: {APP_ID}")
