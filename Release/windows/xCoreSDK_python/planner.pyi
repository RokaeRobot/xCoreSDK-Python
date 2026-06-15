from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
import xCoreSDK_python
import xCoreSDK_python.model
__all__: list[str] = ['CartMotionGenerator', 'FollowPosition_5', 'FollowPosition_6', 'FollowPosition_7', 'JointMotionGenerator']
class CartMotionGenerator:
    """
    S速度规划的笛卡尔空间运动。
    
    Note:
        参考文献: Wisama Khalil and Etienne Dombre. 2002. Modeling, Identification and Control of Robots
        (Kogan Page Science Paper edition).
    """
    def __init__(self, speed_factor: float, s_goal: float) -> None:
        """
        根据路径总长度和速度系数生成一条笛卡尔空间平滑的轨迹
        
        Args:
            speed_factor (float): 速度系数，范围[0, 1]。最终的速度/加速度 = 最大速度/加速度 * 速度系数
            s_goal (float): 路径总长度 [m]
        """
    def calculateDesiredValues(self, t: float, delta_s_d: xCoreSDK_python.PyTypeDouble) -> bool:
        """
        计算时间t时的弧长s
        
        Args:
            t: 距开始规划的时间间隔，单位：秒
            delta_s_d: 计算结果
        
        Returns:
            false: 运动规划没有结束 | true: 运动规划结束
        """
    def calculateSynchronizedValues(self, s_init: float) -> None:
        """
        同步当前弧长
        
        Args:
            s_init: 初始弧长
        """
    def getTime(self) -> float:
        """
        获得总运动时间
        
        Returns:
            运动时间，单位：秒
        """
    def setMax(self, ds_max: float, dds_max_start: float, dds_max_end: float) -> None:
        """
        设置笛卡尔空间运动参数
        
        Args:
            ds_max (float): 最大速度 [m/s], 默认值1.0m/s。
            dds_max_start (float): 最大开始加速度 [m/s^2], 默认值2.5m/s2
            dds_max_end (float): 最大结束加速度 [m/s^2], 默认值2.5m/s2
        """
class FollowPosition_5:
    """
    点位跟随, 点位可以是笛卡尔位姿或轴角度，适用于视觉伺服跟随的使用场景
    """
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor. Call init() to setup Robot instance
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_5, model: xCoreSDK_python.model.xmateModel_1_5) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_5, model: xCoreSDK_python.model.xmateModel_1_5, endInFlange: list) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
            endInFlange: 末端相对于法兰的位姿
        """
    def init(self, robot: xCoreSDK_python.Cobot_5, model: xCoreSDK_python.model.xmateModel_1_5) -> None:
        """
        初始化FollowPosition
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    def setScale(self, scale: float) -> None:
        """
        置速度比例，可在目标跟随的过程中随时调整。
        
        Note:
            * 最终速度受最大值限制，目前数值不能更改。各轴速度最大值为: 120.0, 120.0, 180.0, 180.0, 200.0, 200.0, 200.0 [°/s]；
            * 各轴加速度最大值为500.0 [°/s^2]
        
        Args:
            scale: 速度比例，默认为0.5
        """
    @typing.overload
    def start(self, jnt_desire: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]) -> None:
        """
        开始目标跟随 - 轴角度。该接口非阻塞。
        
        Args:
            jnt_desire: 期望的轴角度.
        """
    @typing.overload
    def start(self, bMe_desire: list) -> None:
        """
        开始目标跟随 - 笛卡尔位姿。该接口非阻塞。
        
        Args:
            bMe_desire: 期望的目标位姿，为末端相对于基坐标系，即TCP位姿.
        """
    def stop(self) -> None:
        """
        停止目标跟随
        """
    @typing.overload
    def update(self, jnt_desired: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(5)]) -> None:
        """
        更新期望的目标轴角度
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            jnt_desired: 轴角度, 单位: 弧度.
        """
    @typing.overload
    def update(self, bMe_desire: list) -> None:
        """
        更新期望的位姿
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            bMe_desire: 末端相对于基坐标系，即TCP位姿.
        """
class FollowPosition_6:
    """
    点位跟随, 点位可以是笛卡尔位姿或轴角度，适用于视觉伺服跟随的使用场景
    """
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor. Call init() to setup Robot instance
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_6, model: xCoreSDK_python.model.xmateModel_1_6) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_6, model: xCoreSDK_python.model.xmateModel_1_6, endInFlange: list) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
            endInFlange: 末端相对于法兰的位姿
        """
    def init(self, robot: xCoreSDK_python.Cobot_6, model: xCoreSDK_python.model.xmateModel_1_6) -> None:
        """
        初始化FollowPosition
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    def setScale(self, scale: float) -> None:
        """
        置速度比例，可在目标跟随的过程中随时调整。
        
        Note:
            * 最终速度受最大值限制，目前数值不能更改。各轴速度最大值为: 120.0, 120.0, 180.0, 180.0, 200.0, 200.0, 200.0 [°/s]；
            * 各轴加速度最大值为500.0 [°/s^2]
        
        Args:
            scale: 速度比例，默认为0.5
        """
    @typing.overload
    def start(self, jnt_desire: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]) -> None:
        """
        开始目标跟随 - 轴角度。该接口非阻塞。
        
        Args:
            jnt_desire: 期望的轴角度.
        """
    @typing.overload
    def start(self, bMe_desire: list) -> None:
        """
        开始目标跟随 - 笛卡尔位姿。该接口非阻塞。
        
        Args:
            bMe_desire: 期望的目标位姿，为末端相对于基坐标系，即TCP位姿.
        """
    def stop(self) -> None:
        """
        停止目标跟随
        """
    @typing.overload
    def update(self, jnt_desired: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(6)]) -> None:
        """
        更新期望的目标轴角度
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            jnt_desired: 轴角度, 单位: 弧度.
        """
    @typing.overload
    def update(self, bMe_desire: list) -> None:
        """
        更新期望的位姿
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            bMe_desire: 末端相对于基坐标系，即TCP位姿.
        """
