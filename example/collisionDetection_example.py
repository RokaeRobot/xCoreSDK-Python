"""碰撞检测的相关操作示例
设置碰撞事件监听
取消碰撞事件监听
开启碰撞检测
关闭碰撞检测
急停复位
"""
import time
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

def collision_detection_op(robot,ec):
    print_separator("collision_detection_op",length=110)
    reset_emergencyStop(robot,ec)
    set_collision_detection_watcher(robot,ec)
    enable_collision_detection(robot,ec)
    time.sleep(2)
    disable_collision_detection(robot,ec)
    cancel_collision_detection_watcher(robot,ec)

def set_collision_detection_watcher(robot,ec):
    '''设置碰撞事件监听'''
    print_separator("set_collision_detection_watcher",length=80)
    robot.setEventWatcher(xCoreSDK_python.Event.safety,print_info,ec)
    print_log("setEventWatcher",ec)
    
def cancel_collision_detection_watcher(robot,ec):
    '''取消碰撞事件监听'''
    print_separator("cancel_collision_detection_watcher",length=80)
    robot.setNoneEventWatcher(xCoreSDK_python.Event.safety,ec)
    print_log("setNoneEventWatcher",ec)
    
def enable_collision_detection(robot,ec):
    '''开启碰撞检测'''
    print_separator("enable_collision_detection",length=80)
    sensitivity = [1.0,1.1,1.2,1.3,1.4,1.5]
    behaviour = xCoreSDK_python.StopLevel.stop2 # 碰撞后机器人行为, 支持stop1(安全停止, stop0和stop1处理方式相同), stop2(触发暂停）, suppleStop(柔顺停止)
    fallback_compliance = 0.05 # 1) 碰撞后行为是安全停止或触发暂停时，该参数含义是碰撞后回退距离，单位: 米 2) 碰撞后行为是柔顺停止时，该参数含义是柔顺度，范围 [0.0, 1.0]
    robot.enableCollisionDetection(sensitivity,behaviour,fallback_compliance,ec)
    print_log("enableCollisionDetection",ec)

def disable_collision_detection(robot,ec):
    '''关闭碰撞检测'''
    print_separator("disable_collision_detection",length=80)
    robot.disableCollisionDetection(ec)
    print_log("disableCollisionDetection",ec)

def reset_emergencyStop(robot,ec):
  '''急停复位'''
  print_separator("reset_emergencyStop",length=80)
  robot.recoverState(1, ec)
  if ec["ec"] != 0:
      print_log("复位失败",ec)
  else:
      print_log("复位成功",ec)


def print_info(info):
    '''打印消息'''
    print(info)
    print(info["collided"])

if __name__ =="__main__":
    try:
        ip = "10.0.40.129"
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        collision_detection_op(robot,ec)

    except Exception as e:
        print(f"An error occurred: {e}")
