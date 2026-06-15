"""添加库文件路径"""
import sys
import os

def add_release_path():
    # 获取Release文件夹路径并添加到执行路径
    current_directory = os.path.dirname(os.path.abspath(__file__))
    root_directory = os.path.join(current_directory, '..')
    release_directory = os.path.join(root_directory, 'Release')
    
    windows_directory = os.path.join(release_directory, 'windows')
    linux_directory = os.path.join(release_directory, 'linux')
    
    pyi_w_directory = os.path.join(windows_directory, 'xCoreSDK_python')
    pyi_l_directory = os.path.join(linux_directory, 'xCoreSDK_python')
    
    sys.path.append(root_directory)
    sys.path.append(release_directory)
    sys.path.append(windows_directory)
    sys.path.append(linux_directory)
    sys.path.append(pyi_w_directory)
    sys.path.append(pyi_l_directory)
# 执行路径添加函数
add_release_path()