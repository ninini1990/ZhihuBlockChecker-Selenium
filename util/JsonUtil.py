import json


# 从配置文件读取JSON，转换为python字典
def readJson(jsonPath):
    f = open(jsonPath, 'r', encoding='UTF-8')
    data = json.load(f)
    f.close()
    return data


# 写入JSON文件
def writeJson(jsonPath, jsonDict):
    try:
        f = open(jsonPath, 'w', encoding='UTF-8')
        json.dump(jsonDict, f, indent=4)
        f.close()
        return True
    except IOError as e:
        print(e, "写入Json文件发生异常")
        return False


# 读取 selectors json
def getJsonSelectors():
    file = __file__ + "\\..\\..\\config\\CssSelector.json"
    return readJson(file)


# 读取 header json
def getJsonHeaderInfo():
    file = __file__ + "\\..\\..\\config\\HeaderInfo.json"
    return readJson(file)

# 读取用户选项 json
def getJsonUserOption():
    jsonPath = __file__ + "\\..\\..\\config\\UserOption.json"
    jsonDict = readJson(jsonPath)
    for (k, v) in jsonDict.items():
        jsonDict[k] = v.strip()
    return jsonDict


# 将用户设置写入到相应JSON文件
def writeJsonUserOption(jsonDict):
    jsonPath = __file__ + "\\..\\..\\config\\UserOption.json"
    writeJson(jsonPath, jsonDict)
    return True

# 读取页面名称与类名的Map
# def getJsonPageClassMap():
#     file = __file__ + "\\..\\..\\config\\PageClassMap.json.reserved"
#     return readJson(file)

# 获取页面名称对应的类
# def getPageClass(pageName):
#     data = getJsonPageClassMap()
#     return data[pageName]
