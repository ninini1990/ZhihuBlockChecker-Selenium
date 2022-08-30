from util.WinUtil import getWinDesktopPath
from util.TimeUtil import getReportTimeStamp
from util.CommonUitl import convertPageName


def outputReportPage(zhihuUserId, pageName, allLinkCount, blockedLinkCount, blockRate, blockedLinkList):
    cnPageName = convertPageName(pageName)
    # 获取style.css路径
    stylePath = '\"' + __file__ + "\\..\\..\\scripts\\style.css" + '\"'

    # 组装html
    htmlHeader = '<!DOCTYPE html><html lang="cn"><head><meta charset="utf-8"><title>' + cnPageName +' - 检查结果</title><link rel="stylesheet" href=' + stylePath +'></head><body>'

    summary = '<div><b>' + cnPageName + ' - 检查结果</b><p><b>知乎用户ID: ' + zhihuUserId + '，总链接数量：</b>' + str(allLinkCount) + '<b>，被屏蔽数量：</b>' + str(blockedLinkCount) + '，<b>被屏蔽比例：</b>' + str(blockRate) +  '</div><div><p><table class="hovertable">'

    table = '<th>所属页码</th><th>被屏蔽链接</th>'

    # 存在被屏蔽回答时，填充报告页面
    if (len(blockedLinkList) != 0):
        for item in blockedLinkList:
            pageNum = item['pageNum']
            link = '<a href=' + item['link'] + ' target = "_blank">' + item['title'] + '</a>'
            cell = '<tr><td>' + pageNum + '</td><td>' + link + '</td></tr>'
            table = table + cell

    htmlFoot = '</table></div></body></html>'
    reportPage = htmlHeader + summary + table + htmlFoot

    reportFileName = pageName + '_report_' + getReportTimeStamp() + '.html'
    reportFilePath = getWinDesktopPath() + reportFileName

    try:
        f = open(reportFilePath, 'w', encoding="utf-8")
        f.write(reportPage)
        f.close()
        print("生成报告文件成功:<br> {0}".format(reportFilePath))
        return reportFilePath
    except Exception as e:
        print(e, "生成报告文件失败")




