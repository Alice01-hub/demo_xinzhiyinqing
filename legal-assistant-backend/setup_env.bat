@echo off
echo 🔧 设置环境变量...

REM 从api-key.txt文件读取配置
for /f "tokens=1,2 delims==" %%a in (..\api-key.txt) do (
    if "%%a"=="API_KEY" set DASHSCOPE_API_KEY=%%b
    if "%%a"=="APP_ID" set APP_ID=%%b
)

REM 检查是否读取成功
if "%DASHSCOPE_API_KEY%"=="" (
    echo ❌ 错误: 未找到API_KEY配置
    echo 请确保..\api-key.txt文件包含: API_KEY=your_api_key
    pause
    exit /b 1
)

if "%APP_ID%"=="" (
    echo ❌ 错误: 未找到APP_ID配置
    echo 请确保..\api-key.txt文件包含: APP_ID=your_app_id
    pause
    exit /b 1
)

echo ✅ API Key: %DASHSCOPE_API_KEY:~0,10%...
echo ✅ App ID: %APP_ID%
echo ✅ 环境变量设置成功!

echo.
echo 🚀 现在可以运行程序了:
echo python main.py
echo python chat_cli.py
echo.
pause
