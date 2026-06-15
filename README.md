# xCore SDK 机器人控制接口

* xCore SDK编程接口库是珞石机器人提供给客户用于二次开发的软件产品.

## 兼容性

### 机器人控制器

* xCore v3.2.1 及以上版本

### 运行环境

| 操作平台 | Python 解释器 | 平台 |
|----------|---------------|------|
| Ubuntu 18.04/20.04/22.04 | 3.8 - 3.12 | x86_64 / aarch64 |
| Windows 10/11 | 3.8 - 3.12 | x86_64 |

## 获取预编译库

本仓库包含示例脚本与类型存根（`.pyi`），**不包含** Python 扩展模块（`.pyd` / `.so`）及依赖的 `xCoreSDK.dll`。这些文件通过 [GitHub Releases](https://github.com/RokaeRobot/xCoreSDK-Python/releases) 按版本分发。

### 获取步骤

1. **克隆本仓库**
   ```bash
   git clone https://github.com/RokaeRobot/xCoreSDK-Python.git
   cd xCoreSDK-Python
   ```
2. **确认 SDK 版本** — 须与 Release 版本一致（当前为 **v0.7.1**，见 [CHANGELOG.md](CHANGELOG.md)）。
3. **打开对应 Release 页面** — [Release v0.7.1](https://github.com/RokaeRobot/xCoreSDK-Python/releases/tag/v0.7.1)  
   链接格式：`https://github.com/RokaeRobot/xCoreSDK-Python/releases/tag/v{VERSION}`
4. **下载与本机平台、Python 版本匹配的库包**（见下表）。
5. **在仓库根目录解压**，使文件落入 `Release/` 目录（解压后应出现 `Release/windows/` 或 `Release/linux/` 等）。

> 示例代码通过 `example/setup_path.py` 自动将 `Release/` 加入模块搜索路径；库文件缺失时 `import xCoreSDK_python` 会失败。

### Release 包对照

| 包名 | 适用场景 |
|------|----------|
| `xCoreSDK-Python-{version}-win.zip` | Windows x86_64（含各 Python 版本的 `.pyd` 及 `xCoreSDK.dll`） |
| `xCoreSDK-Python-{version}-linux-x86_64.tar.gz` | Linux x86_64（含各 Python 版本的 `.so`） |
| `xCoreSDK-Python-{version}-linux-aarch64.tar.gz` | Linux aarch64 / ARM（含各 Python 版本的 `.so`） |

Windows / Linux 包内均包含与扩展模块配套的 `xCoreSDK_python/` 类型存根（`.pyi`），供 IDE 补全使用。

### 解压后目录结构

```
Release/
  windows/
    xCoreSDK.dll
    xCoreSDK_python.cp3xx-win_amd64.pyd    # 按本机 Python 版本选择对应文件
    xCoreSDK_python/                       # .pyi 类型存根
  linux/
    xCoreSDK_python.cpython-3xx-x86_64-linux-gnu.so
    xCoreSDK_python/                       # .pyi 类型存根
    arm/                                   # aarch64 平台库（单独包解压时合并到此）
      xCoreSDK_python.cpython-3xx-aarch64-linux-gnu.so
      xCoreSDK_python/
```

### 示例（Windows）

```powershell
# 在仓库根目录解压
Expand-Archive -Path xCoreSDK-Python-0.7.1-win.zip -DestinationPath .
# 确认存在 Release\windows\xCoreSDK_python.cp312-win_amd64.pyd（版本号按本机 Python 调整）
cd example
python base_example.py
```

### 示例（Linux）

```bash
# 在仓库根目录解压 x86_64 包
tar -xzf xCoreSDK-Python-0.7.1-linux-x86_64.tar.gz
# aarch64 需额外解压 arm 包到 Release/linux/
cd example
python3 base_example.py
```

## 使用示例

**注意**：运行前请确保已按上文下载并解压库文件；将脚本中的 IP 修改为机器人实际 IP。

示例代码见 `example/` 目录。各示例开头通过 `import setup_path` 加载 `Release/` 路径。

```bash
cd example
python base_example.py
```

## License

> Copyright (C) 2026 ROKAE (Beijing) Technology Co., LTD.
