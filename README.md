# 🐈RunCat_for_Linux
🇨🇳[ 简体中文](README.zh.md)  

A cute running cat animation on your Linux taskbar.  
The speed depends on your CPU usage.

# Demo

![Demo](/resources/demo.gif)  

**You only have to run the main.py**

# Installation

```bash
pip3 install -r requirements.txt
```

# Usage

```bash
python3 main.py
```

# Configuration

You can set cat icon color, speed in `config.json`.

```json
{
    "settings": {
        // true for dark mode, using white cat icon
        "dark_mode": true,
        /* cat speed relative to cpu usage, 
        true means the HIGHER cpu usage, 
        the FASTER cat runs*/
        "positive_correlation" : false
    }
}
```

# Acknowledgements

This project was inspired by the work done in [Runcat_for_Windows](https://github.com/Kyome22/RunCat_for_windows). Special thanks to the original authors for their innovative ideas and contributions to the open-source community.😺😺😺
