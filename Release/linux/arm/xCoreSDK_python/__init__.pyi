"""
xCoreSDK, python version based on c++ sdk
"""
from __future__ import annotations
import collections.abc
import datetime
import typing
from . import EventInfoKey
from . import RtSupportedFields
from . import model
from . import motioncontrolRT
from . import planner
from . import utility
__all__: list[str] = ['AvoidSingularityMethod', 'BaseCobot', 'BaseRobot', 'CartesianPosition', 'CartesianPositionOffset', 'CartesianPositionOffsetType', 'Cobot_5', 'Cobot_6', 'Cobot_7', 'CoordinateType', 'DragParameterSpace', 'DragParameterType', 'Event', 'EventInfoKey', 'Finishable', 'Frame', 'FrameCalibrationResult', 'FrameType', 'Idle', 'IndustrialRobot_3', 'IndustrialRobot_4', 'IndustrialRobot_6', 'Info', 'JogOptSpace', 'JointPosition', 'KeyPadState', 'Load', 'LogInfo', 'LogInfoLevel', 'MotionControlMode', 'MoveAbsJCommand', 'MoveCCommand', 'MoveCFCommand', 'MoveCFCommandRotType', 'MoveJCommand', 'MoveLCommand', 'MoveSPCommand', 'MoveWaitCommand', 'NrtCommand', 'NrtCommandMode', 'NrtRLTask', 'OperateMode', 'OperationState', 'PCB3Robot', 'PCB4Robot', 'PowerState', 'PyErrorCode', 'PyForceControl5', 'PyForceControl6', 'PyForceControl7', 'PyString', 'PyTypeBool', 'PyTypeDouble', 'PyTypeFloat', 'PyTypeInt', 'PyTypeUInt64', 'PyTypeUInt8', 'PyTypeVectorArrayDouble2', 'PyTypeVectorBool', 'PyTypeVectorDouble', 'PyTypeVectorFloat', 'PyTypeVectorInt', 'PyTypeVectorString', 'RLProjectInfo', 'Robot_T_Collaborative_5', 'Robot_T_Collaborative_6', 'Robot_T_Collaborative_7', 'Robot_T_Industrial_3', 'Robot_T_Industrial_4', 'Robot_T_Industrial_6', 'RtCommandMode', 'RtControllerMode', 'RtSupportedFields', 'StandardRobot', 'StopLevel', 'Toolset', 'Torque', 'WorkToolInfo', 'WorkType', 'automatic', 'base', 'baseFrame', 'baseParallelMode', 'cartesianImpedance', 'cartesianPosition', 'cartesianSpace', 'collaborative', 'constPose', 'createErrorCode', 'demo', 'drag', 'dynamicIdentify', 'endInRef', 'error', 'estop', 'fixedAxis', 'flange', 'flangeInBase', 'freely', 'frictionIdentify', 'gstop', 'idle', 'industrial', 'info', 'jog', 'jogging', 'jointImpedance', 'jointPosition', 'jointSpace', 'jointWay', 'loadIdentify', 'lockAxis4', 'logReporter', 'manual', 'message', 'model', 'motioncontrolRT', 'moveExecution', 'moving', 'none', 'off', 'offs', 'on', 'path', 'planner', 'rail', 'relTool', 'reserve', 'rlExecution', 'rlProgram', 'rotAxis', 'rotationOnly', 'rtControlling', 'safety', 'singularityAvoidMode', 'stop0', 'stop1', 'stop2', 'suppleStop', 'supply12v', 'supply24v', 'tool', 'toolFrame', 'torque', 'translationOnly', 'unknown', 'utility', 'warning', 'wobj', 'wobjFrame', 'world', 'wrist', 'xMateCr5Robot', 'xMateErProRobot', 'xMateRobot', 'xPanelOptVout']
class AvoidSingularityMethod:
    """
    奇异规避方式
    
    Members:
    
      lockAxis4 : 四轴锁定
    
      wrist : 牺牲姿态
    
      jointWay : 轴空间短轨迹插补
    """
    __members__: typing.ClassVar[dict[str, AvoidSingularityMethod]]  # value = {'lockAxis4': <AvoidSingularityMethod.lockAxis4: 0>, 'wrist': <AvoidSingularityMethod.wrist: 1>, 'jointWay': <AvoidSingularityMethod.jointWay: 2>}
    jointWay: typing.ClassVar[AvoidSingularityMethod]  # value = <AvoidSingularityMethod.jointWay: 2>
    lockAxis4: typing.ClassVar[AvoidSingularityMethod]  # value = <AvoidSingularityMethod.lockAxis4: 0>
    wrist: typing.ClassVar[AvoidSingularityMethod]  # value = <AvoidSingularityMethod.wrist: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BaseCobot(BaseRobot):
    def XPRS485SendData(self, send_byte: typing.SupportsInt | typing.SupportsIndex, rev_byte: typing.SupportsInt | typing.SupportsIndex, send_data: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], rev_data: PyTypeVectorInt, ec: dict) -> None:
        """
        通过xPanel末端直接传输RTU协议裸数据
        
        Args:
             opt (int): 发送字节长度, 0-16
             opt (int): 接收字节长度, 0-16
             opt (list[uint8_t]):发送字节数据, 数组长度需要和send_byte参数一致
             opt (list[uint8_t]):接收字节数据
             ec (dict): 错误码
        """
    def XPRWModbusRTUCoil(self, slave_addr: typing.SupportsInt | typing.SupportsIndex, fun_cmd: typing.SupportsInt | typing.SupportsIndex, coil_addr: typing.SupportsInt | typing.SupportsIndex, num: typing.SupportsInt | typing.SupportsIndex, data_array: PyTypeVectorBool, if_crc_reverse: bool, ec: dict) -> None:
        """
        通过xPanel末端读写modbus线圈或离散输入
        
        Args:
             opt (int): 设备地址, 0-65535
             opt (int): 功能码, 0x03 0x04 0x06 0x10
             opt (int): 线圈或离散输入寄存器地址, 0-65535
             opt (list[bool]): 发送或接收数据的数组, 非const,功能码为0x05时,只使用此数组的数据[0],此时num的值无效,除了0x05功能码,大小需要与num匹配
             opt (int):是否改变CRC校验高低位, 默认使用false,少数厂家末端工具需要反转
             opt (bool): 是否改变CRC校验高低位, true - 改变 | false - 不改变
             ec (dict): 错误码
        """
    def XPRWModbusRTUReg(self, slave_addr: typing.SupportsInt | typing.SupportsIndex, fun_cmd: typing.SupportsInt | typing.SupportsIndex, reg_addr: typing.SupportsInt | typing.SupportsIndex, data_type: str, num: typing.SupportsInt | typing.SupportsIndex, data_array: PyTypeVectorInt, if_crc_reverse: bool, ec: dict) -> None:
        """
        通过xPanel末端读写modbus寄存器
        
        Args:
             opt (int): 设备地址, 0-65535
             opt (int): 功能码, 0x03 0x04 0x06 0x10
             opt (int): 寄存器地址, 0-65535
             opt (string): 支持的数据类型, int32、int16、uint32、uint16
             opt (list[int]): 发送或接收数据的数组, 非const，功能码为0x06时,只使用此数组的数据[0],此时num的值无效,除了0x06功能码,大小需要与num匹配
             opt (int):是否改变CRC校验高低位, 默认使用false,少数厂家末端工具需要反转
             opt (bool): 是否改变CRC校验高低位, true - 改变 | false - 不改变
             ec (dict): 错误码
        """
    def cancelRecordPath(self, ec: dict) -> None:
        """
        取消录制
        
        Args:
             ec (dict): 错误码。缓存的路径数据将被删除
        """
    def disableCollisionDetection(self, ec: dict) -> None:
        """
        关闭碰撞检测功能
        
        Args:
             ec (dict): 错误码
        """
    def disableDrag(self, ec: dict) -> None:
        """
        关闭拖动
        
        Args:
             ec (dict): 错误码
        """
    def enableDrag(self, space: typing.SupportsInt | typing.SupportsIndex, type: typing.SupportsInt | typing.SupportsIndex, ec: dict, enable_drag_button: bool) -> None:
        """
        打开拖动
        
        Args:
             space (int,DragParameterSpace): 拖动空间。轴空间拖动仅支持自由拖拽类型。0: "轴空间", 1: "笛卡尔空间"
             type (int,DragParameterType): 拖动类型。0: "仅平移", 1: "仅旋转", 2: "自由拖拽"
             ec (dict): 错误码
             enable_drag_button (bool): 打开拖动功能之后可以直接拖动机器人，不需要按住末端按键
        """
    def getKeypadState(self, ec: dict) -> KeyPadState:
        """
        获取末端按键状态,不支持的机型会返回错误码
        
        Args:
             ec (dict): 错误码
        
        Returns:
             KeyPadState: 末端按键的状态。末端按键编号见《xCore机器人控制系统使用手册》末端把手的图示
        """
    def queryPathLists(self, ec: dict) -> list[str]:
        """
        查询已保存的所有路径名称
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[str]: 名称列表, 若没有路径则返回空列表
        """
    def removePath(self, name: str, ec: dict, removeAll: bool = False) -> None:
        """
        删除已保存的路径
        
        Args:
             name (str): 要删除的路径名称
             ec (dict): 错误码。若路径不存在,错误码不会被置位
             removeAll (bool, optional): 是否删除所有路径, 默认为否
        """
    def replayPath(self, name: str, rate: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        运动指令-路径回放
        
        和其它运动指令类似,调用replay_path之后,需调用move_start才会开始运动。
        
        Args:
             name (str): 要回放的路径名称
             rate (float): 回放速率, 应小于3.0, 1为路径原始速率。注意当速率大于1时,可能产生驱动器无法跟随错误
             ec (dict): 错误码
        """
    def saveRecordPath(self, name: str, ec: dict, saveAs: str = '') -> None:
        """
        保存录制好的路径
        
        Args:
             name (str): 路径名称
             ec (dict): 错误码
             saveAs (str, optional): 重命名。如果已录制好一条路径但没有保存,则用该名字保存路径。如果没有未保存的路径,则将已保存的名为"name"的路径重命名为"saveAs"
        """
    def setRtNetworkTolerance(self, percent: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置发送实时运动指令网络延迟阈值,即RobotAssist - RCI设置界面中的”包丢失阈值“。
        
        Note:
             请在切换到RtCommand模式前进行设置,否则不生效。
        
        Args:
             percent (int): 允许的范围0 - 100
             ec (dict): 错误码
        """
    def setxPanelRS485(self, opt: typing.SupportsInt | typing.SupportsIndex, if_rs485: bool, ec: dict) -> None:
        """
        设置xPanel对外供电模式和485通信。注:仅部分机型支持xPanel功能
        
        Args:
             opt (int): 模式, 0: 关闭; 1:保持; 2:12V; 3:24V
             opt (bool): 485通信, true - 打开 | false - 关闭
             ec (dict): 错误码
        """
    def setxPanelVout(self, opt: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置xPanel对外供电模式。注:仅部分机型支持xPanel功能,不支持的机型会返回错误码
        
        Args:
             opt (int): 模式. 0: 关闭; 1:保持; 2:12V; 3:24V
             ec (dict): 错误码
        """
    def startRecordPath(self, duration: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        开始录制路径
        
        Args:
             duration (int): 路径的时长,单位:秒,范围1~1800。此时长只做范围检查用,到时后控制器不会停止录制,需要调用stopRecordPath()来停止
             ec (dict): 错误码
        """
    def stopRecordPath(self, ec: dict) -> None:
        """
        停止录制路径
        
        Args:
             ec (dict): 错误码。若录制成功(无错误码),则路径数据保存在缓存中
        """
class BaseRobot:
    @staticmethod
    def sdkVersion() -> str:
        """
        查询SDK版本。
        
        Returns:
             str: 版本号。
        """
    def adjustAcceleration(self, acc: typing.SupportsFloat | typing.SupportsIndex, jerk: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        调节运动加/减速度和加加速度。
        
        Note:
             如果在机器人运动中调用,当前正在执行的指令不生效,下一条指令生效。
        
        Args:
             acc (double): 系统预设加速度的百分比,范围[0.2, 1.5]。超出范围将自动调整为上限或下限值。
             jerk (double): 系统预设的加加速度的百分比,范围[0.1, 2]。超出范围将自动调整为上限或下限值。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def adjustSpeedOnline(self, scale: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        动态调整机器人运动速率。
        
        Note:
             非实时模式时生效。
             当设置scale为1时,机器人将以路径原本速度运动。
        
        Args:
             scale (double): 运动指令的速度的比例,范围 0.01 - 1。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def baseFrame(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(6)"]:
        """
        读取基坐标系, 相对于世界坐标系。
                            
        Args:
             ec (dict): 错误码输出。
        
        Returns:
             List[float]: 长度为6的数组,包含[x, y, z, rx, ry, rz]。
        """
    def cartPosture(self, ct: CoordinateType, ec: dict) -> CartesianPosition:
        """
        获取机器人法兰或末端的当前位姿。
                            
        Args:
             ct (CoordinateType): 坐标系类型。
             ec (dict): 错误码输出。
        
        Returns:
             CartesianPosition: 当前笛卡尔位置。
        """
    @typing.overload
    def checkPath(self, start: CartesianPosition, start_joint: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], target: CartesianPosition, ec: dict) -> list[float]:
        """
        检验笛卡尔轨迹是否可达，直线轨迹。支持导轨，返回的目标轴角为轴数+外部轴数
        
        Args:
             start (CartesianPosition): 起始点
             start_joint (list[double]): 起始轴角 [弧度]
             target (CartesianPosition): 目标点
             ec (dict): 错误码,含不可达的错误原因
        
        Returns:
             list[double]: 计算出的目标轴角，仅当无错误码时有效 
        """
    @typing.overload
    def checkPath(self, start_joint: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], points: collections.abc.Sequence[CartesianPosition], target_joint_calculated: list, ec: dict) -> int:
        """
        校验多个直线轨迹
        
        Args:
             start_joint (list[double]): 起始轴角，单位[弧度]
             points (list[CartesianPosition]): 笛卡尔点位，至少需要2个点，第一个点是起始点
             target_joint_calculated (list[double]): 若校验通过。返回计算出的目标轴角
             ec (dict): 错误码,含校验失败的原因
        
        Returns:
             int: 若校验失败，返回points中出错目标点的下标。其它情况返回0 
        """
    @typing.overload
    def checkPath(self, start: CartesianPosition, start_joint: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], aux: CartesianPosition, target: CartesianPosition, ec: dict, angle: typing.SupportsFloat | typing.SupportsIndex = 0.0, rot_type: MoveCFCommandRotType = ...) -> list[float]:
        """
        检验笛卡尔轨迹是否可达，包括圆弧，全圆。支持导轨，返回的目标轴角为轴数+外部轴数
        
        Args:
             start (CartesianPosition): 起始点
             start_joint (list[double]): 起始轴角，单位[弧度]
             aux (CartesianPosition): 辅助点
             target (CartesianPosition): 目标点
             ec (dict): 错误码,含不可达的错误原因
             angle (double): 全圆执行角度，不等于零时代表校验全圆轨迹，默认0.0
             rot_type (MoveCFCommandRotType): 全圆旋转类型，默认固定位姿
        
        Returns:
             list[double]: 计算出的目标轴角，仅当无错误码时有效 
        """
    def clearServoAlarm(self, ec: dict) -> None:
        """
        清除伺服报警。
        
        Args:
             ec (dict): 错误码,当有伺服报警且清除失败时错误码为-1。
        """
    def configNtp(self, server_ip: str, ec: dict) -> None:
        """
        配置NTP。非标配功能, 需要额外安装
        
        Args:
             server_ip (str): NTP服务端IP
             ec (dict): 错误码，NTP服务未正确安装，或地址非法
        """
    def disconnectFromRobot(self, ec: dict) -> None:
        """
        断开与机器人连接。断开前会停止机器人运动,请注意安全。
                            
        Args:
             ec (dict): 错误码输出。
        """
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveAbsJCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveLCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveJCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveCCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveCFCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: collections.abc.Sequence[MoveSPCommand], ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    @typing.overload
    def executeCommand(self, cmds: ..., ec: dict) -> None:
        ...
    def getAI(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> float:
        """
        查询数字量输入信号值。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             ec (dict): 错误码输出。
        
        Returns:
             bool: true-开 | false-关。
        """
    def getAcceleration(self, acc: PyTypeDouble, jerk: PyTypeDouble, ec: dict) -> None:
        """
        读取当前加/减速度和加加速度。
        
        Args:
             acc (PyTypeDouble): 返回系统预设加速度的百分比。
             jerk (PyTypeDouble): 返回系统预设的加加速度的百分比。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def getDI(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> bool:
        """
        查询数字量输入信号值。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             ec (dict): 错误码输出。
        
        Returns:
             bool: true-开 | false-关。
        """
    def getDO(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> bool:
        """
        查询数字量输出信号值。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             ec (dict): 错误码输出。
        
        Returns:
             bool: true-开 | false-关。
        """
    @typing.overload
    def getExtAxisInfo(self, name: str, info: str, value: PyTypeInt, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名，axis1~axis6
             info (str): 参数名
                  * 点位中第几个数据映射(ext_data_number)
                  * 连接的第几个驱动器(ext_axis_number)
                  * 零点值(zero_value)
                  * 电机过载系数(motor_overload_coefficient)
                  * 分辨率(resolution_ratio)
             value (int): 返回值,0：无外部轴; 1：2轴; 2：3轴
             ec (dict): 错误码 
        """
    @typing.overload
    def getExtAxisInfo(self, name: str, info: str, value: PyTypeBool, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名，axis1~axis6
             info (str): 参数名
                  * 是否是伺服焊枪(is_servo_gun)
                  * 关节方向(joint_orient,true为正)
                  * 是否坐标系标定(coordinate_calibrated)
             value (bool): 返回值
             ec (dict): 错误码 
        """
    @typing.overload
    def getExtAxisInfo(self, name: str, info: str, value: PyTypeDouble, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名，axis1~axis6
             info (str): 参数名
                  * 最大加速度    | max_acc
                  * 最大加加速度  | max_jerk
                  * 最大速度     | max_speed
                  * 软限位下限    | soft_limit_lower
                  * 软限位上限    | soft_limit_upper
                  * 电机转矩限幅   | motor_torque_limiting
                  * 减速比        | reduction_ratio
                  * 电机额定转矩   | rated_torque_of_motor
             value (double): 返回值
             ec (dict): 错误码 
        """
    @typing.overload
    def getExtAxisInfo(self, name: str, info: str, value: PyString, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名，axis1~axis6
             info (str): 参数名,驱动器别名/固定名(driver_name)
             value (str): 返回值
             ec (dict): 错误码
        """
    @typing.overload
    def getMechUnit(self, name: str, info: str, value: PyTypeBool, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名, u1~u6
             info (str): 参数名，机械单元是否激活(activation),机械单元是否启用(enable) 
             value (bool): 返回值
             ec (dict): 错误码 
        """
    @typing.overload
    def getMechUnit(self, name: str, info: str, value: PyTypeVectorString, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名, u1~u6
             info (str): 参数名，轴名称，顺序与设置顺序相同(axes_info)
             value (List[str]): 返回值
             ec (dict): 错误码 
        """
    @typing.overload
    def getMechUnit(self, name: str, info: str, value: PyTypeInt, ec: dict) -> None:
        """
        读取机械单元参数
        
        Args:
             name (str): 参数名, u1~u6
             info (str): 参数名，机械单元类型(mech_link_type) 
             value (int): 返回值,0：基座轴; 1：变位机; 2：伺服焊枪; 3：法兰附加轴
             ec (dict): 错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: PyTypeDouble, ec: dict) -> None:
        """
        读取导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(double) 'reductionRatio'-减速比 | 'maxSpeed'-最大速度(m/s) | 'maxAcc'-最大加速度（m/s^2) | 'maxJerk'-最大加加速度(m/s^3)
             ec (dict): 错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: PyTypeInt, ec: dict) -> None:
        """
        读取导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(int) 'encoderResolution' - 编码器分辨率 | 'motorSpeed' - 电机最大转速(rpm)
             ec (dict): 错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: PyTypeBool, ec: dict) -> None:
        """
        读取导轨参数 - 开关导轨功能
        
        Args:
             name (str) 参数名 'enable'
             value(bool) True - 打开
             ec (dict): 错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: PyString, ec: dict) -> None:
        """
        读取导轨参数 - 导轨名称
        
        Args:
             name (str) 'name'
             value(str) 名称
             ec (dict): 错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: PyTypeVectorDouble, ec: dict) -> None:
        """
        读取导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(List[double]) 'softLimit'-软限位(m), [下限,上限] | 'range'-运动范围(m), [下限,上限]
             ec (dict): 错误码，参数名不存在或数据类型不匹配返回错误码 
        """
    @typing.overload
    def getRailParameter(self, name: str, value: ..., ec: dict) -> None:
        """
        读取导轨参数 - 导轨基坐标系
        
        Args:
             name (str) 参数名 'baseFrame'
             value(Frame) 坐标系
             ec (dict): 错误码 
        """
    def getRobotCfg_DHparam(self, get_nominal: bool, ec: dict) -> list[float]:
        """
        读取DH参数
        
        Args:
             get_nominal (bool): false - 优化后或设置后的参数 | true - 读取标称参数。一般建议使用false
             ec (dict): 错误码
        
        Returns:
             list[float]: DH参数, 错误码为0时有效。依次为各轴的Alpha[°], A[mm], D[mm], Theta[°]
        """
    @typing.overload
    def getStateData(self, fieldName: str, data: PyTypeUInt8) -> int:
        ...
    @typing.overload
    def getStateData(self, fieldName: str, data: PyTypeUInt64) -> int:
        ...
    @typing.overload
    def getStateData(self, fieldName: str, data: PyTypeDouble) -> int:
        ...
    @typing.overload
    def getStateData(self, fieldName: str, data: PyTypeVectorDouble, size: typing.SupportsInt | typing.SupportsIndex) -> int:
        ...
    @typing.overload
    def getStateData(self, fieldName: str, data: PyTypeVectorBool) -> int:
        ...
    def importFile(self, file_path: str, dest: str, overwrite: bool, ec: dict) -> str:
        """
        导入本地文件到控制器。阻塞等到导入完成或失败。
        
        Args:
             src_file_path (str): 本地文件的路径。文件大小需在 10MB 以内。
             dest (str): 目标路径，支持以下两种格式：
                  1. 传输单个 RL 工程的 .mod 文件: project/[工程名]/[任务名]/[mod文件名]
                  2. 传输 RL 工程的 .json/.xml/.sys 格式的配置文件: project/[工程名]/[文件名]
        
                  注意：配置文件名称不可更改，例如任务文件名必须为 "task.xml"。
             overwrite (bool): 是否覆盖同名文件。
                  - True: 覆盖同名文件。
                  - False: 自动重命名文件（仅对 .mod 文件支持自动重命名）。
             ec (dict): 错误码
        
        Returns:
             str: 导入成功后的文件名。
        """
    def importProject(self, file_path: str, overwrite: bool, ec: dict) -> str:
        """
        将本地的RL工程压缩包导入控制器。阻塞等到导入完成或失败。
        
        Args:
             file_path(str) 本地 .zip压缩包路径, 文件大小在10M以内
             overwrite(bool) 是否覆盖同名文件，是：覆盖；否：自动重命名
             ec (dict): 错误码。
        
        Returns:
             list: 工程名（比如自动重命名，返回重命名之后的）。
        """
    def jointPos(self, ec: dict) -> list[float]:
        """
        机器人当前轴角度
        
        Note:
             * 机器人本体 + 外部轴，单位: \\f$[rad/m]\\f$
             * 外部轴导轨单位\\f$[rad/m]\\f$
            
        Args:
             ec (dict): 错误码
        
        Returns:
             list[float]: 长度为\\f$ \\mathbb{R}^{DoF+ExJnt \\times 1} \\f$
        """
    def jointVel(self, ec: dict) -> list[float]:
        """
        机器人当前关节速度,
        
        Note:
             * 机器人本体+外部轴, 单位: rad/s,
             * 外部轴导轨单位m/s
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF+ExJnt \\times 1}$
        """
    def loadProject(self, name: str, tasks: collections.abc.Sequence[str], ec: dict) -> None:
        """
        加载工程。
        
        Args:
             name (str): 工程名称。
             tasks (list[str]): 要运行的任务。该参数必须指定,不能为空,否则无法执行工程。
             ec (dict): 错误码。
        """
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveAbsJCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveLCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveJCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveCCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveCFCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmds: collections.abc.Sequence[MoveSPCommand], cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveAbsJCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveLCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveJCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveCCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveCFCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveSPCommand, cmdID: PyString, ec: dict) -> None:
        ...
    @typing.overload
    def moveAppend(self, cmd: MoveWaitCommand, cmdID: PyString, ec: dict) -> None:
        ...
    def moveReset(self, ec: dict) -> None:
        """
        运动重置,清空已发送的运动指令并清除执行信息。
        
        Note:
             Robot类在初始化时会调用一次运动重置。RL程序和SDK运动指令切换控制,需要先运动重置。
        
        Args:
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def moveStart(self, ec: dict) -> None:
        """
        开始或继续机器人的运动。
        
        Args:
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def operateMode(self, ec: dict) -> OperateMode:
        """
        查询机器人当前操作模式。
                            
        Args:
             ec (dict): 错误码输出。
        
        Returns:
             OperateMode: 手动 | 自动。
        """
    def operationState(self, ec: dict) -> OperationState:
        """
        查询机器人当前运行状态 (空闲, 运动中, 拖动开启等)。
                            
        Args:
             ec (dict): 错误码输出。
        
        Returns:
             OperationState: 运行状态枚举类。
        """
    def pause(self, ec: dict) -> None:
        """
        暂停机器人运动。同stop。
        """
    def pauseProject(self, ec: dict) -> None:
        """
        暂停运行工程。
        
        Args:
             ec (dict): 错误码。
        """
    def posture(self, ct: CoordinateType, ec: dict) -> typing.Annotated[list[float], "FixedSize(6)"]:
        """
        获取机器人法兰或末端的当前位姿 \\f$^{O}T_{F}~[m][rad]\\f$。
                            
        Args:
             ct (CoordinateType): 坐标系类型。
                  1) flangeInBase: 法兰相对于基坐标系;
                  2) endInRef: 末端相对于外部参考坐标系。例如,当设置了手持工具及外部工件后,该坐标系类型返回的是工具相对于工件坐标系的坐标。
                                 再例如,若外部参考坐标系与基坐标系重合,那么返回的结果等同于末端相对于基坐标系的位姿。
             ec (dict): 错误码输出。
        
        Returns:
             std::array<double, 6>: 结果数组, 长度: \\f$ \\mathbb{R}^{6 \\times 1} \\f$ = \\f$ \\mathbb{R}^{3 \\times 1} \\f$ transformation 和 \\f$ \\mathbb{R}^{3 \\times 1} \\f$ rotation \\f$ [x, y, z, rx, ry, rz]^T \\f$。
        """
    def powerState(self, ec: dict) -> PowerState:
        """
        机器人上下电以及急停状态。
                            
        Args:
             ec (dict): 错误码输出。
        
        Returns:
             PowerState: 上电、下电、急停、安全门打开、未知。
        """
    def ppToMain(self, ec: dict) -> None:
        """
        程序指针跳转到main。调用后,等待控制器解析完工程后返回,阻塞时间视工程大小而定,超时时间设定为10秒。
        
        Args:
             ec (dict): 错误码。错误码能提供的信息有限,不能反馈如RL语法错误、变量不存在等错误。可通过queryControllerLog()查询错误日志。
        """
    def projectsInfo(self, ec: dict) -> list[RLProjectInfo]:
        """
        查询工控机中RL工程名称及任务。
        
        Args:
             ec (dict): 错误码。
        
        Returns:
             list[RLProjectInfo]: 工程信息列表,若没有创建工程则返回空列表。
        """
    def queryControllerLog(self, count: typing.SupportsInt | typing.SupportsIndex, level: collections.abc.Set[LogInfoLevel], ec: dict, offset: typing.SupportsInt | typing.SupportsIndex = 0) -> list[LogInfo]:
        """
        查询控制器最新的日志。
        
        Args:
             count (int): 查询个数,最多返回10条日志。
             level (set[LogInfo.Level]): 指定日志等级的集合,为空表示不指定特定等级。
             ec (dict): 错误码。
             offset (int): 偏移数, 比如0代表从最新的日志开始查询, 10代表从第11条开始查询
        
        Returns:
             list[LogInfo]: 包含日志信息的列表。
        """
    def queryEventInfo(self, eventType: Event, ec: dict) -> dict:
        """
        查询事件信息。与 setEventWatcher() 回调时的提供的信息相同,区别是这个接口是主动查询的方式。
        
        Args:
             eventType (Event): 事件类型。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        
        Returns:
             dict: 事件信息。
        """
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeBool, ec: dict) -> None:
        ...
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeInt, ec: dict) -> None:
        ...
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeFloat, ec: dict) -> None:
        ...
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeVectorBool, ec: dict) -> None:
        ...
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeVectorInt, ec: dict) -> None:
        ...
    @typing.overload
    def readRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: PyTypeVectorFloat, ec: dict) -> None:
        ...
    def rebootSystem(self, ec: dict) -> None:
        """
        重启工控机 
        
        Note:
             在自动模式、下电状态、运动和非空闲状态不允许重启操作
                            
        Args:
             ec (dict): 错误码输出。
        """
    def recoverState(self, item: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        根据选项恢复机器人状态。
        
        Args:
             item (int): 恢复选项,1 表示急停恢复。
             ec (dict): 错误码。
        """
    def removeFiles(self, file_path_list: collections.abc.Sequence[str], ec: dict) -> None:
        """
        删除控制器中文件。注: 工程.xml, .json等配置文件不能删除，只能替换
        
        Args:
             file_path_list(list[str]) 文件路径的列表, 单个文件路径如下:
                  1. 删除某工程某任务下的 .mod文件: project/[工程名]/[任务名]/[mod文件名]
                  2. 删除某工程某任务: project/[工程名]/[任务名]
             ec (dict): 参数格式错误或网络错误。工程或任务或文件不存在不返回错误码
        """
    def removeProject(self, name: str, ec: dict, remove_all: bool = False) -> None:
        """
        删除控制器里的RL工程。
        
        Args:
             project_name(str) 工程名
             remove_all(bool, optional) 是否删除所有工程，缺省值是False
             ec (dict): 错误码。
        """
    def robotInfo(self, ec: dict) -> Info:
        """
        查询机器人基本信息。
                            
        Args:
             ec (dict): 错误码输出。
        Returns:
             Info: 机器人基本信息。
        """
    def runProject(self, ec: dict) -> None:
        """
        开始运行当前加载的工程。
        
        Args:
             ec (dict): 错误码。
        """
    def setAO(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, value: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置模拟量输出信号。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             value (float): 输出值。
             ec (dict): 错误码输出。
        """
    def setAutoIgnoreZone(self, enable: bool, ec: dict) -> None:
        """
        设置运动指令是否使自动取消转弯区。初始值为true
        
        Args:
             enable (bool): true - 自动取消转弯区 | false - 不会自动取消转弯区
             ec (dict): 错误码
        """
    def setBaseFrame(self, frame: Frame, ec: dict) -> None:
        """
        设置基坐标系, 设置后仅保存数值,重启控制器后生效。
                            
        Args:
             frame (Frame): 坐标系,默认使用自定义安装方式。
             ec (dict): 错误码输出。
        """
    def setConnectionHandler(self, handler: collections.abc.Callable[[bool], None]) -> None:
        """
        设置连接断开回调函数。
        
        Args:
             handler(bool): 回调函数, 参数为bool, true-连接 | false-断开。
        """
    def setDI(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, state: bool, ec: dict) -> None:
        """
        设置数字量输入信号值。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             state (bool): true-开 | false-关。
             ec (dict): 错误码输出。
        """
    def setDO(self, board: typing.SupportsInt | typing.SupportsIndex, port: typing.SupportsInt | typing.SupportsIndex, state: bool, ec: dict) -> None:
        """
        设置数字量输出信号值。
        
        Args:
             board (int): IO板序号。
             port (int): 信号端口号。
             state (bool): true-开 | false-关。
             ec (dict): 错误码输出。
        """
    def setDefaultConfOpt(self, forced: bool, ec: dict) -> None:
        """
        设置是否使用轴配置数据计算逆解。
        
        Note:
             初始值为false。
             true - 使用运动指令的confData计算笛卡尔点位逆解,如计算失败则返回错误。
             false - 不使用,逆解时会选取机械臂当前轴角度的最近解。
        
        Args:
             forced (bool): 是否强制使用轴配置数据。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setDefaultSpeed(self, speed: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设定默认运动速度。
        
        Note:
             该数值表示末端最大线速度(单位mm/s),自动计算对应关节速度。
             关节速度百分比根据speed划分为5个的范围:
             - < 100 : 10%
             - 100 ~ 200 : 30%
             - 200 ~ 500 : 50%
             - 500 ~ 800 : 80%
             - > 800 : 100%
             空间旋转速度为200°/s。
        
        Args:
             speed (double): 末端线速度。实际有效范围为5-4000(协作)、5-7000(工业)。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setDefaultZone(self, zone: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设定默认转弯区。
        
        Note:
             该数值表示运动最大转弯区半径(单位:mm),自动计算转弯百分比。
             转弯百分比划分4个范围:
             - < 1 : 0 (fine)
             - 1 ~ 20 : 10%
             - 20 ~ 60 : 30%
             - > 60 : 100%
        
        Args:
             zone (float): 转弯区半径大小。实际有效范围为0-200。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setEventWatcher(self, eventType: Event, callback: collections.abc.Callable[[dict], None], ec: dict) -> None:
        """
        设置接收事件的回调函数。
        
        Args:
             eventType (Event): 事件类型。
             callback (EventCallback): 处理事件的回调函数。说明:
                  1) 对于Event::moveExecution, 回调函数在同一个线程执行, 请避免函数中有执行时间较长的操作;
                  2) Event::safety则每次独立线程回调, 没有执行时间的限制。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setMaxCacheSize(self, number: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置最大缓存指令个数。
        
        Note:
             * 指发送到控制器待规划的路径点个数,允许的范围[1,1000]，初始值为300。
             * 如果轨迹多为短轨迹,可以调大这个数值,避免因指令发送不及时导致机器人停止运动。
             * 停止后如果有未执行的指令,可通过调用 moveStart() 继续。
        
        Args:
             number (int): 最大缓存指令个数。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setMotionControlMode(self, mode: MotionControlMode, ec: dict) -> None:
        """
        设置运动控制模式。
        
        Note:
             在调用各运动控制接口之前,须设置对应的控制模式。
        
        Args:
             mode (MotionControlMode): 控制模式。
             ec (dict): 错误码。若设置失败,错误码将被设置为相应的错误信息。
        """
    def setNoneEventWatcher(self, eventType: Event, ec: dict) -> None:
        """
        取消接收事件的回调函数。
        
        Args:
             eventType (Event): 事件类型。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def setOperateMode(self, mode: OperateMode, ec: dict) -> None:
        """
        切换手自动模式。
                            
        Args:
             mode (OperateMode): 手动/自动。
             ec (dict): 错误码输出。
        """
    def setPowerState(self, on: bool, ec: dict) -> None:
        """
        机器人上下电。注: 只有无外接使能开关或示教器的机器人才能手动模式上电。
                            
        Args:
             on (bool): true-上电 | false-下电。
             ec (dict): 错误码输出。
        """
    def setProjectRunningOpt(self, rate: typing.SupportsFloat | typing.SupportsIndex, loop: bool, ec: dict) -> None:
        """
        更改工程的运行速度和循环模式。
        
        Args:
             rate (float): 运行速率,范围 0.01 - 1。
             loop (bool): true - 循环执行 | false - 单次执行。
             ec (dict): 错误码。
        """
    @typing.overload
    def setRailParameter(self, name: str, value: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ec: dict) -> None:
        """
        设置导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(list[double]) 'softLimit'-软限位(m), [下限,上限] | 'range'-运动范围(m), [下限,上限]
             ec (dict): 错误码 
        """
    @typing.overload
    def setRailParameter(self, name: str, value: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(double) 'reductionRatio'-减速比 | 'maxSpeed'-最大速度(m/s) | 'maxAcc'-最大加速度（m/s^2) | 'maxJerk'-最大加加速度(m/s^3)
             ec (dict): 错误码 
        """
    @typing.overload
    def setRailParameter(self, name: str, value: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置导轨参数
        
        Args:
             name (str) 参数名，见value说明
             value(int) 'encoderResolution' - 编码器分辨率 | 'motorSpeed' - 电机最大转速(rpm)
             ec (dict): 错误码 
        """
    @typing.overload
    def setRailParameter(self, name: str, value: str, ec: dict) -> None:
        """
        设置导轨参数 - 导轨名称
        
        Args:
             name (str) 'name'
             value(str) 名称
             ec (dict): 错误码 
        """
    @typing.overload
    def setRailParameter(self, name: str, value: bool, ec: dict) -> None:
        """
        设置导轨参数 - 开关导轨功能
        
        Args:
             name (str) 参数名 'enable'
             value(bool) True - 打开
             ec (dict): 错误码 
        """
    @typing.overload
    def setRailParameter(self, name: str, value: Frame, ec: dict) -> None:
        """
        设置导轨参数 - 导轨基坐标系
        
        Args:
             name (str) 参数名 'baseFrame'
             value(Frame) 坐标系
             ec (dict): 错误码 
        """
    def setSimulationMode(self, state: bool, ec: dict) -> None:
        """
        设置输入仿真模式。
        
        Args:
             state (bool): true - 打开 | false - 关闭。
             ec (dict): 错误码输出。
        """
    def setTeachPendantMode(self, enable: bool, ec: dict) -> None:
        """
        设置机器人示教器模式的启用/禁用状态。
        阻塞执行，接口会等待模式切换完成后返回，预设超时时间适配示教器模式切换的常规耗时（约2秒）。
        
        Args:
             enable (bool): 示教器模式开关，True表示启用示教器模式，False表示禁用示教器模式
             ec (dict): 错误码字典，key包括"ec"（错误码数值）和"message"（错误描述）；
                        常见错误场景：示教器通信异常、模式切换权限不足、机器人处于运动状态无法切换模式
        """
    def setToolInfo(self, tool_info: WorkToolInfo, ec: dict) -> None:
        """
        设置全局工具信息，或新建/设置RL工程中工具的位姿信息和负载信息
        
        Notes:
             1. 全局工具: 控制器支持16个全局工具，名称固定为 "g_tool_0" ~ "g_tool_15"
             2. RL工程工具: 使用起来限制条件较多，不建议通过该接口设置工程工具，建议用全局工具。限制条件有:
                  - 需要先加载好一个工程，再设置。只要名称不是全局工具的，都视为工程工具。
                  - 若工具不存在则新建，存在则修改。
                  - 需要配合修改工程的工具配置文件，否则RL指令可能无法正常解析工具信息。并且如果不改配置文件，设置后的数据也不会保存。
             3. 暂不支持设置工具包络信息
        
        Args:
             tool_info(WorkToolInfo) 工具信息。
             ec (dict):  全局工具一般不会设置失败。工程中工具可能会设置失败，比如给控制器推送了工程的工具配置文件但是没有重新加载工程，工具配置不一致的情况下会返回错误码
        """
    @typing.overload
    def setToolset(self, toolset: Toolset, ec: dict) -> None:
        """
        设置工具工件组信息。
                            
        Note:
             此工具工件组仅为SDK使用, 不与RL工程相关。
             设置后RobotAssist右上角会显示“toolx", "wobjx", 状态监控显示的末端坐标也会变化。
             除此接口外, 如果通过RobotAssist更改默认工具工件(右上角的选项), 该工具工件组也会相应更改。
        
        Args:
             toolset (Toolset): 工具工件组信息。
             ec (dict): 错误码输出。
        """
    @typing.overload
    def setToolset(self, toolName: str, wobjName: str, ec: dict) -> Toolset:
        """
        使用已创建的工具和工件,设置工具工件组信息。
        
        Note:
             设置前提: 已加载一个RL工程,且创建了工具和工件。否则,只能设置为默认的工具工件,即"tool0"和"wobj0"。
             一组工具工件无法同时为手持或外部;如果有冲突,以工具的位置为准,例如工具工件同时为手持,不会返回错误,但是工件的坐标系变成了外部。
        
        Args:
             toolName (str): 工具名称。
             wobjName (str): 工件名称。
             ec (dict): 错误码输出。
        
        Returns:
             Toolset: 设置后的工具工件组信息。当发生错误设置失败时,返回Toolset类型初始化默认值0。
        """
    def setWobjInfo(self, wobj_info: WorkToolInfo, ec: dict) -> None:
        """
        设置全局工件信息，或新建/设置RL工程中工件的位姿信息和负载信息
        
        Notes:
             1. 全局工件: 控制器支持16个全局工件，名称固定为 "g_wobj_0" ~ "g_wobj_15"
             2. RL工程工件: 使用起来限制条件较多，不建议通过该接口设置工程工件，建议用全局工件。限制条件有:
                  - 需要先加载好一个工程，再设置。只要名称不是全局工件的，都视为工程工件。
                  - 若工件不存在则新建，存在则修改。
                  - 需要配合修改工程的工件配置文件，否则RL指令可能无法正常解析工具信息。并且如果不改配置文件，设置后的数据也不会保存。
             3. 暂不支持设置相关用户坐标系，全局工件默认为"g_user_0", 工程工件默认为 "userframe0"
        
        Args:
             wobj_info(WorkToolInfo) 工件信息
             ec (dict): 同理设置工具接口，全局工件一般不会设置失败。工程中工件可能会设置失败
        """
    def shutdownSystem(self, ec: dict) -> None:
        """
        关闭工控机。
        
        Note:
             在自动模式、下电状态、运动和非空闲状态不允许重启操作。控制柜断电后重新上电才能重新启动控制器软件。
                            
        Args:
             ec (dict): 错误码输出。
        """
    def startJog(self, space: JogOptSpace, rate: typing.SupportsFloat | typing.SupportsIndex, step: typing.SupportsFloat | typing.SupportsIndex, index: typing.SupportsInt | typing.SupportsIndex, direction: bool, ec: dict) -> None:
        """
        开始jog机器人,需要切换到手动操作模式。
        
        Note:
             调用此接口并且机器人开始运动后,无论机器人是否已经自行停止,都必须调用 stop() 来结束jog操作,否则机器人会一直处于jog的运行状态。
        
        Args:
             space (JogOpt::Space): jog参考坐标系。工具/工件坐标系使用原则同 setToolset(); 工业六轴机型和xMateCR/SR六轴机型支持两种奇异规避方式: JogOpt::singularityAvoidMode JogOpt::baseParallelMode; CR5轴机型支持平行基座模式Jog: JogOpt::baseParallelMode。
             rate (double): 速率,范围 0.01 - 1。
             step (double): 步长。单位: 笛卡尔空间-毫米 | 轴空间-度。步长大于0即可,不设置上限,如果机器人无法继续jog会自行停止运动。
             index (unsigned): 根据不同的space,该参数含义如下：
                  世界坐标系,基坐标系,法兰坐标系,工具工件坐标系:
                       a) 6轴机型: 0~5分别对应X, Y, Z, Rx, Ry, Rz。>5代表外部轴(若有)
                       b) 7轴机型6代表肘关节, >6代表外部轴(若有)
                  轴空间: 关节序号,从0开始计数;
                  奇异规避模式,平行基座模式:
                       a) 6轴机型 0~5分别对应X, Y, Z, J4(4轴), Ry, J6(6轴);
                       b) 5轴机型 0~4分别对应X, Y, Z, Ry, J5(5轴)。
             direction (bool): 根据不同的space和index,该参数含义如下：
                  奇异规避模式 J4: true - ±180° | false - 0°;
                  平行基座模式 J4 & Ry: true - ±180° | false - 0°;
                  其它,true - 正向 | false - 负向。
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def startJogWithExt(self, space: JogOptSpace, rate: typing.SupportsFloat | typing.SupportsIndex, step: typing.SupportsFloat | typing.SupportsIndex, index: typing.SupportsInt | typing.SupportsIndex, direction: bool, fixed_name: str, ec: dict, is_ext: bool = True) -> None:
        """
        开始jog机器人
        
        Note:
             其余参数同startJog
        
        Args:
             fixed_name (str): 固定名称。
                  * fixed_name与index配合使用，fixed_name传入任意字符，is_ext为false，index为0，则jog机器人第一个轴
                  * fixed_name传入u1，index为0，则jog机械单元u1的第一个轴
             is_ext (bool): 是否为移动外部轴
        """
    def stop(self, ec: dict) -> None:
        """
        暂停机器人运动。
        
        Note:
             目前支持stop2停止类型,规划停止不断电,参见StopLevel。
        
        Args:
             ec (dict): 错误码。若操作失败,错误码将被设置为相应的错误信息。
        """
    def stopReceiveRobotState(self) -> None:
        """
        停止接收实时状态数据，同时控制器停止发送。可用于重新设置要接收的状态数据。
        """
    def syncTimeWithServer(self, ec: dict) -> None:
        """
        手动同步一次时间，远端IP是通过configNtp配置的。耗时几秒钟，阻塞等待同步完成，接口预设的超时时间是12秒。非标配功能, 需要额外安装
        
        Args:
             ec (dict): 错误码，NTP服务未正确安装，或无法和服务端同步
        """
    def toolsInfo(self, ec: dict) -> list[WorkToolInfo]:
        """
        查询当前加载工程的工具信息。
        
        Args:
             ec (dict): 错误码。
        
        Returns:
             list: 工具信息列表,若未加载任何工程或没有创建工具,则返回默认工具tool0的信息。
        """
    def toolset(self, ec: dict) -> Toolset:
        """
        查询当前工具工件组信息。
                            
        Note:
             此工具工件组仅为SDK运动控制使用, 不与RL工程相关。
        
        Args:
             ec (dict): 错误码输出。
        
        Returns:
             Toolset: 工具工件组信息。
        """
    def updateRobotState(self, timeout: datetime.timedelta) -> int:
        """
        接收一次机器人状态数据,在每周期读取数据前,需调用此函数。建议按照设定的发送频率来调用,以获取最新的数据。
        
        Args:
             timeout (duration): 超时时间。
        
        Returns:
             unsigned: 接收到的数据长度。如果超时前没有收到数据,返回0。
        
        Raises:
             RealtimeControlException: 无法收到数据或收到的数据有误导致无法解析。
        """
    def wobjsInfo(self, ec: dict) -> list[WorkToolInfo]:
        """
        查询当前加载工程的工件信息。
        
        Args:
             ec (dict): 错误码。
        
        Returns:
             list: 工件信息列表,若未加载任何工程或没有创建工件,则返回空vector。
        """
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: bool, ec: dict) -> None:
        ...
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        ...
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        ...
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: collections.abc.Sequence[bool], ec: dict) -> None:
        ...
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex], ec: dict) -> None:
        ...
    @typing.overload
    def writeRegister(self, name: str, index: typing.SupportsInt | typing.SupportsIndex, value: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], ec: dict) -> None:
        ...
