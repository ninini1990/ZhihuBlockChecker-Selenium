import time
import random
import threading

from util.JsonUtil import getJsonUserOption


# 根据用户指定的上下限，生成生成随机等待时间(秒，两位小数)
def getWaitTime():
    data = getJsonUserOption()
    minDelayTime = int(data['minDelayTime'])
    maxDelayTime = int(data['maxDelayTime'])
    waitTime = round(random.uniform(minDelayTime, maxDelayTime), 2)
    return waitTime


# 自定义等待方法
def customSleep(t):
    event = threading.Event()
    event.wait(t)


# 估算脚本执行时长(分钟，整数)
def calcScriptTime(list):
    allCount = len(list)
    scriptTime = int((allCount * 3) / 60)
    return scriptTime


# 获取时间戳
def getTimeStamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 报单独处理告文件名的时间戳
def getReportTimeStamp():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())
