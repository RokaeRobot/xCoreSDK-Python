# xCore SDK 机器人控制接口

* xCore SDK编程接口库是珞石机器人提供给客户用于二次开发的软件产品.

## 兼容性
### 机器人控制器
* xCore V2.0.1: 适配SDK v0.1.6

### 编译环境
|操作平台|解释器|平台|语言|
|----|---|----|----|
|Ubuntu 18.04/20.04/22.04|python3.8.X|x86_64|python|
|Windows 10|python3.8.X|x86_64|python|

## 获取预编译库

本仓库仅包含示例脚本，**不包含** Python 扩展模块（`.so` / `.pyd`）。

1. 克隆本仓库
2. 打开 [Release v0.1.6](https://github.com/RokaeRobot/xCoreSDK-Python/releases/tag/v0.1.6)
3. 下载对应平台包：
   - Linux：`xCoreSDK-Python-0.1.6-linux-py38.tar.gz`
   - Windows：`xCoreSDK-Python-0.1.6-win-py38.zip`
4. 在**仓库根目录**解压，使文件落入各 SDK 目录下的 `lib/` 文件夹

详见各平台目录下 `lib/README.md`。

### 使用示例

**注意**: 应将库文件所在路径添加至运行脚本可识别的路径中。将脚本中的ip修改为连接机器人所设置的ip。

```bash
# 运行 firstexample.py
$ python firstexample.py

```
