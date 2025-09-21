from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from http import HTTPStatus
from dashscope import Application
import sys
import os

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 使用新的配置管理器
from config_manager import get_config

# 获取配置
config_manager = get_config()

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
    api_key: str = ""
    app_id: str = ""

class ApiKeyRequest(BaseModel):
    api_key: str
    app_id: str

# 响应模型
class ChatResponse(BaseModel):
    success: bool
    message: str
    response: str = ""
    request_id: str = ""

class ApiKeyResponse(BaseModel):
    success: bool
    message: str

@app.get("/")
async def root():
    return {"message": "法律助手API服务正在运行", "status": "ok"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "legal-assistant-api"}

@app.post("/validate-api-key", response_model=ApiKeyResponse)
async def validate_api_key(request: ApiKeyRequest):
    """
    验证API密钥和App ID
    """
    try:
        # 验证API密钥和App ID是否提供
        if not request.api_key or not request.app_id:
            return ApiKeyResponse(
                success=False,
                message="请提供API密钥和App ID"
            )
        
        # 使用Application.call()进行测试调用
        response = Application.call(
            api_key=request.api_key,
            app_id=request.app_id,
            prompt="你好，请简单介绍一下你自己"
        )
        
        if response.status_code == HTTPStatus.OK:
            return ApiKeyResponse(
                success=True,
                message="智能体验证成功"
            )
        else:
            return ApiKeyResponse(
                success=False,
                message=f"智能体验证失败: {response.message}"
            )
            
    except Exception as e:
        return ApiKeyResponse(
            success=False,
            message=f"验证过程中出现错误: {str(e)}"
        )

@app.post("/chat", response_model=ChatResponse)
async def chat_with_ai(request: ChatRequest):
    """
    与AI进行对话的接口
    """
    try:
        # 验证API密钥和App ID
        if not request.api_key or not request.app_id:
            return ChatResponse(
                success=False,
                message="请提供有效的API密钥和App ID"
            )
        
        # 调用Application API
        response = Application.call(
            api_key=request.api_key,
            app_id=request.app_id,
            prompt=request.message
        )
        
        if response.status_code != HTTPStatus.OK:
            return ChatResponse(
                success=False,
                message=f"智能体调用失败: {response.message}",
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
        # 使用Application.call()
        response = Application.call(
            api_key=config_manager.get_api_key(),
            app_id=config_manager.get_app_id(),
            prompt="你好，请简单介绍一下你自己"
        )
        
        if response.status_code == HTTPStatus.OK:
            return {
                "success": True,
                "message": "智能体连接测试成功",
                "response": response.output.text,
                "request_id": getattr(response, 'request_id', 'unknown')
            }
        else:
            return {
                "success": False,
                "message": f"智能体连接测试失败: {response.message}",
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
    # 从环境变量获取配置，提供默认值
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', '8000'))
    uvicorn.run(app, host=host, port=port)
