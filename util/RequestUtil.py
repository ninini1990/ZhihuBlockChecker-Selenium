import requests
from retrying import retry

from util.JsonUtil import getJsonHeaderInfo
from util.TimeUtil import getWaitTime, customSleep
from project.BrowserHandler import getHomePage


# 链接检测方法。最大重试3次, 如3次全部错误则抛异常
@retry(stop_max_attempt_number=3)
def requestLink(url, pageName):
    customSleep(getWaitTime())
    # 单独组装referer
    hds = getJsonHeaderInfo()
    referer = getHomePage() + '/' + pageName
    hds['Referer'] = referer
    # 超时或状态码不是200时, 报错并重试
    response = requests.get(url, headers=hds, timeout=5)
    assert response.status_code == 200
    return response

