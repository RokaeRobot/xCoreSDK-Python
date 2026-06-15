import setup_path
import platform
# 根据操作系统导入相应的模块
if platform.system() == 'Windows':
    from Release.windows import xCoreSDK_python
elif platform.system() == 'Linux':
    from Release.linux import xCoreSDK_python
else:
    raise ImportError("Unsupported operating system")
from log import print_separator
from base_example import base_op
from calibrate_frame_example import calibrate_frame
from collisionDetection_example import collision_detection_op
from communicate_example import communicate_op
from drag_example import drag_op
from get_keypad_state_example import get_keypad_state_op
from jog_example import jog_op
from move_example import move_op
from read_robot_state_example import read_robot_state_op
from rl_project_example import rl_project_op

if __name__ == "__main__":
    try:
        ip = "192.168.110.129"
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        base_op(robot, ec)
        calibrate_frame(robot, ec)
        collision_detection_op(robot, ec)
        communicate_op(robot, ec)
        drag_op(robot, ec)
        jog_op(robot, ec)
        move_op(robot, ec)
        rl_project_op(robot, ec)

        local_ip = "192.168.110.91"
        robot = xCoreSDK_python.xMateRobot(ip, local_ip)
        get_keypad_state_op(robot, ec)
        read_robot_state_op(robot, ec)
    except Exception as e:
        print(f"An error occurred: {e}")
