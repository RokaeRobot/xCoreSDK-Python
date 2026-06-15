# -*- coding: utf-8 -*-
"""
@file: get_keypad_state_example.py
@brief: 读取末端按键状态
@copyright: Copyright (C) 2024 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
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

import threading
import time
from datetime import timedelta


def get_keypad_state_op(robot, ec):
    print_separator("get_keypad_state_op", length=110)
    state = robot.getKeypadState(ec)
    print_log("getKeypadState", ec)
    print(
        f"当前末端按键的状态, key1: {state.key1_state}, key2: {state.key2_state}, key3: {state.key3_state}, key4: {state.key4_state}, key5: {state.key5_state}, key6: {state.key6_state}, key7: {state.key7_state}"
    )

    # 设置要接收数据。其中keypads是本示例程序会用到的
    robot.startReceiveRobotState(
        timedelta(milliseconds=1), [xCoreSDK_python.RtSupportedFields.keypads]
    )

    def read_keypad():
        keypad = xCoreSDK_python.PyTypeVectorBool()
        count = 10  # 运行10次
        while count > 0:
            count -= 1
            # 每隔1毫秒读取一次末端按键状态
            robot.updateRobotState(timedelta(milliseconds=1))
            robot.getStateData(xCoreSDK_python.RtSupportedFields.keypads, keypad)
            print(f"当前末端按键的状态, {keypad.content()}")

    read_thread = threading.Thread(target=read_keypad)
    read_thread.start()
    read_thread.join()

    # 停止接收数据
    robot.stopReceiveRobotState()


if __name__ == "__main__":
    try:
        ip = "192.168.0.160"
        local_ip = "192.168.0.2"
        robot = xCoreSDK_python.xMateRobot(ip, local_ip)
        ec = {}
        get_keypad_state_op(robot, ec)

    except Exception as e:
        print(f"An error occurred: {e}")
