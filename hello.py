import sys
import os
import platform

print("=" * 46)
print("Hello, Python!")
print("=" * 46)
print(f"Python 版本 : {sys.version.split()[0]}")
print(f"解释器路径  : {sys.executable}")
print(f"conda 环境  : {os.environ.get('CONDA_DEFAULT_ENV', '未激活')}")
print(f"操作系统    : {platform.system()} {platform.release()}")
print("=" * 46)
print("看到这段文字，说明你的环境已经配好了。")
