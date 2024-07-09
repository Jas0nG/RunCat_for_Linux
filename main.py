import time
import pystray
import psutil
import threading
import json
from pathlib import Path
from PIL import Image

# 从配置文件中读取设置
# Read settings from the configuration file
def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config['settings']['dark_mode'], config['settings']['positive_correlation']

# 设置前缀字符串和时间间隔列表(s)
# Set the prefix string and interval list
def get_interval_list(dark_mode, positive_correlation):
    prefix_string = 'dark' if dark_mode else 'light'
    interval_list = [0.5, 0.3, 0.2, 0.1, 0.07]
    if not positive_correlation:
        interval_list.reverse()
    return prefix_string, interval_list

# 读取所有图像文件
# Read all icon files
def load_images(prefix_string):
    image_paths = [Path(f'./resources/cat/{prefix_string}_cat_{i}.ico') for i in range(5)]
    return [Image.open(image_path) for image_path in image_paths]

# 获取 CPU 使用率并更新间隔
# Get CPU usage and update interval
def get_cpu_usage(interval_list, update_interval):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        if cpu_usage < 10.0:
            update_interval[0] = interval_list[0]
        elif 10.0 <= cpu_usage < 20.0:
            update_interval[0] = interval_list[1]
        elif 20.0 <= cpu_usage < 40.0:
            update_interval[0] = interval_list[2]
        elif 40.0 <= cpu_usage < 60.0:
            update_interval[0] = interval_list[3]
        elif 60.0 <= cpu_usage < 80.0:
            update_interval[0] = interval_list[4]

# 更新托盘图标
# Update tray icon
def update_icon(icon, images, update_interval):
    index = 0
    while True:
        icon.icon = images[index]
        index = (index + 1) % len(images)
        time.sleep(update_interval[0])

# 设置托盘图标
# Setup tray icon
def setup_tray_icon(images, update_interval):
    tray = pystray.Icon("RunCat_for_Linux")
    tray.icon = images[0]

    # 启动一个线程来更新图标
    # Start a thread to update the icon
    threading.Thread(target=update_icon, args=(tray, images, update_interval), daemon=True).start()

    # 运行托盘图标
    # Run the tray icon
    tray.run()

def main():
    dark_mode, positive_correlation = load_config()
    prefix_string, interval_list = get_interval_list(dark_mode, positive_correlation)
    images = load_images(prefix_string)

    # 共享变量
    # Shared variables
    update_interval = [1.0]

    # 启动一个线程来获取 CPU 使用率
    # Start a thread to get CPU usage
    cpu_thread = threading.Thread(target=get_cpu_usage, args=(interval_list, update_interval), daemon=True)
    cpu_thread.start()

    # 显示状态栏图标
    # Show the status bar icon
    setup_tray_icon(images, update_interval)

if __name__ == "__main__":
    main()
