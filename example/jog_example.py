# -*- coding: utf-8 -*-
"""
@file: jog_example.py
@brief: jog操作
@copyright: Copyright (C) 2024 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""
import sys
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


def jog_op(robot, ec):
    print_separator("jog_op", length=110)
    jog(robot, ec)
    jog_avoid_singularity(robot, ec)


def jog(robot, ec):
    robot.setMotionControlMode(xCoreSDK_python.MotionControlMode.NrtCommandMode, ec)
    print_log("setMotionControlMode", ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    print_log("setOperateMode", ec)
    # 对于有外接使能开关的情况，需要按住开关手动上电
    robot.setPowerState(True, ec)
    print_log("setPowerState", ec)
    space = xCoreSDK_python.JogOptSpace.world
    robot.startJog(space, 0.5, 100, 2, True, ec)
    print_log("startJog", ec)
    # 按回车停止
    while True:
        print("按回车停止")
        char = sys.stdin.read(1)
        if char == "\n":
            break
    robot.stop(ec)
    print_log("stop", ec)

    space = xCoreSDK_python.JogOptSpace.jointSpace
    robot.startJog(space, 0.05, 5000, 0, False, ec)
    print_log("startJog", ec)
    # 按回车停止
    while True:
        print("按回车停止")
        char = sys.stdin.read(1)
        if char == "\n":
            break
    robot.stop(ec)  # jog结束必须调用stop()停止
    print_log("stop", ec)


def jog_avoid_singularity(robot, ec):
    """奇异点规避Jog"""
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)  # 手动模式下jog
    print_log("setOerateMode", ec)
    # 对于有外接使能开关的情况，需要按住开关手动上电
    robot.setPowerState(True, ec)
    print_log("setPowerState", ec)
    print(
        "-- 开始Jog机器人-- \n奇异规避模式, 沿Y+方向运动50mm, 速率20%，等待机器人停止运动后按回车继续"
    )
    robot.startJog(
        xCoreSDK_python.JogOptSpace.singularityAvoidMode, 0.2, 50, 1, True, ec
    )
    print_log("startJog", ec)
    while True:
        print("按回车停止")
        char = sys.stdin.read(1)
        if char == "\n":
            break
    robot.stop(ec)  # jog结束必须调用stop()停止
    print_log("stop", ec)


if __name__ == "__main__":
    try:
        ip = "192.168.0.160"
        # 连接机器人
        # 不同的机器人对应不同的类型
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        jog_op(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