class CartesianPosition(Frame, Finishable):
    """
    笛卡尔点位
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], arg1: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        ...
    @property
    def confData(self) -> list[int]:
        """
        轴配置数据，长度为8：[cf1, cf2, cf3, cf4, cf5, cf6, cf7, cfx]
        """
    @confData.setter
    def confData(self, arg0: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @property
    def elbow(self) -> float:
        """
        臂角, 适用于7轴机器人, 单位：弧度
        """
    @elbow.setter
    def elbow(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def external(self) -> list[float]:
        """
        外部关节数值 单位:弧度|米。导轨单位米
        """
    @external.setter
    def external(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    @property
    def hasElbow(self) -> bool:
        """
        是否有臂角
        """
    @hasElbow.setter
    def hasElbow(self, arg0: bool) -> None:
        ...
class CartesianPositionOffset:
    """
    笛卡尔点位偏移
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, type: CartesianPositionOffsetType, frame: Frame) -> None:
        """
        构造函数
        
        Args:
             type (Offset.Type): 偏移类型
             frame (Frame): 相对于指定工具/工件坐标系的偏移
        """
    @property
    def frame(self) -> Frame:
        """
        相对于指定工具/工件坐标系的偏移
        """
    @frame.setter
    def frame(self, arg0: Frame) -> None:
        ...
    @property
    def type(self) -> CartesianPositionOffsetType:
        """
        偏移类型
        """
    @type.setter
    def type(self, arg0: CartesianPositionOffsetType) -> None:
        ...
