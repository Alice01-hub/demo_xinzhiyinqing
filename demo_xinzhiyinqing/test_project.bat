@echo off
echo 🚀 正在测试demo_xinzhiyinqing项目...

echo.
echo 1. 检查后端服务状态
curl -s http://localhost:8000/health
if %errorlevel% equ 0 (
    echo ✅ 后端服务运行正常
) else (
    echo ❌ 后端服务未启动，正在启动...
    start /B cmd /c "cd backend && python main.py"
    timeout /t 3
)

echo.
echo 2. 检查前端服务状态
curl -s http://localhost:3000
if %errorlevel% equ 0 (
    echo ✅ 前端服务运行正常
) else (
    echo ❌ 前端服务未启动，正在启动...
    start /B cmd /c "cd frontend && npm start"
    timeout /t 5
)

echo.
echo 3. 测试API连接
curl -X POST http://localhost:8000/test
if %errorlevel% equ 0 (
    echo ✅ API连接测试成功
) else (
    echo ❌ API连接测试失败
)

echo.
echo 4. 打开浏览器
echo 正在打开浏览器访问项目...
start http://localhost:3000

echo.
echo 测试完成！
echo 前端地址: http://localhost:3000
echo 后端地址: http://localhost:8000
echo API文档: http://localhost:8000/docs
pause
