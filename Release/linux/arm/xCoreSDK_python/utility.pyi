"""
数据类型转换工具函数
"""
from __future__ import annotations
import collections.abc
import typing
import xCoreSDK_python
__all__: list[str] = ['EndInRefToFlanInBase', 'FlanInBaseToEndInRef', 'arrayToTransMatrix', 'arrayToTransMatrix_all', 'degToRad', 'degToRad_array16', 'degToRad_array6', 'eulerToMatrix', 'eulerToQuaternion', 'postureToTransArray', 'quaternionToEuler', 'radToDeg', 'radToDeg_array16', 'radToDeg_array6', 'toolsetCalcPos', 'transArrayToPosture', 'transMatrixToArray', 'transMatrixToArray_all']
def EndInRefToFlanInBase(base_in_world: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], tool_set: xCoreSDK_python.Toolset, end_in_ref: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> typing.Annotated[list[float], "FixedSize(6)"]:
    """
    T坐标系转换：将 末端相对与外部参考坐标 转换为 法兰相对于基坐标系的坐标
    
    Args:
        base_in_world: 基坐标系相对世界坐标系设置
        tool_set: 工具工件设置
        end_in_ref: 末端相对（外部）参考坐标系坐标
    
    Returns:
        法兰相对于基坐标系坐标
    """
def FlanInBaseToEndInRef(base_in_world: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"], tool_set: xCoreSDK_python.Toolset, flan_in_base: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> typing.Annotated[list[float], "FixedSize(6)"]:
    """
    坐标系转换：将 法兰相对于基坐标系坐标 转换为 末端相对于外部参考系坐标
    
    Args:
        base_in_world: 基坐标系相对世界坐标系设置
        tool_set: 工具工件设置
        flan_in_base: 法兰相对于基坐标系坐标
    
    Returns:
        末端相对（外部）参考坐标系坐标
    """
def arrayToTransMatrix(arr: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> tuple[typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 3]"], typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 1]"]]:
    """
    数组转为变换矩阵
    
    Args:
        array: 数组, 行优先
    
    Returns:
        Tuple: (旋转矩阵,平移向量)
    """
def arrayToTransMatrix_all(arr: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[4, 4]"]:
    """
    数组转为变换矩阵
    
    Args:
        array: 数组, 行优先
    
    Returns:
        4*4变换矩阵
    """
@typing.overload
def degToRad(degrees: typing.SupportsFloat | typing.SupportsIndex) -> float:
    """
    度转弧度
    """
@typing.overload
def degToRad(degrees: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> list[float]:
    """
    数组度转弧度
    """
def degToRad_array16(degrees: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> typing.Annotated[list[float], "FixedSize(16)"]:
    """
    将16元素角度数组转换为弧度数组
    """
def degToRad_array6(degrees: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> typing.Annotated[list[float], "FixedSize(6)"]:
    """
    将6元素角度数组转换为弧度数组
    """
def eulerToMatrix(euler: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]) -> typing.Annotated[numpy.typing.NDArray[numpy.float64], "[3, 3]"]:
    """
    欧拉角转为旋转矩阵
    
    Args:
        euler: 欧拉角, 顺序[z, y, x], 单位: 弧度
    
    Returns:
        旋转矩阵
    """
def eulerToQuaternion(rpy: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(3)"]) -> typing.Annotated[list[float], "FixedSize(4)"]:
    """
    欧拉角转四元数
    
    Args:
        rpy (list[float]): 欧拉角, 顺序[z, y, x], 单位: 弧度
    
    Returns:
        四元数 { Q1, Q2, Q3, Q4 }
    """
def postureToTransArray(xyz_abc: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> typing.Annotated[list[float], "FixedSize(16)"]:
    """
    将表示位姿的数组{X, Y, Z, Rx, Ry, Rz}转换成行优先齐次变换矩阵
    
    Args:
        xyz_abc: 输入位姿, {X, Y, Z, Rx, Ry, Rz}
    
    Returns:
        list: 转换结果，行优先
    """
def quaternionToEuler(w: typing.SupportsFloat | typing.SupportsIndex, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, z: typing.SupportsFloat | typing.SupportsIndex) -> typing.Annotated[list[float], "FixedSize(3)"]:
    """
    四元数转欧拉角
    
    Args:
        w: Q1
        x: Q2
        y: Q3
        z: Q4
    
    Returns:
        list: [Rx, Ry, Rz]
    """
@typing.overload
def radToDeg(rad: typing.SupportsFloat | typing.SupportsIndex) -> float:
    """
    弧度转度
    """
@typing.overload
def radToDeg(rad: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> list[float]:
    """
    数组弧度转度
    """
def radToDeg_array16(rad: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> typing.Annotated[list[float], "FixedSize(16)"]:
    """
    将16元素弧度数组转换为角度数组
    """
def radToDeg_array6(rad: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(6)"]) -> typing.Annotated[list[float], "FixedSize(6)"]:
    """
    将6元素弧度数组转换为角度数组
    """
def toolsetCalcPos(toolset: xCoreSDK_python.Toolset) -> tuple[typing.Annotated[list[float], "FixedSize(16)"], typing.Annotated[list[float], "FixedSize(16)"]]:
    """
    Toolset转换成工具和工件
    
    Args:
        tool_set: 工具工件组
    
    Returns:
        Tuple: (外部坐标系变换矩阵,末端坐标系变换矩阵)
    """
def transArrayToPosture(transMat: typing.Annotated[collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex], "FixedSize(16)"]) -> typing.Annotated[list[float], "FixedSize(6)"]:
    """
    将行优先齐次变换矩阵转换成{X, Y, Z, Rx, Ry, Rz}数组
    
    Args:
        transMatrix: 行优先齐次变换矩阵
    
    Returns:
        list: 转换结果，{X, Y, Z, Rx, Ry, Rz}
    """
def transMatrixToArray(rot: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 3]"], trans: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[3, 1]"]) -> typing.Annotated[list[float], "FixedSize(16)"]:
    """
    变换矩阵转为数组
    
    Args:
        rot: 旋转矩阵
        trans: 平移向量
    
    Returns:
        list: 转换结果，行优先
    """
def transMatrixToArray_all(R: typing.Annotated[numpy.typing.ArrayLike, numpy.float64, "[4, 4]"]) -> typing.Annotated[list[float], "FixedSize(16)"]:
    """
    变换矩阵转为数组
    
    Args:
        R: 变换矩阵
    
    Returns:
        list: 转换结果，行优先
    """
