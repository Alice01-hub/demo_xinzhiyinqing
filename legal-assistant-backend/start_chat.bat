@echo off
echo 🚀 启动法律助手聊天程序...

REM 设置环境变量
call setup_env.bat
if errorlevel 1 (
    echo ❌ 环境变量设置失败
    pause
    exit /b 1
)

echo.
echo 🚀 启动聊天程序...
python chat_cli.py

pause
