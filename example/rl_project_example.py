# -*- coding: utf-8 -*-
"""
@file: rl_project_example.py
@brief: RL工程操作示例
@copyright: Copyright (C) 2025 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""

import setup_path
import platform

# 根据操作系统导入相应的模块
if platform.system() == "Windows":
    from Release.windows import xCoreSDK_python
elif platform.system() == "Linux":
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator


def rl_project_op(robot: xCoreSDK_python.BaseRobot, ec):
    print_separator("rl_project_op", length=110)
    robot.setMotionControlMode(xCoreSDK_python.MotionControlMode.NrtRLTask, ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
    printHelp()

    cmd = " "
    while cmd != "q":
        cmd = input().strip()

        if cmd == "0":
            robot.setPowerState(True, ec)
            print("* 机器人上电")
            if ec["ec"]:
                print_log("setPowerState", ec)
                break
            continue
        elif cmd == "x":
            robot.setPowerState(False, ec)
            print("* 机器人下电")
            if ec["ec"]:
                print_log("setPowerState", ec)
                break
            continue
        elif cmd == "i":
            print("* 查询工程信息:")
            infos = robot.projectsInfo(ec)
            if not infos:
                print("无工程")
            else:
                for info in infos:
                    print(f"名称: {info.name} 任务: {' '.join(info.taskList)}")
            if ec["ec"]:
                print_log("projectsInfo", ec)
                break
            continue
        elif cmd == "l":
            print("* 加载工程, 请输入加载工程名称: ", end="")
            name = input().strip()
            print("请输入要运行的任务,空格分割: ", end="")
            tasks = input().strip().split()
            robot.loadProject(name, tasks, ec)
            if ec["ec"]:
                print_log("loadProject", ec)
                break
            continue
        elif cmd == "m":
            robot.ppToMain(ec)
            print("* 程序指针指向main")
            if ec["ec"]:
                print_log("ppToMain", ec)
                break
            continue
        elif cmd == "s":
            robot.runProject(ec)
            print("* 开始运行工程")
            if ec["ec"]:
                print_log("runProject", ec)
                break
            continue
        elif cmd == "p":
            robot.pauseProject(ec)
            print("* 暂停运行")
            if ec["ec"]:
                print_log("pauseProject", ec)
                break
            continue
        elif cmd == "t":
            print("* 查询工具信息")
            tools = robot.toolsInfo(ec)
            if not tools:
                print("无工具")
            else:
                for tool in tools:
                    print(f"工具: {tool.name}, 质量: {tool.load.mass}")
            if ec["ec"]:
                print_log("toolsInfo", ec)
                break
            continue
        elif cmd == "w":
            print("* 查询工件信息")
            wobjs = robot.wobjsInfo(ec)
            if not wobjs:
                print("无工件")
            else:
                for wobj in wobjs:
                    print(f"工件: {wobj.name}, 是否手持: {wobj.robotHeld}")
            if ec["ec"]:
                print_log("wobjsInfo", ec)
                break
            continue
        elif cmd == "o":
            print(
                "* 设置运行参数, 请依次输入运行速率和是否循环([0]单次/[1]循环), 空格分隔: ",
                end="",
            )
            rate, isLoop = input().strip().split()
            robot.setProjectRunningOpt(float(rate), int(isLoop), ec)
            if ec["ec"]:
                print_log("setProjectRunningOpt", ec)
                break
            continue
        elif cmd == "ip":
            print("* 导入RL工程, 请输入工程路径: ", end="")
            name = input().strip()
            # name = r"D:\test_file\sdk_import_test.zip" # 不要有中文路径
            robot.importProject(name,False, ec)
            if ec["ec"]:
                print_log("importProject", ec)
                break
            continue
        elif cmd == "rp":
            print("* 删除RL工程, 请输入工程名称: ", end="")
            name = input().strip()
            # name = "sdk_import_test"
            robot.removeProject(name, ec)
            if ec["ec"]:
                print_log("removeProject", ec)
                break
            continue
        elif cmd == "if":
            print("* 导入文件, 请输入文件路径: ", end="")
            file_path = input().strip()
            # file_path = r"D:\test_file\sdk_import_test\task0\test.mod"
            print("输入目标路径：" , end="")
            dest = input().strip()
            # dest = "project/sdk_import_test/task0"
            robot.importFile(file_path, dest,True, ec)
            if ec["ec"]:
                print_log("importFile", ec)
                break
            continue
        elif cmd == "rf":
            print("* 删除文件, 请输入文件路径: ", end="")
            path = input().strip()
            # path = "project/sdk_import_test/task0/test.mod"
            robot.removeFiles([path], ec)
            if ec["ec"]:
                print_log("removeFiles", ec)
                break
            continue
        elif cmd == "st":
            tool = xCoreSDK_python.WorkToolInfo()
            tool.name = "g_tool_0"
            tool.robotHeld = True
            tool.pos.trans = [0.0, 0.05, 0.0]  # 位置变换信息
            tool.pos.rpy = [0.0, 0.0, 0.0]  # 姿态变换信息
            tool.load.mass = 1.5
            tool.load.cog = [0, 0.02, 0]
            tool.load.inertia = [0, 0, 0]
            robot.setToolInfo(tool, ec)
            if ec["ec"]:
                print_log("setToolInfo", ec)
                break
            continue
        elif cmd == "sw":
            wobj = xCoreSDK_python.WorkToolInfo()
            wobj.name = "g_wobj_0"
            wobj.robotHeld = True
            wobj.pos.trans = [0.2, 0.2, 0.0]  # 位置变换信息
            wobj.pos.rpy = [0.0, 0.0, 0.0]  # 姿态变换信息
            wobj.load.mass = 1
            wobj.load.cog = [0, 0, 0]
            wobj.load.inertia = [0, 0, 0]
            robot.setWobjInfo(wobj, ec)
            if ec["ec"]:
                print_log("setWobjInfo", ec)
                break
            continue
        elif cmd == "h":
            printHelp()
            continue
        elif cmd == "q":
            print(" --- Quit --- ")
            continue
        else:
            print("无效输入")
            continue


# 假设print已经正确导入
def printHelp():
    print("Usage:")
    print("0: 机器人上电")
    print("x: 机器人下电")
    print("i: 查询工程信息")
    print("l: 加载工程")
    print("m: 程序指针指向main")
    print("s: 开始运行工程")
    print("p: 暂停运行")
    print("t: 查询工具信息")
    print("w: 查询工件信息")
    print("o: 设置运行参数")
    print("ip: 导入RL工程")
    print("rp: 删除RL工程")
    print("if: 导入文件")
    print("rf: 删除文件")
    print("st: 设置全局工具信息")
    print("sw: 设置全局工件信息")
    print("h: 帮助")
    print("q: 退出")


if __name__ == "__main__":
    try:
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateRobot(ip)  # 创建机器人对象
        ec = {}
        rl_project_op(robot, ec)

    except Exception as e:
        print(f"An error occurred: {e}")
