#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理器 - 安全地管理API密钥和配置
"""
import os
import sys
from pathlib import Path

class ConfigManager:
    """配置管理器类"""
    
    def __init__(self):
        self.api_key = None
        self.app_id = None
        self.config_file = None
        
    def load_config(self):
        """
        加载配置，按优先级尝试不同的配置源
        优先级：环境变量 > 配置文件 > 用户输入
        """
        # 1. 首先尝试从环境变量获取
        if self._load_from_env():
            return True
            
        # 2. 尝试从配置文件获取
        if self._load_from_file():
            return True
            
        # 3. 如果都没有，提示用户输入
        return self._load_from_user_input()
    
    def _load_from_env(self):
        """从环境变量加载配置"""
        self.api_key = os.getenv('DASHSCOPE_API_KEY')
        self.app_id = os.getenv('APP_ID')
        
        if self.api_key and self.app_id:
            print("✅ 从环境变量加载配置成功")
            return True
        return False
    
    def _load_from_file(self):
        """从配置文件加载配置"""
        # 尝试多个可能的配置文件位置
        config_files = [
            Path(__file__).parent.parent / 'api-key.txt',
            Path(__file__).parent / 'api-key.txt',
            Path.home() / '.xinzhiyinqing' / 'api-key.txt'
        ]
        
        for config_file in config_files:
            if config_file.exists():
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 解析配置文件
                    lines = content.strip().split('\n')
                    for line in lines:
                        line = line.strip()
                        if line.startswith('#') or not line:
                            continue
                        if '=' in line:
                            key, value = line.split('=', 1)
                            key = key.strip()
                            value = value.strip()
                            
                            if key == 'API_KEY':
                                self.api_key = value
                            elif key == 'APP_ID':
                                self.app_id = value
                    
                    if self.api_key and self.app_id:
                        self.config_file = str(config_file)
                        print(f"✅ 从配置文件加载成功: {config_file}")
                        return True
                        
                except Exception as e:
                    print(f"⚠️ 读取配置文件失败 {config_file}: {e}")
                    continue
        
        return False
    
    def _load_from_user_input(self):
        """从用户输入获取配置"""
        print("\n🔑 需要配置API密钥和App ID")
        print("您可以通过以下方式配置：")
        print("1. 设置环境变量")
        print("2. 创建配置文件")
        print("3. 现在输入（临时使用）")
        
        choice = input("\n请选择配置方式 (1/2/3): ").strip()
        
        if choice == '1':
            print("\n请设置以下环境变量：")
            print("DASHSCOPE_API_KEY=your_api_key")
            print("APP_ID=your_app_id")
            return False
            
        elif choice == '2':
            return self._create_config_file()
            
        elif choice == '3':
            self.api_key = input("请输入API密钥: ").strip()
            self.app_id = input("请输入App ID: ").strip()
            
            if self.api_key and self.app_id:
                print("✅ 配置成功（仅本次运行有效）")
                return True
            else:
                print("❌ 配置信息不完整")
                return False
        else:
            print("❌ 无效选择")
            return False
    
    def _create_config_file(self):
        """创建配置文件"""
        config_dir = Path(__file__).parent.parent
        config_file = config_dir / 'api-key.txt'
        
        print(f"\n将在 {config_file} 创建配置文件")
        
        api_key = input("请输入API密钥: ").strip()
        app_id = input("请输入App ID: ").strip()
        
        if not api_key or not app_id:
            print("❌ 配置信息不完整")
            return False
        
        try:
            # 确保目录存在
            config_dir.mkdir(parents=True, exist_ok=True)
            
            # 创建配置文件
            with open(config_file, 'w', encoding='utf-8') as f:
                f.write(f"# 心知引擎API配置\n")
                f.write(f"# 请妥善保管此文件，不要提交到版本控制系统\n\n")
                f.write(f"API_KEY={api_key}\n")
                f.write(f"APP_ID={app_id}\n")
            
            self.api_key = api_key
            self.app_id = app_id
            self.config_file = str(config_file)
            
            print(f"✅ 配置文件创建成功: {config_file}")
            print("⚠️ 请确保将此文件添加到 .gitignore 中")
            return True
            
        except Exception as e:
            print(f"❌ 创建配置文件失败: {e}")
            return False
    
    def get_api_key(self):
        """获取API密钥"""
        return self.api_key
    
    def get_app_id(self):
        """获取App ID"""
        return self.app_id
    
    def is_configured(self):
        """检查是否已配置"""
        return bool(self.api_key and self.app_id)
    
    def print_status(self):
        """打印配置状态"""
        if self.is_configured():
            print(f"✅ API Key: {self.api_key[:10]}...")
            print(f"✅ App ID: {self.app_id}")
            if self.config_file:
                print(f"✅ 配置文件: {self.config_file}")
        else:
            print("❌ 配置未完成")

def get_config():
    """获取配置实例"""
    config = ConfigManager()
    if not config.load_config():
        print("❌ 配置加载失败")
        sys.exit(1)
    return config

if __name__ == "__main__":
    config = ConfigManager()
    config.load_config()
    config.print_status()
