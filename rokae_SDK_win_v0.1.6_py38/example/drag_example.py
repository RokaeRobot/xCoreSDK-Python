from robot import *
from convert_tools import *
import time


def waitRobot(robot):
    running = True
    while running:
        time.sleep(0.1)
        ec = {}
        st = robot.operationState(ec)
        if st == rokae.OperationState.idle.value or st == rokae.OperationState.unknown.value:
            running = False


def main():
    ip = "192.168.0.160"
    ec = {}

    with XMateRobot(ip) as robot:
        robot.connectToRobot(ec)
        robot.setPowerState(False, ec)
        robot.setOperateMode(rokae.OperateMode.manual, ec)
        robot.moveReset(ec)

        while True:
            cmd = input("d: enable drag, k: disable drag, r: start record path， p: replay specific path: ")
            if cmd == 'd':
                # 打开拖动
                robot.enableDrag(rokae.DragParameter.Space.cartesianSpace.value, rokae.DragParameter.Type.freely.value, ec)
            elif cmd == 'k':
                # 关闭拖动
                robot.disableDrag(ec)
            elif cmd == 'r':
                # 开始路径录制并保存
                robot.startRecordPath(10, ec)
                path_name = input("path name is: ")
                robot.saveRecordPath(path_name, ec)
                print(message(ec))
                print("current record paths are:", robot.queryPathLists(ec))
            elif cmd == 'p':
                # 路径回放
                name = input("input path name: ")
                robot.disableDrag(ec)
                robot.setOperateMode(rokae.OperateMode.automatic, ec)
                robot.setPowerState(True, ec)
                robot.replayPath(name, 1, ec)
            else:
                break
        waitRobot(robot)
        robot.stop(ec)
        time.sleep(1)
        robot.setPowerState(False, ec)
        robot.disconnectFromRobot(ec)


if __name__ == '__main__':
    main()
