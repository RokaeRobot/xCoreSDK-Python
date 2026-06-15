"""
机器人实时数据支持的字段

jointPos_m: 关节角度 [rad] - ArrayXD
tcpPose_m: 末端位姿, 相对于基坐标系, 行优先齐次变换矩阵 - Array16D
tcpPoseAbc_m: 末端位姿, 相对于基坐标系 [X,Y,Z,Rx,Ry,Rz] - Array6D
elbow_m: 臂角 [rad] - double
keypads: 末端按键状态 - ArrayXD
exJointPos_m: 外部轴数值 [rad] 导轨[m] - Array6D 实际有效数据个数为外部轴数
exJointVel_m: 外部轴速度 [rad/s] 导轨[m/s] - Array6D 实际有效数据个数为外部轴数
exMotor_m: 外部轴电机位置 - Array6D 实际有效数据个数为外部轴数 
"""
from __future__ import annotations
__all__: list[str] = ['elbow_m', 'exJointPos_m', 'exJointVel_m', 'exMotor_m', 'jointPos_m', 'keypads', 'tcpPoseAbc_m', 'tcpPose_m']
elbow_m: str = 'psi_m'
exJointPos_m: str = 'ex_q_m'
exJointVel_m: str = 'ex_dq_m'
exMotor_m: str = 'ex_motor_m'
jointPos_m: str = 'q_m'
keypads: str = 'io_keypad'
tcpPoseAbc_m: str = 'pos_abc_m'
tcpPose_m: str = 'pos_m'
