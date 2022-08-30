# Author: 尼尼尼@知乎
# HomePage: https://www.zhihu.com/people/nidaye2

import os
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from util.JsonUtil import getJsonSelectors, getJsonUserOption
from util.TimeUtil import customSleep


# 获取知乎用户ID
def getUserId():
    data = getJsonUserOption()
    return data['zhihuUserId']


# 获取用户主页
def getHomePage():
    data = getJsonUserOption()
    homePage = "https://www.zhihu.com/people/" + data['zhihuUserId']
    return homePage


# 设置当前检查页面的URL主干
def getPageBase(pageName):
    home = getHomePage()
    pageBase = home + "/" + pageName + "?page="
    return pageBase


# 组装页面链接
def getPageUrl(pageBase, pageNum):
    return pageBase + str(pageNum)


# 设置Selenium浏览器参数
def getBrowserOptions():
    data = getJsonUserOption()
    browserAddress = data['browserIp'] + ":" + data['browserPort']
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("debuggerAddress", browserAddress)
    return opts


# 判断登录状态
def isLogin(browser):
    try:
        selectors = getJsonSelectors()
        writeCenterCard = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selectors['writeCenterCard']))
        )
        print('检测登录状态成功：用户已登录')
        return True
    except Exception as e:
        print(e, '检测登录状态出错：用户未登录，或与设置的用户不一致')
        return False


# 启动Debug模式浏览器
def launchBrowser():
    userOption = getJsonUserOption()
    chromePath =userOption['chromeInstallPath']
    port = userOption['browserPort']
    profilePath = __file__ + "\\..\\..\\log\\profile"

    os.system('chcp 65001')
    folderCmd = chromePath
    launchCmd = 'chrome.exe https://www.zhihu.com --remote-debugging-port=' + port + ' --user-data-dir=' + '"' + profilePath + '"'
    subprocess.Popen(launchCmd, shell=True, cwd=folderCmd)


# 初始化浏览器
def initBrowser():
    print('开始初始化浏览器...')
    try:
        opts = getBrowserOptions()
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
        browser.implicitly_wait(10)
        # 打开用户主页
        homePage = getHomePage()
        browser.get(homePage)
        customSleep(5)
        # 检查是否已经登录
        if(isLogin(browser) == False):
            raise (Exception, '用户未登录')

        print('浏览器初始化完成')
        return browser

    except Exception as e:
        print(e, '浏览器未启动，或初始化失败')


# 获取相应Page的总页面数量
# 如回答只有一页，不存在翻页栏，则抛出异常，总页数设置为1
def getPageCount(browser):
    print('获取页数中...')

    # 等待页面加载
    customSleep(5)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    selectors = getJsonSelectors()
    try:
        pageBar = browser.find_element(By.CSS_SELECTOR, selectors['pageBar'])
        # 如存在翻页栏，则获取总页数
        pageCountList = browser.find_elements(By.CSS_SELECTOR, selectors['pageCount'])
        pageCount = int(pageCountList[-1].text)
        print("总页数为：{0}".format(pageCount))
        return pageCount

    except Exception as e:
        print('当前用户回答只有一页或发生异常，继续执行')
        return 1
