from util.JsonUtil import getJsonUserOption, getJsonSelectors


# 获取要检查的页面名称
def getPageNameList():
    userOption = getJsonUserOption()
    pageNameList = userOption['selectedPageName'].split(",")
    return pageNameList


# 页面名称转换为中文
def convertPageName(pageName):
    pageNameDict = {
        'answers': '回答',
        'posts': '文章',
        'zvideos': '视频',
        'pins': '想法'
    }
    return pageNameDict[pageName]


# 获取判断屏蔽的标识
def getBlockFlag():
    data = getJsonSelectors()
    return data['blockFlag']
