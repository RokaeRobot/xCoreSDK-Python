'''拖拽和录制的相关操作示例
'''
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
from move_example import wait_robot

def drag_op(robot,ec):
    print_separator("drag_op",length=110)
    robot.setPowerState(False, ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.manual, ec)
    # 打开拖动之前，需要机械臂处于手动模式下电状态
    robot.moveReset(ec)
    while True:
        cmd = input(f"""
                    d: enable drag, k: disable drag, 
                    a: start record, b: stop record, 
                    s: save record path, c: cancel record, 
                    u: query path lists, v: delete path, 
                    p: replay specific path, q: exit\n""")
        if cmd == 'd':
            open_drag(robot,ec)
        elif cmd =='k':
            close_drag(robot,ec)
        elif cmd =='a':
            start_record_path(robot,ec)
        elif cmd =='b':
            stop_record_path(robot,ec)
        elif cmd =='s':
            save_record_path(robot,ec)
        elif cmd =='c':
            cancel_record_path(robot,ec)
        elif cmd == 'u':
            query_path_lists(robot,ec)
        elif cmd == 'v':
            delete_path(robot,ec)
        elif cmd =='p':
            replay_path(robot,ec)
        elif cmd == 'q':
            break
        else:
            print("wrong cmd")
    wait_robot(robot,ec)
    robot.stop(ec)
    time.sleep(1)
    robot.setPowerState(False, ec)
    # robot.disconnectFromRobot(ec)
    
def open_drag(robot,ec):
    '''打开拖动'''
    robot.enableDrag(1, 2, ec)  
    print_log("enableDrag",ec)
    
def close_drag(robot,ec):
    '''关闭拖动'''
    robot.disableDrag(ec)
    print_log("disableDrag",ec)

def start_record_path(robot,ec):
    '''开始录制路径'''
    robot.startRecordPath(10, ec)
    print_log("startRecordPath",ec)
    
def stop_record_path(robot,ec):
    '''停止录制路径'''
    robot.stopRecordPath(ec)
    print_log("stopRecordPath",ec)

def save_record_path(robot,ec):
    '''保存录制路径'''
    path_name = input("input path name: ")
    robot.saveRecordPath(path_name, ec)
    print_log("saveRecordPath",ec)

def cancel_record_path(robot,ec):
    '''取消录制路径'''
    robot.cancelRecordPath(ec)
    print_log("cancelRecordPath",ec)
    
def query_path_lists(robot,ec):
    '''查询路径列表'''
    lists =  robot.queryPathLists(ec)
    print_log("queryPathLists",ec)
    print(lists)

def delete_path(robot,ec):
    '''删除路径'''
    path_name = input("input delete path name: ")
    robot.removePath(path_name, ec)
    print_log("removePath",ec)
    
def replay_path(robot,ec):
    '''路径回放'''
    name = input("input replay path name: ")
    robot.disableDrag(ec)
    robot.setOperateMode(xCoreSDK_python.OperateMode.automatic, ec)
    robot.setPowerState(True, ec)
    robot.replayPath(name, 1, ec)
    robot.moveStart(ec)
    print_log("replayPath",ec)
    
if __name__=="__main__":
    try:
        ip = "192.168.0.160"
        robot = xCoreSDK_python.xMateRobot(ip)
        ec = {}
        drag_op(robot,ec)
    except Exception as e:
        print(f"An error occurred: {e}")