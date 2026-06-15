from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
import xCoreSDK_python
__all__: list[str] = ['Model_0_3', 'Model_0_4', 'Model_0_6', 'Model_1_5', 'Model_1_6', 'Model_1_7', 'SegmentFrame', 'TorqueType', 'xmateModel_1_5', 'xmateModel_1_6', 'xmateModel_1_7']
class Model_0_3:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Industrial_3) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class Model_0_4:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Industrial_4) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(4)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class Model_0_6:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Industrial_6) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class Model_1_5:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Collaborative_5) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class Model_1_6:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Collaborative_6) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class Model_1_7:
    """
    用于在python中使用model类
    """
    def __init__(self, arg0: xCoreSDK_python.Robot_T_Collaborative_7) -> None:
        ...
    def calcAllIkSolutions(self, posture: xCoreSDK_python.CartesianPosition, confs: list, ec: dict) -> list[list[float]]:
        """
        计算笛卡尔位姿所有逆解结果。支持除xMateSR(XMS)之外的所有机型
        
        Args:
            posture (CartesianPosition): 笛卡尔位姿，法兰相对与基座标系。其它坐标系需自行转换。
            confs (list[list[int]]): 对应的confdata，错误码为0时有效
            ec (dict): 错误码，含逆解计算失败错误：-50102奇异点 | -50114 超限位 | -50519 超范围 | -50002 其它逆解错误
        
        Returns:
            逆解结果 (list[list[float]]): 单位弧度，错误码为0时有效
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcFk(self, joints: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], toolset: xCoreSDK_python.Toolset, ec: dict) -> xCoreSDK_python.CartesianPosition:
        """
        根据轴角度计算正解
        
        Args:
            joints (list[float]): 轴角度列表，单位：弧度
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            CartesianPosition: 机器人末端位姿，相对于外部参考坐标系
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
    @typing.overload
    def calcIk(self, posture: xCoreSDK_python.CartesianPosition, toolset: xCoreSDK_python.Toolset, ec: dict) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]:
        """
        根据位姿计算逆解
        
        Args:
            posture (CartesianPosition): 机器人末端位姿，相对于外部参考坐标系
            toolset (Toolset): 工具工件坐标系设置
            ec (dict): 错误码
        
        Returns:
            list[float]: 轴角度，单位弧度
        """
