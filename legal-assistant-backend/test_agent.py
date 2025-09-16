#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试阿里云百炼智能体
"""

import sys
import os
from http import HTTPStatus

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 先设置环境变量，再导入config
from setup_env import setup_environment
if not setup_environment():
    print("❌ 环境变量设置失败，程序退出")
    sys.exit(1)

import config
from dashscope import Application

def test_agent():
    """测试百炼智能体"""
    print("🧪 测试阿里云百炼智能体...")
    
    try:
        print(f"API Key: {config.DASHSCOPE_API_KEY[:10]}...")
        print(f"App ID: {config.APP_ID}")
        
        # 调用百炼智能体
        response = Application.call(
            api_key=config.DASHSCOPE_API_KEY,
            app_id=config.APP_ID,
            prompt="你好，请简单介绍一下你自己"
        )
        
        print(f"状态码: {response.status_code}")
        print(f"请求ID: {response.request_id}")
        
        if response.status_code == HTTPStatus.OK:
            print("✅ 百炼智能体调用成功！")
            print(f"回复内容: {response.output.text}")
            return True
        else:
            print("❌ 百炼智能体调用失败")
            print(f"错误信息: {response.message}")
            print(f"请参考文档：https://help.aliyun.com/zh/model-studio/developer-reference/error-code")
            return False
            
    except Exception as e:
        print(f"❌ 测试过程中出现错误: {str(e)}")
        return False

def test_legal_question():
    """测试法律问题"""
    print("\n🧪 测试法律问题...")
    
    try:
        response = Application.call(
            api_key=config.DASHSCOPE_API_KEY,
            app_id=config.APP_ID,
            prompt="请简单介绍一下合同法的基本原则"
        )
        
        if response.status_code == HTTPStatus.OK:
            print("✅ 法律问题测试成功！")
            print(f"回复内容: {response.output.text}")
            return True
        else:
            print("❌ 法律问题测试失败")
            print(f"错误信息: {response.message}")
            return False
            
    except Exception as e:
        print(f"❌ 法律问题测试出现错误: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 阿里云百炼智能体测试")
    print("=" * 60)
    
    # 测试基本调用
    basic_ok = test_agent()
    
    # 测试法律问题
    legal_ok = test_legal_question()
    
    print(f"\n=== 测试结果 ===")
    print(f"基本调用: {'✓' if basic_ok else '✗'}")
    print(f"法律问题: {'✓' if legal_ok else '✗'}")
    
    if basic_ok and legal_ok:
        print("\n🎉 所有测试通过！百炼智能体工作正常。")
    else:
        print("\n❌ 部分测试失败，请检查配置。")
