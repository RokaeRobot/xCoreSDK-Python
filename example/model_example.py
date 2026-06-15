# -*- coding: utf-8 -*-
"""
@file: model_example.py
@brief: model类相关接口示例，模型库接口示例
@copyright: Copyright (C) 2025 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""
import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
    from Release.windows.xCoreSDK_python import model
    from Release.windows.xCoreSDK_python import utility
    from Release.windows.xCoreSDK_python.model import SegmentFrame, TorqueType
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
    from Release.linux.xCoreSDK_python import model
    from Release.linux.xCoreSDK_python import utility
    from Release.linux.xCoreSDK_python.model import SegmentFrame, TorqueType
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator

# Model = model.Model_1_6 # 协作6轴
# XMateModel = model.xmateModel_1_6 # 协作6轴
XMateModel = model.xmateModel_1_7 # 协作7轴

def model_op(xmate_model:XMateModel):
    setLoad(xmate_model)
    setTcpCoor(xmate_model)
    getCartPose(xmate_model)
    getCartVel(xmate_model)
    getCartAcc(xmate_model)
    getJntPos(xmate_model)
    getJntVel(xmate_model)
    getJointAcc(xmate_model)
    jacobian(xmate_model)
    getTorqueNoFriction(xmate_model)

# 设置负载参数，只在计算时使用，并不将参数传给机器人控制器，设置后动力学计算结果相应改变
def setLoad(xmate_model:XMateModel):
    xmate_model.setLoad(100, [0.1,0.1,0.1],[ 0, 0, 0])

# 设置TCP工具，只在计算时使用，并不将参数传给机器人控制器，设置TCP后，正逆解结果和输入参数相应改变
def setTcpCoor(xmate_model:XMateModel):
    F_TO_EE = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    EE_TO_K = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    xmate_model.setTcpCoor(F_TO_EE, EE_TO_K)

# 获取笛卡尔空间位置
def getCartPose(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    pose = xmate_model.getCartPose(jointPos_in)
    print("getCartPose: ", pose)

# 获取笛卡尔空间速度
def getCartVel(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    jointVel_in = [0.3, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1]
    vel = xmate_model.getCartVel(jointPos_in, jointVel_in)
    print("getCartVel: ", vel)
    
# 获取笛卡尔空间加速度
def getCartAcc(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    jointVel_in = [0.3, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1]
    jointAcc_in = [1.3, 3.1, 4.1, 1.5, 1.6, 4.1, 8.1]
    acc = xmate_model.getCartAcc(jointPos_in, jointVel_in, jointAcc_in)
    print("getCartAcc: ", acc)
    
# 逆解获得关节空间位置。一个位姿可能对应多个关节角度，jntPos的选取原则是选取一个与jntInit最近的解。
def getJntPos(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    pos = xmate_model.getCartPose(jointPos_in)
    psi = utility.degToRad(-7.543)
    jointInit = utility.degToRad([6, 45, -9, 92, 0, -103, 10])
    array = []
    ret = xmate_model.getJointPos(pos, psi, jointInit, array)
    print("getJntPos: ", ret, array)
    
# 逆解获得关节空间速度
def getJntVel(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    jointVel_in = [0.3, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1]
    cartVel_out = xmate_model.getCartVel(jointPos_in, jointVel_in)
    ret = xmate_model.getJointVel(cartVel_out, jointPos_in)
    print("getJntVel: ", ret)
    
# 逆解获得关节空间加速度
def getJointAcc(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    jointVel_in = [0.3, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1]
    jointAcc_in = [1.3, 3.1, 4.1, 1.5, 1.6, 4.1, 8.1]
    cartAcc_out = xmate_model.getCartAcc(jointPos_in, jointVel_in, jointAcc_in)
    ret = xmate_model.getJointAcc(cartAcc_out, jointPos_in, jointVel_in)
    print("getJntAcc: ", ret)
    
# 获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
def jacobian(xmate_model:XMateModel):
    zeros = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ret = xmate_model.jacobian(zeros)
    print("jacobian: ", ret)
    
    F_TO_EE = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    EE_TO_K = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    ret = xmate_model.jacobian(zeros, F_TO_EE, EE_TO_K, SegmentFrame.endEffector)
    print("jacobian: ", ret)
    
# 由模型计算无摩擦力的关节力矩, 计算结果单位: Nm。如有负载，先通过setLoad()设置负载参数。
def getTorqueNoFriction(xmate_model:XMateModel):
    jointPos_in = utility.degToRad([5, 46, -10, 91, 1, -105, 11])
    jointVel_in = [0.3, 0.2, 0.5, 0.4, 0.1, 0.1, 0.1]
    jointAcc_in = [1.3, 3.1, 4.1, 1.5, 1.6, 4.1, 8.1]
    trq_full = []
    trq_inertia = []
    trq_coriolis = []
    trq_gravity = []
    xmate_model.getTorqueNoFriction(jointPos_in, jointVel_in, jointAcc_in, trq_full, trq_inertia, trq_coriolis, trq_gravity)
    print("getTorqueNoFriction: ", trq_full, trq_inertia, trq_coriolis, trq_gravity)
    
if __name__ == "__main__":
    try:
        # 连接机器人
        # 不同的机器人对应不同的类型
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateErProRobot(ip)
        ec = {}
        xmate_model:XMateModel = robot.model()
        model_op(xmate_model)
    except Exception as e:
        print(f"An error occurred: {e}")