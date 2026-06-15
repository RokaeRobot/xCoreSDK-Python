# -*- coding: utf-8 -*-
"""
@file: follow_joint_position.py
@brief: 点位跟随功能
@copyright: Copyright (C) 2024 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""

import setup_path
import platform
import math
import threading
import sys
import time
from datetime import timedelta

# 根据操作系统导入相应的模块
if platform.system() == "Windows":
    from Release.windows import xCoreSDK_python
    from Release.windows.xCoreSDK_python import model, planner
    from Release.windows.xCoreSDK_python import utility
    from Release.windows.xCoreSDK_python.model import SegmentFrame, TorqueType
elif platform.system() == "Linux":
    from Release.linux import xCoreSDK_python
    from Release.linux.xCoreSDK_python import model, planner
    from Release.linux.xCoreSDK_python import utility
    from Release.linux.xCoreSDK_python.model import SegmentFrame, TorqueType
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator

M_PI = math.pi
RTMotionController = xCoreSDK_python.motioncontrolRT.PyRTmotioncontrol6
XMateModel = model.xmateModel_1_6  # 协作6轴,模型库的model类
FollowPostion = planner.FollowPosition_6  # 协作6轴，点位跟随类
# XMateModel = model.xmateModel_1_7  # 协作7轴,模型库的model类
# FollowPostion = planner.FollowPosition_7  # 协作7轴，点位跟随类

q_drag_cr7 = [0, M_PI / 6, -M_PI / 2, 0, -M_PI / 3, 0]  # CR拖拽位姿
points_xMateCR7 = [
    [0.0, 0.52359877559829882, -1.5707963267948966, 0.0, -1.0471975511965976, 0.0],
    [0.035487243764309395,0.51814607597827012,-1.5806637828906964,2.2607167760800269e-06,-1.0427832278773319,0.035483868678714996,],
    [0.035487413139973299,0.49909067450196087,-1.5511913155197452,9.3407434715976597e-07,-1.0913084154146433,0.035484721003813273,],
    [0.071110628309228666,0.49472131619011839,-1.5588670555401505,2.9525157013044446e-06,-1.088002334582413,0.071110798879156752,],
    [0.07111079887915675,0.47725271541391456,-1.5271895838122274,1.6430438164069251e-06,-1.1371457593165677,0.071105740122233752,],
    [0.035487819996022588,0.48173318109035573,-1.5195061702471038,-7.7889329104740884e-08,-1.1403483431212154,0.035485819230280602,],
    [-3.914398970759767e-07,0.49302452409585185,-1.5204379705599096,-1.4197211698704796e-06,-1.1281255631689342,1.198405110455232e-07,],
    [-0.011784714972041753,0.50683103334891477, -1.5375423532367758,-1.2986068389168909e-06,-1.0972162124211495,-0.011783476036831626,],
    [-7.7890503523341657e-07,0.51711158261127554,-1.5612157759668301,2.5489758866954378e-07,-1.0632642491857673,-9.773599037238323e-07,],
]
points_xMateCR7_array = [
    [-1.0, -1.2246467991473527e-16, 3.8857805861880484e-16, 0.556769145362398, -1.2246467991473532e-16, 1.0, -1.2246467991473527e-16, -0.15000000000000005, -3.8857805861880484e-16, -1.2246467991473532e-16, -1.0, 0.41335244785437497, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999973737, -2.2360948079042907e-06, -5.021686623566647e-07, 0.5586271073753248, -2.2360957802151904e-06, 0.9999999999956254, 1.936231554086809e-06, -0.13026178992316625, 5.021643327571429e-07, 1.9362326769789513e-06, -0.9999999999979992, 0.4133071250450868, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999949849, -2.2612263482989e-06, 2.2173344919751e-06, 0.5589044764432676, -2.2612243350023805e-06, 0.9999999999970313, 9.07982604018757e-07, -0.13025199169344276, -2.2173365451227053e-06, 9.079775901234916e-07, -0.9999999999971294, 0.4331525264616479, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999972693, 1.5412869969520132e-06, 1.7565566120187959e-06, 0.5607619392865555, 1.5412918218467185e-06, 0.9999999999950397, 2.746793418863331e-06, -0.11043623764495855, -1.756552378413103e-06, 2.746796126222171e-06, -0.9999999999946845, 0.4331177220398218, 0.0, 0.0, 0.0, 1.0],
    [-0.999999999980435, -4.368379975668135e-06, 4.477500461444657e-06, 0.5610188730463997, -4.368371854977351e-06, 0.999999999988814, 1.8136742717162988e-06, -0.1104179848345723, -4.477508384212942e-06, 1.813654712293817e-06, -0.9999999999883316, 0.452981728740564, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999856397, -2.0332673278020223e-06, 4.958520167455138e-06, 0.5591596556776541, -2.0332668061301747e-06, 0.9999999999979273, 1.052122033538044e-07, -0.13024282093457995, -4.958520381369397e-06, 1.0520212135782949e-07, -0.9999999999877012, 0.4530162561559928, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999894347, -9.685739370751905e-08, 4.5957649851832976e-06, 0.5572144929327519, -9.686328951084552e-08, 0.9999999999991724, -1.2828772581404572e-06, -0.15000038104102736, -4.595764860923347e-06, -1.2828777032878175e-06, -0.9999999999886164, 0.446437780731501, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999951676, 6.466762926683569e-07, 3.0407521000433567e-06, 0.556423836885425, 6.466726693105917e-07, 0.999999999999081, -1.1916000307144647e-06, -0.1565681632439256, -3.0407528706200524e-06, -1.1915980643374295e-06, -0.9999999999946669, 0.4332147453625901, 0.0, 0.0, 0.0, 1.0],
    [-0.9999999999994507, -7.456929202462628e-08, 1.0458261075987368e-06, 0.5568629758301338, -7.45690590500887e-08, 0.9999999999999724, 2.227660744248311e-07, -0.15000040545202156, -1.0458261242102163e-06, 2.2276599643843988e-07, -0.9999999999994287, 0.41996528267601696, 0.0, 0.0, 0.0, 1.0],
]
running = True


def updater_thread(follow_pose: FollowPostion, points_list: list):
    global running
    time.sleep(2)

    follow_pose.setScale(2)
    it_idx = 0

    try:
        while running:
            # 向前遍历 (Forward)
            while running:
                follow_pose.update(points_list[it_idx])
                it_idx += 1
                time.sleep(0.6)  # 600ms

                if it_idx == len(points_list):
                    it_idx -= 1
                    break

            # 向后遍历 (Backward)
            while running:
                follow_pose.update(points_list[it_idx])
                it_idx -= 1
                time.sleep(0.6)  # 600ms

                if it_idx < 0:
                    it_idx = 0  # 重置到起点准备下一轮循环
                    break
    except IndexError:
        pass


def console_input_thread():
    global running
    print("Press 'q' and hit Enter to stop...")
    while True:
        user_input = sys.stdin.read(1)
        if user_input == "q":
            running = False
            break


def example_followPosition_CR(robot: xCoreSDK_python.xMateRobot, ec: dict):
    """
    CR7跟随示例
    """
    global running
    rtCon: RTMotionController = robot.getRtMotionController()
    try:
        rtCon.MoveJ(0.3, robot.jointPos(ec), q_drag_cr7)
        time.sleep(1)

        model: XMateModel = robot.model()

        follow_pose: FollowPostion = FollowPostion(robot, model)
        print("start follow")
        # 目标点， 如果使用tcp位姿作为参数，需要使用16位行优先矩阵
        bMe_desire = [-1.0, 0.0, 0.0,  0.464, 0.0, 1.0, 0.0, 0.136, 0.0, 0.0, -1.0, 0.364, 0.0, 0.0, 0.0, 1.0,]
        follow_pose.start(bMe_desire)

        # 目标点，使用轴角度
        # jnt_desire = [0.6040245700346581, 0.42571977624355756, -1.922172672770141, -6.353182535575415e-08, -0.7936999130773172, 0.6040245308286039]
        # follow_pose.start(jnt_desire)

        # 更新轴角度
        # updater = threading.Thread(
        #     target=updater_thread, args=(follow_pose, points_xMateCR7)
        # )

        # 更新位置
        updater = threading.Thread(
            target=updater_thread, args=(follow_pose, points_xMateCR7_array)
        )

        updater.start()
        input_t = threading.Thread(target=console_input_thread, daemon=True)
        input_t.start()
        while running:
            time.sleep(0.1)
        follow_pose.stop()
        updater.join()
    except Exception as e:
        print(f"An error occurred: {e}")
        follow_pose.stop()
        running = False
        if updater is not None and updater.is_alive():
            updater.join()


if __name__ == "__main__":
    try:
        # 连接机器人
        # 不同的机器人对应不同的类型
        remote_ip = "192.168.0.160"
        local_ip = "192.168.0.2"
        robot: xCoreSDK_python.xMateRobot = xCoreSDK_python.xMateRobot(
            remote_ip, local_ip
        )
        ec = {}
        robot.setRtNetworkTolerance(20, ec)
        robot.setMotionControlMode(xCoreSDK_python.MotionControlMode.RtCommandMode, ec)
        robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
        robot.setPowerState(True, ec)
        rtCon = robot.getRtMotionController()
        robot.startReceiveRobotState(
            timedelta(milliseconds=1), [xCoreSDK_python.RtSupportedFields.jointPos_m]
        )
        example_followPosition_CR(robot, ec)
    except Exception as e:
        print(f"An error occurred in main: {e}")
