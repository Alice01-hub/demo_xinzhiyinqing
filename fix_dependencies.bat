@echo off
echo 正在修复依赖问题...

echo.
echo 1. 清理 legal-assistant 项目的 node_modules 和 package-lock.json
cd legal-assistant
if exist node_modules rmdir /s /q node_modules
if exist package-lock.json del package-lock.json

echo.
echo 2. 重新安装依赖
npm install --legacy-peer-deps

echo.
echo 3. 测试构建
npm run build

if %errorlevel% equ 0 (
    echo.
    echo ✅ 构建成功！GitHub部署问题已修复。
) else (
    echo.
    echo ❌ 构建失败，请检查错误信息。
)

echo.
echo 4. 清理 demo_xinzhiyinqing 项目的依赖
cd ..\demo_xinzhiyinqing\frontend
if exist node_modules rmdir /s /q node_modules
if exist package-lock.json del package-lock.json

echo.
echo 5. 重新安装依赖
npm install --legacy-peer-deps

echo.
echo 6. 测试构建
npm run build

if %errorlevel% equ 0 (
    echo.
    echo ✅ demo_xinzhiyinqing 构建也成功！
) else (
    echo.
    echo ❌ demo_xinzhiyinqing 构建失败，请检查错误信息。
)

echo.
echo 修复完成！现在可以提交代码到GitHub了。
pause
