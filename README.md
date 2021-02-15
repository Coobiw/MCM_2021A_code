# MCM_2021A_code

## 介绍
The repository is about some of my codes which I do in 2021 MCM Question A. 
这一资料仓库是关于我在此次2021年数学建模美赛A题的部分数据和代码。

### 数据来源声明：

[1]Fungi Database: https://github.com/dsmaynard/fungal_biogeography/tree/master/fungi_data.

[2]WorldClim Global Climate Data database(https://www.worldclim.org/)

[3]The vegetation distribution data (https://commons.wikimedia.org/wiki/File:Vegetation.pn)

代码均采用python编程语言，虚拟环境选用Anaconda管理python的相关库（如：numpy,pandas,matplotlib,sklearn,scipy等）

## 软件功能

### 软件功能说明：

[1]2Dpicture和3D-Normal这个两个.py文件是用于绘制真菌生长速率随温度湿度两个因素的变化的2D和3D图像，其中，2D图像选用了热力图进行描述，3D图像选择使用surface图并显示除了三个平面上的等高线轮廓，比较清晰。

[2]double.py文件是用来描述双真菌/多真菌的微分方程求解，此处使用了SIS model和种群竞争模型的结合，导致微分方程难以求得解析解，为了可视化方便我们仍采用定量分析，故选择求数值解并进行绘图（注意：前段部分是Logistic（单种群S型曲线增长），后半部分是微分方程的数值解绘制的曲线）。

[3]Logistic.py文件在一张figure中绘制了4种真菌的单种群增长曲线与增长率曲线。

[4]Normal_fit.py文件是利用最小二乘法拟合两个正态分布，为何要描述两个可详见我们的论文解析。

[5]Regression.py文件是用多元回归分析，确定真菌分解速率与真菌的生长速率、真菌的耐湿性的线性关系（数据见data文件夹），并做出了三维图和投影的两个二维图。（三元回归分析）

[6]剩余两个文件则是绘制了树木的分解百分比（纵坐标单位：%）与树木的分解百分比速率（单位：%/day）随时间的变化曲线，公式仍参见我们的论文。

若对我们的论文感兴趣，可以给我的个人邮箱发邮件，在情况允许后，会进行分享。

