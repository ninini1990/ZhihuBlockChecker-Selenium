import os
import socket


# 获取系统用户目录名称
def getWinUserName():
    winUserHome = os.path.expanduser('~')
    winUserName =os.path.split(winUserHome)[-1]
    return winUserName


# 获取用户桌面路径, 输出结果"C:\Users\UserName\Desktop\"
def getWinDesktopPath():
    winUserName = getWinUserName()
    winDesktopPath = "C:\\Users\\" + winUserName + "\\Desktop\\"
    return winDesktopPath


# 启动浏览器前检查端口是否可用
# def isPortAvailable(ip, port):
#     try:
#         if port >= 65535:
#             raise(Exception, "端口设置不能超过65535")
#
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(500)
#         s.connect((ip, port))
#         s.shutdown(2)
#         s.close()
#         print("端口 {0} 可用".format(port))
#         return True
#     except Exception as e:
#         print(e, "端口 {0} 已被占用, 或浏览器已启动".format(port))
#         return False
