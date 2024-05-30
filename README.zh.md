# 🐈RunCat_for_Linux

可爱的猫猫在你的 Linux 任务栏上奔跑，用于显示 CPU 负载情况。

# 示例

![Demo](/resources/demo.gif)  

**只需要简单运行 main.py 就可以达到这个效果**

# 安装

```bash
pip3 install -r requirements.txt
```

# 使用

```bash
python3 main.py
```

# 配置

你可以通过配置 `config.json` 来调整猫猫的显示模式与速度模式。

```json
{
    "settings": {
        // 暗黑模式下将显示白色的猫猫
        "dark_mode": true,
        /* 猫猫奔跑速度与 CPU 负载是否正相关
        （CPU 负载越大，猫猫速度越快）*/
        "positive_correlation" : false
    }
}
```

# Acknowledgements

该项目受到 [Runcat_for_Windows](https://github.com/Kyome22/RunCat_for_windows) 项目的启发。非常感谢原项目的作者和贡献者们对开源社区的贡献！😺😺😺
