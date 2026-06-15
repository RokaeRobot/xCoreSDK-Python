# -*- coding: utf-8 -*-
"""
@file: force_control_example.py
@brief: 力控接口示例
@copyright: Copyright (C) 2025 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""
import math
import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_log
from move_example import wait_robot

M_PI = math.pi
M_PI_2 = math.pi / 2

def fc_cartesian_control(robot,ec):
    '''笛卡尔控制力控。适用机型：xMateCR'''
    # 设置手持工具坐标系，Ry旋转90°
    toolset1 = xCoreSDK_python.Toolset()
    toolset1.end.rpy[1] = M_PI_2
    robot.setToolset(toolset1, ec)

    fc = robot.forceControl()
    # 力控初始化，使用工具坐标系
    fc.fcInit(xCoreSDK_python.FrameType.tool, ec)
    print_log("fcInit",ec)
    # 笛卡尔控制模式
    fc.setControlType(1, ec)
    print_log("setControlType",ec)
     # 设置笛卡尔刚度。本示例用的是工具坐标系，所以工具坐标系的x方向0阻抗，其余方向阻抗较大
    fc.setCartesianStiffness([0, 1000, 1000, 500, 500, 500], ec)
    print_log("setCartesianStiffness",ec)
    # 开始力控
    print( "开始笛卡尔模式力控")
    fc.fcStart(ec)
    print_log("fcStart",ec)
    
    # 设置负载, 请根据实际情况设置，确保安全
    #   load = xCoreSDK_python.Load()
    #   load.mass = 1
    #   fc.setLoad(load, ec)
    # print_log("setLoad",ec)
    
    # 设置期望力
    fc.setCartesianDesiredForce([0, 0, 1, 0, 0, 0], ec)
    print_log("setCartesianDesiredForce",ec)

    # 按回车结束力控
    press_enter_for_finish()
    fc.fcStop(ec)
    print_log("fcStop",ec)
    
def fc_joint_control(fc,ec):
    '''关节模式力控。适用机型：xMateCR'''
    
    fc.fcInit(xCoreSDK_python.FrameType.base, ec)
    print_log("fcInit",ec)
    fc.setControlType(0, ec)
    print_log("setControlType",ec)
    # 设置各轴刚度。2轴4轴小阻抗，其余轴阻抗较大
    fc.setJointStiffness([1000, 10, 1000, 5, 50, 50], ec)
    print_log("setJointStiffness",ec)

    print("开始关节模式力控")
    fc.fcStart(ec)
    print_log("fcStart",ec)
    #  设置期望力
    fc.setJointDesiredTorque([1,1,3,0,0,0], ec)
    print_log("setJointDesiredTorque",ec)

    # 按回车结束力控
    press_enter_for_finish()
    fc.fcStop(ec)
    print_log("fcStop",ec)

def fc_overlay(robot,ec):
    '''搜索运动 & 力控监控。测试机型：xMateER3'''

    # 设置手持工具坐标系，Ry旋转90°
    toolset1 = xCoreSDK_python.Toolset()
    toolset1.end.rpy[1] = M_PI_2
    robot.setToolset(toolset1, ec)
    print_log("setToolset",ec)

    fc = robot.forceControl()

    # 可选：设置力控监控参数，示例里用的参数是xMateER3机型默认阈值
    # 设置最大轴速度
    fc.setJointMaxVel([3.0, 3.0, 3.5, 3.5, 3.5, 4.0], ec)
    print_log("setJointMaxVel",ec)
    # 设置最大轴动量
    fc.setJointMaxMomentum([0.1, 0.1, 0.1, 0.055, 0.055, 0.055], ec)
    print_log("setJointMaxMomentum",ec)
    # 设置最大轴动能
    fc.setJointMaxEnergy([250, 250, 250, 150, 150, 100], ec)
    print_log("setJontMaxEnergy",ec)
    #设置笛卡尔空间最大速度
    fc.setCartesianMaxVel([1.0, 1.0, 1.0, 2.5, 2.5, 2.5], ec)
    print_log("setCartesianMaxVel",ec)
    #开始监控
    fc.fcMonitor(True, ec)
    print_log("fcMonitor",ec)

    #力控初始化
    fc.fcInit(xCoreSDK_python.FrameType.tool, ec)
    print_log("fcInit",ec)
    
    #搜索运动必须为笛卡尔阻抗控制
    fc.setControlType(1, ec)
    print_log("setControlType",ec)

    #设置绕Z轴(因为前面指定了力控坐标系为工具坐标系，所有这里是工具Z轴)的正弦搜索运动
    fc.setSineOverlay(2, 6, 1, M_PI, 1, ec)
    print_log("setSineOverlay",ec)
    #开始力控
    fc.fcStart(ec)
    print_log("fcStart",ec)
    #叠加XZ平面莉萨如搜索运动
    fc.setLissajousOverlay(1, 5, 1, 10, 5, 0, ec)
    print_log("setLissajousOverlay",ec)
    #开始搜索运动
    print("开始搜索运动")
    fc.startOverlay(ec)
    print_log("startOverlay",ec)

    #暂停和重新开始搜索运动
    # fc.pauseOverlay(ec)
    # fc.restartOverlay(ec)


    #按回车结束力控
    press_enter_for_finish()
    fc.stopOverlay(ec)
    print_log("stopOverlay",ec)

    #监控参数恢复到默认值
    fc.fcMonitor(False, ec)
    print_log("fcMonitor",ec)
    #停止力控
    fc.fcStop(ec)
    print_log("fcStop",ec)

def fc_condition(robot,ec):
    '''设置力控终止条件。测试机型：xMateER3'''
    fc = robot.forceControl()
    toolset = xCoreSDK_python.Toolset()
    toolset.ref.trans[2] = 0.1
    robot.setToolset(toolset, ec)
    print_log("setToolset",ec)

    fc.fcInit(xCoreSDK_python.FrameType.world, ec)
    print_log("fcInit",ec)
    fc.setControlType(1, ec)
    print_log("setControlType",ec)
    fc.fcStart(ec)
    print_log("fcStart",ec)
    # 设置力限制
    fc.setForceCondition([-20, 20, -15, 15, -15, 15], True, 20, ec)
    print_log("setForceCondition",ec)
    # 设置长方体区域限制, isInside=false代表在这个区域内时终止等待
    # 长方体所在的坐标系，会叠加外部工件坐标系
    supvFrame = xCoreSDK_python.Frame()
    supvFrame.trans[2] = -0.1
    fc.setPoseBoxCondition(supvFrame, [-0.6, 0.6, -0.6, 0.6, 0.2, 0.3], False, 20, ec)
    print_log("setPoseBoxCondition",ec)

    # 阻塞等待满足终止条件
    print("开始等待")
    fc.waitCondition(ec)
    print_log("waitCondition",ec)

    print("等待结束，停止力控")
    fc.fcStop(ec)
    print_log("fcStop",ec)

def calibrate_force_sensor(robot,ec):
    '''力矩传感器标定'''
    # 标定全部轴
    robot.calibrateForceSensor(True, 0, ec)
    print_log("calibrateForceSensor",ec)
    # 单轴(4轴)标定
    robot.calibrateForceSensor(False, 3, ec)
    print_log("calibrateForceSensor",ec)

def read_torque_info(fc,ec):
    '''读取末端力矩信息'''
    joint_torque = xCoreSDK_python.PyTypeVectorDouble()
    external_torque = xCoreSDK_python.PyTypeVectorDouble()
    cart_force = xCoreSDK_python.PyTypeVectorDouble() 
    cart_torque = xCoreSDK_python.PyTypeVectorDouble()

    #   读取当前力矩信息
    fc.getEndTorque(xCoreSDK_python.FrameType.flange, joint_torque, external_torque, cart_torque, cart_force, ec)
    print("末端力矩")
    print("各轴测量力 -", joint_torque.content())
    print("各轴外部力 -", external_torque.content())
    print("笛卡尔力矩 -", cart_torque.content())
    print("笛卡尔力   -", cart_force.content())

def press_enter_for_finish():
    '''按回车结束力控'''
    while True:
        user_input = input("按回车结束力控：")
        if user_input == "":
            break
        else:
            print(f"You entered: {user_input}")

def main():
    try:
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateRobot(ip) 
        ec = {}
        # 力控类
        fc = robot.forceControl()
        read_torque_info(fc,ec)
        
        # 上电
        robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        
        # 先运动到拖拽位姿, 注意选择正确的机型
        drag_cr = [0, M_PI/6, -M_PI_2, 0, -M_PI/3, 0] # cr
        drag_er = [0, M_PI/6, M_PI/3, 0, M_PI_2, 0] # er
        abs_j = xCoreSDK_python.MoveAbsJCommand(drag_cr,100)
        robot.executeCommand([abs_j], ec)
        wait_robot(robot, ec)
        
        # 运行示例程序
        calibrate_force_sensor(robot,ec)
        fc_cartesian_control(robot,ec)
        fc_joint_control(fc,ec)
        fc_condition(robot,ec)
        
        robot.setPowerState(False, ec)
        robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == '__main__':
    main()