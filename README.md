<h2> ZhihuBlockChecker-Selenium </h2>
知乎用户用于检查全部创作内容被屏蔽情况的小工具，包括回答、文章、视频、想法等。<p>
目前仅支持Windows10系统、Chrome浏览器。<p>

**使用过程概述：**<p>
下载解压后运行exe -> 输入知乎用户ID -> 保存设置 ->启动浏览器(并手工登录) -> 执行检查。<p>
说明文档位置：工具界面 -> 帮助菜单 -> 使用说明。

**下载地址：**<p>
百度网盘: https://pan.baidu.com/s/1cYQtcfRqW_IsrOBNch4Zew?pwd=6666  --子目录：知乎屏蔽检查工具(Selenium版) <p>
Github: https://github.com/ninini1990/ZhihuBlockChecker-Selenium/releases<p>

**运行环境需求：**<p>
Windows 10 (64位), Chrome浏览器 (v104 或其他较高版本, 64位）<p>
暂时未对其它环境/版本进行详细测试。

**问题反馈：**<p>
知乎私信，或发送邮件到 ninini19900319@gmail.com
 
---
<h2>使用提示</h2> <p>

**安全性：**<p>
1. 此工具只发布于上述 Github和百度网盘指定的两个分享链接。不要从其它来源下载。<p>
2. 工具中只需要输入你的知乎用户ID, 不需要输入密码。<p>
第一次执行时需要人工登录，是在Chrome浏览器中操作。<p>
此工具不会获取、保存、发送你的用户密码。<p>
3. 如果仍然担心安全性，可从Github下载源码。在本地安装Python环境，并执行脚本。入口是Pyqt_Instance.py<p>

**使用风险提示：**<p>
虽然已使用Selenium模拟用户操作，且设置了合理的检查间隔，但仍然不要过度频繁使用。<p>
以免被知乎识别为爬虫，导致用户IP、账户被屏蔽。<p>
建议使用频率为一周一次。<p>

**开源协议:**<p>
使用GPL3协议，请保持代码开源及遵守GPL3其他规则。

---
<h2>安装及使用详细说明</h2><p>


1. 从Github或百度网盘指定地址，下载最新版本的zip压缩包。<p>  
  
2. 解压到任意目录。路径中不要包含中文，且需要有大于200MB的磁盘空间 (运行时Chrome用户文件所需空间)。<p>
  
3. 双击执行ZhihuBlockChecker.exe <p>
  
![image](https://user-images.githubusercontent.com/112439804/187325189-0a291217-6c9c-4330-9d5c-5775eb1c309b.png)<p>
  
4. 在工具界面中输入你的知乎用户ID (非知乎用户名）。<p>
例如一个知乎用户的个人主页链接是 https://www.zhihu.com/people/heheda111 <p>
那么对应的知乎用户ID就是 heheda111<p>
  
![image](https://user-images.githubusercontent.com/112439804/187323968-3f7ee940-5c5e-4ae2-b783-8416b6481261.png)<p>
  
![image](https://user-images.githubusercontent.com/112439804/187323927-8ed39060-4257-44df-b1fa-1b805a0e93b0.png)<p>
  
5. 选择需要检查的项目：回答、文章、视频、想法。可选择单个或多个。<p>
其中“想法”的数量一般较多，且价值较低，不建议检查。<p>
  
![image](https://user-images.githubusercontent.com/112439804/187318983-00b368a1-25da-4272-9949-61e0a91778da.png)<p>
  
6. 设置检查时间间隔，防止被识别为爬虫。<p>
最小值为1秒（不可修改），最大值默认为3秒（可修改）。<p>
  
![image](https://user-images.githubusercontent.com/112439804/187319847-eca651a7-9371-4c24-baf2-88dc68dacede.png)<p>
  
7. 设置Chrome浏览器信息。目前只允许设置其监听端口，默认为8888。<p>
如果已被其它程序占用，可自定义为其它端口。不能大于65535。<p>
Chrome安装路径需要确认为 "C:\\Program Files (x86)\\Google\\Chrome\\Application" （通常默认安装在此路径下）<p>
  
![image](https://user-images.githubusercontent.com/112439804/187319865-13c4528c-2b52-4fc5-895a-9642a3acf036.png)<p>
  
8. 如果修改了上述设置后，请先点击“保存设置”按钮。<p>
  
![image](https://user-images.githubusercontent.com/112439804/187324053-e4c9837c-a5a6-4fcb-898d-948586e71302.png)<p>
  
9. 保存设置后，请点击“启动浏览器”按钮，会自动启动一个单独的Chrome实例并打开知乎首页。<p>
与你自己打开的Chrome不冲突，不需要关闭你正在使用的Chrome页面。<p>
第一次通过工具启动浏览器时，打开的知乎页面是未登录状态，需要手工登录你的知乎账户。<p>
登录一次之后，在知乎cookie失效之前(大约半年），再执行检查都不需要再做这一步登录操作。<p>
如cookie失效之后，又会进入未登录页面，再手工登录一次就好。<p>

![image](https://user-images.githubusercontent.com/112439804/187320429-76ed4425-fd15-471e-801a-08fee7bb8dca.png)<p>
  
![image](https://user-images.githubusercontent.com/112439804/187551588-dba7dd7f-2a1a-4802-8c44-40797629eef0.png)<p>
  
10. 通过工具启动Chrome浏览器，并确认已登录知乎账户之后，点击“执行检查”按钮。<p>
工具即开始检查你所选择的项目。检查700个回答大约需要40分钟。<p>
最终结果会以html页面输出到你的桌面上（暂时不支持修改保存路径)。<p>
  
![image](https://user-images.githubusercontent.com/112439804/187551226-8637a1f5-7751-412c-bda2-133a123d64f8.png)<p>
  
11. 检查结果示例<p>
  
![image](https://user-images.githubusercontent.com/112439804/187554384-828d38e8-8c3e-4156-9cef-cdc2bdbe6c13.png)






