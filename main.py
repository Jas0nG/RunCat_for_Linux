import os
import time
import pystray
import psutil
from PIL import Image

# 图像文件路径列表
image_paths = [
    './resources/dark_cat_0.ico',
    './resources/dark_cat_1.ico',
    './resources/dark_cat_2.ico',
    './resources/dark_cat_3.ico',
    './resources/dark_cat_4.ico'
]

# 读取所有图像文件
images = [Image.open(image_path) for image_path in image_paths]

# 创建托盘图标
def setup_tray_icon():
    tray = pystray.Icon("name")

    # 定义一个变量用于索引当前显示的图像
    index = 0

    # 更新托盘图标的回调函数
    def update_icon(icon):
        nonlocal index
        icon.icon = images[index]
        icon.visible = True  # 确保图标可见
        index = (index + 1) % len(images)
        cpu_usage = psutil.cpu_percent(interval=0.05)
        interval = 1.0 - min(cpu_usage, 30.0) / 30.0
        # 每隔一段时间更新一次
        time.sleep(interval)
        update_icon(icon)

    # 设置托盘图标的更新函数
    tray.icon = images[index]
    tray.title = "Tray Icon"
    tray.run(update_icon)

# 显示状态栏图标
setup_tray_icon()
