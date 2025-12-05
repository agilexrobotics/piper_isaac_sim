# Piper_isaac_sim

测试系统配置：
- Ubuntu 20.04 / 22.04 / 24.04
- Python 3.10
- NVIDIA RTX 系列显卡（Driver 535+）

**NOTE: 当前模型没有颜色**

## 1、配置系统环境

### 1）安装显卡驱动

[下载链接](https://www.nvidia.com/Download/index.aspx)

请确保已安装适合您显卡的 NVIDIA 驱动程序（建议版本 535 或更高）。

### 2）配置 Python 环境

建议使用 Python 虚拟环境（Anaconda/Miniconda 或 Pyenv），并推荐 **Python 3.10**。

```bash
# 使用 Conda 创建环境示例
conda create -n isaac_sim python=3.10
conda activate isaac_sim
```

### 3）安装 Isaac Sim（Pip 方式）

由于 Omniverse Launcher 的安装方式已逐渐被弃用，建议使用 Python 环境直接通过 `pip` 安装 Isaac Sim 相关组件。

对于 Ubuntu 24.04 用户，建议显式安装以下组件以确保兼容性。

```bash
# 更新 pip
pip install --upgrade pip

# 安装 Isaac Sim 核心组件
# 注意：下载文件较大，请确保网络连接畅通
pip install isaacsim-robot isaacsim-gui isaacsim-utils isaacsim-sensor \
  --extra-index-url https://pypi.nvidia.com
```

### 4）下载代码并安装依赖

下载本仓库代码并安装其余依赖项：

```bash
git clone https://github.com/agilexrobotics/piper_isaac_sim.git
cd piper_isaac_sim

# 安装项目依赖
pip install -r requirements.txt
```

## 2、启动仿真

### 1）运行 Isaac Sim

本项目提供了启动脚本 `launch_sim.py`，直接运行即可启动仿真器：

```bash
python launch_sim.py
```

注意：首次运行时，Isaac Sim 需要编译着色器（RTX Shaders），可能会出现几分钟的黑屏或长时间加载，请耐心等待。

### 2）导入 USD 模型

仿真器启动并出现窗口后：

1. 在菜单栏点击 `File > Open`。
2. 找到本项目路径下的 `usd` 文件夹。
3. 选择 `piper_description.usd`（或 `piper.usd`）并打开。
4. 成功导入后，点击左侧工具栏的 `Play`（三角按钮）开始仿真。

