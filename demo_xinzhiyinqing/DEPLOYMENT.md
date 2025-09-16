# 部署指南

## GitHub Pages 部署

### 1. 推送代码到GitHub

```bash
# 初始化Git仓库
git init

# 添加文件
git add .

# 提交代码
git commit -m "Initial commit: 面试智能助手"

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

### 3. 配置GitHub Actions

在项目根目录创建 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v3
      
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
        cache-dependency-path: frontend/package-lock.json
        
    - name: Install dependencies
      run: |
        cd frontend
        npm ci
        
    - name: Build
      run: |
        cd frontend
        npm run build
        
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./frontend/build
```

### 4. 访问部署的网站

部署完成后，您的网站将在以下地址访问：
`https://YOUR_USERNAME.github.io/YOUR_REPO_NAME`

## 本地开发

### 前端开发
```bash
cd frontend
npm install
npm start
```

### 后端开发
```bash
cd backend
pip install -r requirements.txt
python main.py
```

## 环境变量配置

### 后端环境变量
创建 `backend/.env` 文件：
```env
DASHSCOPE_API_KEY=your_api_key_here
APP_ID=your_app_id_here
```

### 前端API配置
在 `frontend/src/components/ChatInterface.tsx` 中修改API地址：
```typescript
const API_BASE_URL = 'https://your-backend-domain.com';
```

## 注意事项

1. **API密钥安全**：不要将API密钥提交到GitHub，使用环境变量
2. **CORS配置**：确保后端允许前端域名的跨域请求
3. **HTTPS**：生产环境建议使用HTTPS
4. **域名配置**：可以配置自定义域名指向GitHub Pages
