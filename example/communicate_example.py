"""使用python sdk的通信操作
包括：
获取DO端口状态
设置DO端口状态
获取DI端口状态
设置DI端口状态
获取AI端口数据
设置AO数据
读取寄存器
写入寄存器
"""
import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_log, print_separator
import numpy as np


def communicate_op(robot, ec):
    print_separator("communicate_op", length=110)
    get_DO(robot, ec)
    set_DO(robot, ec)
    get_DI(robot, ec)
    set_DI(robot, ec)
    get_AI(robot, ec)
    set_AO(robot, ec)
    read_register(robot, ec)
    write_register(robot, ec)
    example_485(robot, ec)


def get_DO(robot, ec):
    '''获取DO端口状态'''
    print_separator("get_DO", length=80)
    board = 2  # IO板序号
    port = 1  # 端口号
    switch = robot.getDO(board, port, ec)
    print_log("get_DO", ec, f"ret={switch}")


def set_DO(robot, ec):
    '''设置DO端口状态'''
    print_separator("set_DO", length=80)
    board = 2  # IO板序号
    port = 0  # 端口号
    state = True
    robot.setDO(board, port, state, ec)
    print_log("set_DO", ec, f"ret={robot.getDO(board,port,ec)}")


def get_DI(robot, ec):
    '''获取DI端口状态'''
    print_separator("get_DI", length=80)
    board = 2  # IO板序号
    port = 1  # 端口号
    switch = robot.getDI(board, port, ec)
    print_log("get_DI", ec, f"ret={switch}")


def set_DI(robot, ec):
    '''设置DI端口状态'''
    print_separator("set_DI", length=80)
    robot.setSimulationMode(True, ec)
    # 打开输入仿真模式
    print_log("open setSimulationMode", ec)
    board = 2  # IO板序号
    port = 0  # 端口号
    state = True
    robot.setDI(board, port, state, ec)
    print_log("set_DI", ec, f"ret={robot.getDI(board,port,ec)}")
    robot.setSimulationMode(False, ec)
    # 关闭仿真模式
    print_log("close setSimulationMode", ec)


def get_AI(robot, ec):
    '''获取AI端口数据'''
    print_separator("get_AI", length=80)
    board = 2
    port = 0
    value = robot.getAI(board, port, ec)
    print_log("get_AI", ec, f"value={value}")


def set_AO(robot, ec):
    '''设置AO数据'''
    print_separator("set_AO", length=80)
    board = 2
    port = 0
    value = 1.5
    robot.setAO(board, port, value, ec)
    print_log("set_AO", ec)


def read_register(robot, ec):
    '''读取寄存器'''
    print_separator("read_register", length=80)

    # 假设"register2"是个寄存器数组, 长度是5

    # 读取第1个寄存器，类型为float，HMI上寄存器索引从1开始
    val_f = xCoreSDK_python.PyTypeFloat()  # bool为PyTypeBool，int为PyTypeInt
    robot.readRegister("register2", 0, val_f, ec)
    print_log("readRegister", ec, f"val_f={val_f.content()}")

    # 读整个数组，赋值给float列表val_af, val_af的长度也变为5。此时index参数是多少都无所谓
    val_af = xCoreSDK_python.PyTypeVectorFloat(
    )  # bool列表为PyTypeVectorBool，int为PyTypeVectorInt
    robot.readRegister("register2", 0, val_af, ec)
    print_log("readRegister", ec, f"val_f={val_af.content()}")


def write_register(robot, ec):
    '''写入寄存器'''
    print_separator("write_register", length=80)
    value = 1.5
    robot.writeRegister("register2", 0, value, ec)
    #写整个数组
    values = [1, 2, 3, 4, 5]
    robot.writeRegister("register2", 0, values, ec)
    print_log("writeRegister", ec)


def example_485(robot, ec):
    '''485通信'''
    print_separator("example_485", length=80)
    robot.setxPanelRS485(xCoreSDK_python.xPanelOptVout.reserve, True, ec)
    print_log("setxPanelRS485", ec)

    data_array = xCoreSDK_python.PyTypeVectorInt([0])
    robot.XPRWModbusRTUReg(1, 0x03, 1, "int32", 1, data_array, False, ec)
    print_log("XPRWModbusRTUReg", ec, f"ret={data_array.content()}")

    data_array_bool = xCoreSDK_python.PyTypeVectorBool([0, 0, 0])
    robot.XPRWModbusRTUCoil(1, 1, 1, 3, data_array_bool, False, ec)
    print_log("XPRWModbusRTUCoil", ec, f"ret={data_array_bool.content()}")

    send_data = [1, 1, 1]
    uint8_array = np.array(send_data, dtype=np.uint8)
    rev_data = xCoreSDK_python.PyTypeVectorInt()
    robot.XPRS485SendData(3, 3, uint8_array, rev_data, ec)
    print_log("XPRS485SendData", ec, f"ret={rev_data.content()}")


if __name__ == "__main__":
    try:
        ip = "192.168.0.160"
        # 连接机器人
        # 最好使用创建方法代替构造函数，不同的机器人对应不同的类型
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        communicate_op(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
