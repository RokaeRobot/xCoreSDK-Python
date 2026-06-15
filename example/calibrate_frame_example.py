"""标定坐标系示例"""
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

class CalibrateFrame:
    def __init__(self, robot, type, point_num, is_held, base_aux=None):
        """
        :param robot: 已创建好的机器人类
        :param type: 标定坐标系
        :param point_num: 传入的位置数量，对应N点法
        :param is_held: 是否机器人手持
        :param base_aux: 基坐标系标定辅助点
        """
        self.robot_ = robot
        self.type_ = type
        self.point_list_ = [None] * point_num
        self.is_held_ = is_held
        self.base_aux_ = base_aux if base_aux is not None else [0.0, 0.0, 0.0]

    def set_point(self, point_index,ec):
        """
        设置标定点
        """
        if point_index >= len(self.point_list_):
            # 自行添加异常处理
            print("标定点下标超出范围")
            return
        # 请保证在调用前 robot 是有效的
        self.point_list_[point_index] = self.robot_.jointPos(ec)
        print_log("设置标定点",ec, f"{point_index}:{self.point_list_[point_index]}")

    def confirm(self, ec):
        """
        所有标定位置已确认，得到标定结果
        :param ec: 标定结果错误码
        :return: 标定结果
        """
        return self.robot_.calibrateFrame(self.type_, self.point_list_, self.is_held_, ec, self.base_aux_)
    
def calibrate_frame(robot,ec):
    '''标定工具/工件坐标系'''
    print_separator("calibrate_frame",length=110)
    point_count = 4
    calibrate_frame = CalibrateFrame(robot, xCoreSDK_python.FrameType.tool, point_count, True)
    
    for i in range(point_count):
        print("将机器人Jog到标定点，按回车确认")
        input()  # 等待用户按回车
        calibrate_frame.set_point(i,ec)
    
    calibrate_result = calibrate_frame.confirm(ec)
    
    if ec["ec"]:
        print("标定失败:", xCoreSDK_python.message(ec))
    else:
        print("标定成功，结果 -", calibrate_result.frame, "\n偏差:", calibrate_result.errors)

def main():
    try:
        ip = "10.0.40.129"
        robot = xCoreSDK_python.xMateRobot(ip) 
        ec = {}
        calibrate_frame(robot,ec)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
    