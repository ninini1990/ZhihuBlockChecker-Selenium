# Author: 尼尼尼@知乎
# HomePage: https://www.zhihu.com/people/nidaye2

from util.TimeUtil import *
from util.CommonUitl import *
from util.RequestUtil import requestLink
from project.BrowserHandler import *
from project.ReportHandler import outputReportPage


# 检查功能函数
def checkLink(browser, pageName):
    try:
        # 设置全局变量
        allLinkList = []
        blockedLinkList = []
        blockFlag = getBlockFlag()
        zhihuUserId = getUserId()
        pageBase = getPageBase(pageName)
        cnPageName = convertPageName(pageName)

        # 获取对应页面Seletor
        selectors = getJsonSelectors()
        selector = selectors[pageName]

        # 进入该页面类型的首页
        url = getPageUrl(pageBase, 1)
        browser.get(url)

        # 获取该页面类型的总页数
        pageCount = getPageCount(browser)
        pageNum = 1

        # 获取该页面类型要检查的全部链接
        print("开始获取页面中的链接...")
        while(pageNum <= pageCount):
            # 拼接页面URL并打开对应页面
            pageUrl = getPageUrl(pageBase, str(pageNum))
            browser.get(pageUrl)

            # 等待页面加载
            customSleep(getWaitTime())
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            # 获取当前页上所有需要检查的链接
            currentPageList = browser.find_elements(By.CSS_SELECTOR, selector)
            for item in currentPageList:
                link = item.get_property('href')
                title = item.text
                temp = {'pageNum': str(pageNum), 'link': link, 'title': title}
                allLinkList.append(temp)

            print('已获取到第{0}页中的{1}个链接'.format(pageNum, len(currentPageList)))
            pageNum = pageNum + 1

        # 估算检查所需时长
        allLinkCount = len(allLinkList)
        needTime = int((allLinkCount * 3) / 60)
        print('开始检查链接...总计{0}个链接，预计所需时间为{1}分钟'.format(allLinkCount, needTime))

        # 开始批量检测链接
        try:
            for item in allLinkList:
                # 加入随机等待
                customSleep(getWaitTime())
                # 打印检查日志
                timestamp = getTimeStamp()
                index = allLinkList.index(item)
                link = item['link']
                print('{0} 检查中({1}/{2}): {3}'.format(timestamp, index + 1, allLinkCount, link))

                response = requestLink(link, pageName)
                if (blockFlag in response.text):
                    blockedLinkList.append(item)

            # 生成检查结果报告
            blockedLinkCount = len(blockedLinkList)
            if (blockedLinkCount != 0):
                blockRate = format(blockedLinkCount / allLinkCount, '.2%')
            else:
                blockRate = 'n/a'

            print('{0} - 全部链接数量：{1}, 被屏蔽链接数量：{2}, 请求异常数量：{3} '.format(cnPageName, allLinkCount, blockedLinkCount, blockRate))
            print('正在生成报告...')
            report = outputReportPage(zhihuUserId, pageName, allLinkCount, blockedLinkCount, blockRate, blockedLinkList)
        except Exception as e:
            print(e, "当前检查出现网络错误或其它错误，跳过。继续检查下一项。")
    finally:
        print('------ 当前页面项检查完成 ------')


# 检查流程
def checkProcess():
    try:
        # 脚本耗时打点
        startTime = time.perf_counter()

        # 启动浏览器(Debug模式)
        # launchBrowser()

        # 初始化浏览器
        browser = initBrowser()
        if (browser == None):
            raise (Exception, "错误：浏览器实例为空")

        # 获取用户指定检查的页面名称列表
        pageNameList = getPageNameList()

        # 执行检查
        for pageName in pageNameList:
            cnPageName = convertPageName(pageName)
            print('------ 开始检查：' + cnPageName + " ------")
            checkLink(browser, pageName)

        # 关闭浏览器实例,计算脚本实际耗时
        browser.close()
        browser.quit()
        endTime = time.perf_counter()
        timeCost = int((endTime - startTime) / 60)
        print('====== 全部检查执行完毕，脚本总计耗时约{0}分钟 ======'.format(timeCost))

    except Exception as e:
        print(e, '执行发生异常')