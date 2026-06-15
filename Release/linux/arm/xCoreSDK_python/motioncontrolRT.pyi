from __future__ import annotations
import collections.abc
import typing
import xCoreSDK_python
__all__: list[str] = ['PyRTmotioncontrol5', 'PyRTmotioncontrol6', 'PyRTmotioncontrol7']
class PyRTmotioncontrol5:
    """
    用于在python中使用实时接口
    """
    def MoveC(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, aux: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveC指令，在到达target之前处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveCCommand。
        
        Args:
            speed: 速度比例系数
            start: 机器人起始位姿, 需要是机器人当前位姿。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            aux: 机器人辅助点位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
            target: 机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        
        Raises:
            RealtimeParameterException: 点位错误, 无法计算出圆弧路径
            RealtimeMotionException: 机器人运动过程中发生错误
        """
    def MoveJ(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], target: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"]) -> None:
        """
        MoveJ指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveAbsJCommand。
        
        Args:
            speed (double): 速度比例系数
            start (List[double]): 起始关节角度，需要是机器人当前关节角度，否则可能造成下电。
            target (List[double])   机器人目标关节角度
        """
    def MoveL(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveL指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveLCommand。
        
        Args:
            speed (double): 速度比例系数, 范围 0 - 1
            start (CartesianPosition): 起始位姿, 需要是机器人当前位姿，否则可能造成下电。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            target (CartesianPosition)   机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        """
    def __init__(self, arg0: xCoreSDK_python.Cobot_5) -> None:
        ...
    def automaticErrorRecovery(self, ec: dict) -> None:
        """
        当错误发生后，自动恢复机器人。
        
        Args:
            ec (dict): 错误码输出
        """
    def disconnectNetwork(self) -> None:
        """
        断开与实时控制服务器的连接, 关闭数据接收和指令发送端口。不会断开和机器人的连接。
            
        Note:
            若机器人在运动，断开后会立即停止运动
        """
    def hasMotionError(self) -> bool:
        """
        实时模式运动是否发生了运动错误
        
        Returns:
            bool: true - 有报错
        """
    def reconnectNetwork(self, ec: dict) -> None:
        """
        重新连接到实时控制服务器
        
        Args:
            ec (dict): 错误码输出
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.JointPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.CartesianPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.Torque) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    def setCartesianImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔空间阻抗控制系数, 笛卡尔阻抗运动时生效。
        
        Args:
            factor (List[double]): 阻抗系数[ X, Y, Z, Rx, Ry, Rz], 最大值为 { 3000, 3000, 3000, 300, 300, 300 }, 单位: N/m, Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianImpedanceDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置末端期望力, 在笛卡尔空间阻抗运动时生效。
        
        Args:
            torque (List[double]): 笛卡尔空间末端期望力, 允许的范围为 { ±60, ±60, ±60, ±30, ±30, ±30 }, 单位: N, N·m
            ec (dict): 错误码输出
        """
    def setCartesianLimit(self, lengths: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置笛卡尔空间运动区域，超过设置区域运动会停止。
        
        非力控虚拟墙。若机器人末端或TCP末端超过安全区域，电机同样会做下电处理。
        
        Args:
            lengths (List[double]): 安全区域长方体长宽高，对应XYZ, 单位: 米
            frame (List[double]): 安全区域长方体中心相对于基坐标系位姿（齐次矩阵）
            ec (dict): 错误码输出
        """
    def setCollisionBehaviour(self, torqueThresholds: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置碰撞检测阈值。
        
        碰撞检测只在位置控制时生效，力控时不生效。若检测到碰撞，控制器会下发下电指令，电机抱闸吸合下使能。
        
        Args:
            torqueThresholds (List[double]): 关节碰撞检测阈值, 单位N
            ec (dict): 错误码输出
        """
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    def setControlLoopCar(self, callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopJoi(self, callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopTor(self, callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setEndEffectorFrame(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置末端执行器相对于机器人法兰的位姿，设置TCP后控制器会保存配置，机器人重启后恢复默认设置。
        
        Args:
            frame (List[double]): 末端执行器坐标系相对于法兰坐标系的齐次矩阵，单位: rad, m
            ec (dict): 错误码输出
        """
    def setFcCoor(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], type: xCoreSDK_python.FrameType, ec: dict) -> None:
        """
        设置机器人力控坐标系。
        
        Args:
            frame (List[double]): 力控坐标系相对于法兰坐标系的变换矩阵（齐次矩阵）
            type (FrameType): 类别, 指定哪个坐标系为力控任务坐标系, 支持:
                1) 世界坐标系 FrameType::world;
                2) 工具坐标系 FrameType::tool;
                3) 路径坐标系 FrameType::path (力控任务坐标系需要跟踪轨迹变化的过程)
            ec (dict): 错误码输出
        """
    def setFilterFrequency(self, jointFrequency: typing.SupportsFloat | typing.SupportsIndex, cartesianFrequency: typing.SupportsFloat | typing.SupportsIndex, torqueFrequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置机器人控制器的滤波截止频率，用来平滑指令。允许的范围: 1 ~ 1000Hz, 建议设置为10 ~ 100Hz。
        
        Args:
            jointFrequency (double): 关节位置的滤波截止频率，单位: Hz
            cartesianFrequency (double): 笛卡尔空间位置的滤波截止频率，单位: Hz
            torqueFrequency (double): 关节力矩的滤波截止频率，单位: Hz
            ec (dict): 错误码输出
        """
    def setFilterLimit(self, limit_rate: bool, cutoff_frequency: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        """
        设置限幅滤波参数。
        
        Args:
            limit_rate (bool): true - 限幅开启
            cutoff_frequency (double): 截止频率。范围是0 ~ 1000Hz，建议10~100Hz.
        
        Returns:
            bool: true - 设定成功
        """
    def setJointImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(5)"], ec: dict) -> None:
        """
        设置轴空间阻抗控制系数，轴空间阻抗运动时生效。
        
        Args:
            factor (List[double]): 轴空间阻抗系数，单位: Nm/rad
            ec (dict): 错误码输出
        """
    def setLoad(self, load: xCoreSDK_python.Load, ec: dict) -> None:
        """
        设置工具和负载的质量、质心和惯性矩阵。设置负载后控制器会保存负载配置，机器人重启后恢复默认设置。
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setServoJoint(self, ServoJ_T: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Lookahead: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Kp: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        通过实时模式sendCommand下发关节位置，开放调用周期、增益和前瞻时间的设置，且开启servoJ功能
        
        Args:
            ServoJ_T (float): 下发关节位置时调用servoJ的周期, 单位s
            ServoJ_Lookahead (float): 前瞻时间，对下发关节位置后运动速度的限制, 单位s
            ServoJ_Kp (float): 控制增益
            ec (dict): 错误码输出
        """
    def setTorqueFilterCutOffFrequency(self, frequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置滤波参数。
        
        Args:
            frequency (double): 允许的范围 1 ~ 1000Hz
            ec (dict): 错误码输出
        """
    def startLoop(self, blocking: bool = True) -> None:
        """
        开始执行回调函数。
        
        Args:
            blocking (bool): true 是否阻塞调用此函数的线程。若为非阻塞线程，需调用stopLoop()停止调度任务，否则无法开始下一次循环周期。
        """
    def startMove(self, rtMode: xCoreSDK_python.RtControllerMode) -> None:
        """
        指定控制模式，机器人准备开始运动，在每段回调执行前需要先调用此接口。
        
        调用此接口机器人不会立即开始运动, 而是有运动命令发送后才会开始。
        
        Note:
            1) 在startMove之前应将参数依次设置好，例如滤波阻抗参数等等，设置完成后再调用startMove()。
            在调用startMove后执行其他指令可能会失败，例如下电等操作。正确停止方法是调用stopMove。
        
        Args:
            rtMode (RtControllerMode): 控制模式
        
        Raises:
            RealtimeStateException: 已经开始运动运动后重复调用
            RealtimeParameterException: 指定了不支持的控制模式
            RealtimeControlException: 控制器无法切换到该控制模式，多出现于切换到力控模式时
        """
    def stopLoop(self) -> None:
        """
         停止执行周期性调度任务。
        """
    def stopMove(self) -> None:
        """
         机器人停止运动，停止接收客户端发送的运动指令。
        """
    def stopServoJoint(self) -> None:
        """
        关闭servoJ功能，停止使用setServoJoint需要进行关闭。
        """
class PyRTmotioncontrol6:
    """
    用于在python中使用实时接口
    """
    def MoveC(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, aux: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveC指令，在到达target之前处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveCCommand。
        
        Args:
            speed: 速度比例系数
            start: 机器人起始位姿, 需要是机器人当前位姿。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            aux: 机器人辅助点位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
            target: 机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        
        Raises:
            RealtimeParameterException: 点位错误, 无法计算出圆弧路径
            RealtimeMotionException: 机器人运动过程中发生错误
        """
    def MoveJ(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], target: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> None:
        """
        MoveJ指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveAbsJCommand。
        
        Args:
            speed (double): 速度比例系数
            start (List[double]): 起始关节角度，需要是机器人当前关节角度，否则可能造成下电。
            target (List[double])   机器人目标关节角度
        """
    def MoveL(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveL指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveLCommand。
        
        Args:
            speed (double): 速度比例系数, 范围 0 - 1
            start (CartesianPosition): 起始位姿, 需要是机器人当前位姿，否则可能造成下电。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            target (CartesianPosition)   机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        """
    def __init__(self, arg0: xCoreSDK_python.Cobot_6) -> None:
        ...
    def automaticErrorRecovery(self, ec: dict) -> None:
        """
        当错误发生后，自动恢复机器人。
        
        Args:
            ec (dict): 错误码输出
        """
    def disconnectNetwork(self) -> None:
        """
        断开与实时控制服务器的连接, 关闭数据接收和指令发送端口。不会断开和机器人的连接。
            
        Note:
            若机器人在运动，断开后会立即停止运动
        """
    def hasMotionError(self) -> bool:
        """
        实时模式运动是否发生了运动错误
        
        Returns:
            bool: true - 有报错
        """
    def reconnectNetwork(self, ec: dict) -> None:
        """
        重新连接到实时控制服务器
        
        Args:
            ec (dict): 错误码输出
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.JointPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.CartesianPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.Torque) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    def setCartesianImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔空间阻抗控制系数, 笛卡尔阻抗运动时生效。
        
        Args:
            factor (List[double]): 阻抗系数[ X, Y, Z, Rx, Ry, Rz], 最大值为 { 3000, 3000, 3000, 300, 300, 300 }, 单位: N/m, Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianImpedanceDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置末端期望力, 在笛卡尔空间阻抗运动时生效。
        
        Args:
            torque (List[double]): 笛卡尔空间末端期望力, 允许的范围为 { ±60, ±60, ±60, ±30, ±30, ±30 }, 单位: N, N·m
            ec (dict): 错误码输出
        """
    def setCartesianLimit(self, lengths: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置笛卡尔空间运动区域，超过设置区域运动会停止。
        
        非力控虚拟墙。若机器人末端或TCP末端超过安全区域，电机同样会做下电处理。
        
        Args:
            lengths (List[double]): 安全区域长方体长宽高，对应XYZ, 单位: 米
            frame (List[double]): 安全区域长方体中心相对于基坐标系位姿（齐次矩阵）
            ec (dict): 错误码输出
        """
    def setCollisionBehaviour(self, torqueThresholds: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置碰撞检测阈值。
        
        碰撞检测只在位置控制时生效，力控时不生效。若检测到碰撞，控制器会下发下电指令，电机抱闸吸合下使能。
        
        Args:
            torqueThresholds (List[double]): 关节碰撞检测阈值, 单位N
            ec (dict): 错误码输出
        """
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    def setControlLoopCar(self, callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopJoi(self, callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopTor(self, callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setEndEffectorFrame(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置末端执行器相对于机器人法兰的位姿，设置TCP后控制器会保存配置，机器人重启后恢复默认设置。
        
        Args:
            frame (List[double]): 末端执行器坐标系相对于法兰坐标系的齐次矩阵，单位: rad, m
            ec (dict): 错误码输出
        """
    def setFcCoor(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], type: xCoreSDK_python.FrameType, ec: dict) -> None:
        """
        设置机器人力控坐标系。
        
        Args:
            frame (List[double]): 力控坐标系相对于法兰坐标系的变换矩阵（齐次矩阵）
            type (FrameType): 类别, 指定哪个坐标系为力控任务坐标系, 支持:
                1) 世界坐标系 FrameType::world;
                2) 工具坐标系 FrameType::tool;
                3) 路径坐标系 FrameType::path (力控任务坐标系需要跟踪轨迹变化的过程)
            ec (dict): 错误码输出
        """
    def setFilterFrequency(self, jointFrequency: typing.SupportsFloat | typing.SupportsIndex, cartesianFrequency: typing.SupportsFloat | typing.SupportsIndex, torqueFrequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置机器人控制器的滤波截止频率，用来平滑指令。允许的范围: 1 ~ 1000Hz, 建议设置为10 ~ 100Hz。
        
        Args:
            jointFrequency (double): 关节位置的滤波截止频率，单位: Hz
            cartesianFrequency (double): 笛卡尔空间位置的滤波截止频率，单位: Hz
            torqueFrequency (double): 关节力矩的滤波截止频率，单位: Hz
            ec (dict): 错误码输出
        """
    def setFilterLimit(self, limit_rate: bool, cutoff_frequency: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        """
        设置限幅滤波参数。
        
        Args:
            limit_rate (bool): true - 限幅开启
            cutoff_frequency (double): 截止频率。范围是0 ~ 1000Hz，建议10~100Hz.
        
        Returns:
            bool: true - 设定成功
        """
    def setJointImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置轴空间阻抗控制系数，轴空间阻抗运动时生效。
        
        Args:
            factor (List[double]): 轴空间阻抗系数，单位: Nm/rad
            ec (dict): 错误码输出
        """
    def setLoad(self, load: xCoreSDK_python.Load, ec: dict) -> None:
        """
        设置工具和负载的质量、质心和惯性矩阵。设置负载后控制器会保存负载配置，机器人重启后恢复默认设置。
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setServoJoint(self, ServoJ_T: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Lookahead: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Kp: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        通过实时模式sendCommand下发关节位置，开放调用周期、增益和前瞻时间的设置，且开启servoJ功能
        
        Args:
            ServoJ_T (float): 下发关节位置时调用servoJ的周期, 单位s
            ServoJ_Lookahead (float): 前瞻时间，对下发关节位置后运动速度的限制, 单位s
            ServoJ_Kp (float): 控制增益
            ec (dict): 错误码输出
        """
    def setTorqueFilterCutOffFrequency(self, frequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置滤波参数。
        
        Args:
            frequency (double): 允许的范围 1 ~ 1000Hz
            ec (dict): 错误码输出
        """
    def startLoop(self, blocking: bool = True) -> None:
        """
        开始执行回调函数。
        
        Args:
            blocking (bool): true 是否阻塞调用此函数的线程。若为非阻塞线程，需调用stopLoop()停止调度任务，否则无法开始下一次循环周期。
        """
    def startMove(self, rtMode: xCoreSDK_python.RtControllerMode) -> None:
        """
        指定控制模式，机器人准备开始运动，在每段回调执行前需要先调用此接口。
        
        调用此接口机器人不会立即开始运动, 而是有运动命令发送后才会开始。
        
        Note:
            1) 在startMove之前应将参数依次设置好，例如滤波阻抗参数等等，设置完成后再调用startMove()。
            在调用startMove后执行其他指令可能会失败，例如下电等操作。正确停止方法是调用stopMove。
        
        Args:
            rtMode (RtControllerMode): 控制模式
        
        Raises:
            RealtimeStateException: 已经开始运动运动后重复调用
            RealtimeParameterException: 指定了不支持的控制模式
            RealtimeControlException: 控制器无法切换到该控制模式，多出现于切换到力控模式时
        """
    def stopLoop(self) -> None:
        """
         停止执行周期性调度任务。
        """
    def stopMove(self) -> None:
        """
         机器人停止运动，停止接收客户端发送的运动指令。
        """
    def stopServoJoint(self) -> None:
        """
        关闭servoJ功能，停止使用setServoJoint需要进行关闭。
        """
class PyRTmotioncontrol7:
    """
    用于在python中使用实时接口
    """
    def MoveC(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, aux: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveC指令，在到达target之前处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveCCommand。
        
        Args:
            speed: 速度比例系数
            start: 机器人起始位姿, 需要是机器人当前位姿。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            aux: 机器人辅助点位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
            target: 机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        
        Raises:
            RealtimeParameterException: 点位错误, 无法计算出圆弧路径
            RealtimeMotionException: 机器人运动过程中发生错误
        """
    def MoveJ(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], target: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"]) -> None:
        """
        MoveJ指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveAbsJCommand。
        
        Args:
            speed (double): 速度比例系数
            start (List[double]): 起始关节角度，需要是机器人当前关节角度，否则可能造成下电。
            target (List[double])   机器人目标关节角度
        """
    def MoveL(self, speed: typing.SupportsFloat | typing.SupportsIndex, start: xCoreSDK_python.CartesianPosition, target: xCoreSDK_python.CartesianPosition) -> None:
        """
        MoveL指令，上位机规划路径，在到达target之前处于处于阻塞状态。如果运动中发生错误将停止阻塞状态并返回。
        
        Note:
            已不建议使用，请使用非实时模式指令MoveLCommand。
        
        Args:
            speed (double): 速度比例系数, 范围 0 - 1
            start (CartesianPosition): 起始位姿, 需要是机器人当前位姿，否则可能造成下电。如果设置了TCP，那么应该是工具相对于基坐标系的位姿。
            target (CartesianPosition)   机器人目标位姿。同理如果设置了TCP，应是TCP相对于基坐标系的位姿
        """
    def __init__(self, arg0: xCoreSDK_python.Cobot_7) -> None:
        ...
    def automaticErrorRecovery(self, ec: dict) -> None:
        """
        当错误发生后，自动恢复机器人。
        
        Args:
            ec (dict): 错误码输出
        """
    def disconnectNetwork(self) -> None:
        """
        断开与实时控制服务器的连接, 关闭数据接收和指令发送端口。不会断开和机器人的连接。
            
        Note:
            若机器人在运动，断开后会立即停止运动
        """
    def hasMotionError(self) -> bool:
        """
        实时模式运动是否发生了运动错误
        
        Returns:
            bool: true - 有报错
        """
    def reconnectNetwork(self, ec: dict) -> None:
        """
        重新连接到实时控制服务器
        
        Args:
            ec (dict): 错误码输出
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.JointPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.CartesianPosition) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    @typing.overload
    def sendCommand(self, cmd: xCoreSDK_python.Torque) -> None:
        """
        发送JointPosition/CartesianPosition/Torque命令。适用于不使用调度周期，程序直接发送命令。
        
        Note:
            开始运动后，持续调用此函数发送运动命令。由于控制器执行命令的周期为1ms，发送命令的间隔也需要控制在1ms，
            如果发送间隔过长会判断为通信丢包，间隔过短会造成伺服报错。
            直接发送命令的话就不需要用调度周期了，setControlLoop(), startLoop(), stopLoop()等相关函数都不需要。
            实时运动报错可通过BaseRobot::updateRobotState()获知，有报错会抛出异常；
            需要调用Robot_T::startReceiveRobotState()接收数据，建议间隔为1ms，避免报错信息被覆盖。
        
        Args:
            cmd (Union[JointPosition, CartesianPosition, Torque]): 根据控制模式(RtControllerMode)不同，有3种运动命令: 关节角度/笛卡尔位姿/力矩
        
        Raises:
            ArgumentException: 指令数值存在非法值
            RealtimeStateException: 未开始运动
            RealtimeControlException: 命令发送网络异常; 或命令类型与控制模式不匹配; 或控制器执行已发送命令时发生错误
        """
    def setCartesianImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置笛卡尔空间阻抗控制系数, 笛卡尔阻抗运动时生效。
        
        Args:
            factor (List[double]): 阻抗系数[ X, Y, Z, Rx, Ry, Rz], 最大值为 { 3000, 3000, 3000, 300, 300, 300 }, 单位: N/m, Nm/rad
            ec (dict): 错误码输出
        """
    def setCartesianImpedanceDesiredTorque(self, torque: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], ec: dict) -> None:
        """
        设置末端期望力, 在笛卡尔空间阻抗运动时生效。
        
        Args:
            torque (List[double]): 笛卡尔空间末端期望力, 允许的范围为 { ±60, ±60, ±60, ±30, ±30, ±30 }, 单位: N, N·m
            ec (dict): 错误码输出
        """
    def setCartesianLimit(self, lengths: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"], frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置笛卡尔空间运动区域，超过设置区域运动会停止。
        
        非力控虚拟墙。若机器人末端或TCP末端超过安全区域，电机同样会做下电处理。
        
        Args:
            lengths (List[double]): 安全区域长方体长宽高，对应XYZ, 单位: 米
            frame (List[double]): 安全区域长方体中心相对于基坐标系位姿（齐次矩阵）
            ec (dict): 错误码输出
        """
    def setCollisionBehaviour(self, torqueThresholds: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置碰撞检测阈值。
        
        碰撞检测只在位置控制时生效，力控时不生效。若检测到碰撞，控制器会下发下电指令，电机抱闸吸合下使能。
        
        Args:
            torqueThresholds (List[double]): 关节碰撞检测阈值, 单位N
            ec (dict): 错误码输出
        """
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    @typing.overload
    def setControlLoop(self: ..., callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        ...
    def setControlLoopCar(self, callback: collections.abc.Callable[[], xCoreSDK_python.CartesianPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopJoi(self, callback: collections.abc.Callable[[], xCoreSDK_python.JointPosition], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setControlLoopTor(self, callback: collections.abc.Callable[[], xCoreSDK_python.Torque], priority: typing.SupportsInt | typing.SupportsIndex = 0, useStateDataInLoop: bool = False) -> None:
        """
        开始执行回调函数。
        
        Args:
            callback (Command): 回调函数。根据控制模式(RtControllerMode)不同，函数返回值有3种: 关节角度/笛卡尔位姿/力矩。
            priority (int): 任务优先级, 0为不指定。此参数仅当使用实时操作系统时生效，若无法设置会打印控制台错误信息。
            useStateDataInLoop (bool): 是否需要在周期内读取状态数据。
        """
    def setEndEffectorFrame(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], ec: dict) -> None:
        """
        设置末端执行器相对于机器人法兰的位姿，设置TCP后控制器会保存配置，机器人重启后恢复默认设置。
        
        Args:
            frame (List[double]): 末端执行器坐标系相对于法兰坐标系的齐次矩阵，单位: rad, m
            ec (dict): 错误码输出
        """
    def setFcCoor(self, frame: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"], type: xCoreSDK_python.FrameType, ec: dict) -> None:
        """
        设置机器人力控坐标系。
        
        Args:
            frame (List[double]): 力控坐标系相对于法兰坐标系的变换矩阵（齐次矩阵）
            type (FrameType): 类别, 指定哪个坐标系为力控任务坐标系, 支持:
                1) 世界坐标系 FrameType::world;
                2) 工具坐标系 FrameType::tool;
                3) 路径坐标系 FrameType::path (力控任务坐标系需要跟踪轨迹变化的过程)
            ec (dict): 错误码输出
        """
    def setFilterFrequency(self, jointFrequency: typing.SupportsFloat | typing.SupportsIndex, cartesianFrequency: typing.SupportsFloat | typing.SupportsIndex, torqueFrequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置机器人控制器的滤波截止频率，用来平滑指令。允许的范围: 1 ~ 1000Hz, 建议设置为10 ~ 100Hz。
        
        Args:
            jointFrequency (double): 关节位置的滤波截止频率，单位: Hz
            cartesianFrequency (double): 笛卡尔空间位置的滤波截止频率，单位: Hz
            torqueFrequency (double): 关节力矩的滤波截止频率，单位: Hz
            ec (dict): 错误码输出
        """
    def setFilterLimit(self, limit_rate: bool, cutoff_frequency: typing.SupportsFloat | typing.SupportsIndex) -> bool:
        """
        设置限幅滤波参数。
        
        Args:
            limit_rate (bool): true - 限幅开启
            cutoff_frequency (double): 截止频率。范围是0 ~ 1000Hz，建议10~100Hz.
        
        Returns:
            bool: true - 设定成功
        """
    def setJointImpedance(self, factor: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(7)"], ec: dict) -> None:
        """
        设置轴空间阻抗控制系数，轴空间阻抗运动时生效。
        
        Args:
            factor (List[double]): 轴空间阻抗系数，单位: Nm/rad
            ec (dict): 错误码输出
        """
    def setLoad(self, load: xCoreSDK_python.Load, ec: dict) -> None:
        """
        设置工具和负载的质量、质心和惯性矩阵。设置负载后控制器会保存负载配置，机器人重启后恢复默认设置。
        
        Args:
            load (Load): 负载信息
            ec (dict): 错误码输出
        """
    def setServoJoint(self, ServoJ_T: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Lookahead: typing.SupportsFloat | typing.SupportsIndex, ServoJ_Kp: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        通过实时模式sendCommand下发关节位置，开放调用周期、增益和前瞻时间的设置，且开启servoJ功能
        
        Args:
            ServoJ_T (float): 下发关节位置时调用servoJ的周期, 单位s
            ServoJ_Lookahead (float): 前瞻时间，对下发关节位置后运动速度的限制, 单位s
            ServoJ_Kp (float): 控制增益
            ec (dict): 错误码输出
        """
    def setTorqueFilterCutOffFrequency(self, frequency: typing.SupportsFloat | typing.SupportsIndex, ec: dict) -> None:
        """
        设置滤波参数。
        
        Args:
            frequency (double): 允许的范围 1 ~ 1000Hz
            ec (dict): 错误码输出
        """
    def startLoop(self, blocking: bool = True) -> None:
        """
        开始执行回调函数。
        
        Args:
            blocking (bool): true 是否阻塞调用此函数的线程。若为非阻塞线程，需调用stopLoop()停止调度任务，否则无法开始下一次循环周期。
        """
    def startMove(self, rtMode: xCoreSDK_python.RtControllerMode) -> None:
        """
        指定控制模式，机器人准备开始运动，在每段回调执行前需要先调用此接口。
        
        调用此接口机器人不会立即开始运动, 而是有运动命令发送后才会开始。
        
        Note:
            1) 在startMove之前应将参数依次设置好，例如滤波阻抗参数等等，设置完成后再调用startMove()。
            在调用startMove后执行其他指令可能会失败，例如下电等操作。正确停止方法是调用stopMove。
        
        Args:
            rtMode (RtControllerMode): 控制模式
        
        Raises:
            RealtimeStateException: 已经开始运动运动后重复调用
            RealtimeParameterException: 指定了不支持的控制模式
            RealtimeControlException: 控制器无法切换到该控制模式，多出现于切换到力控模式时
        """
    def stopLoop(self) -> None:
        """
         停止执行周期性调度任务。
        """
    def stopMove(self) -> None:
        """
         机器人停止运动，停止接收客户端发送的运动指令。
        """
    def stopServoJoint(self) -> None:
        """
        关闭servoJ功能，停止使用setServoJoint需要进行关闭。
        """
