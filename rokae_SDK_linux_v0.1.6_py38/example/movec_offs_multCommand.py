import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0] + '/lib'
sys.path.append(rootPath)

import time
from robot import *


def waitRobot(robot):
    running = True
    while running:
        time.sleep(0.1)
        ec = {}
        st = robot.operationState(ec)
        if st == rokae.OperationState.idle.value or st == rokae.OperationState.unknown.value:
            running = False


def executeMultCommandTEST():
    ip = "10.0.40.50"
    ec = {}
    with XMateErProRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        p0 = MoveJCommand(
            [0.5630000000000001 - 0.1, 0.0 + 0.1, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16,
             3.141592653589793], 200, 0)
        p1 = MoveLCommand(
            [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
            200, 0)
        p2 = MoveCCommand(
            [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
            [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
            200, 100)
        p2.target_offset = [-0.1, 0, 0, 0, 0, 0]
        p2.aux_offset = [-0.05, 0.05, 0, 0, 0, 0]

        p3 = MoveCCommand(
            [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
            [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
            200, 100)
        p3.aux_offset = [-0.05, -0.05, 0, 0, 0, 0]

        robot.executeDiffCommand([p0, p1, p2, p3], ec)
        robot.executeDiffCommand([p0], ec)
        robot.executeDiffCommand([p1], ec)
        robot.executeDiffCommand([p2], ec)
        robot.executeDiffCommand([p3], ec)

        robot.moveStart(ec)
        waitRobot(robot)
        robot.stop(ec)


if __name__ == '__main__':
    executeMultCommandTEST()
