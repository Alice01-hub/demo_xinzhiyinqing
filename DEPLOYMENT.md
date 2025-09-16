# 部署指南

## GitHub Pages 部署

### 1. 推送代码到GitHub

```bash
# 添加远程仓库
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# 推送代码
git push -u origin main
```

### 2. 配置GitHub Pages

1. 在GitHub仓库页面，点击 "Settings"
2. 找到 "Pages" 选项
3. 选择 "Deploy from a branch"
4. 选择 "main" 分支和 "/ (root)" 文件夹
5. 点击 "Save"

### 3. 自动部署

项目已配置GitHub Actions，每次推送代码到main分支时会自动：
- 安装依赖
- 构建React应用
- 部署到GitHub Pages

### 4. 访问部署的网站

部署完成后，您的网站将在以下地址访问：
`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## 本地开发

### 前端开发
```bash
cd legal-assistant
npm install
npm start
```

### 后端开发
```bash
cd legal-assistant-backend
pip install -r requirements.txt
python main.py
```

## 环境变量配置

### 后端环境变量
创建 `legal-assistant-backend/.env` 文件：
```env
DASHSCOPE_API_KEY=your_api_key_here
APP_ID=your_app_id_here
```

### 前端API配置
在 `legal-assistant/src/components/ChatInterface.tsx` 中修改API地址：
```typescript
const API_BASE_URL = 'https://your-backend-domain.com';
```

## 注意事项

1. **API密钥安全**：不要将API密钥提交到GitHub，使用环境变量
2. **CORS配置**：确保后端允许前端域名的跨域请求
3. **HTTPS**：生产环境建议使用HTTPS
4. **域名配置**：可以配置自定义域名指向GitHub Pages
