# -*- coding: utf-8 -*-
"""
@file: utility_example.py
@brief: 数据转换示例
@copyright: Copyright (C) 2025 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""

import numpy as np
import math
import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
    from Release.windows.xCoreSDK_python import utility
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
    from Release.linux.xCoreSDK_python import utility
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator

PI = math.pi

if __name__ == "__main__":
    # 度转弧度
    ret = utility.degToRad(90)
    print(f"ret = {ret}")
    ret = utility.degToRad([90, 180, 270])
    print(f"ret = {ret}")

    # 弧度转度
    ret = utility.radToDeg(1.5708)
    print(f"ret = {ret}")
    ret = utility.radToDeg([1.5708, 3.14159, 4.71239])
    print(f"ret = {ret}")

    # 变换矩阵转为数组
    rot_matrix = np.eye(3)  # 3x3 单位矩阵
    trans_vector = np.array([1.0, 2.0, 3.0])
    ret = utility.transMatrixToArray(rot_matrix, trans_vector)
    print(f"ret = {ret}")

    # 变换矩阵转为数组
    r = np.eye(4)
    ret = utility.transMatrixToArray_all(r)
    print(f"ret = {ret}")

    # 数组转为变换矩阵
    array = [
        1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0,
        0.0, 1.0
    ]
    ret = utility.arrayToTransMatrix(array)
    print(f"rot = {ret[0]}")
    print(f"trans = {ret[1]}")

    array = [
        1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 3.0, 0.0, 0.0,
        0.0, 1.0
    ]
    ret = utility.arrayToTransMatrix(array)
    print(f"rot = {ret[0]}")
    print(f"trans = {ret[1]}")

    # 数组转为变换矩阵
    array = [
        1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 0.0, 1.0, 3.0, 0.0, 0.0,
        0.0, 1.0
    ]
    ret = utility.arrayToTransMatrix_all(array)
    print(f"ret = {ret}")

    # 将表示位姿的数组{X, Y, Z, Rx, Ry, Rz}转换成行优先齐次变换矩阵
    xyz_abc = [0.1, 0.4, 0.5, PI, PI / 2, PI / 4]
    ret = utility.postureToTransArray(xyz_abc)
    print(f"ret = {ret}")

    # 将行优先齐次变换矩阵转换成{X, Y, Z, Rx, Ry, Rz}数组
    trans_matrix = [
        -2.220446049250313e-16, 0.7071067811865477, -0.7071067811865475, 0.1,
        0.0, -0.7071067811865477, -0.7071067811865477, 0.4,
        -1.0000000000000002, 0.0, -2.220446049250313e-16, 0.5, 0.0, 0.0, 0.0,
        1.0
    ]
    ret = utility.transArrayToPosture(trans_matrix)
    print(f"ret = {ret}")

    # 欧拉角转为旋转矩阵
    euler = [PI / 2, PI / 4, PI / 8]
    ret = utility.eulerToMatrix(euler)
    print(f"ret = {ret}")

    # 四元数转欧拉角
    quat = [0.0, 0.0, 0.0, 1.0]
    ret = utility.quaternionToEuler(quat[0], quat[1], quat[2], quat[3])
    print(f"ret = {ret}")
    
    # 欧拉角转四元数
    euler = [PI / 2, PI / 4, PI / 3]
    ret = utility.eulerToQuaternion(euler)
    print(f"ret = {ret}")

    # Toolset转换成工具和工件
    toolset = xCoreSDK_python.Toolset()
    toolset.end = xCoreSDK_python.Frame([0.1, 0.2, 0.3, 0.0, 0.0, 0.0])
    toolset.ref = xCoreSDK_python.Frame([0.0, 0.5, 0.1, 0.0, 0.0, 0.0])
    ret = utility.toolsetCalcPos(toolset)
    print(f"ref = {ret[0]}")
    print(f"end = {ret[1]}")

    # 坐标系转换：将 末端相对与外部参考坐标 转换为 法兰相对于基坐标系的坐标
    base_in_word = [0.1, 0.2, 0.3, 0.0, 0.0, 0.0]
    toolset = xCoreSDK_python.Toolset()
    toolset.end = xCoreSDK_python.Frame([0.1, 0.2, 0.3, 0.0, 0.0, 0.0])
    toolset.ref = xCoreSDK_python.Frame([0.0, 0.5, 0.1, 0.0, 0.0, 0.0])
    end_in_ref = [0.4, 0.5, 1.1, 0.0, 0.0, 0.0]
    ret = utility.EndInRefToFlanInBase(base_in_word, toolset, end_in_ref)
    print(f"ret = {ret}")

    # 坐标系转换：将 法兰相对于基坐标系坐标 转换为 末端相对于外部参考系坐标
    base_in_word = [0.1, 0.2, 0.3, 0.0, 0.0, 0.0]
    toolset = xCoreSDK_python.Toolset()
    toolset.end = xCoreSDK_python.Frame([0.1, 0.2, 0.3, 0.0, 0.0, 0.0])
    toolset.ref = xCoreSDK_python.Frame([0.0, 0.5, 0.1, 0.0, 0.0, 0.0])
    flan_in_base = [
        0.20000000000000004, 0.6000000000000001, 0.6000000000000001, 0.0, -0.0,
        0.0
    ]
    ret = utility.FlanInBaseToEndInRef(base_in_word, toolset, flan_in_base)
    print(f"ret = {ret}")
