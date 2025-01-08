import win32api
import win32con
import time
import keyboard
import random


def mouse_move(dx, dy):
    # 使用win32api模拟真实的鼠标移动
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)


def recoil_control():
    # 压枪参数,可根据具体游戏调整
    recoil_patterns = [
        (0, 5),  # 垂直上抬
        (2, 1),  # 稍微右偏
        (-2, 2),  # 稍微左偏
    ]

    print("压枪程序已启动,按住右键开始压枪,按 'q' 退出")

    while True:
        if keyboard.is_pressed('q'):  # 按q退出
            break

        if win32api.GetKeyState(win32con.VK_RBUTTON) < 0:  # 检测右键是否按下
            for dx, dy in recoil_patterns:
                # 添加随机偏移,模拟人工操作
                rand_x = dx + random.uniform(-0.5, 0.5)
                rand_y = dy + random.uniform(-0.3, 0.3)

                mouse_move(int(rand_x), int(rand_y))
                # 随机延迟,模拟人工操作节奏
                time.sleep(random.uniform(0.01, 0.02))

        time.sleep(0.001)  # 降低CPU占用


if __name__ == "__main__":
    # 给用户1秒准备时间
    print("程序将在1秒后启动...")
    time.sleep(1)
    recoil_control()