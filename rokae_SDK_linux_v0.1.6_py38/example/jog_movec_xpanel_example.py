import convert_tools
from robot import *

import time
import numpy as np


def waitRobot(robot):
    running = True
    while running:
        time.sleep(0.1)
        ec = {}
        st = robot.operationState(ec)
        if st == rokae.OperationState.idle.value or st == rokae.OperationState.unknown.value or st == rokae.OperationState.jog.value:
            running = False


def wait_move_test():
    ip = "192.168.0.160"
    ec = {}
    start_pos = [0.5630031225839083, 6.07079258706767e-06 - 0.15, 0.43240405879030314, -3.1415710820102154,
                 -1.1389796302986454e-06, -3.141550109145439]
    end_pos = [0.5630031225839083, 6.07079258706767e-06 + 0.15, 0.43240405879030314, -3.1415710820102154,
               -1.1389796302986454e-06, -3.141550109145439]

    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.adjustSpeedOnline(1, ec)

        robot.setDefaultSpeed(50, ec)
        robot.setDefaultZone(0, ec)

        p1 = MoveLCommand(start_pos)
        p2 = MoveLCommand(end_pos)
        path = [p1, p2, p1, p2, p1]
        # 当机器人运动至第三个点后，机器人将等待2s后继续运动。
        robot.wait_move(path, 2, 3, ec)

        robot.stop(ec)
        robot.setPowerState(False, ec)
        robot.disconnectFromRobot(ec)


def jog_test():
    ip = "10.0.40.50"
    ec = {}
    robot = XMateRobot(ip)
    robot.connectToRobot(ec)
    robot.setOperateMode(rokae.OperateMode.manual, ec)
    # flange = robot.flangePos(ec)
    # flange_to_base = convert_tools.np.array(
    #     convert_tools.getT_fromPose(flange[0], flange[1], flange[2], flange[3], flange[4], flange[5]))
    # welding = [0.1, 0.1, 0.1, 0.4, 0.5, 0.6]
    # tool_pose = convert_tools.np.array(
    #     convert_tools.getT_fromPose(welding[0], welding[1], welding[2], welding[3], welding[4], welding[5]))
    #
    # z_offs = convert_tools.np.array([0, 0, 1, 0])
    #
    # point_cal = flange_to_base @ tool_pose @ z_offs
    # print(point_cal)
    print("请在5s内握紧使能开关")
    time.sleep(5)
    robot.startJog(rokae.JogOpt.space.world.value, 0.5, 50, 2, True, ec)
    waitRobot(robot)
    print(robot.operationState(ec))
    robot.stop(ec)
    print(robot.operationState(ec))


def moveCtest():
    ip = "10.0.40.50"
    ec = {}
    # robot = XMateRobot(ip)
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)
        p1 = MoveLCommand([0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793], 200, 0 )
        # p2 = MoveCCommand([0.5630000000000001 + 0.1, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
        #                   [0.5630000000000001 + 0.05, 0.05, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793], 200, 100)
        # p3 = MoveCCommand([0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
        #                   [0.5630000000000001 + 0.05, -0.05, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793], 200, 100)

        p2 = MoveCCommand([0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
                          [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793], 200, 100)
        p2.target_offset = [-0.1, 0, 0, 0, 0, 0]
        p2.aux_offset = [-0.05, 0.05, 0, 0, 0, 0]

        p3 = MoveCCommand([0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
                          [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793], 200, 100)
        p3.aux_offset = [-0.05, -0.05, 0, 0, 0, 0]

        robot.executeCommand([p1], ec)
        robot.executeCommand([p2, p3], ec)
        robot.moveStart(ec)
        print(message(ec))
        waitRobot(robot)
        robot.stop(ec)


def setXpanelOut_test():
    ip = "10.0.40.50"
    ec = {}
    # with XMateErProRobot(ip) as robot:
    robot = XMateRobot(ip)
    robot.connectToRobot(ec)
    robot.setxPanelVout(0, ec)
    print(message(ec))


if __name__ == '__main__':
    moveCtest()
