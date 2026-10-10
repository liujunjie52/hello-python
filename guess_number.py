"""
猜数字游戏 —— 你的第一个真正的 Python 程序

运行方法：用 VS Code 打开这个文件，点右上角的 ▶ 播放按钮。
玩的时候在下方终端里输入数字，按回车。
"""

import random                      # 「导入」一个工具箱，里面有随机数功能

print("=" * 36)
print("        猜数字游戏")
print("=" * 36)
print("我心里想了一个 1 到 100 之间的整数。")
print()

answer = random.randint(1, 100)    # answer = 答案。电脑随机挑一个数当谜底
tries = 0                          # tries  = 次数。先记成 0

while True:                        # 「一直重复」下面这段，直到猜中才停

    guess = int(input("请输入你的猜测："))   # guess = 猜测。读入你打的数字
    tries = tries + 1                        # 每猜一次，次数就加 1

    if guess > answer:             # 如果你猜的比答案大
        print("太大了，再试试")
    elif guess < answer:           # 如果比答案小
        print("太小了，再试试")
    else:                          # 剩下的情况：正好相等，猜中了
        print()
        print(f"猜对了！答案就是 {answer}")
        print(f"你一共猜了 {tries} 次")
        break                      # 跳出循环，程序到此结束
