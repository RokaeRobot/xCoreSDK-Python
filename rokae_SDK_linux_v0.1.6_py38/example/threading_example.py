# coding=UTF-8

# import sys
# import os
# #
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath + '/lib')

from robot import *
from convert_tools import *
import time
import threading
from threading import Lock
from time import sleep
runState = False
ip = "10.0.40.50"
# 创建机器人实例
robot = XMateRobot(ip)
# lock = Lock()

# 线程：到达点判定
def pointPose():
    global runState
    ec = {}
    while True:
        if runState == True:
            # time_start = time.time()
            # time.sleep(0.5)
            # lock.acquire()
            point_pose = robot.getPointPos(ec)
            print("point_pose: ", point_pose)     
            if point_pose == -1:
                robot.adjustSpeedOnline(1/11.5,ec)
                print("speed: ", 1)                 
            elif point_pose == 0:
                robot.adjustSpeedOnline(0.5/11.5,ec)
                print("speed: ", 0.5)   
            elif point_pose == 1:
                robot.adjustSpeedOnline(1/11.5,ec)
                print("speed: ", 1)  
            elif point_pose == 2:
                runState = False
                robot.adjustSpeedOnline(0.5/11.5,ec)
                print("speed: ", 0.5)
            # time_end = time.time()
            # print("time consume is: ", time_end - time_start)
            # lock.release()

# 线程： 定时器暂停
def pause():
    ec = {}
    while True:
        if runState == True:
            sleep(2)
            # lock.acquire()
            robot.pause(ec)
            print("pause!!")
            sleep(2)
            robot.moveStart(ec)
            print("goOn!!")
            # lock.release()
    


def waitRobot(robot):
    running = True
    while running:
        time.sleep(0.1)
        ec = {}
        st = robot.operationState(ec)
        if st == rokae.OperationState.idle.value or st == rokae.OperationState.unknown.value:
            running = False



def main():
    global runState
    ec = {}

    with robot:
        # 连接机器人
        robot.connectToRobot(ec)

        pose_thread = threading.Thread(target=pointPose)
        pose_thread.setDaemon = True
        pose_thread.start()

        pause_thread = threading.Thread(target=pause)
        pause_thread.setDaemon = True
        pause_thread.start()

        # 设置机器人上下电状态-上电
        robot.setPowerState(True, ec)
        # 查询机器人状态
        power = robot.powerState(ec)
        print("当前上下电状态为:", power)
        time.sleep(2)
       
        ############################################### 9. 运动指令 ########################################################
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)
        # robot.setDefaultZone(100, ec)
        # robot.setDefaultSpeed(1000, ec)
        # p0 = robot.flangePos(ec)
        # print(p0)

        # ############################################### 10. Move L 点位测试/ NB4 运动指令 ########################################################
        p1 = MoveLCommand(
        [0.029520704007313464,
            1.164288323886427,
            0.2785416036566716,
            -3.1365962383117285,
            0.20560752310596622,
            -2.0594276971060843], 200, 50)

        p2 = MoveLCommand(
        [0.01191111536948755,
            1.1749144596534273,
            -0.010390754054596552,
            2.9947602054143125,
            0.0722267217100297,
            3.088732723146514],
        200, 50)
        # p2.offset = [0, 0, 0.01, 0, 0, 0]

        p3 = MoveLCommand(
        [-0.09903707990884443,
            1.1857338234888655,
            -0.012297766645275432,
            2.976636843038453,
            0.040892412582994545,
            3.045798168339249],
        200, 50)

        p4 = MoveLCommand(
        [-0.07970314546523967,
            1.1335848187833402,
            0.18845733744454263,
            3.109848113699997,
            0.019670544099268442,
            -3.0985615022362247],
        200, 50)


        index = 0
        while True:
            sleep(0.2)
            index = index + 1
            if runState == False and index < 10:
                robot.executeCommand([p1, p2, p3, p4], ec)
                print("start move")
                robot.moveStart(ec)
                runState = True


if __name__ == '__main__':
    main()