class SegmentFrame:
    """
    连杆标号
    
    Members:
    
      joint1
    
      joint2
    
      joint3
    
      joint4
    
      joint5
    
      joint6
    
      joint7
    
      flange
    
      endEffector
    
      stiffness
    """
    __members__: typing.ClassVar[dict[str, SegmentFrame]]  # value = {'joint1': <SegmentFrame.joint1: 1>, 'joint2': <SegmentFrame.joint2: 2>, 'joint3': <SegmentFrame.joint3: 3>, 'joint4': <SegmentFrame.joint4: 4>, 'joint5': <SegmentFrame.joint5: 5>, 'joint6': <SegmentFrame.joint6: 6>, 'joint7': <SegmentFrame.joint7: 7>, 'flange': <SegmentFrame.flange: 8>, 'endEffector': <SegmentFrame.endEffector: 9>, 'stiffness': <SegmentFrame.stiffness: 10>}
    endEffector: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.endEffector: 9>
    flange: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.flange: 8>
    joint1: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint1: 1>
    joint2: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint2: 2>
    joint3: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint3: 3>
    joint4: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint4: 4>
    joint5: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint5: 5>
    joint6: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint6: 6>
    joint7: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.joint7: 7>
    stiffness: typing.ClassVar[SegmentFrame]  # value = <SegmentFrame.stiffness: 10>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TorqueType:
    """
    力矩类型
    
    Members:
    
      full : 关节力矩，由动力学模型计算得到
    
      inertia : 惯性力
    
      coriolis :  科氏力
    
      friction : 摩擦力
    
      gravity : 重力
    """
    __members__: typing.ClassVar[dict[str, TorqueType]]  # value = {'full': <TorqueType.full: 0>, 'inertia': <TorqueType.inertia: 1>, 'coriolis': <TorqueType.coriolis: 2>, 'friction': <TorqueType.friction: 3>, 'gravity': <TorqueType.gravity: 4>}
    coriolis: typing.ClassVar[TorqueType]  # value = <TorqueType.coriolis: 2>
    friction: typing.ClassVar[TorqueType]  # value = <TorqueType.friction: 3>
    full: typing.ClassVar[TorqueType]  # value = <TorqueType.full: 0>
    gravity: typing.ClassVar[TorqueType]  # value = <TorqueType.gravity: 4>
    inertia: typing.ClassVar[TorqueType]  # value = <TorqueType.inertia: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class xmateModel_1_5(Model_1_5):
    """
    xMate模型库。支持的机型: xMateER系列, XMC7/12/18/20, XMS3/4
    """
    def __init__(self, arg0: xCoreSDK_python.Cobot_5) -> None:
        ...
    def getCartAcc(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间加速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            jntAcc: 需要计算笛卡尔空间速度的关节角加速度
            nr: 指定坐标系
        
        Returns:
            计算结果
        """
    def getCartPose(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        获取笛卡尔空间位置
        
        Args:
            jntPos: 需要计算笛卡尔位姿的关节角度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            向量化4x4位姿矩阵，行优先.
        """
    def getCartVel(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            计算结果
        """
    def getJointAcc(self, cartAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        逆解获得关节空间加速度
        
        Args:
            cartAcc: 法兰笛卡尔空间加速度
            jntPos: 此时关节角度
            jntVel: 此时关节角速度
        
        Returns:
            计算结果
        """
    def getJointPos(self, cartPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], elbow: float, jntInit: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntPos: list) -> int:
        """
        逆解获得关节空间位置。一个位姿可能对应多个关节角度，jntPos的选取原则是选取一个与jntInit最近的解。
            
        Args:
            cartPos: 法兰笛卡尔空间位姿
            elbow: 臂角
            jntInit: 初始关节角度
            jntPos: 关节空间位置
        
        Returns:
            计算逆解结果 -
                1) -1, -2, -3: 无解，原因是cartPos超出机器人工作空间;
                2) -4, -5: jntPos与jntInit相差较大，一般认为jntInit代表机器人当前位置，jntPos与jntInit之差可以等效为电机转速。
                若超过机器人轴额定转速，则返回-4或-5;
                3) -6, -7: jntPos超过软限位;
                4)	-8: 机器人奇异；
        """
    def getJointVel(self, cartVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]:
        """
        逆解获得关节空间速度
        
        Args:
            cartVel: 法兰笛卡尔空间速度
            jntPos: 此时关节角度
        
        Returns:
            计算结果
        """
    def getTorqueNoFriction(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], trq_full: list, trq_inertia: list, trq_coriolis: list, trq_gravity: list) -> None:
        """
        由模型计算无摩擦力的关节力矩, 计算结果单位: Nm。如有负载，先通过setLoad()设置负载参数。
        
        Args:
            jntPos: 关节角度
            jntVel: 关节角速度
            jntAcc: 关节角加速度
            trq_full: 总关节力矩
            trq_inertia: 离心力
            trq_coriolis: 科氏力
            trq_gravity: 重力矩
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(30)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)], f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(30)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            f_t_ee: 末端执行器相对于法兰坐标系的位姿.
            ee_t_k: 刚度坐标系相对于末端执行器的位姿.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    def setLoad(self, mass: float, cog: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], inertia: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        设置负载参数，只在计算时使用，并不将参数传给机器人控制器，设置后动力学计算结果相应改变
        
        Args:
            mass: 质量
            cog: 质心, 单位: m
            inertia: 惯量
        """
    def setTcpCoor(self, f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]) -> None:
        """
        设置TCP工具，只在计算时使用，并不将参数传给机器人控制器，设置TCP后，正逆解结果和输入参数相应改变
        
        Args:
            f_t_ee: 末端执行器相对于法兰的位姿
            ee_t_k: 刚度坐标系相对于末端执行器的位姿
        """
