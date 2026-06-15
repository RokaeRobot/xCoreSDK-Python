"""
RL程序执行状态

TaskName: 执行的任务名称; 类型string
LookaheadLine: 前瞻行号; 类型int
LookaheadFile: 前瞻到的文件名; 类型string
ExecuteLine: 执行行号; 类型int
ExecuteFile: 正在执行的文件名; 类型string
"""
from __future__ import annotations
__all__ = ['ExecuteFile', 'ExecuteLine', 'LookaheadFile', 'LookaheadLine', 'TaskName']
ExecuteFile: str = 'executeFile'
ExecuteLine: str = 'executeLine'
LookaheadFile: str = 'lookaheadFile'
LookaheadLine: str = 'lookaheadLine'
TaskName: str = 'taskName'
