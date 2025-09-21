# 🔐 安全配置指南

## 重要提醒

**请勿将真实的API密钥提交到版本控制系统！** 这就像把银行卡密码写在纸上贴在墙上一样危险。

## 配置方法

### 方法一：使用配置文件（推荐）

1. 复制示例配置文件：
   ```bash
   copy api-key.txt.example api-key.txt
   ```

2. 编辑 `api-key.txt` 文件，填入您的真实密钥：
   ```
   API_KEY=your_real_api_key_here
   APP_ID=your_real_app_id_here
   ```

3. 确保 `api-key.txt` 在 `.gitignore` 中（已自动配置）

### 方法二：设置环境变量

#### Windows PowerShell：
```powershell
$env:DASHSCOPE_API_KEY="your_api_key_here"
$env:APP_ID="your_app_id_here"
```

#### Windows CMD：
```cmd
set DASHSCOPE_API_KEY=your_api_key_here
set APP_ID=your_app_id_here
```

#### Linux/Mac：
```bash
export DASHSCOPE_API_KEY="your_api_key_here"
export APP_ID="your_app_id_here"
```

### 方法三：使用配置管理器

运行配置管理器：
```bash
cd backend
python config_manager.py
```

按照提示进行配置。

## 安全检查清单

- [ ] 确认没有硬编码的API密钥在代码中
- [ ] 确认 `api-key.txt` 在 `.gitignore` 中
- [ ] 确认不会将敏感文件提交到Git
- [ ] 定期轮换API密钥
- [ ] 不要在公开场所或截图中显示API密钥

## 如果密钥泄露了怎么办？

1. **立即更换API密钥** - 在阿里云控制台重新生成
2. **检查使用情况** - 查看API调用日志
3. **更新所有环境** - 确保新密钥在所有地方都更新了
4. **检查代码仓库** - 确保没有历史记录包含旧密钥

## 最佳实践

1. **使用环境变量** - 生产环境推荐使用环境变量
2. **配置文件权限** - 确保配置文件只有您能读取
3. **定期检查** - 定期检查代码中是否有敏感信息
4. **团队协作** - 团队成员之间通过安全渠道分享密钥

## 故障排除

### 问题：提示"配置未完成"
**解决方案**：按照上述方法之一配置API密钥

### 问题：API调用失败
**解决方案**：
1. 检查API密钥是否正确
2. 检查网络连接
3. 检查API服务状态

### 问题：配置文件读取失败
**解决方案**：
1. 检查文件路径是否正确
2. 检查文件格式是否正确
3. 检查文件权限
