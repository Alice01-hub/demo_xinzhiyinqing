#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
法律助手启动脚本
快速启动终端对话程序
"""

import sys
import os

def main():
    """启动法律助手对话程序"""
    try:
        # 检查配置文件
        if not os.path.exists('config.py'):
            print("❌ 错误：未找到配置文件 config.py")
            print("请确保在正确的目录下运行此脚本")
            sys.exit(1)
        
        # 导入并运行对话程序
        from chat_cli import main as chat_main
        chat_main()
        
    except ImportError as e:
        print(f"❌ 导入错误：{e}")
        print("请确保已安装所需依赖：pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ 启动失败：{e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
