"""使用python sdk的基础操作
主要包括：
连接、断连机器人
获取上电状态
设置上下电
获取操作模式
设置操作模式
获取操作状态
获取机器人信息
获取python sdk版本
获取当前位姿
获取当前笛卡尔坐标信息
获取关节位置
获取关节速度
获取当前关节力矩
查询基坐标系
设置基坐标系
查询当前工具工件组
设置工具工件组
通过 HMI 标定工具设置坐标系
清除伺服报警
计算正解
计算逆解
读取当前软限位设置
设置软限位
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


def base_op(robot, ec):
    print_separator("base_op", length=110)
    disconnect(robot, ec)
    connect(robot, ec)
    get_sdk_version(robot)
    get_powerstate(robot, ec)
    set_powerstate(robot, ec)
    get_operatemode(robot, ec)
    set_operatemode(robot, ec)
    get_robotinfo(robot, ec)
    get_operationState(robot, ec)
    get_posture(robot, ec)
    get_cart_posture(robot, ec)
    get_joint_pos(robot, ec)
    get_joint_vel(robot, ec)
    get_joint_torque(robot, ec)
    get_baseframe(robot, ec)
    set_baseframe(robot, ec)
    get_toolset(robot, ec)
    set_toolset(robot, ec)
    set_toolset_by_name(robot, ec)
    clear_servo_alarm(robot, ec)
    calcFk(robot, ec)
    calcIk(robot, ec)
    calcAllIkSolutions(robot, ec)
    get_soft_limit(robot, ec)
    set_soft_limit(robot, ec)
    restore_soft_limit(robot, ec)
    get_acceleration(robot, ec)
    set_acceleration(robot, ec)
    getRobotCfg_DHparam(robot, ec)


def disconnect(robot, ec):
    """断开连接机器人"""
    print_separator("disconnect", length=80)
    robot.disconnectFromRobot(ec)
    print_log("disconnectFromRobot", ec)


def connect(robot, ec):
    """连接机器人"""
    robot.connectToRobot(ec)


def get_sdk_version(robot):
    """获取sdk版本"""
    print_separator("get_sdk_version", length=80)
    sdk_version = robot.sdkVersion()
    print(f"sdkVersion={sdk_version}")


def get_powerstate(robot, ec):
    """获取上电状态"""
    print_separator("get_powerstate", length=80)
    power_state = robot.powerState(ec)
    print_log("powerState", ec, f"powerState={power_state}")


def set_powerstate(robot, ec):
    """设置机器人上下电状态，true：上电，false：下电"""
    print_separator("set_powerstate", length=80)
    robot.setPowerState(True, ec)
    print_log("setPowerState", ec)


def get_operatemode(robot, ec):
    """获取操作模式"""
    print_separator("get_operatemode", length=80)
    operate_mode = robot.operateMode(ec)
    print_log("operateMode", ec, f"operateMode={operate_mode}")


def set_operatemode(robot, ec):
    """设置操作模式"""
    print_separator("set_operatemode", length=80)
    robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
    print_log("setOperateMode", ec)


def get_robotinfo(robot, ec):
    """获取机器人信息"""
    print_separator("get_robotinfo", length=80)
    robot_info: xCoreSDK_python.Info = robot.robotInfo(ec)
    print_log(
        "robotInfo",
        ec,
        f"id:{robot_info.id},version:{robot_info.version},type:{robot_info.type},joint_num:{robot_info.joint_num},mac:{robot_info.mac}",
    )


def get_operationState(robot, ec):
    """获取操作状态"""
    print_separator("get_operationState", length=80)
    operation_state = robot.operationState(ec)
    print_log("operationState", ec, f"operation_state={operation_state}")


def get_posture(robot, ec):
    """获取当前位姿"""
    print_separator("get_posture", length=80)
    pos = robot.posture(xCoreSDK_python.CoordinateType.endInRef, ec)
    print_log("posture", ec, ", ".join(map(str, pos)))


def get_cart_posture(robot, ec):
    """获取当前笛卡尔坐标信息"""
    print_separator("get_cart_posture", length=80)
    cart_posture = robot.cartPosture(xCoreSDK_python.CoordinateType.endInRef, ec)
    print_log("cartPosture", ec)
    print(f"elbow,{cart_posture.elbow}")
    print(f"hasElbow,{cart_posture.hasElbow}")
    print(f"confData,f{','.join(map(str,cart_posture.confData))}")
    print(f"external size,{len(cart_posture.external)}")
    print(f"trans,{','.join(map(str,cart_posture.trans))}")
    print(f"rpy,{','.join(map(str,cart_posture.rpy))}")
    print(f"pos,{','.join(map(str,cart_posture.pos))}")


def get_joint_pos(robot, ec):
    """获取关节位置"""
    print_separator("get_joint_pos", length=80)
    joint_pos = robot.jointPos(ec)
    print_log("jointPos", ec, ",".join(map(str, joint_pos)))


def get_joint_vel(robot, ec):
    """获取关节速度"""
    print_separator("get_joint_vel", length=80)
    joint_vel = robot.jointVel(ec)
    print_log("jointVel", ec, ",".join(map(str, joint_vel)))


def get_joint_torque(robot, ec):
    """获取当前关节力矩"""
    print_separator("get_joint_torque", length=80)
    joint_torque = robot.jointTorque(ec)
    print_log("jointTorque", ec, ",".join(map(str, joint_torque)))


def get_baseframe(robot, ec):
    """查询基坐标系"""
    print_separator("get_baseframe", length=80)
    baseframe = robot.baseFrame(ec)
    print_log("baseFrame", ec, ",".join(map(str, baseframe)))


def set_baseframe(robot, ec):
    """设置基坐标系"""
    print_separator("set_baseframe", length=80)
    frame = xCoreSDK_python.Frame()
    robot.setBaseFrame(frame, ec)
    print_log("setBaseFrame", ec)


def get_toolset(robot, ec):
    """查询当前工具工件组"""
    print_separator("get_toolset", length=80)
    toolset = robot.toolset(ec)
    print_log("toolset", ec)
    print(
        f"""
          load mass: {toolset.load.mass}
          load cog: {', '.join(map(str, toolset.load.cog))}
          load inertia:{','.join(map(str,toolset.load.inertia))}
          end trans:{','.join(map(str,toolset.end.trans))}
          end rpy:{','.join(map(str,toolset.end.rpy))}
          end pos:{','.join(map(str,toolset.end.pos))}
          ref trans:{','.join(map(str,toolset.ref.trans))}
          ref rpy:{','.join(map(str,toolset.ref.rpy))}
          ref pos:{','.join(map(str,toolset.ref.pos))}
            """
    )


def set_toolset(robot, ec):
    """设置工具工件组"""
    print_separator("set_toolset", length=80)
    toolset = xCoreSDK_python.Toolset()
    # 设置toolset参数
    robot.setToolset(toolset, ec)
    print_log("setToolset", ec)


def set_toolset_by_name(robot, ec):
    """通过已加载的工程中的工具工件名设置坐标系"""
    print_separator("set_toolset_by_name", length=80)
    # 调用已设置好的工具工件名
    toolset = robot.setToolset("tool0", "wobj0", ec)
    print_log("setToolset", ec)
    print(
        f"""
          load mass: {toolset.load.mass}
          load cog: {', '.join(map(str, toolset.load.cog))}
          load inertia:{','.join(map(str,toolset.load.inertia))}
          end trans:{','.join(map(str,toolset.end.trans))}
          end rpy:{','.join(map(str,toolset.end.rpy))}
          end pos:{','.join(map(str,toolset.end.pos))}
          ref trans:{','.join(map(str,toolset.ref.trans))}
          ref rpy:{','.join(map(str,toolset.ref.rpy))}
          ref pos:{','.join(map(str,toolset.ref.pos))}
            """
    )


def clear_servo_alarm(robot, ec):
    """清除伺服报警"""
    print_separator("clear_servo_alarm", length=80)
    robot.clearServoAlarm(ec)
    print_log("clearServoAlarm", ec)


def calcFk(robot, ec):
    """计算正解，关节角度->笛卡尔坐标"""
    print_separator("calcFk", length=80)
    start_angle = [0, 0.557737, -1.5184888, 0, -1.3036738, 0]  # 单位弧度
    robot_model = robot.model()
    toolset = xCoreSDK_python.Toolset()  # 新建一个toolset
    cart_pose = robot_model.calcFk(start_angle, toolset, ec)
    print_log("calcFk", ec)
    print(f"elbow,{cart_pose.elbow}")
    print(f"hasElbow,{cart_pose.hasElbow}")
    print(f"confData,f{','.join(map(str,cart_pose.confData))}")
    print(f"external size,{len(cart_pose.external)}")
    print(f"trans,{','.join(map(str,cart_pose.trans))}")
    print(f"rpy,{','.join(map(str,cart_pose.rpy))}")
    print(f"pos,{','.join(map(str,cart_pose.pos))}")


def calcIk(robot, ec):
    """计算逆解，笛卡尔坐标 -> 关节角度"""
    print_separator("calcIk", length=80)
    cart_pos = xCoreSDK_python.CartesianPosition(
        [0.614711, 0.136, 0.416211, -1.57, 0, -1.57]
    )  # s4拖拽位姿
    robot_model = robot.model()
    toolset = xCoreSDK_python.Toolset()  # 新建toolset
    joint_pos = robot_model.calcIk(cart_pos, toolset, ec)
    print_log("calcIk", ec, ",".join(map(str, joint_pos)))


def calcAllIkSolutions(robot: xCoreSDK_python.BaseRobot, ec):
    """计算所有逆解，笛卡尔坐标 -> 关节角度"""
    print_separator("calcAllIkSolutions", length=80)
    cart_pos = xCoreSDK_python.CartesianPosition(
        [0.614711, 0.136, 0.416211, -1.57, 0, -1.57]
    )
    robot_model: xCoreSDK_python.model.Model_1_6 = robot.model()  # 协作6轴的model类
    confs = []
    joint_positions = robot_model.calcAllIkSolutions(cart_pos, confs, ec)
    print_log("calcAllIkSolutions", ec)
    for joint_pos, conf in zip(joint_positions, confs):
        print(f"joint_pos = {joint_pos}, conf = {conf}")


def get_soft_limit(robot, ec):
    """读取当前软限位设置"""
    print_separator("get_soft_limit", length=80)
    soft_limits = xCoreSDK_python.PyTypeVectorArrayDouble2()
    robot.getSoftLimit(soft_limits, ec)
    limits_content = soft_limits.content()
    print_log("soft_limit", ec, limits_content)


def set_soft_limit(robot, ec):
    """设置软限位"""
    print_separator("set_soft_limit", length=80)
    # 设置软限位需要在下电和手动模式
    robot.setPowerState(False, ec)
    print_log("setPowerState", ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    print_log("setOperateMode", ec)
    robot.setSoftLimit(False, ec)  # 关闭软限位
    print_log("setSoftLimit", ec)

    # 打开并且设置软限位值
    soft_limits = [
        [-2.0543261909900767, 2.0543261909900767],
        [-1.356194490192345, 1.356194490192345],
        [-1.96705972839036, 1.443460952792061],
        [-2.0543261909900767, 2.0543261909900767],
        [-2.0543261909900767, 2.0543261909900767],
        [-2.0543261909900767, 2.0543261909900767],
    ]
    robot.setSoftLimit(True, ec, soft_limits)
    print_log("setSoftLimit", ec)


def restore_soft_limit(robot, ec):
    """还原软限位"""
    print_separator("restore_soft_limit", length=80)
    # 设置软限位需要在下电和手动模式
    robot.setPowerState(False, ec)
    print_log("setPowerState", ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    print_log("setOperateMode", ec)
    robot.setSoftLimit(False, ec)  # 关闭软限位
    print_log("setSoftLimit", ec)

    # 打开并且设置软限位值
    sr4_default_limit = [
        [-6.283185307179586, 6.283185307179586],
        [-2.356194490192345, 2.356194490192345],
        [-2.96705972839036, 2.443460952792061],
        [-6.283185307179586, 6.283185307179586],
        [-6.283185307179586, 6.283185307179586],
        [-6.283185307179586, 6.283185307179586],
    ]  # sr4默认软限位
    soft_limits = sr4_default_limit
    robot.setSoftLimit(True, ec, soft_limits)
    print_log("setSoftLimit", ec)


def get_acceleration(robot, ec):
    """读取当前加速度设置"""
    print_separator("get_acceleration", length=80)
    acc = xCoreSDK_python.PyTypeDouble()
    jerk = xCoreSDK_python.PyTypeDouble()
    robot.getAcceleration(acc, jerk, ec)
    print_log("getAcceleration", ec)
    print(f"acc,{acc.content()}")
    print(f"jerk,{jerk.content()}")


def set_acceleration(robot, ec):
    """设置加速度"""
    print_separator("set_acceleration", length=80)
    acc = 0.5
    jerk = 0.5
    robot.adjustAcceleration(acc, jerk, ec)
    print_log("adjustAcceleration", ec)
    get_acceleration(robot, ec)


def query_controllerLog(robot: xCoreSDK_python.BaseRobot, ec):
    """查询控制器日志"""
    print_separator("query_controllerLog", length=80)
    loginfos = robot.queryControllerLog(
        10,
        {
            xCoreSDK_python.LogInfoLevel.info,
            xCoreSDK_python.LogInfoLevel.warning,
            xCoreSDK_python.LogInfoLevel.error,
        },
        ec,
    )  # 最多查询最近十条日志,也可以根据情况只查询特定级别的日志

    # loginfos = robot.queryControllerLog(
    #     10,
    #     {
    #         xCoreSDK_python.LogInfoLevel.info,
    #         xCoreSDK_python.LogInfoLevel.warning,
    #         xCoreSDK_python.LogInfoLevel.error,
    #     },
    #     ec,
    #     offset=11,
    # )  # 指定开始查询的位置，例如从第11条开始查询

    for log in loginfos:
        print(f"时间:{log.timestamp}")
        print(f"内容:{log.content}")
        print(f"修复办法:{log.repair}")
    print_log("queryControllerLog", ec, log)


def getRobotCfg_DHparam(robot: xCoreSDK_python.BaseRobot, ec):
    """获取机器人DH参数"""
    print_separator("getRobotCfg_DHparam", length=80)
    dh_param = robot.getRobotCfg_DHparam(False, ec)
    print(f"DH参数:{dh_param}")
    print_log("getRobotCfg_DHparam", ec)

def set_defaultSpeed(robot: xCoreSDK_python.BaseRobot, ec):
    """设置默认速度"""
    print_separator("set_defaultSpeed", length=80)
    speed = 10
    robot.setDefaultSpeed(speed, ec)
    print_log("setDefaultSpeed", ec)


def set_defaultZone(robot: xCoreSDK_python.BaseRobot, ec):
    """设置默认工作空间"""
    print_separator("set_defaultZone", length=80)
    zone = 2
    robot.setDefaultZone(zone, ec)
    print_log("setDefaultZone", ec)


def set_defaultConfOpt(robot: xCoreSDK_python.BaseRobot, ec):
    """设置默认配置选项"""
    print_separator("set_defaultConfOpt", length=80)
    conf_opt = False
    robot.setDefaultConfOpt(conf_opt, ec)
    print_log("setDefaultConfOpt", ec)


def set_maxCacheSize(robot: xCoreSDK_python.BaseRobot, ec):
    """设置最大缓存大小"""
    print_separator("set_maxCacheSize", length=80)
    max_cache_size = 400
    robot.setMaxCacheSize(max_cache_size, ec)
    print_log("setMaxCacheSize", ec)


def reboot_system(robot: xCoreSDK_python.BaseRobot, ec):
    """重启系统"""
    print_separator("reboot_system", length=80)
    robot.rebootSystem(ec)
    print_log("rebootSystem", ec)


def shutdown_system(robot: xCoreSDK_python.BaseRobot, ec):
    """关闭系统"""
    print_separator("shutdown_system", length=80)
    robot.shutdownSystem(ec)
    print_log("shutdownSystem", ec)


if __name__ == "__main__":
    try:
        # 连接机器人
        # 不同的机器人对应不同的类型
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        base_op(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