class xmateModel_1_6(Model_1_6):
    """
    xMate模型库。支持的机型: xMateER系列, XMC7/12/18/20, XMS3/4
    """
    def __init__(self, arg0: xCoreSDK_python.Cobot_6) -> None:
        ...
    def getCartAcc(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间加速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            jntAcc: 需要计算笛卡尔空间速度的关节角加速度
            nr: 指定坐标系
        
        Returns:
            计算结果
        """
    def getCartPose(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        获取笛卡尔空间位置
        
        Args:
            jntPos: 需要计算笛卡尔位姿的关节角度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            向量化4x4位姿矩阵，行优先.
        """
    def getCartVel(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            计算结果
        """
    def getJointAcc(self, cartAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        逆解获得关节空间加速度
        
        Args:
            cartAcc: 法兰笛卡尔空间加速度
            jntPos: 此时关节角度
            jntVel: 此时关节角速度
        
        Returns:
            计算结果
        """
    def getJointPos(self, cartPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], elbow: float, jntInit: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: list) -> int:
        """
        逆解获得关节空间位置。一个位姿可能对应多个关节角度，jntPos的选取原则是选取一个与jntInit最近的解。
            
        Args:
            cartPos: 法兰笛卡尔空间位姿
            elbow: 臂角
            jntInit: 初始关节角度
            jntPos: 关节空间位置
        
        Returns:
            计算逆解结果 -
                1) -1, -2, -3: 无解，原因是cartPos超出机器人工作空间;
                2) -4, -5: jntPos与jntInit相差较大，一般认为jntInit代表机器人当前位置，jntPos与jntInit之差可以等效为电机转速。
                若超过机器人轴额定转速，则返回-4或-5;
                3) -6, -7: jntPos超过软限位;
                4)	-8: 机器人奇异；
        """
    def getJointVel(self, cartVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        逆解获得关节空间速度
        
        Args:
            cartVel: 法兰笛卡尔空间速度
            jntPos: 此时关节角度
        
        Returns:
            计算结果
        """
    def getTorqueNoFriction(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], trq_full: list, trq_inertia: list, trq_coriolis: list, trq_gravity: list) -> None:
        """
        由模型计算无摩擦力的关节力矩, 计算结果单位: Nm。如有负载，先通过setLoad()设置负载参数。
        
        Args:
            jntPos: 关节角度
            jntVel: 关节角速度
            jntAcc: 关节角加速度
            trq_full: 总关节力矩
            trq_inertia: 离心力
            trq_coriolis: 科氏力
            trq_gravity: 重力矩
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(36)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(36)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            f_t_ee: 末端执行器相对于法兰坐标系的位姿.
            ee_t_k: 刚度坐标系相对于末端执行器的位姿.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    def setLoad(self, mass: float, cog: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], inertia: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        设置负载参数，只在计算时使用，并不将参数传给机器人控制器，设置后动力学计算结果相应改变
        
        Args:
            mass: 质量
            cog: 质心, 单位: m
            inertia: 惯量
        """
    def setTcpCoor(self, f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]) -> None:
        """
        设置TCP工具，只在计算时使用，并不将参数传给机器人控制器，设置TCP后，正逆解结果和输入参数相应改变
        
        Args:
            f_t_ee: 末端执行器相对于法兰的位姿
            ee_t_k: 刚度坐标系相对于末端执行器的位姿
        """
class xmateModel_1_7(Model_1_7):
    """
    xMate模型库。支持的机型: xMateER系列, XMC7/12/18/20, XMS3/4
    """
    def __init__(self, arg0: xCoreSDK_python.Cobot_7) -> None:
        ...
    def getCartAcc(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间加速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            jntAcc: 需要计算笛卡尔空间速度的关节角加速度
            nr: 指定坐标系
        
        Returns:
            计算结果
        """
    def getCartPose(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]:
        """
        获取笛卡尔空间位置
        
        Args:
            jntPos: 需要计算笛卡尔位姿的关节角度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            向量化4x4位姿矩阵，行优先.
        """
    def getCartVel(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]:
        """
        获取笛卡尔空间速度
        
        Args:
            jntPos: 需要计算笛卡尔空间速度的关节角度
            jntVel: 需要计算笛卡尔空间速度的关节角速度
            nr: 指定坐标系, 缺省值为flange
        
        Returns:
            计算结果
        """
    def getJointAcc(self, cartAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]:
        """
        逆解获得关节空间加速度
        
        Args:
            cartAcc: 法兰笛卡尔空间加速度
            jntPos: 此时关节角度
            jntVel: 此时关节角速度
        
        Returns:
            计算结果
        """
    def getJointPos(self, cartPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], elbow: float, jntInit: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntPos: list) -> int:
        """
        逆解获得关节空间位置。一个位姿可能对应多个关节角度，jntPos的选取原则是选取一个与jntInit最近的解。
            
        Args:
            cartPos: 法兰笛卡尔空间位姿
            elbow: 臂角
            jntInit: 初始关节角度
            jntPos: 关节空间位置
        
        Returns:
            计算逆解结果 -
                1) -1, -2, -3: 无解，原因是cartPos超出机器人工作空间;
                2) -4, -5: jntPos与jntInit相差较大，一般认为jntInit代表机器人当前位置，jntPos与jntInit之差可以等效为电机转速。
                若超过机器人轴额定转速，则返回-4或-5;
                3) -6, -7: jntPos超过软限位;
                4)	-8: 机器人奇异；
        """
    def getJointVel(self, cartVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)], jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]:
        """
        逆解获得关节空间速度
        
        Args:
            cartVel: 法兰笛卡尔空间速度
            jntPos: 此时关节角度
        
        Returns:
            计算结果
        """
    def getTorqueNoFriction(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntVel: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], jntAcc: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], trq_full: list, trq_inertia: list, trq_coriolis: list, trq_gravity: list) -> None:
        """
        由模型计算无摩擦力的关节力矩, 计算结果单位: Nm。如有负载，先通过setLoad()设置负载参数。
        
        Args:
            jntPos: 关节角度
            jntVel: 关节角速度
            jntAcc: 关节角加速度
            trq_full: 总关节力矩
            trq_inertia: 离心力
            trq_coriolis: 科氏力
            trq_gravity: 重力矩
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(42)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    @typing.overload
    def jacobian(self, jntPos: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], nr: SegmentFrame = ...) -> typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(42)]:
        """
        获取指定坐标系相对于基坐标系的雅克比矩阵, 行优先
            
        Args:
            jntPos: 关节角度.
            f_t_ee: 末端执行器相对于法兰坐标系的位姿.
            ee_t_k: 刚度坐标系相对于末端执行器的位姿.
            nr: 指定坐标系
        
        Returns:
            计算结果, 长度 \\f$ \\mathbb{R}^{6 \\times DoF} \\f$
        """
    def setLoad(self, mass: float, cog: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)], inertia: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(3)]) -> None:
        """
        设置负载参数，只在计算时使用，并不将参数传给机器人控制器，设置后动力学计算结果相应改变
        
        Args:
            mass: 质量
            cog: 质心, 单位: m
            inertia: 惯量
        """
    def setTcpCoor(self, f_t_ee: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)], ee_t_k: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(16)]) -> None:
        """
        设置TCP工具，只在计算时使用，并不将参数传给机器人控制器，设置TCP后，正逆解结果和输入参数相应改变
        
        Args:
            f_t_ee: 末端执行器相对于法兰的位姿
            ee_t_k: 刚度坐标系相对于末端执行器的位姿
        """
