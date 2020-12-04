# SpiderOnFinance
## 起因：
项目中，我们需要一些能有效爬取的非法金融原始数据源，但现阶段非法金融原始数据源爬取数量不如预期，于是笔者前段时间去其它网址逛了一逛。
## 经过：
现阶段很多网站都配置了一定的反扒技术，尤其像这种金融数据源网站，笔者略过了一些技术复杂度比较高的反爬技术（如验证码、封IP、滑块验证等），针对一般的反扒技术爬取了相关的金融原始数据源。
## 快速简单入手
### 准备基础：
笔者 python版本2.7.16，操作系统为deepin，python编辑器为Pycharm
接下来展示实际爬取的案例
1. Clone本地的python代码文件，接着用pycharm编辑器打开这些文件

 ![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/1.png)

2. 爬取目标为中国银监会上的处罚信息公开表，如下所示
 
 ![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/2.png)
 
3. 运行requesthtml.py程序，得到银监会相当数量的信息公开表（如下所示）
 
 ![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/3.png)
 
4. 爬取目标为网贷天眼上可疑公司相关数据（如下所示）
 
 ![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/4.png)
 
5. 运行项目中P2P.py,得到相关爬取数据信息源，在项目的P2P.et文件中爬取收集了5000多个可疑公司数据信息
 
 ![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/5.png)
 
6. 此外还有爬取的公司融资网友评价信息等等，就不一一举例，运行相关代码即可。

![image](https://github.com/GreenEli/SpiderOnFinance/blob/main/pic/6.png)
