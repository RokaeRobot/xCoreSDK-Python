
'''运动相关的示例'''
import time
import math
import numpy as np
import locale

import sys
import setup_path
import platform

from Release.windows.xCoreSDK_python import JointPosition
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
    # calcFk(robot, ec)
    # calcIk(robot, ec)
    #moveJ(robot, ec)     #测试通过
    #setLoop(robot, ec)
    # moveWait(robot, ec)
    # pause_and_continue(robot, ec)
    # print_move_info(get_move_info(robot, ec))
    # query_controller_log(robot, ec)
    # checkpath(robot, ec)
    #robot.setNoneEventWatcher(xCoreSDK_python.Event.moveExecution,ec)  # 结束时需要关闭监视器


def pre_op(robot, ec):
    '''预操作'''
    print_separator("pre_op", length=80)
    # 切换到自动模式并上电
    robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
    print_log("setOperateMode", ec)
    #若程序运行时控制器已经是实时模式，需要先切换到非实时模式后再更改网络延迟阈值，否则不生效
    #robot.setRtNetworkTolerance(20, ec)
    robot.setMotionControlMode(
        xCoreSDK_python.MotionControlMode.RtCommandMode, ec)
    print_log("setMotionControlMode", ec)
    robot.setPowerState(True, ec)
    print_log("setPowerState", ec)



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



def main():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # 或 'C'
    try:
        ip = "192.168.21.10"
        robot = xCoreSDK_python.xMateRobot(ip, "192.168.21.1")    #实时模式分为主从两端，两个ip都要有，否则无法传输进行控制
        ec = {}
        move_op(robot, ec)
        print_separator("setLoop", length=80)
        rtCon = robot.getRtMotionController()
        rtCon.setFilterLimit(True, 10)
        jntPos = np.zeros(6, dtype=np.float64)
        q_drag_xm3p = np.zeros(6, dtype=np.float64)
        q_drag_xm3p[:] = [0.0, M_PI / 6, M_PI / 3, 0.0, M_PI / 2, 0.0]  # 单位弧度非角度

        def create_callback():   #回调函数,务必创建两层，否则只能返回callback函数的地址
            # 需要修改的状态变量
            time = 0.0
            def callback():
                nonlocal time  # 允许修改外部变量
                time += 0.001
                delta_angle = M_PI / 20.0 * (1 - math.cos(M_PI / 2.5 * time))
                cmd = JointPosition()   #分别对JointPosition里的两个参数jntPos和external赋值
                cmd.joints = [jntPos[0] + delta_angle, jntPos[1] + delta_angle,  # 导入JointPosition类即可使用里面的方法
                                        jntPos[2] - delta_angle,
                                        jntPos[3] + delta_angle, jntPos[4] - delta_angle,
                                        jntPos[5] + delta_angle]
                cmd.external = []
                print(time)
                if time > 60:
                    cmd.setFinished()  # 60秒后结束
                return cmd   #返回joints和external两个参数值给回调函数callback
            return callback # 返回闭包函数,保证回调函数传入的参数类型是函数而不是其它变量参数或结构体

        rtCon.MoveJ(0.1, robot.jointPos(ec), q_drag_xm3p)  # 从当前位置MoveJ运动到拖拽位姿
        # 创建回调
        callback = create_callback()   #返回值类型为函数
        result = repr(callback())
        print(result)    #打印回调函数信息
        # 设置回调函数
        rtCon.setControlLoopJoi(callback)
        # 更新起始角度为当前角度
        jntPos = robot.jointPos(ec)
        rtCon.startMove(RtControllerMode.jointPosition)
        rtCon.startLoop(False)  # False 表示非阻塞，仅单步运行.非阻塞模式下，函数只执行单次控制周期.这种方式能够插入调试代码（如 time.sleep 和打印语句）,确保控制周期被多次执行
        time.sleep(20)  # 模拟控制周期多次执行
        # 阻塞loop，开始运动
        # rtCon.startLoop(True)   #这个函数会进入一个无限循环，持续调用你的回调函数，但这个循环可能因为某些条件不满足而立即退出（比如硬件未就绪、控制模式错误等）。由于是阻塞调用，你无法观察到循环内部的执行情况
        print("控制结束")
        # 将控制模式设为空闲并下电
        #robot.setMotionControlMode(MotionControlMode.Idle, ec)
        robot.setMotionControlMode(
            xCoreSDK_python.MotionControlMode.NrtCommandMode, ec)  # 关闭实时模式并下电
        robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
        robot.setPowerState(False, ec)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()