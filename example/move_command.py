'''运动相关的示例'''
import time
import math
import numpy as np
import locale

import sys
import setup_path
import platform

from Release.windows.xCoreSDK_python import JointPosition
from Release.windows.xCoreSDK_python import CartesianPosition
from Release.windows.xCoreSDK_python import MotionControlMode

from Release.windows.xCoreSDK_python import RtControllerMode


# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
    from Release.windows.xCoreSDK_python.EventInfoKey import MoveExecution
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
    from Release.linux.xCoreSDK_python.EventInfoKey import MoveExecution
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator
from datetime import timedelta

M_PI = math.pi

def move_op(robot, ec):
    print_separator("move_op", length=110)
    pre_op(robot, ec)
    calcFk(robot, ec)
    calcIk(robot, ec)
    param(robot, ec)     #测试通过
    #moveJ(robot, ec)     #测试通过
    # moveL(robot, ec)    #测试通过
    # moveWait(robot, ec)
    # pause_and_continue(robot, ec)
    # print_move_info(get_move_info(robot, ec))
    # query_controller_log(robot, ec)
    # checkpath(robot, ec)
    robot.setNoneEventWatcher(xCoreSDK_python.Event.moveExecution,
                              ec)  # 结束时需要关闭监视器


def pre_op(robot, ec):
    '''预操作'''
    print_separator("pre_op", length=80)
    # 切换到自动模式并上电
    robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
    print_log("setOperateMode", ec)
    #若程序运行时控制器已经是实时模式，需要先切换到非实时模式后再更改网络延迟阈值，否则不生效
    robot.setRtNetworkTolerance(20, ec)
    robot.setMotionControlMode(
        xCoreSDK_python.MotionControlMode.RtCommandMode, ec)
    print_log("setMotionControlMode", ec)
    robot.setPowerState(True, ec)
    print_log("setPowerState", ec)
    # 设置默认运动速度和转弯区
    # set_default_zone(robot, ec)
    # set_default_speed(robot, ec)
    # 可选：设置运动指令执行完成和错误信息回调
    # robot.setEventWatcher(xCoreSDK_python.Event.moveExecution, print_move_info,
    #                       ec)

def param(robot, ec):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    print_separator("param", length=80)
    rtCon = robot.getRtMotionController()
    #设置笛卡尔阻抗系数
    impedance_factor = [1200, 0, 100, 0, 0, 0]   #使用list单独定义参数，确保pybind11能正确识别
    rtCon.setCartesianImpedance(impedance_factor, ec)
    print_log("setCartesianImpedance", ec, ','.join(map(str, impedance_factor)))
    #设置X和Z方向3N的期望力
    DesiredTorque = [3, 0, 3, 0, 0, 0]
    rtCon.setCartesianImpedanceDesiredTorque(DesiredTorque, ec)
    print_log("setCartesianImpedance", ec, ','.join(map(str, DesiredTorque)))
    #设置轴空间阻抗系数，
    jointImpedance = [500, 500, 500, 50, 50, 50]
    rtCon.setJointImpedance(jointImpedance, ec)
    print_log("jointImpedance", ec, ','.join(map(str, jointImpedance)))


def calcFk(robot, ec):
    '''计算正解，关节角度->笛卡尔坐标'''
    print_separator("calcFk", length=80)
    start_angle = [0, 0.557737, -1.5184888, 0, -1.3036738, 0]  # 单位弧度
    robot_model = robot.model()
    toolset = xCoreSDK_python.Toolset()  #新建toolset
    cart_pose = robot_model.calcFk(start_angle, toolset, ec)
    print_log("calcFk", ec)
    print(f"elbow,{cart_pose.elbow}")
    print(f"hasElbow,{cart_pose.hasElbow}")
    print(f"confData,f{','.join(map(str,cart_pose.confData))}")
    print(f"external size,{len(cart_pose.external)}")
    print(f"trans,{','.join(map(str,cart_pose.trans))}")
    print(f"rpy,{','.join(map(str,cart_pose.rpy))}")
    print(f"pos,{','.join(map(str,cart_pose.pos))}")


def calcIk(robot, ec):
    '''计算逆解，笛卡尔坐标 -> 关节角度'''
    print_separator("calcIk", length=80)
    cart_pos = xCoreSDK_python.CartesianPosition(
        [0.60, 0.13, 0.41, -3.14, -0.23, -3.14])  #s4点位
    robot_model = robot.model()
    toolset = xCoreSDK_python.Toolset()  #新建toolset
    joint_pos = robot_model.calcIk(cart_pos, toolset, ec)
    print_log("calcIk", ec, ','.join(map(str, joint_pos)))


def wait_robot(robot, ec):
    '''等待运动结束 - 通过查询机械臂是否处于运动中的方式'''
    print_separator("wait_robot", length=80)
    running = True
    while (running):
        time.sleep(0.1)
        st = robot.operationState(ec)
        if (st == xCoreSDK_python.OperationState.idle
                or st == xCoreSDK_python.OperationState.unknown):
            running = False
    print("move finished")




def moveJ(robot, ec):
    '''moveJ运动'''
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    print_separator("moveJ", length=80)
    rtCon = robot.getRtMotionController()
    q_drag_xm6p = np.zeros(6, dtype=np.float64)
    q_drag_xm6p[:] = [0.0, M_PI/6, 0.0, M_PI/3, 0.0, M_PI/2]    #单位弧度非角度
    rtCon.MoveJ(0.1,  robot.jointPos(ec), q_drag_xm6p)
    robot.setMotionControlMode(
        xCoreSDK_python.MotionControlMode.NrtCommandMode, ec)    #关闭实时模式并下电
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    robot.setPowerState(False, ec)


def moveL(robot, ec):
    '''moveJ运动'''
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    print_separator("moveL", length=80)
    start = CartesianPosition()
    target = CartesianPosition()
    start.pos = [ -0.886632, -0.302095, 0.350175, 0.403645, -0.0847275, -0.638256, -0.765148, 0.312204, 0.454649, -0.708074, 0.540302, 0.989367, 0, 0, 0, 1 ]
    target.pos = [ -0.886632, -0.302095, 0.350175, 0.303645, -0.0847275, -0.638256, -0.765148, 0.0122041, 0.454649, -0.708074, 0.540302, 0.739367, 0, 0, 0, 1 ]
    rtCon = robot.getRtMotionController()
    q_drag_xm6p = np.zeros(6, dtype=np.float64)
    q_drag_xm6p[:] = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    rtCon.MoveJ(0.1, robot.jointPos(ec), q_drag_xm6p)
    rtCon.MoveL(0.1, start, target)
    print_log("moveLStart", ec)


def main():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # 或 'C'
    try:
        ip = "192.168.21.10"
        robot = xCoreSDK_python.xMateRobot(ip, "192.168.21.1")    #实时模式分为主从两端，两个ip都要有，否则无法传输进行控制
        ec = {}
        move_op(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()