#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试前后端连接
"""

import subprocess
import time
import requests
import json
import sys

def start_server():
    """启动后端服务"""
    print("🚀 启动后端服务...")
    try:
        # 启动服务
        process = subprocess.Popen([sys.executable, "main.py"], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        
        # 等待服务启动
        print("⏳ 等待服务启动...")
        time.sleep(5)
        
        return process
    except Exception as e:
        print(f"❌ 启动服务失败: {e}")
        return None

def test_api():
    """测试API连接"""
    print("🧪 测试API连接...")
    try:
        response = requests.post('http://localhost:8000/chat', 
                               json={'message': '你好', 'user_id': 'test'},
                               timeout=10)
        
        print(f"✅ 状态码: {response.status_code}")
        print(f"✅ 响应: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ API测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("🔧 前后端连接测试")
    print("=" * 50)
    
    # 启动服务
    process = start_server()
    if not process:
        return
    
    try:
        # 测试API
        if test_api():
            print("\n🎉 前后端连接测试成功！")
            print("现在可以启动前端进行测试了。")
        else:
            print("\n❌ 前后端连接测试失败！")
    finally:
        # 清理
        if process:
            print("\n🛑 停止服务...")
            process.terminate()
            process.wait()

if __name__ == "__main__":
    main()
