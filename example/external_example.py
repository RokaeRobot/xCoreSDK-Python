# -*- coding: utf-8 -*-
"""
@file: external_example.py
@brief: 外部轴数据读写示例
@copyright: Copyright (C) 2025 ROKAE (Beijing) Technology Co., LTD. All Rights Reserved.
Information in this file is the intellectual property of Rokae Technology Co., Ltd,
And may contains trade secrets that must be stored and viewed confidentially.
"""

import setup_path
import platform

# 根据操作系统导入相应的模块
if platform.system() == "Windows":
    from Release.windows import xCoreSDK_python
elif platform.system() == "Linux":
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator


# 读取机械单元参数
def getMechUnit(robot: xCoreSDK_python.BaseRobot, ec: dict):
    # 机械单元是否激活
    is_active = xCoreSDK_python.PyTypeBool()
    robot.getMechUnit("u1", "activation", is_active, ec)
    print_log("getMechUnit", ec)
    print(f"is_active: {is_active.content()}")

    # 轴名称
    axis_names = xCoreSDK_python.PyTypeVectorString()
    robot.getMechUnit("u1", "axes_info", axis_names, ec)
    print_log("getMechUnit", ec)
    print(f"axis_names: {axis_names.content()}")

    # 机械单元是否启用
    is_enabled = xCoreSDK_python.PyTypeBool()
    robot.getMechUnit("u1", "enable", is_enabled, ec)
    print_log("getMechUnit", ec)
    print(f"is_enabled: {is_enabled.content()}")

    # 机械单元类型
    mech_type = xCoreSDK_python.PyTypeInt()
    robot.getMechUnit("u1", "mech_link_type", mech_type, ec)
    print_log("getMechUnit", ec)
    print(f"mech_type: {mech_type.content()}")
    pass


def getExtAxisInfo(robot: xCoreSDK_python.BaseRobot, ec: dict):
    name = "axis1"
    # 点位中第几个数据映射
    ext_data_number = xCoreSDK_python.PyTypeInt()
    robot.getExtAxisInfo(name, "ext_data_number", ext_data_number, ec)
    print_log("getExtAxisInfo", ec)
    print(f"ext_data_number: {ext_data_number.content()}")

    # 连接的第几个驱动器
    ext_axis_number = xCoreSDK_python.PyTypeInt()
    robot.getExtAxisInfo(name, "ext_axis_number", ext_axis_number, ec)
    print_log("getExtAxisInfo", ec)
    print(f"ext_axis_number: {ext_axis_number.content()}")
    # 是否是伺服焊枪
    is_servo_gun = xCoreSDK_python.PyTypeBool()
    robot.getExtAxisInfo(name, "is_servo_gun", is_servo_gun, ec)
    print_log("getExtAxisInfo", ec)
    print(f"is_servo_gun: {is_servo_gun.content()}")
    # 最大加速度
    max_acc = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "max_acc", max_acc, ec)
    print_log("getExtAxisInfo", ec)
    print(f"max_acc: {max_acc.content()}")

    # 最大加加速度
    max_jerk = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "max_jerk", max_jerk, ec)
    print_log("getExtAxisInfo", ec)
    print(f"max_jerk: {max_jerk.content()}")

    # 最大速度
    max_speed = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "max_speed", max_speed, ec)
    print_log("getExtAxisInfo", ec)
    print(f"max_speed: {max_speed.content()}")

    # 软限位下限
    soft_limit_lower = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "soft_limit_lower", soft_limit_lower, ec)
    print_log("getExtAxisInfo", ec)
    print(f"soft_limit_lower: {soft_limit_lower.content()}")

    # 软限位上限
    soft_limit_upper = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "soft_limit_upper", soft_limit_upper, ec)
    print_log("getExtAxisInfo", ec)
    print(f"soft_limit_upper: {soft_limit_upper.content()}")

    # 零点值
    zero_value = xCoreSDK_python.PyTypeInt()
    robot.getExtAxisInfo(name, "zero_value", zero_value, ec)
    print_log("getExtAxisInfo", ec)
    print(f"zero_value: {zero_value.content()}")

    # 电机过载系数
    motor_overload_coefficient = xCoreSDK_python.PyTypeInt()
    robot.getExtAxisInfo(
        name, "motor_overload_coefficient", motor_overload_coefficient, ec
    )
    print_log("getExtAxisInfo", ec)
    print(f"motor_overload_coefficient: {motor_overload_coefficient.content()}")

    # 电机转矩限幅
    motor_torque_limiting = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "motor_torque_limiting", motor_torque_limiting, ec)
    print_log("getExtAxisInfo", ec)
    print(f"motor_torque_limiting: {motor_torque_limiting.content()}")

    # 减速比
    reduction_ratio = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "reduction_ratio", reduction_ratio, ec)
    print_log("getExtAxisInfo", ec)
    print(f"reduction_ratio: {reduction_ratio.content()}")

    # 电机额定转矩
    rated_torque_of_motor = xCoreSDK_python.PyTypeDouble()
    robot.getExtAxisInfo(name, "rated_torque_of_motor", rated_torque_of_motor, ec)
    print_log("getExtAxisInfo", ec)
    print(f"rated_torque_of_motor: {rated_torque_of_motor.content()}")

    # 分辨率
    resolution_ratio = xCoreSDK_python.PyTypeInt()
    robot.getExtAxisInfo(name, "resolution_ratio", resolution_ratio, ec)
    print_log("getExtAxisInfo", ec)
    print(f"resolution_ratio: {resolution_ratio.content()}")

    # 关节方向
    joint_orient = xCoreSDK_python.PyTypeBool()
    robot.getExtAxisInfo(name, "joint_orient", joint_orient, ec)
    print_log("getExtAxisInfo", ec)
    print(f"joint_orient: {joint_orient.content()}")

    # 是否坐标系标定
    coordinate_calibrated = xCoreSDK_python.PyTypeBool()
    robot.getExtAxisInfo(name, "coordinate_calibrated", coordinate_calibrated, ec)
    print_log("getExtAxisInfo", ec)
    print(f"coordinate_calibrated: {coordinate_calibrated.content()}")

    # 驱动器别名/固定名
    driver_name = xCoreSDK_python.PyString()
    robot.getExtAxisInfo(name, "driver_name", driver_name, ec)
    print_log("getExtAxisInfo", ec)
    print(f"driver_name: {driver_name.content()}")


if __name__ == "__main__":
    try:
        # 连接机器人
        # 不同的机器人对应不同的类型
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        getMechUnit(robot, ec)
        getExtAxisInfo(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
