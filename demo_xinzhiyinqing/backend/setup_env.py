#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
环境变量设置脚本
从api-key.txt文件读取配置并设置环境变量
"""

import os
import sys

def setup_environment():
    """设置环境变量"""
    print("🔧 设置环境变量...")
    
    # 从api-key.txt文件读取配置
    api_key_file = "../api-key.txt"
    
    try:
        with open(api_key_file, "r", encoding="utf-8") as f:
            content = f.read()
            
        api_key = None
        app_id = None
        
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("API_KEY="):
                api_key = line.split("=", 1)[1].strip()
            elif line.startswith("APP_ID="):
                app_id = line.split("=", 1)[1].strip()
        
        if not api_key or not app_id:
            print("❌ 错误: api-key.txt文件格式不正确")
            print("请确保文件包含:")
            print("API_KEY=your_api_key")
            print("APP_ID=your_app_id")
            return False
        
        # 设置环境变量
        os.environ["DASHSCOPE_API_KEY"] = api_key
        os.environ["APP_ID"] = app_id
        
        print(f"✅ API Key: {api_key[:10]}...")
        print(f"✅ App ID: {app_id}")
        print("✅ 环境变量设置成功!")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ 错误: 未找到文件 {api_key_file}")
        print("请确保api-key.txt文件存在于上级目录")
        return False
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

if __name__ == "__main__":
    if setup_environment():
        print("\n🚀 现在可以运行程序了:")
        print("python main.py")
        print("python chat_cli.py")
    else:
        print("\n❌ 环境变量设置失败")
        sys.exit(1)
