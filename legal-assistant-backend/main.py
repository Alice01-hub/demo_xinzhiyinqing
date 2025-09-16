from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from http import HTTPStatus
from dashscope import Application
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 先设置环境变量，再导入config
from setup_env import setup_environment
if not setup_environment():
    print("❌ 环境变量设置失败，程序退出")
    sys.exit(1)

import config

app = FastAPI(title="法律助手API", description="基于通义千问的法律知识助手后端服务", version="1.0.0")

# 添加CORS中间件，允许前端跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该指定具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class ChatRequest(BaseModel):
    message: str
    user_id: str = "default_user"

# 响应模型
class ChatResponse(BaseModel):
    success: bool
    message: str
    response: str = ""
    request_id: str = ""

@app.get("/")
async def root():
    return {"message": "法律助手API服务正在运行", "status": "ok"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "legal-assistant-api"}

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    与AI进行对话的接口
    """
    try:
        # 调用阿里云百炼智能体API
        response = Application.call(
            api_key=config.DASHSCOPE_API_KEY,
            app_id=config.APP_ID,
            prompt=request.message
        )
        
        if response.status_code != HTTPStatus.OK:
            return ChatResponse(
                success=False,
                message=f"API调用失败: {response.message}",
                request_id=getattr(response, 'request_id', 'unknown')
            )
        
        return ChatResponse(
            success=True,
            message="请求成功",
            response=response.output.text,
            request_id=getattr(response, 'request_id', 'unknown')
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"服务器内部错误: {str(e)}"
        )

@app.post("/test")
async def test_api():
    """
    测试API连接
    """
    try:
        # 发送一个简单的测试消息
        response = Application.call(
            api_key=config.DASHSCOPE_API_KEY,
            app_id=config.APP_ID,
            prompt="你好，请简单介绍一下你自己"
        )
        
        if response.status_code == HTTPStatus.OK:
            return {
                "success": True,
                "message": "API连接测试成功",
                "response": response.output.text,
                "request_id": getattr(response, 'request_id', 'unknown')
            }
        else:
            return {
                "success": False,
                "message": f"API连接测试失败: {response.message}",
                "code": response.status_code,
                "request_id": getattr(response, 'request_id', 'unknown')
            }
            
    except Exception as e:
        return {
            "success": False,
            "message": f"测试过程中出现错误: {str(e)}"
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
