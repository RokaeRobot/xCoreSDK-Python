# -*- coding: utf-8 -*-
"""
@file: event_example.py
@brief: 事件、日志、告警相关获取方法示例
@copyright: Copyright (C) 2024 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""

import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator


def print_log_reporter(info):
    print("enter PrintLogReporter")
    ecode = info[
        xCoreSDK_python.EventInfoKey.LogReporter.Ecode]  # 回调的日志只有错误码没有具体内容
    print(f"logReporter:{ecode}")

    # 可以通过主动查询控制器日志查看最近日志的详细信息
    ec = {}
    loginfos = robot.queryControllerLog(
        10, {
            xCoreSDK_python.LogInfoLevel.info,
            xCoreSDK_python.LogInfoLevel.warning,
            xCoreSDK_python.LogInfoLevel.error
        }, ec)  # 最多查询最近十条日志，实际不需要这么多,也可以根据情况只查询特定级别的日志

    found = False
    for log in loginfos:
        if ecode == log.id:
            print(f"时间:{log.timestamp}")
            print(f"内容:{log.content}")
            print(f"修复办法:{log.repair}")
            found = True
            break

    if not found:
        print(f"not find id = {ecode}")

    # 注意：可能会出现控制器连续多次发送同一个日志的情况，可以自定义筛选方式，例如忽略同一时间段出现的相同的日志


def set_log_reporter_event(robot: xCoreSDK_python.BaseRobot, ec):
    print("enter SetLogReporterEvent")
    robot.setEventWatcher(xCoreSDK_python.Event.logReporter,
                          print_log_reporter, ec)
    print("按下 'q' 键退出循环")
    while True:
        user_input = input("输入：")
        if user_input.strip() == 'q':
            robot.setNoneEventWatcher(xCoreSDK_python.Event.logReporter,
                                      ec)  # 程序退出前需要取消事件监听
            break

def print_connect_state(state:bool):
    if state:
        print("连接")
    else:
        print("断连")

def set_disconnect_event(robot: xCoreSDK_python.BaseRobot, ec:dict):
    print("enter SetDisconnectEvent")
    robot.setConnectionHandler(print_connect_state)
    print("按下 'q' 键退出循环")
    while True:
        user_input = input("输入：")
        if user_input.strip() == "q":
            break

robot = xCoreSDK_python.xMateRobot()
if __name__ == '__main__':
    try:
        # 连接机器人
        # 不同的机器人对应不同的类型
        ip = "192.168.0.160"
        robot.connectToRobot(ip)
        ec = {}
        # set_log_reporter_event(robot, ec)
        # set_disconnect_event(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
