# GitHub仓库配置指南

## 当前状态
✅ 本地代码已修复并提交
✅ GitHub Actions配置文件已创建
✅ 构建问题已解决

## 下一步：配置GitHub远程仓库

### 1. 在GitHub上创建新仓库
1. 访问 https://github.com
2. 点击右上角的 "+" 按钮
3. 选择 "New repository"
4. 仓库名称建议：`legal-assistant` 或 `心知引擎`
5. 选择 "Public"（用于GitHub Pages）
6. **不要**勾选 "Add a README file"（因为我们已经有了）
7. 点击 "Create repository"

### 2. 配置本地仓库连接
创建仓库后，GitHub会显示连接命令，类似这样：

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### 3. 启用GitHub Pages
1. 在仓库页面，点击 "Settings"
2. 找到 "Pages" 选项
3. 在 "Source" 下选择 "GitHub Actions"
4. 保存设置

### 4. 推送代码
运行以下命令推送代码：
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

## 预期结果
推送后，GitHub Actions会自动：
1. 检测到代码推送
2. 运行构建流程
3. 部署到GitHub Pages
4. 您的网站将在 `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME` 访问

## 故障排除
如果部署失败，请检查：
1. GitHub Actions日志
2. 确保仓库是公开的
3. 确保GitHub Pages已启用
