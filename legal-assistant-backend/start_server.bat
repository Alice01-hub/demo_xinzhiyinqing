@echo off
echo 🚀 启动法律助手后端服务...

REM 设置环境变量
call setup_env.bat
if errorlevel 1 (
    echo ❌ 环境变量设置失败
    pause
    exit /b 1
)

echo.
echo 🚀 启动FastAPI服务...
python main.py

pause