class CartesianPositionOffsetType:
    """
    笛卡尔点位偏移类型
    
    Members:
    
      none : 无偏移
    
      offs : 相对工件坐标系偏移
    
      relTool : 相对工具坐标系偏移
    """
    __members__: typing.ClassVar[dict[str, CartesianPositionOffsetType]]  # value = {'none': <CartesianPositionOffsetType.none: 0>, 'offs': <CartesianPositionOffsetType.offs: 1>, 'relTool': <CartesianPositionOffsetType.relTool: 2>}
    none: typing.ClassVar[CartesianPositionOffsetType]  # value = <CartesianPositionOffsetType.none: 0>
    offs: typing.ClassVar[CartesianPositionOffsetType]  # value = <CartesianPositionOffsetType.offs: 1>
    relTool: typing.ClassVar[CartesianPositionOffsetType]  # value = <CartesianPositionOffsetType.relTool: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Cobot_5(Robot_T_Collaborative_5, BaseCobot):
    """
    协作机器人模板类, 提供协作机器人支持功能的接口
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def calibrateForceSensor(self, all_axes: bool, axis_index: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        力传感器标定。
        
        Note:
             标定过程需要约100ms, 该函数不会阻塞等待标定完成。
             标定前需要通过setToolset()设置正确的负载(Toolset::load), 否则会影响标定结果准确性。
        
        Args:
             all_axes (bool): true - 标定所有轴 | false - 单轴标定
             axis_index (int): 轴下标, 范围[0, DoF), 仅当单轴标定时生效
             ec (dict): 错误码
        """
    def enableCollisionDetection(self, sensitivity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], behaviour: StopLevel, fallback_compliance: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置碰撞检测相关参数, 打开碰撞检测功能。
        
        Args:
             sensitivity (List[float]): 碰撞检测灵敏度,范围0.01-2.0
             behaviour (int): 碰撞后机器人行为,支持0(安全停止), 1(触发暂停), 2(柔顺停止)
             fallback_compliance (float):
                  - 碰撞后行为是安全停止或触发暂停时,回退距离(米)
                  - 碰撞后行为是柔顺停止时,柔顺度范围 [0.0, 1.0]
             ec (dict): 错误码
        """
    def forceControl(self) -> ...:
        """
        力控指令类
        
        Returns:
             ForceControl_T: 力控指令类实例
        """
    def getRtMotionController(self) -> ...:
        """
        创建实时运动控制类(RtMotionControlCobot)实例,通过此实例指针进行实时模式相关的操作。
        
        Note:
             除非重复调用此接口,客户端内部逻辑不会主动析构返回的对象,
             包括但不限于断开和机器人连接disconnectFromRobot(),切换到非实时运动控制模式等,但做上述操作之后再进行实时模式控制会产生异常。
        
        Returns:
             控制器对象
        
        Raises:
             RealtimeControlException: 创建RtMotionControl实例失败,由于网络问题
             ExecutionException: 没有切换到实时运动控制模式
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
class Cobot_6(Robot_T_Collaborative_6, BaseCobot):
    """
    协作机器人模板类, 提供协作机器人支持功能的接口
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def calibrateForceSensor(self, all_axes: bool, axis_index: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        力传感器标定。
        
        Note:
             标定过程需要约100ms, 该函数不会阻塞等待标定完成。
             标定前需要通过setToolset()设置正确的负载(Toolset::load), 否则会影响标定结果准确性。
        
        Args:
             all_axes (bool): true - 标定所有轴 | false - 单轴标定
             axis_index (int): 轴下标, 范围[0, DoF), 仅当单轴标定时生效
             ec (dict): 错误码
        """
    def enableCollisionDetection(self, sensitivity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], behaviour: StopLevel, fallback_compliance: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置碰撞检测相关参数, 打开碰撞检测功能。
        
        Args:
             sensitivity (List[float]): 碰撞检测灵敏度,范围0.01-2.0
             behaviour (int): 碰撞后机器人行为,支持0(安全停止), 1(触发暂停), 2(柔顺停止)
             fallback_compliance (float):
                  - 碰撞后行为是安全停止或触发暂停时,回退距离(米)
                  - 碰撞后行为是柔顺停止时,柔顺度范围 [0.0, 1.0]
             ec (dict): 错误码
        """
    def forceControl(self) -> ...:
        """
        力控指令类
        
        Returns:
             ForceControl_T: 力控指令类实例
        """
    def getRtMotionController(self) -> ...:
        """
        创建实时运动控制类(RtMotionControlCobot)实例,通过此实例指针进行实时模式相关的操作。
        
        Note:
             除非重复调用此接口,客户端内部逻辑不会主动析构返回的对象,
             包括但不限于断开和机器人连接disconnectFromRobot(),切换到非实时运动控制模式等,但做上述操作之后再进行实时模式控制会产生异常。
        
        Returns:
             控制器对象
        
        Raises:
             RealtimeControlException: 创建RtMotionControl实例失败,由于网络问题
             ExecutionException: 没有切换到实时运动控制模式
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
class Cobot_7(Robot_T_Collaborative_7, BaseCobot):
    """
    协作机器人模板类, 提供协作机器人支持功能的接口
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def calibrateForceSensor(self, all_axes: bool, axis_index: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        力传感器标定。
        
        Note:
             标定过程需要约100ms, 该函数不会阻塞等待标定完成。
             标定前需要通过setToolset()设置正确的负载(Toolset::load), 否则会影响标定结果准确性。
        
        Args:
             all_axes (bool): true - 标定所有轴 | false - 单轴标定
             axis_index (int): 轴下标, 范围[0, DoF), 仅当单轴标定时生效
             ec (dict): 错误码
        """
    def enableCollisionDetection(self, sensitivity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], behaviour: StopLevel, fallback_compliance: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置碰撞检测相关参数, 打开碰撞检测功能。
        
        Args:
             sensitivity (List[float]): 碰撞检测灵敏度,范围0.01-2.0
             behaviour (int): 碰撞后机器人行为,支持0(安全停止), 1(触发暂停), 2(柔顺停止)
             fallback_compliance (float):
                  - 碰撞后行为是安全停止或触发暂停时,回退距离(米)
                  - 碰撞后行为是柔顺停止时,柔顺度范围 [0.0, 1.0]
             ec (dict): 错误码
        """
    def forceControl(self) -> ...:
        """
        力控指令类
        
        Returns:
             ForceControl_T: 力控指令类实例
        """
    def getRtMotionController(self) -> ...:
        """
        创建实时运动控制类(RtMotionControlCobot)实例,通过此实例指针进行实时模式相关的操作。
        
        Note:
             除非重复调用此接口,客户端内部逻辑不会主动析构返回的对象,
             包括但不限于断开和机器人连接disconnectFromRobot(),切换到非实时运动控制模式等,但做上述操作之后再进行实时模式控制会产生异常。
        
        Returns:
             控制器对象
        
        Raises:
             RealtimeControlException: 创建RtMotionControl实例失败,由于网络问题
             ExecutionException: 没有切换到实时运动控制模式
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
class CoordinateType:
    """
    位姿坐标系类型
    
    Members:
    
      flangeInBase : 法兰相对于基坐标系
    
      endInRef : 末端相对于外部坐标系
    """
    __members__: typing.ClassVar[dict[str, CoordinateType]]  # value = {'flangeInBase': <CoordinateType.flangeInBase: 0>, 'endInRef': <CoordinateType.endInRef: 1>}
    endInRef: typing.ClassVar[CoordinateType]  # value = <CoordinateType.endInRef: 1>
    flangeInBase: typing.ClassVar[CoordinateType]  # value = <CoordinateType.flangeInBase: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DragParameterSpace:
    """
    机器人拖动模式参数, 拖动类型
    
    Members:
    
      jointSpace : 轴空间
    
      cartesianSpace : 笛卡尔空间
    """
    __members__: typing.ClassVar[dict[str, DragParameterSpace]]  # value = {'jointSpace': <DragParameterSpace.jointSpace: 0>, 'cartesianSpace': <DragParameterSpace.cartesianSpace: 1>}
    cartesianSpace: typing.ClassVar[DragParameterSpace]  # value = <DragParameterSpace.cartesianSpace: 1>
    jointSpace: typing.ClassVar[DragParameterSpace]  # value = <DragParameterSpace.jointSpace: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DragParameterType:
    """
    机器人拖动模式参数, 拖动空间
    
    Members:
    
      translationOnly : 仅平移
    
      rotationOnly : 仅旋转
    
      freely : 自由拖拽
    """
    __members__: typing.ClassVar[dict[str, DragParameterType]]  # value = {'translationOnly': <DragParameterType.translationOnly: 0>, 'rotationOnly': <DragParameterType.rotationOnly: 1>, 'freely': <DragParameterType.freely: 2>}
    freely: typing.ClassVar[DragParameterType]  # value = <DragParameterType.freely: 2>
    rotationOnly: typing.ClassVar[DragParameterType]  # value = <DragParameterType.rotationOnly: 1>
    translationOnly: typing.ClassVar[DragParameterType]  # value = <DragParameterType.translationOnly: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Event:
    """
    事件类型
    
    Members:
    
      moveExecution : 非实时运动指令执行信息
    
      safety : 安全 (是否碰撞)
    
      rlExecution : RL执行状态
    
      logReporter : 控制器日志上报
    """
    __members__: typing.ClassVar[dict[str, Event]]  # value = {'moveExecution': <Event.moveExecution: 0>, 'safety': <Event.safety: 1>, 'rlExecution': <Event.rlExecution: 2>, 'logReporter': <Event.logReporter: 3>}
    logReporter: typing.ClassVar[Event]  # value = <Event.logReporter: 3>
    moveExecution: typing.ClassVar[Event]  # value = <Event.moveExecution: 0>
    rlExecution: typing.ClassVar[Event]  # value = <Event.rlExecution: 2>
    safety: typing.ClassVar[Event]  # value = <Event.safety: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Finishable:
    """
    一次运动循环是否结束
    """
    def __init__(self) -> None:
        """
        默认构造函数
        """
    def isFinished(self) -> int:
        """
        是否已设置运动循环结束
        
        Returns:
             uint8_t: 结束标志 (0 或 1)
        """
    def setFinished(self) -> None:
        """
        标识运动循环已结束
        """
