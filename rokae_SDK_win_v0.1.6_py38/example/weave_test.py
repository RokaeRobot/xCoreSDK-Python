import time
import threading
from robot import *

ip = "10.0.40.50"

p_weave_line1_start = MoveLCommand(
    [0.5630000000000001, 0.0 - 0.2, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    200, 0)

p_weave_line1_end = MoveLCommand(
    [0.5630000000000001, 0.0 + 0.2, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    200, 0)

p_cyc_start = MoveLCommand(
    [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    200, 0)

p_cyc1 = MoveCCommand(
    [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    200, 0)
p_cyc1.target_offset = [-0.1, 0, 0, 0, 0, 0]
p_cyc1.aux_offset = [-0.05, 0.05, 0, 0, 0, 0]

p_cyc2 = MoveCCommand(
    [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    [0.5630000000000001, 0.0, 0.4324140090910689, 3.141592653589793, 2.83276944882399e-16, 3.141592653589793],
    200, 0)
p_cyc2.aux_offset = [-0.05, -0.05, 0, 0, 0, 0]

p_weave_line2_start = MoveLCommand(
    [0.5630000000000001, 0.0 - 0.2, 0.4324140090910689, 3.141592653589793 - 0.2, 2.83276944882399e-16 - 0.1,
     3.141592653589793],
    200, 0)

p_weave_line2_end = MoveLCommand(
    [0.5630000000000001, 0.0 + 0.2, 0.4324140090910689 - 0.15, 3.141592653589793 - 0.2, 2.83276944882399e-16 - 0.1,
     3.141592653589793],
    200, 0)


def waitRobot(robot):
    running = True
    while running:
        time.sleep(0.1)
        ec = {}
        st = robot.operationState(ec)
        if st == rokae.OperationState.idle.value or st == rokae.OperationState.unknown.value:
            running = False


def singleLineTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_weave_line1_end], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.stop(ec)


def multLineTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_weave_line1_end], ec)
        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.stop(ec)


def singleCycTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_cyc_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_cyc1], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.stop(ec)


def multCycTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_cyc_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_cyc1], ec)
        robot.executeCommand([p_cyc2], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.stop(ec)


def line_l_weave_line():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0.1, 0.1, 0.1, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_weave_line1_end], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.stop(ec)


def line_c_weave_line():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_cyc_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0.1, 0.1, 0.1, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_cyc1], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)

        robot.executeCommand([p_cyc_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.stop(ec)


def line_weave_params(amp=0.003, freq=2, wait_time=0):
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        print("幅值测试开始...")
        for amp_test in [0.005, 0.006, 0.007]:
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp_test, freq, wait_time, wait_time, wait_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_weave_line1_end], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("幅值测试结束...")

        print("频率测试开始...")
        for freq_test in [0.5, 1, 1.5]:
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp, freq_test, wait_time, wait_time, wait_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_weave_line1_end], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("频率测试结束...")

        print("停留时间测试开始...")
        for dwell_time in [0.2, 0.5, 1]:
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp, freq_test, dwell_time, dwell_time, dwell_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_weave_line1_end], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_weave_line1_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("停留时间测试结束...")


def cyc_weave_params(amp=0.003, freq=2, wait_time=0):
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        print("幅值测试开始...")
        for amp_test in [0.004, 0.005, 0.006]:
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp_test, freq, wait_time, wait_time, wait_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_cyc1], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("幅值测试结束...")

        print("频率测试开始...")
        for freq_test in [0.5, 1, 1.5]:
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp, freq_test, wait_time, wait_time, wait_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_cyc1], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("频率测试结束...")

        print("停留时间测试开始...")
        for dwell_time in [0.2, 0.5, 1]:
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.setWeaveParameters(amp, freq_test, dwell_time, dwell_time, dwell_time, ec)
            robot.weaveOn(ec)
            robot.executeCommand([p_cyc1], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.weaveOff(ec)
            robot.executeCommand([p_cyc_start], ec)
            robot.moveStart(ec)
            waitRobot(robot)
            robot.stop(ec)
        print("停留时间测试结束...")


def watch(robot):
    ec = {}
    while robot:
        time.sleep(0.5)
        print("current pos id: ", robot.getPointPos(ec))


def get_weaving_pos():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.moveReset(ec)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeDiffCommand([p_weave_line1_end, p_weave_line1_start], ec)
        robot.moveStart(ec)

        pose_thread = threading.Thread(target=watch(robot))
        pose_thread.setDaemon = True
        pose_thread.start()

        waitRobot(robot)
        robot.weaveOff(ec)
        robot.stop(ec)

        print("please shut down program by hand~")


def oriWeaveTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line2_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_weave_line2_end], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.weaveOff(ec)
        robot.stop(ec)


def pauseCalled(robot):
    ec = {}
    time.sleep(5)
    robot.pause(ec)


def weavePauseTest():
    ec = {}
    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)

        robot.executeCommand([p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)

        robot.moveReset(ec)

        robot.setWeaveParameters(0.003, 2, 0, 0, 0, ec)
        robot.weaveOn(ec)
        robot.executeCommand([p_weave_line1_end, p_weave_line1_start], ec)
        robot.moveStart(ec)

        pose_thread = threading.Thread(target=pauseCalled(robot))
        pose_thread.setDaemon = True
        pose_thread.start()

        waitRobot(robot)
        robot.weaveOff(ec)
        robot.stop(ec)

        time.sleep(1)

        robot.moveReset(ec)
        robot.executeCommand([p_weave_line1_end, p_weave_line1_start], ec)
        robot.moveStart(ec)
        waitRobot(robot)
        robot.stop(ec)


if __name__ == '__main__':
    print("单直线摆动测试开始...")
    singleLineTest()
    print("单直线摆动测试结束...")
    #
    # print("多直线摆动测试开始...")
    # multLineTest()
    # print("多直线摆动测试结束...")
    #
    # print("单圆弧摆动测试开始...")
    # singleCycTest()
    # print("单圆弧摆动测试结束...")
    #
    # print("多圆弧摆动测试开始...")
    # multCycTest()
    # print("多圆弧摆动测试结束...")
    #
    # print("直线-直线摆动-直线测试开始...")
    # line_l_weave_line()
    # print("直线-直线摆动-直线测试结束...")
    #
    # print("直线-圆弧摆动-直线测试开始...")
    # line_c_weave_line()
    # print("直线-圆弧摆动-直线测试结束...")
    #
    # print("直线摆动变参数测试开始...")
    # line_weave_params()
    # print("直线摆动变参数测试结束...")
    #
    # print("圆弧摆动变参数测试开始...")
    # cyc_weave_params()
    # print("圆弧摆动变参数测试结束...")

    # print("变姿态摆动测试开始...")
    # oriWeaveTest()
    # print("变姿态摆动测试结束...")

    # print("摆动暂停测试开始...")
    # weavePauseTest()
    # print("摆动暂停测试结束...")

    # print("点位反馈测试开始...")
    # get_weaving_pos()
    # print("点位反馈测试结束...")
