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

    with XMateErProRobot(ip) as robot:
        # 连接机器人

        robot.connectToRobot(ec)
        # 设置机器人上下电状态-上电
        robot.setPowerState(True, ec)
        # 查询机器人状态
        power = robot.powerState(ec)
        print("当前上下电状态为:", power)
        time.sleep(2)
        # 设置机器人上下电状态-下电
        robot.setPowerState(False, ec)
        power = robot.powerState(ec)
        print("当前上下电状态为:", power)

        ################################################ 2. 查询信息 #########################################################
        # 获取机器人的基本信息
        info = robot.robotInfo(ec)
        print("机器人轴数:", info["joint_num"], "机型:", info["type"], "控制器版本:", info["version"])
        # 获取SDK版本
        print("SDK版本:", robot.sdkVersion(ec))
        # 获取机器人的上下电状态
        power = robot.powerState(ec)
        print("当前上下电状态为:", power)
        # 获取机器人的操作模式
        mode = robot.operateMode(ec)
        print("当前机器人的操作模式为:", mode)
        # 获取机器人运行状态
        state = robot.operationState(ec)
        print("当前机器人的运行状态为:", state)

        ######################################## 3. 获取机器人当前位姿，轴角度，基坐标系等信息 #####################################
        # 获取关节位置
        joint_pos = robot.jointPos(ec)
        print("当前关节位置:", joint_pos)
        # 获取关节速度
        joint_vel = robot.jointVel(ec)
        print("当前关节速度:", joint_vel)
        # 获取关节力矩
        joint_torque = robot.jointTorque(ec)
        print("当前关节力矩:", joint_torque)
        # 获取法兰位姿
        posture = robot.flangePos(ec)
        print("当前法兰位姿:", posture)
        # 获取基坐标系-----原model()类
        base = robot.baseFrame(ec)
        print("当前基坐标系:", base)
        # 获取当前的工具坐标系
        toolset = robot.toolset(ec)
        print("当前的工具坐标系为:", toolset)
        # 设置新的坐标系
        # coor_new = {'end': {'rot': [0, 0, 0], 'trans': [0.0, 0.0, -0.01]}, 'load': {'cog': [0.0, 0.0, 0.0],
        #                                                                            'inertia': [0.0, 0.0, 0.0], 'mass': 0.0},
        #             'ref': {'rot': [0.0, -0.0, 0.0], 'trans': [0.0, 0.0, 0.0]}}
        # robot.setToolset(coor_new, ec)
        # 获取当前的工具坐标系
        # toolset = robot.toolset(ec)
        # print("修改后的工具坐标系为:", toolset)

        # 获取法兰位姿
        posture_ = robot.flangePos(ec)
        print("修改坐标系后的法兰位姿:", posture_)

        # zero = zeroToolset()
        # robot.setToolset(zero, ec)

        ############################################## 4. 计算正解和逆解 #####################################################
        # 计算正解->输入一个与当前机型轴数相同的List，返回一个当前位姿的list
        point = [10, 20, 30, 40, 50, 10]
        point = degree2rad(point)
        print(point)
        fk = robot.calcFK(point, ec)
        print("计算正解为:", fk)

        # 计算逆解->输入一个位姿，返回一个轴角的list
        # pos = [0.5930779237738772, -0.060094684364914094, 0.4260427869095114, 3.110893947990362, 0.04429035357891989, -2.9729572573550245]
        # ik = robot.calcIK(pos, ec)
        # # ik = rad2degree(ik)
        # print("计算逆解为:", ik)

        ############################################## 5. 查询DO和DI ########################################################
        # 查询端口1_0的DO值
        do = robot.getDO(1, 0, ec)
        print(message(ec))
        print("DO1_0当前的信号值为:", do)
        # 查询端口1_0的DI值
        di = robot.getDI(0, 0, ec)
        print("DI1_0当前的信号值为:", di)
        # 将DO1_0的值设为false
        robot.setDO(0, 0, False, ec)
        # 查询端口1_0的DO值
        do = robot.getDO(0, 0, ec)
        print("DO0_0修改后信号值为:", do)
        robot.setDO(0, 0, True, ec)

        ############################################## 6. 断开连接再重连 #####################################################
        # 机器人断开连接
        robot.disconnectFromRobot(ec)
        time.sleep(2)
        # 机器人再次连接
        robot.connectToRobot(ec)

        ############################################## 7. 打开和关闭拖动 ######################################################
        # # 机器人下电，因机器人拖动模式自动上电
        # robot.setPowerState(False, ec)
        # # 将机器人操作模式设为手动
        # robot.setOperateMode(rokae.OperateMode.manual, ec)
        # # 开启拖动
        # robot.enableDrag(rokae.DragParameter.Space.cartesianSpace.value, rokae.DragParameter.Type.freely.value, ec)
        # print("机器人状态:", robot.operationState(ec))
        # time.sleep(2)
        # # 关闭拖动
        # robot.disableDrag(ec)
        # print("机器人状态:", robot.operationState(ec))
        # print("非Drag模式下的上下电模式为：", robot.powerState(ec))
        # time.sleep(2)

        ############################################## 8. 查询工件/工具信息 ###################################################
        # 查询所有工具的信息
        # tool = robot.toolsInfo(ec)
        # print(tool)
        # for name in tool.keys():
        #     print(name, "质量:", tool[str(name)]["load"]["mass"])
        # # 查询所有工件的信息
        # wobj = robot.wobjsInfo(ec)
        # print("查询工件名信息为:")
        # for name in wobj.keys():
        #     print(name)

        ############################################### 9. 运动指令 ########################################################
        robot.setOperateMode(rokae.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        robot.moveReset(ec)
        # robot.setDefaultZone(100, ec)
        # robot.setDefaultSpeed(100, ec)
        # p0 = robot.flangePos(ec)
        # print(p0)

        # ############################################### 10. Move L 点位测试/ NB4 运动指令 ########################################################
        p1 = MoveLCommand(
            [0.6319677128120011, -8.34603520129436e-05, 0.5079049014875741, 3.1415841917280183, -0.0005208332350316503, -3.1415883987024773],
            500, 0)
        # p1.offset = [0.1, 0, 0, 0, 0, 0]

        p2 = MoveLCommand(
            [0.6319677128120011, -8.34603520129436e-05 + 0.2, 0.5079049014875741, 3.1415841917280183, -0.0005208332350316503, -3.1415883987024773],
            400, 0)
        # p2.offset = [0, 0, 0.01, 0, 0, 0]

        p3 = MoveLCommand(
            [0.6319677128120011, -8.34603520129436e-05 + 0.2, 0.5079049014875741 - 0.2, 3.1415841917280183, -0.0005208332350316503, -3.1415883987024773],
            300, 0)

        p4 = MoveLCommand(
            [0.6319677128120011, -8.34603520129436e-05 + 0.2, 0.5079049014875741, 3.1415841917280183, -0.0005208332350316503, -3.1415883987024773],
            100, 300)
        # p1.offset = [0.1, 0, 0, 0, 0, 0]

        p5 = MoveLCommand(
            [0.6319677128120011, -8.34603520129436e-05, 0.5079049014875741, 3.1415841917280183, -0.0005208332350316503, -3.1415883987024773],
            100, 300)

        while True:
            cmd = input("please input"
                        " 'm(start move)', 'p(pause)', 'c(continue)', 'q(break)', 'i(check)', 's(stop)','a(adjust)',"
                        "'r(reset)', d(drag), k(stop_drag) ")
            if cmd == 'm':
                print("start move")
                robot.executeCommand([p1, p2, p3, p4, p5], ec)
                robot.moveStart(ec)
                print(ec)
            elif cmd == 'p':
                print("suspend")
                robot.pause(ec)
            elif cmd == 'd':
                print("drag")
                robot.setOperateMode(rokae.OperateMode.manual, ec)
                robot.enableDrag(rokae.DragParameter.Space.jointSpace.value, rokae.DragParameter.Type.freely.value, ec)
            elif cmd == 'k':
                print("kill drag")
                robot.disableDrag(ec)
            elif cmd == 'c':
                print("continue move")
                robot.moveStart(ec)
            elif cmd == 'a':
                print("adjust speed percentage 0.5")
                robot.adjustSpeedOnline(0.1, ec)
            elif cmd == 'i':
                print("current pos id:", robot.getPointPos(ec))
            elif cmd == 'r':
                robot.moveReset(ec)
            elif cmd == 's':
                robot.stop(ec)
            else:
                print("stop")
                break
        robot.stop(ec)
        time.sleep(1)
        robot.setPowerState(False, ec)
        robot.disconnectFromRobot(ec)


#
if __name__ == '__main__':
    main()