class Frame:
    """
    坐标系
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, trans: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], rpy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        """
        初始化trans & rpy
        
        Args:
             trans (array[3]): 平移量   
             rpy (array[3]): 欧拉角XYZ
        """
    @typing.overload
    def __init__(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> None:
        """
        初始化trans & rpy
        
        Args:
             frame (array[6]): [X, Y, Z, Rx, Ry, Rz]
        """
    @typing.overload
    def __init__(self, matrix: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> None:
        """
        初始化pos
        
        Args:
             matrix (array[16]): 4*4变换矩阵
        """
    @typing.overload
    def __init__(self, values: ...) -> None:
        """
        初始化
        
        Args:
             values (initializer_list[double]): 长度为6时初始化trans & rot = [X, Y, Z, Rx, Ry, Rz]; 长度为16时初始化pos
        
        Raises:
             ArgumentException: 初始化列表长度错误
        """
    @property
    def pos(self) -> typing.Annotated[list[float], "FixedSize(16)"]:
        """
        行优先齐次变换矩阵
        """
    @pos.setter
    def pos(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> None:
        ...
    @property
    def rpy(self) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        欧拉角 [Rx, Ry, Rz], 单位：弧度
        """
    @rpy.setter
    def rpy(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
    @property
    def trans(self) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        平移量 [X, Y, Z], 单位：米
        """
    @trans.setter
    def trans(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
class FrameCalibrationResult:
    """
    坐标系标定结果
    """
    def __init__(self) -> None:
        ...
    @property
    def errors(self) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        样本点与TCP标定值的偏差, 依次为最小值,平均值,最大值, 单位：m
        """
    @errors.setter
    def errors(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
    @property
    def frame(self) -> Frame:
        """
        标定结果
        """
    @frame.setter
    def frame(self, arg0: Frame) -> None:
        ...
class FrameType:
    """
    坐标系类型
    
    Members:
    
      world : 世界坐标系
    
      base : 基坐标系
    
      flange : 法兰坐标系
    
      tool : 工具坐标系
    
      wobj : 工件坐标系
    
      path : 路径坐标系
    
      rail : 导轨基坐标系
    """
    __members__: typing.ClassVar[dict[str, FrameType]]  # value = {'world': <FrameType.world: 0>, 'base': <FrameType.base: 1>, 'flange': <FrameType.flange: 2>, 'tool': <FrameType.tool: 3>, 'wobj': <FrameType.wobj: 4>, 'path': <FrameType.path: 5>, 'rail': <FrameType.rail: 6>}
    base: typing.ClassVar[FrameType]  # value = <FrameType.base: 1>
    flange: typing.ClassVar[FrameType]  # value = <FrameType.flange: 2>
    path: typing.ClassVar[FrameType]  # value = <FrameType.path: 5>
    rail: typing.ClassVar[FrameType]  # value = <FrameType.rail: 6>
    tool: typing.ClassVar[FrameType]  # value = <FrameType.tool: 3>
    wobj: typing.ClassVar[FrameType]  # value = <FrameType.wobj: 4>
    world: typing.ClassVar[FrameType]  # value = <FrameType.world: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IndustrialRobot_3(Robot_T_Industrial_3):
    """
    工业机器人模板类
    """
class IndustrialRobot_4(Robot_T_Industrial_4):
    """
    工业机器人模板类
    """
class IndustrialRobot_6(Robot_T_Industrial_6):
    """
    工业机器人模板类
    """
class Info:
    """
    机器人基本信息，在与建立机器人连接后加载
    """
    def __init__(self) -> None:
        ...
    @property
    def id(self) -> str:
        """
        机器人uid, 可用于区分连接的机器人
        """
    @id.setter
    def id(self, arg0: str) -> None:
        ...
    @property
    def joint_num(self) -> int:
        """
        轴数
        """
    @joint_num.setter
    def joint_num(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def mac(self) -> str:
        """
        Mac地址
        """
    @mac.setter
    def mac(self, arg0: str) -> None:
        ...
    @property
    def type(self) -> str:
        """
        机器人机型名称
        """
    @type.setter
    def type(self, arg0: str) -> None:
        ...
    @property
    def version(self) -> str:
        """
        控制器版本
        """
    @version.setter
    def version(self, arg0: str) -> None:
        ...
class JogOptSpace:
    """
    Jog选项: 坐标系
    
    Members:
    
      world : 世界坐标系
    
      flange : 法兰坐标系
    
      baseFrame : 基坐标系
    
      toolFrame : 工具坐标系
    
      wobjFrame : 工件坐标系
    
      jointSpace : 轴空间
    
      singularityAvoidMode : 奇异规避模式，适用于工业六轴, xMateCR和xMateSR机型，规避方法是锁定4轴
    
      baseParallelMode : 平行基座模式，仅适用于xMateCR和xMateSR机型
    """
    __members__: typing.ClassVar[dict[str, JogOptSpace]]  # value = {'world': <JogOptSpace.world: 0>, 'flange': <JogOptSpace.flange: 1>, 'baseFrame': <JogOptSpace.baseFrame: 2>, 'toolFrame': <JogOptSpace.toolFrame: 3>, 'wobjFrame': <JogOptSpace.wobjFrame: 4>, 'jointSpace': <JogOptSpace.jointSpace: 5>, 'singularityAvoidMode': <JogOptSpace.singularityAvoidMode: 6>, 'baseParallelMode': <JogOptSpace.baseParallelMode: 7>}
    baseFrame: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.baseFrame: 2>
    baseParallelMode: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.baseParallelMode: 7>
    flange: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.flange: 1>
    jointSpace: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.jointSpace: 5>
    singularityAvoidMode: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.singularityAvoidMode: 6>
    toolFrame: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.toolFrame: 3>
    wobjFrame: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.wobjFrame: 4>
    world: typing.ClassVar[JogOptSpace]  # value = <JogOptSpace.world: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class JointPosition(Finishable):
    """
    关节点位
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, joints: ...) -> None:
        """
        构造函数
        
        Args:
             joints (initializer_list[float]): 关节角度值, 单位：弧度
        """
    @typing.overload
    def __init__(self, joints: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        """
        构造函数
        
        Args:
             joints (list[float]): 轴角度
        """
    @typing.overload
    def __init__(self, n: typing.SupportsInt | typing.SupportsIndex, v: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
        """
        构造函数
        
        Args:
             n (int): 长度, 应和机型轴数匹配
             v (float, optional): 初始值，默认为0
        """
    @property
    def external(self) -> list[float]:
        """
        外部关节数值 单位:弧度|米。导轨单位米
        """
    @external.setter
    def external(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    @property
    def joints(self) -> list[float]:
        """
        关节角度值, 单位：弧度
        """
    @joints.setter
    def joints(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
class KeyPadState:
    """
    末端按键状态
    """
    def __init__(self) -> None:
        ...
    @property
    def key1_state(self) -> bool:
        """
        CR1号
        """
    @key1_state.setter
    def key1_state(self, arg0: bool) -> None:
        ...
    @property
    def key2_state(self) -> bool:
        """
        CR2号
        """
    @key2_state.setter
    def key2_state(self, arg0: bool) -> None:
        ...
    @property
    def key3_state(self) -> bool:
        """
        CR3号
        """
    @key3_state.setter
    def key3_state(self, arg0: bool) -> None:
        ...
    @property
    def key4_state(self) -> bool:
        """
        CR4号
        """
    @key4_state.setter
    def key4_state(self, arg0: bool) -> None:
        ...
    @property
    def key5_state(self) -> bool:
        """
        CR5号
        """
    @key5_state.setter
    def key5_state(self, arg0: bool) -> None:
        ...
    @property
    def key6_state(self) -> bool:
        """
        CR6号
        """
    @key6_state.setter
    def key6_state(self, arg0: bool) -> None:
        ...
    @property
    def key7_state(self) -> bool:
        """
        CR7号
        """
    @key7_state.setter
    def key7_state(self, arg0: bool) -> None:
        ...
class Load:
    """
    负载信息
    """
    def __init__(self, mass: typing.SupportsFloat | typing.SupportsIndex, cog: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], inertia: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        """
        构造函数
        
        Args:
             mass (float): 质量，单位：千克
             cog (array[3]): 质心 [x, y, z]，单位：米
             inertia (array[3]): 惯量 [ix, iy, iz]，单位：千克·平方米
        """
    @property
    def cog(self) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        质心 [x, y, z], 单位：米
        """
    @cog.setter
    def cog(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
    @property
    def inertia(self) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        惯量 [ix, iy, iz], 单位：千克·平方米
        """
    @inertia.setter
    def inertia(self, arg0: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> None:
        ...
    @property
    def mass(self) -> float:
        """
        负载质量, 单位：千克
        """
    @mass.setter
    def mass(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class LogInfo:
    """
    控制器日志信息
    """
    def __init__(self, id: typing.SupportsInt | typing.SupportsIndex, timestamp: str, content: str, repair: str) -> None:
        """
        构造函数
        
        Args:
             id (int): 日志ID号
             timestamp (str): 日期及时间
             content (str): 日志内容
             repair (str): 修复办法
        """
    @property
    def content(self) -> str:
        """
        日志内容
        """
    @property
    def id(self) -> int:
        """
        日志ID号
        """
    @property
    def repair(self) -> str:
        """
        修复办法
        """
    @property
    def timestamp(self) -> str:
        """
        日期及时间
        """
class LogInfoLevel:
    """
    控制器日志信息级别
    
    Members:
    
      info : 通知
    
      warning : 警告
    
      error : 错误
    """
    __members__: typing.ClassVar[dict[str, LogInfoLevel]]  # value = {'info': <LogInfoLevel.info: 0>, 'warning': <LogInfoLevel.warning: 1>, 'error': <LogInfoLevel.error: 2>}
    error: typing.ClassVar[LogInfoLevel]  # value = <LogInfoLevel.error: 2>
    info: typing.ClassVar[LogInfoLevel]  # value = <LogInfoLevel.info: 0>
    warning: typing.ClassVar[LogInfoLevel]  # value = <LogInfoLevel.warning: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MotionControlMode:
    """
    SDK运动控制模式
    
    Members:
    
      Idle : 空闲
    
      NrtCommandMode : 非实时模式执行运动指令
    
      NrtRLTask : 非实时模式运行RL工程
    
      RtCommandMode : 实时模式控制
    """
    Idle: typing.ClassVar[MotionControlMode]  # value = <MotionControlMode.Idle: 0>
    NrtCommandMode: typing.ClassVar[MotionControlMode]  # value = <MotionControlMode.NrtCommandMode: 1>
    NrtRLTask: typing.ClassVar[MotionControlMode]  # value = <MotionControlMode.NrtRLTask: 2>
    RtCommandMode: typing.ClassVar[MotionControlMode]  # value = <MotionControlMode.RtCommandMode: 3>
    __members__: typing.ClassVar[dict[str, MotionControlMode]]  # value = {'Idle': <MotionControlMode.Idle: 0>, 'NrtCommandMode': <MotionControlMode.NrtCommandMode: 1>, 'NrtRLTask': <MotionControlMode.NrtRLTask: 2>, 'RtCommandMode': <MotionControlMode.RtCommandMode: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MoveAbsJCommand(NrtCommand):
    """
    运动指令 - 轴运动MoveAbsJ
    """
    @typing.overload
    def __init__(self, target: JointPosition, speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (JointPosition): 目标关节点位
             speed (double, optional): 运行速度，默认使用默认速度
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @typing.overload
    def __init__(self, target: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (std::vector<double>): 目标关节点位
             speed (double, optional): 运行速度，默认使用默认速度
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @property
    def jointSpeed(self) -> float:
        """
        关节速度百分比，范围[0, 1]。大于等于0时生效；小于0时仍使用speed计算出的关节速度
        """
    @jointSpeed.setter
    def jointSpeed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def target(self) -> JointPosition:
        """
        目标关节点位
        """
    @target.setter
    def target(self, arg0: JointPosition) -> None:
        ...
class MoveCCommand(NrtCommand):
    """
    运动指令 - 圆弧轨迹MoveC
    """
    def __init__(self, target: CartesianPosition, aux: CartesianPosition, speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (CartesianPosition): 目标点
             aux (CartesianPosition): 辅助点
             speed (double, optional): 运行速度，默认使用默认速度
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @property
    def aux(self) -> CartesianPosition:
        """
        辅助点笛卡尔坐标
        """
    @aux.setter
    def aux(self, arg0: CartesianPosition) -> None:
        ...
    @property
    def auxOffset(self) -> CartesianPositionOffset:
        """
        辅助点偏移选项
        """
    @auxOffset.setter
    def auxOffset(self, arg0: CartesianPositionOffset) -> None:
        ...
    @property
    def rotSpeed(self) -> float:
        """
        空间旋转速度，单位rad/s。大于等于0时生效；小于0时旋转速度默认为200°/s
        """
    @rotSpeed.setter
    def rotSpeed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def target(self) -> CartesianPosition:
        """
        目标笛卡尔点位
        """
    @target.setter
    def target(self, arg0: CartesianPosition) -> None:
        ...
    @property
    def targetOffset(self) -> CartesianPositionOffset:
        """
        目标点偏移选项
        """
    @targetOffset.setter
    def targetOffset(self, arg0: CartesianPositionOffset) -> None:
        ...
class MoveCFCommand(NrtCommand):
    """
    运动指令 - 全圆轨迹MoveCF
    """
    def __init__(self, target: CartesianPosition, aux: CartesianPosition, angle: typing.SupportsFloat | typing.SupportsIndex, speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (CartesianPosition): 目标点
             aux (CartesianPosition): 辅助点
             angle (double): 执行角度，单位弧度
             speed (double, optional): 运行速度，默认使用默认速度
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @property
    def angle(self) -> float:
        """
        全圆执行角度，单位弧度
        """
    @angle.setter
    def angle(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def rotType(self) -> MoveCFCommandRotType:
        """
        全圆姿态旋转模式
        """
    @rotType.setter
    def rotType(self, arg0: MoveCFCommandRotType) -> None:
        ...
class MoveCFCommandRotType:
    """
    全圆轨迹MoveCF旋转类型
    
    Members:
    
      constPose : 不变姿态
    
      rotAxis : 动轴旋转
    
      fixedAxis : 定轴旋转
    """
    __members__: typing.ClassVar[dict[str, MoveCFCommandRotType]]  # value = {'constPose': <MoveCFCommandRotType.constPose: 0>, 'rotAxis': <MoveCFCommandRotType.rotAxis: 1>, 'fixedAxis': <MoveCFCommandRotType.fixedAxis: 2>}
    constPose: typing.ClassVar[MoveCFCommandRotType]  # value = <MoveCFCommandRotType.constPose: 0>
    fixedAxis: typing.ClassVar[MoveCFCommandRotType]  # value = <MoveCFCommandRotType.fixedAxis: 2>
    rotAxis: typing.ClassVar[MoveCFCommandRotType]  # value = <MoveCFCommandRotType.rotAxis: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MoveJCommand(NrtCommand):
    """
    运动指令 - 轴运动MoveJ
    """
    @typing.overload
    def __init__(self, target: CartesianPosition, speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (CartesianPosition): 目标笛卡尔点位
             speed (double, optional): 运行速度，默认使用默认速度
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @typing.overload
    def __init__(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @typing.overload
    def __init__(self, matrix: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @typing.overload
    def __init__(self, values: ..., speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @property
    def jointSpeed(self) -> float:
        """
        关节速度百分比，范围[0, 1]。大于等于0时生效；小于0时仍使用speed计算出的关节速度
        """
    @jointSpeed.setter
    def jointSpeed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def offset(self) -> CartesianPositionOffset:
        """
        偏移选项
        """
    @offset.setter
    def offset(self, arg0: CartesianPositionOffset) -> None:
        ...
    @property
    def target(self) -> CartesianPosition:
        """
        目标笛卡尔点位
        """
    @target.setter
    def target(self, arg0: CartesianPosition) -> None:
        ...
class MoveLCommand(NrtCommand):
    """
    运动指令 - 末端直线轨迹MoveL
    """
    @typing.overload
    def __init__(self, target: CartesianPosition, speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (CartesianPosition): 目标笛卡尔点位
             speed (double, optional): 速率，默认使用默认速率
             zone (double, optional): 转弯区，默认使用默认转弯区
        """
    @typing.overload
    def __init__(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @typing.overload
    def __init__(self, matrix: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @typing.overload
    def __init__(self, values: ..., speed: typing.SupportsFloat | typing.SupportsIndex = -1, zone: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        ...
    @property
    def offset(self) -> CartesianPositionOffset:
        """
        偏移选项
        """
    @offset.setter
    def offset(self, arg0: CartesianPositionOffset) -> None:
        ...
    @property
    def rotSpeed(self) -> float:
        """
        空间旋转速度，单位rad/s。大于等于0时生效；小于0时旋转速度默认为200°/s
        """
    @rotSpeed.setter
    def rotSpeed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def target(self) -> CartesianPosition:
        """
        目标笛卡尔点位
        """
    @target.setter
    def target(self, arg0: CartesianPosition) -> None:
        ...
class MoveSPCommand(NrtCommand):
    """
    运动指令 - 螺旋线轨迹MoveSP
    """
    def __init__(self, target: CartesianPosition, r0: typing.SupportsFloat | typing.SupportsIndex, rStep: typing.SupportsFloat | typing.SupportsIndex, angle: typing.SupportsFloat | typing.SupportsIndex, dir: bool, speed: typing.SupportsFloat | typing.SupportsIndex = -1) -> None:
        """
        构造函数
        
        Args:
             target (CartesianPosition): 终点姿态
             r0 (double): 初始半径，单位：米
             rStep (double): 每旋转单位角度，半径的变化，单位：米/弧度
             angle (double): 合计旋转角度，单位：弧度
             dir (bool): 旋转方向，true - 顺时针，false - 逆时针
             speed (double, optional): 运行速度，默认使用默认速度
        """
    @property
    def angle(self) -> float:
        """
        合计旋转角度，单位弧度
        """
    @angle.setter
    def angle(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def direction(self) -> bool:
        """
        旋转方向，true - 顺时针，false - 逆时针
        """
    @direction.setter
    def direction(self, arg0: bool) -> None:
        ...
    @property
    def radius(self) -> float:
        """
        初始半径，单位米
        """
    @radius.setter
    def radius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def radius_step(self) -> float:
        """
        每旋转单位角度，半径的变化，单位米/弧度
        """
    @radius_step.setter
    def radius_step(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def target(self) -> CartesianPosition:
        """
        终点笛卡尔点位，只使用点位的rpy来指定终点的姿态
        """
    @target.setter
    def target(self, arg0: CartesianPosition) -> None:
        ...
    @property
    def targetOffset(self) -> CartesianPositionOffset:
        """
        偏移选项
        """
    @targetOffset.setter
    def targetOffset(self, arg0: CartesianPositionOffset) -> None:
        ...
class MoveWaitCommand(NrtCommand):
    """
    运动停留指令。可插在两条运动指令之间，前一条运动到位后，等待一段时间，再执行下一条。该指令执行完不会有信息反馈
    """
    def __init__(self, duration: datetime.timedelta) -> None:
        """
        构造函数
        Args:
             duration (std::chrono::steady_clock::duration): 时长
        """
    @property
    def duration_(self) -> datetime.timedelta:
        """
        停留时长, 最小有效时长1ms
        """
    @duration_.setter
    def duration_(self, arg0: datetime.timedelta) -> None:
        ...
class NrtCommand:
    """
    非实时运动指令
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, speed: typing.SupportsFloat | typing.SupportsIndex, zone: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        构造函数
        
        Args:
             speed (double): 本条指令的速度，单位mm/s
             zone (double): 本条指令的转弯区大小，单位mm
        """
    @property
    def customInfo(self) -> str:
        """
        自定义信息，可在运动信息反馈中返回出来
        """
    @customInfo.setter
    def customInfo(self, arg0: str) -> None:
        ...
    @property
    def speed(self) -> float:
        """
        机器人末端最大线速度, 单位mm/s
        """
    @speed.setter
    def speed(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def zone(self) -> float:
        """
        转弯区半径大小，单位mm
        """
    @zone.setter
    def zone(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class OperateMode:
    """
    机器人操作模式
    
    Members:
    
      manual : 手动
    
      automatic : 自动
    
      unknown : 未知(发生异常)
    """
    __members__: typing.ClassVar[dict[str, OperateMode]]  # value = {'manual': <OperateMode.manual: 0>, 'automatic': <OperateMode.automatic: 1>, 'unknown': <OperateMode.unknown: -1>}
    automatic: typing.ClassVar[OperateMode]  # value = <OperateMode.automatic: 1>
    manual: typing.ClassVar[OperateMode]  # value = <OperateMode.manual: 0>
    unknown: typing.ClassVar[OperateMode]  # value = <OperateMode.unknown: -1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class OperationState:
    """
    机器人工作状态
    
    Members:
    
      idle : 机器人静止
    
      jog : jog状态(未运动)
    
      rtControlling : 实时模式控制中
    
      drag : 拖动已开启
    
      rlProgram : RL工程运行中
    
      demo : Demo演示中
    
      dynamicIdentify : 动力学辨识中
    
      frictionIdentify : 摩擦力辨识中
    
      loadIdentify : 负载辨识中
    
      moving : 机器人运动中
    
      jogging : Jog运动中
    
      unknown : 未知
    """
    __members__: typing.ClassVar[dict[str, OperationState]]  # value = {'idle': <OperationState.idle: 0>, 'jog': <OperationState.jog: 1>, 'rtControlling': <OperationState.rtControlling: 2>, 'drag': <OperationState.drag: 3>, 'rlProgram': <OperationState.rlProgram: 4>, 'demo': <OperationState.demo: 5>, 'dynamicIdentify': <OperationState.dynamicIdentify: 6>, 'frictionIdentify': <OperationState.frictionIdentify: 7>, 'loadIdentify': <OperationState.loadIdentify: 8>, 'moving': <OperationState.moving: 9>, 'jogging': <OperationState.jogging: 10>, 'unknown': <OperationState.unknown: -1>}
    demo: typing.ClassVar[OperationState]  # value = <OperationState.demo: 5>
    drag: typing.ClassVar[OperationState]  # value = <OperationState.drag: 3>
    dynamicIdentify: typing.ClassVar[OperationState]  # value = <OperationState.dynamicIdentify: 6>
    frictionIdentify: typing.ClassVar[OperationState]  # value = <OperationState.frictionIdentify: 7>
    idle: typing.ClassVar[OperationState]  # value = <OperationState.idle: 0>
    jog: typing.ClassVar[OperationState]  # value = <OperationState.jog: 1>
    jogging: typing.ClassVar[OperationState]  # value = <OperationState.jogging: 10>
    loadIdentify: typing.ClassVar[OperationState]  # value = <OperationState.loadIdentify: 8>
    moving: typing.ClassVar[OperationState]  # value = <OperationState.moving: 9>
    rlProgram: typing.ClassVar[OperationState]  # value = <OperationState.rlProgram: 4>
    rtControlling: typing.ClassVar[OperationState]  # value = <OperationState.rtControlling: 2>
    unknown: typing.ClassVar[OperationState]  # value = <OperationState.unknown: -1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PCB3Robot(IndustrialRobot_3):
    """
    PCB3轴机型
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str) -> None:
        ...
class PCB4Robot(IndustrialRobot_4):
    """
    PCB4轴机型
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str) -> None:
        ...
class PowerState:
    """
    机器人上下电及急停状态
    
    Members:
    
      on : 上电
    
      off : 下电
    
      estop : 急停被按下
    
      gstop : 安全门打开
    
      unknown : 未知(发生异常)
    """
    __members__: typing.ClassVar[dict[str, PowerState]]  # value = {'on': <PowerState.on: 0>, 'off': <PowerState.off: 1>, 'estop': <PowerState.estop: 2>, 'gstop': <PowerState.gstop: 3>, 'unknown': <PowerState.unknown: -1>}
    estop: typing.ClassVar[PowerState]  # value = <PowerState.estop: 2>
    gstop: typing.ClassVar[PowerState]  # value = <PowerState.gstop: 3>
    off: typing.ClassVar[PowerState]  # value = <PowerState.off: 1>
    on: typing.ClassVar[PowerState]  # value = <PowerState.on: 0>
    unknown: typing.ClassVar[PowerState]  # value = <PowerState.unknown: -1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PyErrorCode:
    """
    用于转换c++中的std::errorcode在python中使用
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: ...) -> None:
        ...
    def get(self) -> ...:
        ...
    def message(self) -> str:
        ...
    def value(self) -> int:
        ...
class PyForceControl5:
    """
    用于在python中使用力控类
    """
    def __init__(self, arg0: Cobot_5) -> None:
        ...
    def fcInit(self, frame_type: FrameType, ec: dict) -> None:
        """
        力控初始化
        
        Args:
            frame_type (FrameType): 力控坐标系,支持 'world', 'wobj', 'tool', 'base', 'flange'
            ec (dict): 错误码
        """
    def fcMonitor(self, enable: bool, ec: dict) -> None:
        """
        启动/关闭力控模块保护监控
        
        设置监控参数后,不立即生效,调用 fcMonitor(true) 后开始生效,并且一直保持,直到调用 fcMotion(false) 后结束
        结束后保护阈值恢复成默认值,即仍然会有保护效果,关闭监控后不再是用户设置的参数
        
        Args:
            enable (bool): true - 打开,false - 关闭
            ec (dict): 错误码输出
        """
    def fcStart(self, ec: dict) -> None:
        """
        开始力控,需在调用 fcInit() 后执行
        
        如果需要在力控模式下执行运动指令,可在调用 fcStart() 后执行
        注意,如果在调用 fcStart() 前使用 moveAppend() 下发了运动指令但未开始运动,那么这些运动指令将在调用 fcStart() 后执行
        
        Args:
            ec (dict): 错误码输出
        """
    def fcStop(self, ec: dict) -> None:
        """
        停止力控
        
        Args:
            ec (dict): 错误码输出
        """
    def getEndTorque(self, ref_type: FrameType, joint_torque_measured: PyTypeVectorDouble, external_torque_measured: PyTypeVectorDouble, cart_torque: PyTypeVectorDouble, cart_force: PyTypeVectorDouble, ec: dict) -> None:
        """
        获取当前力矩信息
                            
        Args:
            ref_type (FrameType): 力矩相对的参考系
                1) FrameType::world - 末端相对世界坐标系的力矩信息
                2) FrameType::flange - 末端相对于法兰盘的力矩信息
                3) FrameType::tool - 末端相对于TCP点的力矩信息
            joint_torque_measured (List[float]): 轴空间测量力信息,力传感器测量到的各轴所受力矩,单位Nm
            external_torque_measured (List[float]): 轴空间外部力信息,控制器根据机器人模型和测量力计算出的各轴所受力矩信息,单位Nm
            cart_torque (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力矩,单位Nm
            cart_force (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力,单位N
            ec (dict): 错误码输出
        """
    def pauseOverlay(self, ec: dict) -> None:
        """
        暂停搜索运动。需在调用 startOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def reset(self) -> None:
        ...
    def restartOverlay(self, ec: dict) -> None:
        """
        重新开启暂停的搜索运动。需在调用 pauseOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxVel(self, max_cart_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_cart_vel (List[float]): 范围 XYZ - [0, 3.0], 单位m/s, ABC - [0, 10.0], 单位rad/s, 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxWrench(self, max_wrench: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_wrench (List[float]): 依次为：XYZ [N], ABC [Nm], 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianDesiredForce(self, value: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔期望力/力矩。需在调用 fcStart() 后调用
                            
        Args:
            value (List[float]): X、Y、Z方向的笛卡尔期望力范围为 [-60, 60] N,笛卡尔期望力矩范围为 [-10, 10] Nm
            ec (dict): 错误码输出
        """
    def setCartesianMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下,机械臂末端相对基坐标系的最大速度
                            
        Args:
            velocity (List[float]): 依次为 X Y Z [m/s], A B C [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setCartesianNullspaceStiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置笛卡尔零空间阻抗刚度。需在调用 fcInit() 后调用生效
        
        Args:
            stiffness (float): 阻抗刚度,范围为 [0, 4],大于4会被自动设置为4,单位为 Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔阻抗刚度。需在调用 fcInit() 后调用生效
        
        各机型的最大刚度不同,请参考《xCore控制系统手册》 SetCartCtrlStiffVec 指令的说明
        
        Args:
            stiffness (List[float]): X、Y、Z方向的阻抗力刚度 [N/m] 和阻抗力矩刚度 [Nm/rad]
            ec (dict): 错误码输出
        """
    def setControlType(self, type: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置阻抗控制类型
        
        Args:
            type (int): 控制类型,0 - 关节阻抗 | 1 - 笛卡尔阻抗
            ec (dict): 错误码输出
        """
    def setFcGain(self, gain: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置各轴力控带宽。fcStart()开始生效, fcStop后失效。
                            
        Args:
            gain (List[float]): 各轴带宽, 范围 [0, 60], 各轴默认值20, 无单位
            ec (dict): 错误码输出
        """
    def setForceCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 N
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setFriction(self, fric: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置各轴摩擦力补偿系数。fcStart()开始生效, fcStop后失效。
                            
        Args:
            fric (List[float]): 补偿系数, 范围 [0, 1], 各轴默认值0.9, 无单位
            ec (dict): 错误码输出
        """
    def setJointControlMaxTorque(self, max_torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_torque (List[float]): 力限幅, 单位：Nm, 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointControlMaxVel(self, max_joint_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_joint_vel (List[float]): 关节速度最大值, 单位: rad/s, 范围 [0, 10.0], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置关节期望力矩。fcStart()之后可调用
                            
        Args:
            torque (List[float]): 力矩值,范围[-30,30],单位Nm
            ec (dict): 错误码输出
        """
    def setJointMaxEnergy(self, energy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动能
                            
        Args:
            energy (List[float]): 动能 [N·rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxMomentum(self, momentum: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动量
                            
        Args:
            momentum (List[float]): 动量 [N·s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置力控模式下的轴最大速度
                            
        Args:
            velocity (List[float]): 轴速度 [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置关节阻抗刚度。fcInit()之后调用生效
                            
        Args:
            stiffness (List[float]): 各轴刚度
            ec (dict): 错误码输出
        """
    def setLissajousOverlay(self, plane: typing.SupportsInt | typing.SupportsIndex, amplify_one: typing.SupportsFloat | typing.SupportsIndex, frequency_one: typing.SupportsFloat | typing.SupportsIndex, amplify_two: typing.SupportsFloat | typing.SupportsIndex, frequency_two: typing.SupportsFloat | typing.SupportsIndex, phase_diff: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置平面内的莉萨如搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        
        Args:
            plane (int): 搜索运动参考平面,0 - XY,1 - XZ,2 - YZ
            amplify_one (float): 搜索运动一方向幅值,范围为 [0, 20],单位为 Nm
            frequency_one (float): 搜索运动一方向频率,范围为 [0, 5],单位为 Hz
            amplify_two (float): 搜索运动二方向幅值,范围为 [0, 20],单位为 Nm
            frequency_two (float): 搜索运动二方向频率,范围为 [0, 5],单位为 Hz
            phase_diff (float): 搜索运动两个方向相位偏差,范围为 [0, PI],单位为弧度
            ec (dict): 错误码输出
        """
    def setLoad(self, load: Load, ec: dict) -> None:
        """
        设置力控模块使用的负载信息,需在调用 fcStart() 后调用
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setPoseBoxCondition(self, supervising_frame: Frame, box: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触位置有关的终止条件
                            
        Args:
            supervising_frame (Frame): 长方体所在的参考坐标系,相对于外部工件坐标系
                外部工件坐标系是通过 setToolset() 设置的 (Toolset::ref)
            box (List[float]): 定义一个长方体 { X_start, X_end, Y_start, Y_end, Z_start, Z_end },单位为米
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setSineOverlay(self, line_dir: typing.SupportsInt | typing.SupportsIndex, amplify: typing.SupportsFloat | typing.SupportsIndex, frequency: typing.SupportsFloat | typing.SupportsIndex, phase: typing.SupportsFloat | typing.SupportsIndex, bias: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置绕单轴旋转的正弦搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        各机型的搜索运动幅值上限和搜索运动频率上限不同,请参考《xCore控制系统手册》SetSineOverlay 指令的说明
        
        Args:
            line_dir (int): 搜索运动参考轴,0 - X,1 - Y,2 - Z
            amplify (float): 搜索运动幅值,单位为 Nm
            frequency (float): 搜索运动频率,单位为 Hz
            phase (float): 搜索运动相位,范围为 [0, PI],单位为弧度
            bias (float): 搜索运动偏置,范围为 [0, 10],单位为 Nm
            ec (dict): 错误码输出
        """
    def setTorqueCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力矩有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力矩限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 Nm
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def startOverlay(self, ec: dict) -> None:
        """
        开启搜索运动。需在调用 fcStart() 后调用生效
        
        搜索运动为前序设置的 setSineOverlay() 或 setLissajousOverlay() 的叠加
        
        Args:
            ec (dict): 错误码输出
        """
    def stopOverlay(self, ec: dict) -> None:
        """
        停止搜索运动
                            
        Args:
            ec (dict): 错误码输出
        """
    def waitCondition(self, ec: dict) -> None:
        """
        激活前序设置的终止条件并等待,直到满足这些条件或者超时
                            
        Args:
            ec (dict): 错误码输出
        """
class PyForceControl6:
    """
    用于在python中使用力控类
    """
    def __init__(self, arg0: Cobot_6) -> None:
        ...
    def fcInit(self, frame_type: FrameType, ec: dict) -> None:
        """
        力控初始化
        
        Args:
            frame_type (FrameType): 力控坐标系,支持 'world', 'wobj', 'tool', 'base', 'flange'
            ec (dict): 错误码
        """
    def fcMonitor(self, enable: bool, ec: dict) -> None:
        """
        启动/关闭力控模块保护监控
        
        设置监控参数后,不立即生效,调用 fcMonitor(true) 后开始生效,并且一直保持,直到调用 fcMotion(false) 后结束
        结束后保护阈值恢复成默认值,即仍然会有保护效果,关闭监控后不再是用户设置的参数
        
        Args:
            enable (bool): true - 打开,false - 关闭
            ec (dict): 错误码输出
        """
    def fcStart(self, ec: dict) -> None:
        """
        开始力控,需在调用 fcInit() 后执行
        
        如果需要在力控模式下执行运动指令,可在调用 fcStart() 后执行
        注意,如果在调用 fcStart() 前使用 moveAppend() 下发了运动指令但未开始运动,那么这些运动指令将在调用 fcStart() 后执行
        
        Args:
            ec (dict): 错误码输出
        """
    def fcStop(self, ec: dict) -> None:
        """
        停止力控
        
        Args:
            ec (dict): 错误码输出
        """
    def getEndTorque(self, ref_type: FrameType, joint_torque_measured: PyTypeVectorDouble, external_torque_measured: PyTypeVectorDouble, cart_torque: PyTypeVectorDouble, cart_force: PyTypeVectorDouble, ec: dict) -> None:
        """
        获取当前力矩信息
                            
        Args:
            ref_type (FrameType): 力矩相对的参考系
                1) FrameType::world - 末端相对世界坐标系的力矩信息
                2) FrameType::flange - 末端相对于法兰盘的力矩信息
                3) FrameType::tool - 末端相对于TCP点的力矩信息
            joint_torque_measured (List[float]): 轴空间测量力信息,力传感器测量到的各轴所受力矩,单位Nm
            external_torque_measured (List[float]): 轴空间外部力信息,控制器根据机器人模型和测量力计算出的各轴所受力矩信息,单位Nm
            cart_torque (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力矩,单位Nm
            cart_force (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力,单位N
            ec (dict): 错误码输出
        """
    def pauseOverlay(self, ec: dict) -> None:
        """
        暂停搜索运动。需在调用 startOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def reset(self) -> None:
        ...
    def restartOverlay(self, ec: dict) -> None:
        """
        重新开启暂停的搜索运动。需在调用 pauseOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxVel(self, max_cart_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_cart_vel (List[float]): 范围 XYZ - [0, 3.0], 单位m/s, ABC - [0, 10.0], 单位rad/s, 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxWrench(self, max_wrench: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_wrench (List[float]): 依次为：XYZ [N], ABC [Nm], 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianDesiredForce(self, value: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔期望力/力矩。需在调用 fcStart() 后调用
                            
        Args:
            value (List[float]): X、Y、Z方向的笛卡尔期望力范围为 [-60, 60] N,笛卡尔期望力矩范围为 [-10, 10] Nm
            ec (dict): 错误码输出
        """
    def setCartesianMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下,机械臂末端相对基坐标系的最大速度
                            
        Args:
            velocity (List[float]): 依次为 X Y Z [m/s], A B C [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setCartesianNullspaceStiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置笛卡尔零空间阻抗刚度。需在调用 fcInit() 后调用生效
        
        Args:
            stiffness (float): 阻抗刚度,范围为 [0, 4],大于4会被自动设置为4,单位为 Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔阻抗刚度。需在调用 fcInit() 后调用生效
        
        各机型的最大刚度不同,请参考《xCore控制系统手册》 SetCartCtrlStiffVec 指令的说明
        
        Args:
            stiffness (List[float]): X、Y、Z方向的阻抗力刚度 [N/m] 和阻抗力矩刚度 [Nm/rad]
            ec (dict): 错误码输出
        """
    def setControlType(self, type: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置阻抗控制类型
        
        Args:
            type (int): 控制类型,0 - 关节阻抗 | 1 - 笛卡尔阻抗
            ec (dict): 错误码输出
        """
    def setFcGain(self, gain: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置各轴力控带宽。fcStart()开始生效, fcStop后失效。
                            
        Args:
            gain (List[float]): 各轴带宽, 范围 [0, 60], 各轴默认值20, 无单位
            ec (dict): 错误码输出
        """
    def setForceCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 N
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setFriction(self, fric: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置各轴摩擦力补偿系数。fcStart()开始生效, fcStop后失效。
                            
        Args:
            fric (List[float]): 补偿系数, 范围 [0, 1], 各轴默认值0.9, 无单位
            ec (dict): 错误码输出
        """
    def setJointControlMaxTorque(self, max_torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_torque (List[float]): 力限幅, 单位：Nm, 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointControlMaxVel(self, max_joint_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_joint_vel (List[float]): 关节速度最大值, 单位: rad/s, 范围 [0, 10.0], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置关节期望力矩。fcStart()之后可调用
                            
        Args:
            torque (List[float]): 力矩值,范围[-30,30],单位Nm
            ec (dict): 错误码输出
        """
    def setJointMaxEnergy(self, energy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动能
                            
        Args:
            energy (List[float]): 动能 [N·rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxMomentum(self, momentum: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动量
                            
        Args:
            momentum (List[float]): 动量 [N·s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下的轴最大速度
                            
        Args:
            velocity (List[float]): 轴速度 [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置关节阻抗刚度。fcInit()之后调用生效
                            
        Args:
            stiffness (List[float]): 各轴刚度
            ec (dict): 错误码输出
        """
    def setLissajousOverlay(self, plane: typing.SupportsInt | typing.SupportsIndex, amplify_one: typing.SupportsFloat | typing.SupportsIndex, frequency_one: typing.SupportsFloat | typing.SupportsIndex, amplify_two: typing.SupportsFloat | typing.SupportsIndex, frequency_two: typing.SupportsFloat | typing.SupportsIndex, phase_diff: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置平面内的莉萨如搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        
        Args:
            plane (int): 搜索运动参考平面,0 - XY,1 - XZ,2 - YZ
            amplify_one (float): 搜索运动一方向幅值,范围为 [0, 20],单位为 Nm
            frequency_one (float): 搜索运动一方向频率,范围为 [0, 5],单位为 Hz
            amplify_two (float): 搜索运动二方向幅值,范围为 [0, 20],单位为 Nm
            frequency_two (float): 搜索运动二方向频率,范围为 [0, 5],单位为 Hz
            phase_diff (float): 搜索运动两个方向相位偏差,范围为 [0, PI],单位为弧度
            ec (dict): 错误码输出
        """
    def setLoad(self, load: Load, ec: dict) -> None:
        """
        设置力控模块使用的负载信息,需在调用 fcStart() 后调用
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setPoseBoxCondition(self, supervising_frame: Frame, box: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触位置有关的终止条件
                            
        Args:
            supervising_frame (Frame): 长方体所在的参考坐标系,相对于外部工件坐标系
                外部工件坐标系是通过 setToolset() 设置的 (Toolset::ref)
            box (List[float]): 定义一个长方体 { X_start, X_end, Y_start, Y_end, Z_start, Z_end },单位为米
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setSineOverlay(self, line_dir: typing.SupportsInt | typing.SupportsIndex, amplify: typing.SupportsFloat | typing.SupportsIndex, frequency: typing.SupportsFloat | typing.SupportsIndex, phase: typing.SupportsFloat | typing.SupportsIndex, bias: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置绕单轴旋转的正弦搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        各机型的搜索运动幅值上限和搜索运动频率上限不同,请参考《xCore控制系统手册》SetSineOverlay 指令的说明
        
        Args:
            line_dir (int): 搜索运动参考轴,0 - X,1 - Y,2 - Z
            amplify (float): 搜索运动幅值,单位为 Nm
            frequency (float): 搜索运动频率,单位为 Hz
            phase (float): 搜索运动相位,范围为 [0, PI],单位为弧度
            bias (float): 搜索运动偏置,范围为 [0, 10],单位为 Nm
            ec (dict): 错误码输出
        """
    def setTorqueCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力矩有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力矩限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 Nm
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def startOverlay(self, ec: dict) -> None:
        """
        开启搜索运动。需在调用 fcStart() 后调用生效
        
        搜索运动为前序设置的 setSineOverlay() 或 setLissajousOverlay() 的叠加
        
        Args:
            ec (dict): 错误码输出
        """
    def stopOverlay(self, ec: dict) -> None:
        """
        停止搜索运动
                            
        Args:
            ec (dict): 错误码输出
        """
    def waitCondition(self, ec: dict) -> None:
        """
        激活前序设置的终止条件并等待,直到满足这些条件或者超时
                            
        Args:
            ec (dict): 错误码输出
        """
class PyForceControl7:
    """
    用于在python中使用力控类
    """
    def __init__(self, arg0: Cobot_7) -> None:
        ...
    def fcInit(self, frame_type: FrameType, ec: dict) -> None:
        """
        力控初始化
        
        Args:
            frame_type (FrameType): 力控坐标系,支持 'world', 'wobj', 'tool', 'base', 'flange'
            ec (dict): 错误码
        """
    def fcMonitor(self, enable: bool, ec: dict) -> None:
        """
        启动/关闭力控模块保护监控
        
        设置监控参数后,不立即生效,调用 fcMonitor(true) 后开始生效,并且一直保持,直到调用 fcMotion(false) 后结束
        结束后保护阈值恢复成默认值,即仍然会有保护效果,关闭监控后不再是用户设置的参数
        
        Args:
            enable (bool): true - 打开,false - 关闭
            ec (dict): 错误码输出
        """
    def fcStart(self, ec: dict) -> None:
        """
        开始力控,需在调用 fcInit() 后执行
        
        如果需要在力控模式下执行运动指令,可在调用 fcStart() 后执行
        注意,如果在调用 fcStart() 前使用 moveAppend() 下发了运动指令但未开始运动,那么这些运动指令将在调用 fcStart() 后执行
        
        Args:
            ec (dict): 错误码输出
        """
    def fcStop(self, ec: dict) -> None:
        """
        停止力控
        
        Args:
            ec (dict): 错误码输出
        """
    def getEndTorque(self, ref_type: FrameType, joint_torque_measured: PyTypeVectorDouble, external_torque_measured: PyTypeVectorDouble, cart_torque: PyTypeVectorDouble, cart_force: PyTypeVectorDouble, ec: dict) -> None:
        """
        获取当前力矩信息
                            
        Args:
            ref_type (FrameType): 力矩相对的参考系
                1) FrameType::world - 末端相对世界坐标系的力矩信息
                2) FrameType::flange - 末端相对于法兰盘的力矩信息
                3) FrameType::tool - 末端相对于TCP点的力矩信息
            joint_torque_measured (List[float]): 轴空间测量力信息,力传感器测量到的各轴所受力矩,单位Nm
            external_torque_measured (List[float]): 轴空间外部力信息,控制器根据机器人模型和测量力计算出的各轴所受力矩信息,单位Nm
            cart_torque (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力矩,单位Nm
            cart_force (List[float]): 笛卡尔空间各个方向[X, Y, Z]受到的力,单位N
            ec (dict): 错误码输出
        """
    def pauseOverlay(self, ec: dict) -> None:
        """
        暂停搜索运动。需在调用 startOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def reset(self) -> None:
        ...
    def restartOverlay(self, ec: dict) -> None:
        """
        重新开启暂停的搜索运动。需在调用 pauseOverlay() 后调用生效
                            
        Args:
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxVel(self, max_cart_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_cart_vel (List[float]): 范围 XYZ - [0, 3.0], 单位m/s, ABC - [0, 10.0], 单位rad/s, 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianControlMaxWrench(self, max_wrench: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 笛卡尔。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_wrench (List[float]): 依次为：XYZ [N], ABC [Nm], 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setCartesianDesiredForce(self, value: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔期望力/力矩。需在调用 fcStart() 后调用
                            
        Args:
            value (List[float]): X、Y、Z方向的笛卡尔期望力范围为 [-60, 60] N,笛卡尔期望力矩范围为 [-10, 10] Nm
            ec (dict): 错误码输出
        """
    def setCartesianMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置力控模式下,机械臂末端相对基坐标系的最大速度
                            
        Args:
            velocity (List[float]): 依次为 X Y Z [m/s], A B C [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setCartesianNullspaceStiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置笛卡尔零空间阻抗刚度。需在调用 fcInit() 后调用生效
        
        Args:
            stiffness (float): 阻抗刚度,范围为 [0, 4],大于4会被自动设置为4,单位为 Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔阻抗刚度。需在调用 fcInit() 后调用生效
        
        各机型的最大刚度不同,请参考《xCore控制系统手册》 SetCartCtrlStiffVec 指令的说明
        
        Args:
            stiffness (List[float]): X、Y、Z方向的阻抗力刚度 [N/m] 和阻抗力矩刚度 [Nm/rad]
            ec (dict): 错误码输出
        """
    def setControlType(self, type: typing.SupportsInt | typing.SupportsIndex, ec: dict) -> None:
        """
        设置阻抗控制类型
        
        Args:
            type (int): 控制类型,0 - 关节阻抗 | 1 - 笛卡尔阻抗
            ec (dict): 错误码输出
        """
    def setFcGain(self, gain: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置各轴力控带宽。fcStart()开始生效, fcStop后失效。
                            
        Args:
            gain (List[float]): 各轴带宽, 范围 [0, 60], 各轴默认值20, 无单位
            ec (dict): 错误码输出
        """
    def setForceCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 N
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setFriction(self, fric: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置各轴摩擦力补偿系数。fcStart()开始生效, fcStop后失效。
                            
        Args:
            fric (List[float]): 补偿系数, 范围 [0, 1], 各轴默认值0.9, 无单位
            ec (dict): 错误码输出
        """
    def setJointControlMaxTorque(self, max_torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        阻抗力限幅指令 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            在部分力控装配场景，采用阻抗下运动，同时想限制末端出力，也起到一个末端力监控的作用。
        
        Args:
            max_torque (List[float]): 力限幅, 单位：Nm, 范围 [0, 1000], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointControlMaxVel(self, max_joint_vel: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        阻抗速度限幅 - 关节。fcStart()开始生效, fcStop后失效。
        
        Note:
            以加期望力下压直到接触这个场景为例，一般是设置期望力的方式来实现。此接口可对该接触过程做限速处理。
                            
        Args:
            max_joint_vel (List[float]): 关节速度最大值, 单位: rad/s, 范围 [0, 10.0], 默认设置最大值
            ec (dict): 错误码输出
        """
    def setJointDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置关节期望力矩。fcStart()之后可调用
                            
        Args:
            torque (List[float]): 力矩值,范围[-30,30],单位Nm
            ec (dict): 错误码输出
        """
    def setJointMaxEnergy(self, energy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动能
                            
        Args:
            energy (List[float]): 动能 [N·rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxMomentum(self, momentum: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置力控模式下轴最大动量
                            
        Args:
            momentum (List[float]): 动量 [N·s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointMaxVel(self, velocity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置力控模式下的轴最大速度
                            
        Args:
            velocity (List[float]): 轴速度 [rad/s],范围 >=0
            ec (dict): 错误码输出
        """
    def setJointStiffness(self, stiffness: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置关节阻抗刚度。fcInit()之后调用生效
                            
        Args:
            stiffness (List[float]): 各轴刚度
            ec (dict): 错误码输出
        """
    def setLissajousOverlay(self, plane: typing.SupportsInt | typing.SupportsIndex, amplify_one: typing.SupportsFloat | typing.SupportsIndex, frequency_one: typing.SupportsFloat | typing.SupportsIndex, amplify_two: typing.SupportsFloat | typing.SupportsIndex, frequency_two: typing.SupportsFloat | typing.SupportsIndex, phase_diff: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置平面内的莉萨如搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        
        Args:
            plane (int): 搜索运动参考平面,0 - XY,1 - XZ,2 - YZ
            amplify_one (float): 搜索运动一方向幅值,范围为 [0, 20],单位为 Nm
            frequency_one (float): 搜索运动一方向频率,范围为 [0, 5],单位为 Hz
            amplify_two (float): 搜索运动二方向幅值,范围为 [0, 20],单位为 Nm
            frequency_two (float): 搜索运动二方向频率,范围为 [0, 5],单位为 Hz
            phase_diff (float): 搜索运动两个方向相位偏差,范围为 [0, PI],单位为弧度
            ec (dict): 错误码输出
        """
    def setLoad(self, load: Load, ec: dict) -> None:
        """
        设置力控模块使用的负载信息,需在调用 fcStart() 后调用
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setPoseBoxCondition(self, supervising_frame: Frame, box: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触位置有关的终止条件
                            
        Args:
            supervising_frame (Frame): 长方体所在的参考坐标系,相对于外部工件坐标系
                外部工件坐标系是通过 setToolset() 设置的 (Toolset::ref)
            box (List[float]): 定义一个长方体 { X_start, X_end, Y_start, Y_end, Z_start, Z_end },单位为米
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def setSineOverlay(self, line_dir: typing.SupportsInt | typing.SupportsIndex, amplify: typing.SupportsFloat | typing.SupportsIndex, frequency: typing.SupportsFloat | typing.SupportsIndex, phase: typing.SupportsFloat | typing.SupportsIndex, bias: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置绕单轴旋转的正弦搜索运动
        
        在设置阻抗控制类型为笛卡尔阻抗（即调用 setControlType(1)）并在调用 startOverlay() 之前调用生效
        各机型的搜索运动幅值上限和搜索运动频率上限不同,请参考《xCore控制系统手册》SetSineOverlay 指令的说明
        
        Args:
            line_dir (int): 搜索运动参考轴,0 - X,1 - Y,2 - Z
            amplify (float): 搜索运动幅值,单位为 Nm
            frequency (float): 搜索运动频率,单位为 Hz
            phase (float): 搜索运动相位,范围为 [0, PI],单位为弧度
            bias (float): 搜索运动偏置,范围为 [0, 10],单位为 Nm
            ec (dict): 错误码输出
        """
    def setTorqueCondition(self, range: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], isInside: bool, timeout: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置与接触力矩有关的终止条件
                            
        Args:
            range (List[float]): 各方向上的力矩限制 { X_min, X_max, Y_min, Y_max, Z_min, Z_max },单位为 Nm
                设置下限时,负值表示负方向上的最大值;设置上限时,负值表示负方向上的最小值
            isInside (bool): true - 超出限制条件时停止等待;false - 符合限制条件时停止等待
            timeout (float): 超时时间,范围为 [1, 600] 秒
            ec (dict): 错误码输出
        """
    def startOverlay(self, ec: dict) -> None:
        """
        开启搜索运动。需在调用 fcStart() 后调用生效
        
        搜索运动为前序设置的 setSineOverlay() 或 setLissajousOverlay() 的叠加
        
        Args:
            ec (dict): 错误码输出
        """
    def stopOverlay(self, ec: dict) -> None:
        """
        停止搜索运动
                            
        Args:
            ec (dict): 错误码输出
        """
    def waitCondition(self, ec: dict) -> None:
        """
        激活前序设置的终止条件并等待,直到满足这些条件或者超时
                            
        Args:
            ec (dict): 错误码输出
        """
class PyString:
    """
    用于在python中使用的string类型可以在c++函数内更改
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str) -> None:
        ...
    def content(self) -> str:
        """
        获取string的值
        """
    def get(self) -> str:
        ...
class PyTypeBool:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: bool) -> None:
        ...
    def content(self) -> bool:
        """
        获取內部值
        """
    def get(self) -> bool:
        ...
class PyTypeDouble:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def content(self) -> float:
        """
        获取內部值
        """
    def get(self) -> float:
        ...
class PyTypeFloat:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def content(self) -> float:
        """
        获取內部值
        """
    def get(self) -> float:
        ...
class PyTypeInt:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def content(self) -> int:
        """
        获取內部值
        """
    def get(self) -> int:
        ...
class PyTypeUInt64:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def content(self) -> int:
        """
        获取內部值
        """
    def get(self) -> int:
        ...
class PyTypeUInt8:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def content(self) -> int:
        """
        获取內部值
        """
    def get(self) -> int:
        ...
class PyTypeVectorArrayDouble2:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]]) -> None:
        ...
    def content(self) -> list[typing.Annotated[list[float], "FixedSize(2)"]]:
        """
        获取內部值
        """
    def get(self) -> list[typing.Annotated[list[float], "FixedSize(2)"]]:
        ...
class PyTypeVectorBool:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[bool]) -> None:
        ...
    def content(self) -> list[bool]:
        """
        获取內部值
        """
    def get(self) -> list[bool]:
        ...
class PyTypeVectorDouble:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    def content(self) -> list[float]:
        """
        获取內部值
        """
    def get(self) -> list[float]:
        ...
class PyTypeVectorFloat:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    def content(self) -> list[float]:
        """
        获取內部值
        """
    def get(self) -> list[float]:
        ...
class PyTypeVectorInt:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    def content(self) -> list[int]:
        """
        获取內部值
        """
    def get(self) -> list[int]:
        ...
class PyTypeVectorString:
    """
    用于在python中使用的类型,包括bool,int,float,vector<bool>,vector<int>,vector<float>,vector<double>,vector<std::array<double, 2>>
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: collections.abc.Sequence[str]) -> None:
        ...
    def content(self) -> list[str]:
        """
        获取內部值
        """
    def get(self) -> list[str]:
        ...
class RLProjectInfo:
    """
    RL工程信息
    """
    def __init__(self, name: str) -> None:
        """
        构造函数
        
        Args:
             name (str): RL工程名
        """
    @property
    def name(self) -> str:
        """
        工程名称
        """
    @name.setter
    def name(self, arg0: str) -> None:
        ...
    @property
    def taskList(self) -> list[str]:
        """
        任务名称列表
        """
    @taskList.setter
    def taskList(self, arg0: collections.abc.Sequence[str]) -> None:
        ...
class Robot_T_Collaborative_5(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(5)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(5)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class Robot_T_Collaborative_6(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(6)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(6)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class Robot_T_Collaborative_7(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(7)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(7)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class Robot_T_Industrial_3(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(3)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(3)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class Robot_T_Industrial_4(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(4)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(4)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(4)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class Robot_T_Industrial_6(BaseRobot):
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, arg0: str, arg1: str) -> None:
        ...
    def calibrateFrame(self, type: FrameType, points: collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]], is_held: bool, ec: dict, base_aux: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"] = [0.0, 0.0, 0.0]) -> FrameCalibrationResult:
        """
        坐标系标定 (N点标定)
        
        Note:
             各坐标系类型支持的标定方法及注意事项：
             1) 工具坐标系: 三点/四点/六点标定法
             2) 工件坐标系: 三点标定。标定结果不会相对用户坐标系做变换,即,若为外部工件,返回的结果是相对于基坐标系的
             3) 基坐标系: 六点标定。标定前请确保动力学约束和前馈已关闭。若标定成功(无错误码),控制器会自动保存标定结果,重启控制器后生效
             4) 导轨基坐标系: 三点标定。若标定成功(无错误码)，控制器会自动保存标定结果，重启控制器后生效。
        
        Args:
             type (FrameType): 坐标系类型,支持工具(FrameType.tool), 工件(FrameType.wobj), 基坐标系(FrameType.base)
             points (List[List[float]]): 轴角度列表,列表长度为N。例如,使用三点法标定工具坐标系,应传入3组轴角度。轴角度的单位是弧度
             is_held (bool): true - 机器人手持 | false - 外部。仅影响工具/工件的标定
             ec (dict): 错误码
             base_aux (List[float], optional): 基坐标系标定时用到的辅助点, 单位[米]
        
        Returns:
             FrameCalibrationResult: 标定结果,当错误码没有被置位时,标定结果有效
        """
    @typing.overload
    def connectToRobot(self, ec: dict) -> None:
        """
        连接到机器人。机器人地址为创建robot实例时传入的
        
        Args:
             ec (dict): 错误码
        """
    @typing.overload
    def connectToRobot(self, remoteIP: str, localIP: str = '') -> None:
        """
        连接到机器人
        
        Args:
             remoteIP (str): 机器人IP地址
             localIP (str, optional): 本机地址。实时模式下收发交互数据用,可不设置;PCB3/4轴机型不支持
        
        Raises:
             NetworkException: 网络连接错误
             ExecutionException: 机器人实例与连接机型不符,或未授权SDK
        """
    def getSoftLimit(self, limits: PyTypeVectorArrayDouble2, ec: dict) -> bool:
        """
        获取当前软限位数值
        
        Args:
             limits (List[List[float]]): 各轴软限位 [下限, 上限],单位: 弧度
             ec (dict): 错误码
        
        Returns:
             bool: true - 已打开 | false - 已关闭
        """
    def jointTorque(self, ec: dict) -> typing.Annotated[list[float], "FixedSize(6)"]:
        """
        关节力传感器数值, 单位: $[Nm]$
        
        Args:
             ec (dict): 错误码
        
        Returns:
             List[float]: 长度: $\\mathbb{R}^{DoF \\times 1}$
        """
    def model(self) -> ...:
        """
        获取模型类
        
        Returns:
             Model6: Model类
        """
    def setSoftLimit(self, enable: bool, ec: dict, limits: typing.Annotated[collections.abc.Sequence[typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(2)"]], "FixedSize(6)"] = [[1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308], [1.7976931348623157e+308, 1.7976931348623157e+308]]) -> None:
        """
        设置软限位
        
        Note:
             1) 当limits为默认值时,视为仅打开软限位不修改数值;不为默认值时,先修改软限位再打开
             2) 关闭软限位时不会修改限位数值
        
        Args:
             enable (bool): true - 打开 | false - 关闭
             ec (dict): 错误码
             limits (List[List[float]], optional): 各轴 [下限, 上限],单位：弧度
        """
    def startReceiveRobotState(self, arg0: datetime.timedelta, arg1: collections.abc.Sequence[str]) -> None:
        """
        让机器人控制器开始发送实时状态数据。阻塞等待收到第一帧消息,超时时间为3秒
        
        Args:
             interval (datetime.timedelta): 控制器发送状态数据的间隔,允许的时长:1ms/2ms/4ms/8ms/1s
             fields (List[str]): 接收的机器人状态数据,最大总长度为1024个字节
        
        Raises:
             RealtimeControlException: 设置了不支持的状态数据;或机器人无法开始发送数据;或总长度超过1024
             RealtimeStateException: 已经开始发送数据;或超时后仍未收到第一帧数据
        """
class RtControllerMode:
    """
    控制器实时控制模式
    
    Members:
    
      jointPosition : 实时轴空间位置控制
    
      cartesianPosition : 实时笛卡尔空间位置控制
    
      jointImpedance : 实时轴空间阻抗控制
    
      cartesianImpedance : 实时笛卡尔空间阻抗控制
    
      torque : 实时力矩控制
    """
    __members__: typing.ClassVar[dict[str, RtControllerMode]]  # value = {'jointPosition': <RtControllerMode.jointPosition: 0>, 'cartesianPosition': <RtControllerMode.cartesianPosition: 1>, 'jointImpedance': <RtControllerMode.jointImpedance: 2>, 'cartesianImpedance': <RtControllerMode.cartesianImpedance: 3>, 'torque': <RtControllerMode.torque: 4>}
    cartesianImpedance: typing.ClassVar[RtControllerMode]  # value = <RtControllerMode.cartesianImpedance: 3>
    cartesianPosition: typing.ClassVar[RtControllerMode]  # value = <RtControllerMode.cartesianPosition: 1>
    jointImpedance: typing.ClassVar[RtControllerMode]  # value = <RtControllerMode.jointImpedance: 2>
    jointPosition: typing.ClassVar[RtControllerMode]  # value = <RtControllerMode.jointPosition: 0>
    torque: typing.ClassVar[RtControllerMode]  # value = <RtControllerMode.torque: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StandardRobot(IndustrialRobot_6):
    """
    标准工业6轴机型
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def disableCollisionDetection(self, ec: dict) -> None:
        """
        关闭碰撞检测功能。
        
        Args:
             ec (dict): 错误码。
        """
    def enableCollisionDetection(self, sensitivity: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], fallback: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置碰撞检测相关参数, 打开碰撞检测功能。工业机型只支持stop1(安全停止)。
        
        Args:
             sensitivity (list of float): 碰撞检测灵敏度,长度为6的数组,范围0.01-2.0。
             fallback (float): 碰撞后回退距离,单位米。
             ec (dict): 错误码。
        """
    def getAvoidSingularity(self, method: AvoidSingularityMethod, ec: dict) -> bool:
        """
        查询是否处于规避奇异点的状态。
        
        Args:
             method (AvoidSingularityMethod): 奇异规避的方式。
             ec (dict): 错误码。
        
        Returns:
             bool: true - 已打开。
        """
    def setAvoidSingularity(self, method: AvoidSingularityMethod, enable: bool, threshold: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        打开/关闭奇异点规避功能。
        
        Args:
             method (AvoidSingularityMethod): 奇异规避方式,三种方式都支持。
             enable (bool): true - 打开功能 | false - 关闭。
             threshold (double): 不同的规避方式,具体含义如下：
                  1) 牺牲姿态: 允许的姿态误差,范围 (0, PI*2],单位弧度。
                  2) 轴空间插补: 规避半径,范围 [0.005, 10],单位米。
                  3) 四轴锁定: 无参数。
        
             ec (dict): 错误码。
        """
class StopLevel:
    """
    机器人停止运动等级
    
    Members:
    
      stop0 : 快速停止机器人运动后断电
    
      stop1 : 规划停止机器人运动后断电, 停在原始路径上
    
      stop2 : 规划停止机器人运动后不断电, 停在原始路径上
    
      suppleStop : 柔顺停止，仅适用于协作机型
    """
    __members__: typing.ClassVar[dict[str, StopLevel]]  # value = {'stop0': <StopLevel.stop0: 0>, 'stop1': <StopLevel.stop1: 1>, 'stop2': <StopLevel.stop2: 2>, 'suppleStop': <StopLevel.suppleStop: 3>}
    stop0: typing.ClassVar[StopLevel]  # value = <StopLevel.stop0: 0>
    stop1: typing.ClassVar[StopLevel]  # value = <StopLevel.stop1: 1>
    stop2: typing.ClassVar[StopLevel]  # value = <StopLevel.stop2: 2>
    suppleStop: typing.ClassVar[StopLevel]  # value = <StopLevel.suppleStop: 3>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Toolset:
    """
    工具工件组信息，根据一对工具工件的坐标、负载、机器人手持设置计算得出
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, load: Load, end: Frame, ref: Frame) -> None:
        """
        构造函数
        
        Args:
             load (Load): 负载信息
             end (Frame): 末端坐标系
             ref (Frame): 参考坐标系
        """
    @property
    def end(self) -> Frame:
        """
        机器人末端坐标系相对法兰坐标系转换
        """
    @end.setter
    def end(self, arg0: Frame) -> None:
        ...
    @property
    def load(self) -> Load:
        """
        机器人末端手持负载
        """
    @load.setter
    def load(self, arg0: Load) -> None:
        ...
    @property
    def ref(self) -> Frame:
        """
        机器人参考坐标系相对世界坐标系转换
        """
    @ref.setter
    def ref(self, arg0: Frame) -> None:
        ...
class Torque(Finishable):
    """
    关节扭矩，不包含重力和摩擦力
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, tau: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        """
        构造函数
        
        Args:
             tau (list[float]): 力矩指令值，单位： Nm
        """
    @typing.overload
    def __init__(self, tau: ...) -> None:
        """
        构造函数
        
        Args:
             tau (initializer_list[float]): 力矩指令值，单位： Nm
        """
    @typing.overload
    def __init__(self, n: typing.SupportsInt | typing.SupportsIndex, v: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
        """
        构造函数
        
        Args:
             n (int): 长度, 应和机型轴数匹配
             v (float, optional): 初始值，默认为0
        """
    @property
    def tau(self) -> list[float]:
        """
        期望关节扭矩，单位： Nm
        """
    @tau.setter
    def tau(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
class WorkToolInfo:
    """
    工具/工件信息。工件的坐标系已相对其用户坐标系变换
    """
    @typing.overload
    def __init__(self) -> None:
        """
        默认构造函数
        """
    @typing.overload
    def __init__(self, name: str, isHeld: bool, posture: Frame, load: Load) -> None:
        """
        构造函数
        
        Args:
             name (str): 名称
             isHeld (bool): 是否机器人手持
             posture (Frame): 位姿
             load (Load): 负载
        """
    @property
    def alias(self) -> str:
        """
        描述
        """
    @alias.setter
    def alias(self, arg0: str) -> None:
        ...
    @property
    def load(self) -> Load:
        """
        负载
        """
    @load.setter
    def load(self, arg0: Load) -> None:
        ...
    @property
    def name(self) -> str:
        """
        名称
        """
    @name.setter
    def name(self, arg0: str) -> None:
        ...
    @property
    def pos(self) -> Frame:
        """
        位姿
        """
    @pos.setter
    def pos(self, arg0: Frame) -> None:
        ...
    @property
    def robotHeld(self) -> bool:
        """
        是否机器人手持
        """
    @robotHeld.setter
    def robotHeld(self, arg0: bool) -> None:
        ...
class WorkType:
    """
    机型类别
    
    Members:
    
      industrial : 工业机器人
    
      collaborative :  协作机器人
    """
    __members__: typing.ClassVar[dict[str, WorkType]]  # value = {'industrial': <WorkType.industrial: 0>, 'collaborative': <WorkType.collaborative: 1>}
    collaborative: typing.ClassVar[WorkType]  # value = <WorkType.collaborative: 1>
    industrial: typing.ClassVar[WorkType]  # value = <WorkType.industrial: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class xMateCr5Robot(Cobot_5):
    """
    5轴协作机器人, 包括 XMC17_5/XMC25_5
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def enableCompletePostureLerp(self, enable: bool, ec: dict) -> None:
        """
        是否使能平行基座模式
        
        Args:
             enable (bool): 使能，true: 开启，false: 关闭
             ec (dict): 错误码。
        """
class xMateErProRobot(Cobot_7):
    """
    7轴协作机器人, 包括 xMateER3 Pro / xMateER7 Pro
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
class xMateRobot(Cobot_6):
    """
    6轴协作机器人, 包括 xMateCR7/12, xMateSR3/4, xMateER3/7
    """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, remoteIP: str, localIP: str = '') -> None:
        ...
    def getAvoidSingularity(self, method: AvoidSingularityMethod, ec: dict) -> bool:
        """
        查询是否处于规避奇异点的状态。
        
        Args:
             method (AvoidSingularityMethod): 奇异规避的方式。
             ec (dict): 错误码。
        
        Returns:
             bool: true - 已打开。
        """
    def setAvoidSingularity(self, method: AvoidSingularityMethod, enable: bool, limit: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        打开/关闭奇异点规避功能。只适用于部分机型:
        
        1) 四轴锁定: 支持xMateCR和xMateSR机型;
        2) 牺牲姿态: 支持所有协作六轴机型;
        3) 轴空间插补: 不支持
        
        Args:
             method (AvoidSingularityMethod): 奇异规避方式。
             enable (bool): true - 打开功能 | false - 关闭;
                  对于四轴锁定方式, 打开之前要确保4轴处于零位。
             limit (double): 不同的规避方式,该参数含义分别为:
                  1) 牺牲姿态: 允许的姿态误差, 范围 (0, PI*2], 单位弧度
                  2) 四轴锁定: 无参数
             ec (dict): 错误码。
        """
class xPanelOptVout:
    """
    xPanel配置: 对外供电模式
    
    Members:
    
      off : 不输出
    
      reserve : 保留
    
      supply12v : 输出12V
    
      supply24v : 输出24V
    """
    __members__: typing.ClassVar[dict[str, xPanelOptVout]]  # value = {'off': <xPanelOptVout.off: 0>, 'reserve': <xPanelOptVout.reserve: 1>, 'supply12v': <xPanelOptVout.supply12v: 2>, 'supply24v': <xPanelOptVout.supply24v: 3>}
    off: typing.ClassVar[xPanelOptVout]  # value = <xPanelOptVout.off: 0>
    reserve: typing.ClassVar[xPanelOptVout]  # value = <xPanelOptVout.reserve: 1>
    supply12v: typing.ClassVar[xPanelOptVout]  # value = <xPanelOptVout.supply12v: 2>
    supply24v: typing.ClassVar[xPanelOptVout]  # value = <xPanelOptVout.supply24v: 3>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def createErrorCode() -> PyErrorCode:
    """
    创建一个空的PyErrorCode对象
    """
def message(arg0: dict) -> ...:
    """
    打印错误码信息
    """
Idle: MotionControlMode  # value = <MotionControlMode.Idle: 0>
NrtCommandMode: MotionControlMode  # value = <MotionControlMode.NrtCommandMode: 1>
NrtRLTask: MotionControlMode  # value = <MotionControlMode.NrtRLTask: 2>
RtCommandMode: MotionControlMode  # value = <MotionControlMode.RtCommandMode: 3>
automatic: OperateMode  # value = <OperateMode.automatic: 1>
base: FrameType  # value = <FrameType.base: 1>
baseFrame: JogOptSpace  # value = <JogOptSpace.baseFrame: 2>
baseParallelMode: JogOptSpace  # value = <JogOptSpace.baseParallelMode: 7>
cartesianImpedance: RtControllerMode  # value = <RtControllerMode.cartesianImpedance: 3>
cartesianPosition: RtControllerMode  # value = <RtControllerMode.cartesianPosition: 1>
cartesianSpace: DragParameterSpace  # value = <DragParameterSpace.cartesianSpace: 1>
collaborative: WorkType  # value = <WorkType.collaborative: 1>
constPose: MoveCFCommandRotType  # value = <MoveCFCommandRotType.constPose: 0>
demo: OperationState  # value = <OperationState.demo: 5>
drag: OperationState  # value = <OperationState.drag: 3>
dynamicIdentify: OperationState  # value = <OperationState.dynamicIdentify: 6>
endInRef: CoordinateType  # value = <CoordinateType.endInRef: 1>
error: LogInfoLevel  # value = <LogInfoLevel.error: 2>
estop: PowerState  # value = <PowerState.estop: 2>
fixedAxis: MoveCFCommandRotType  # value = <MoveCFCommandRotType.fixedAxis: 2>
flange: JogOptSpace  # value = <JogOptSpace.flange: 1>
flangeInBase: CoordinateType  # value = <CoordinateType.flangeInBase: 0>
freely: DragParameterType  # value = <DragParameterType.freely: 2>
frictionIdentify: OperationState  # value = <OperationState.frictionIdentify: 7>
gstop: PowerState  # value = <PowerState.gstop: 3>
idle: OperationState  # value = <OperationState.idle: 0>
industrial: WorkType  # value = <WorkType.industrial: 0>
info: LogInfoLevel  # value = <LogInfoLevel.info: 0>
jog: OperationState  # value = <OperationState.jog: 1>
jogging: OperationState  # value = <OperationState.jogging: 10>
jointImpedance: RtControllerMode  # value = <RtControllerMode.jointImpedance: 2>
jointPosition: RtControllerMode  # value = <RtControllerMode.jointPosition: 0>
jointSpace: JogOptSpace  # value = <JogOptSpace.jointSpace: 5>
jointWay: AvoidSingularityMethod  # value = <AvoidSingularityMethod.jointWay: 2>
loadIdentify: OperationState  # value = <OperationState.loadIdentify: 8>
lockAxis4: AvoidSingularityMethod  # value = <AvoidSingularityMethod.lockAxis4: 0>
logReporter: Event  # value = <Event.logReporter: 3>
manual: OperateMode  # value = <OperateMode.manual: 0>
moveExecution: Event  # value = <Event.moveExecution: 0>
moving: OperationState  # value = <OperationState.moving: 9>
none: CartesianPositionOffsetType  # value = <CartesianPositionOffsetType.none: 0>
off: xPanelOptVout  # value = <xPanelOptVout.off: 0>
offs: CartesianPositionOffsetType  # value = <CartesianPositionOffsetType.offs: 1>
on: PowerState  # value = <PowerState.on: 0>
path: FrameType  # value = <FrameType.path: 5>
rail: FrameType  # value = <FrameType.rail: 6>
relTool: CartesianPositionOffsetType  # value = <CartesianPositionOffsetType.relTool: 2>
reserve: xPanelOptVout  # value = <xPanelOptVout.reserve: 1>
rlExecution: Event  # value = <Event.rlExecution: 2>
rlProgram: OperationState  # value = <OperationState.rlProgram: 4>
rotAxis: MoveCFCommandRotType  # value = <MoveCFCommandRotType.rotAxis: 1>
rotationOnly: DragParameterType  # value = <DragParameterType.rotationOnly: 1>
rtControlling: OperationState  # value = <OperationState.rtControlling: 2>
safety: Event  # value = <Event.safety: 1>
singularityAvoidMode: JogOptSpace  # value = <JogOptSpace.singularityAvoidMode: 6>
stop0: StopLevel  # value = <StopLevel.stop0: 0>
stop1: StopLevel  # value = <StopLevel.stop1: 1>
stop2: StopLevel  # value = <StopLevel.stop2: 2>
suppleStop: StopLevel  # value = <StopLevel.suppleStop: 3>
supply12v: xPanelOptVout  # value = <xPanelOptVout.supply12v: 2>
supply24v: xPanelOptVout  # value = <xPanelOptVout.supply24v: 3>
tool: FrameType  # value = <FrameType.tool: 3>
toolFrame: JogOptSpace  # value = <JogOptSpace.toolFrame: 3>
torque: RtControllerMode  # value = <RtControllerMode.torque: 4>
translationOnly: DragParameterType  # value = <DragParameterType.translationOnly: 0>
unknown: PowerState  # value = <PowerState.unknown: -1>
warning: LogInfoLevel  # value = <LogInfoLevel.warning: 1>
wobj: FrameType  # value = <FrameType.wobj: 4>
wobjFrame: JogOptSpace  # value = <JogOptSpace.wobjFrame: 4>
world: JogOptSpace  # value = <JogOptSpace.world: 0>
wrist: AvoidSingularityMethod  # value = <AvoidSingularityMethod.wrist: 1>
