#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
法律助手终端对话程序
支持多轮对话，短期记忆为5轮
"""

from dashscope import Application
import sys
import os
import time
from datetime import datetime

# 添加当前目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 先设置环境变量，再导入config
from setup_env import setup_environment
if not setup_environment():
    print("❌ 环境变量设置失败，程序退出")
    sys.exit(1)

import config

class LegalAssistant:
    def __init__(self, memory_size=5):
        self.memory_size = memory_size
        self.conversation_history = []
        self.api_key = config.DASHSCOPE_API_KEY
        self.app_id = config.APP_ID
        
    def add_to_memory(self, user_input, ai_response):
        """添加对话到记忆中"""
        self.conversation_history.append({
            'user': user_input,
            'ai': ai_response,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        })
        
        # 保持记忆大小不超过设定值
        if len(self.conversation_history) > self.memory_size:
            self.conversation_history.pop(0)
    
    def build_context_prompt(self, current_input):
        """构建包含历史对话的提示词"""
        if not self.conversation_history:
            return current_input
        
        context = "以下是我们的对话历史：\n"
        for i, conv in enumerate(self.conversation_history, 1):
            context += f"第{i}轮对话：\n"
            context += f"用户：{conv['user']}\n"
            context += f"助手：{conv['ai']}\n"
            context += f"时间：{conv['timestamp']}\n\n"
        
        context += f"现在用户说：{current_input}\n"
        context += "请基于以上对话历史，以罗老师的身份回答用户的问题。"
        
        return context
    
    def call_ai(self, user_input):
        """调用AI接口"""
        try:
            # 构建包含上下文的提示词
            prompt = self.build_context_prompt(user_input)
            
            response = Application.call(
                api_key=self.api_key,
                app_id=self.app_id,
                prompt=prompt
            )
            
            if response.status_code == 200:
                return response.output.text.strip()
            else:
                return f"抱歉，API调用失败：{response.message}"
                
        except Exception as e:
            return f"抱歉，发生了错误：{str(e)}"
    
    def print_welcome(self):
        """打印欢迎信息"""
        print("=" * 60)
        print("🏛️  欢迎使用罗老师法律助手！")
        print("=" * 60)
        print("我是罗老师，您的个人法律顾问。")
        print("有什么法律问题都可以问我，我会尽力为您解答。")
        print("输入 'quit' 或 'exit' 退出程序")
        print("输入 'clear' 清空对话历史")
        print("输入 'history' 查看对话历史")
        print("=" * 60)
        print()
    
    def print_ai_response(self, response):
        """格式化打印AI回复"""
        print("🤖 罗老师：")
        print("-" * 40)
        print(response)
        print("-" * 40)
        print()
    
    def show_history(self):
        """显示对话历史"""
        if not self.conversation_history:
            print("📝 暂无对话历史")
            return
        
        print("📝 对话历史：")
        print("=" * 50)
        for i, conv in enumerate(self.conversation_history, 1):
            print(f"第{i}轮对话 ({conv['timestamp']})：")
            print(f"👤 用户：{conv['user']}")
            print(f"🤖 罗老师：{conv['ai']}")
            print("-" * 30)
        print()
    
    def run(self):
        """运行对话程序"""
        self.print_welcome()
        
        while True:
            try:
                # 获取用户输入
                user_input = input("👤 您：").strip()
                
                # 处理特殊命令
                if user_input.lower() in ['quit', 'exit', '退出']:
                    print("👋 感谢使用罗老师法律助手，再见！")
                    break
                elif user_input.lower() in ['clear', '清空']:
                    self.conversation_history.clear()
                    print("✅ 对话历史已清空")
                    continue
                elif user_input.lower() in ['history', '历史']:
                    self.show_history()
                    continue
                elif not user_input:
                    print("请输入您的问题...")
                    continue
                
                # 显示思考中
                print("🤔 罗老师正在思考...")
                
                # 调用AI
                ai_response = self.call_ai(user_input)
                
                # 显示AI回复
                self.print_ai_response(ai_response)
                
                # 添加到记忆中
                self.add_to_memory(user_input, ai_response)
                
            except KeyboardInterrupt:
                print("\n\n👋 程序被中断，感谢使用！")
                break
            except Exception as e:
                print(f"❌ 发生错误：{str(e)}")
                print("请重试...")

def main():
    """主函数"""
    try:
        # 创建法律助手实例
        assistant = LegalAssistant(memory_size=5)
        
        # 运行对话
        assistant.run()
        
    except Exception as e:
        print(f"❌ 程序启动失败：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