class FollowPosition_7:
    """
    点位跟随, 点位可以是笛卡尔位姿或轴角度，适用于视觉伺服跟随的使用场景
    """
    @typing.overload
    def __init__(self) -> None:
        """
        Default constructor. Call init() to setup Robot instance
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_7, model: xCoreSDK_python.model.xmateModel_1_7) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    @typing.overload
    def __init__(self, robot: xCoreSDK_python.Cobot_7, model: xCoreSDK_python.model.xmateModel_1_7, endInFlange: list) -> None:
        """
        constructor
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
            endInFlange: 末端相对于法兰的位姿
        """
    def init(self, robot: xCoreSDK_python.Cobot_7, model: xCoreSDK_python.model.xmateModel_1_7) -> None:
        """
        初始化FollowPosition
        
        Args:
            robot: rokae::Robot实例
            model: rokae::xMateModel实例, 通过robot.model()获取
        """
    def setScale(self, scale: float) -> None:
        """
        置速度比例，可在目标跟随的过程中随时调整。
        
        Note:
            * 最终速度受最大值限制，目前数值不能更改。各轴速度最大值为: 120.0, 120.0, 180.0, 180.0, 200.0, 200.0, 200.0 [°/s]；
            * 各轴加速度最大值为500.0 [°/s^2]
        
        Args:
            scale: 速度比例，默认为0.5
        """
    @typing.overload
    def start(self, jnt_desire: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        """
        开始目标跟随 - 轴角度。该接口非阻塞。
        
        Args:
            jnt_desire: 期望的轴角度.
        """
    @typing.overload
    def start(self, bMe_desire: list) -> None:
        """
        开始目标跟随 - 笛卡尔位姿。该接口非阻塞。
        
        Args:
            bMe_desire: 期望的目标位姿，为末端相对于基坐标系，即TCP位姿.
        """
    def stop(self) -> None:
        """
        停止目标跟随
        """
    @typing.overload
    def update(self, jnt_desired: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        """
        更新期望的目标轴角度
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            jnt_desired: 轴角度, 单位: 弧度.
        """
    @typing.overload
    def update(self, bMe_desire: list) -> None:
        """
        更新期望的位姿
        
        Note:
            跟随带有加减速过程，在接近目标点时减速，故更新的目标点不宜密集，更新频率不宜过快。更新间隔建议至少几十毫秒的量级
        
        Args:
            bMe_desire: 末端相对于基坐标系，即TCP位姿.
        """
class JointMotionGenerator:
    """
    S速度规划的关节空间运动。
    
    Note:
        参考文献: Wisama Khalil and Etienne Dombre. 2002. Modeling, Identification and Control of Robots
        (Kogan Page Science Paper edition).
    """
    def __init__(self, speed_factor: float, q_goal: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        """
        根据关节目标位置和速度系数生成一条轴空间轨迹，可用来回零或到达指定位置。
            
        Args:
            speed_factor (float): 速度系数，范围[0, 1]。最终的各轴速度/加速度 = 轴空间最大速度/加速度 * 速度系数
            q_goal (list[float]): 目标关节角度 [rad]
        """
    def calculateDesiredValues(self, t: float, delta_q_d: list) -> bool:
        """
        计算时间t时的关节角度增量
        
        Args:
            t: 时间点, 单位秒
            delta_q_d: 计算结果
        
        Returns:
            false: 运动规划没有结束 | true: 运动规划结束
        """
    def calculateSynchronizedValues(self, q_init: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        """
        同步当前关节角度
        
        Args:
            q_init: 初始关节角度
        """
    def getTime(self) -> float:
        """
        获得总运动时间
        
        Returns:
            运动时间，单位：秒
        """
    def setMax(self, dq_max: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], ddq_max_start: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)], ddq_max_end: typing.Annotated[list[float], pybind11_stubgen.typing_ext.FixedSize(7)]) -> None:
        """
        设置轴空间S速度规划的运动参数
        
        Args:
            ds_max (list[float]): 最大速度 [rad/s], 默认值J1~J4 1.0rad/s, J5~J7 1.25rad/s
            dds_max_start (list[float]): 最大开始加速度 [rad/s^2], 默认值2.5rad/s^2
            dds_max_end (list[float]): 最大结束加速度 [rad/s^2], 默认值2.5rad/s^2
        """
