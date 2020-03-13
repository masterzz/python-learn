# coding=utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#windws和linux设置字体的方式
# font = {'family' : 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font",**font)
# 这个好像是设置全局的
matplotlib.rc("font",family='MicroSoft YaHei',weight="bold")

#另外一种设置字体的方式
# my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

# dpi:图像每英寸长度内的像素点数
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
print("len1:%s"%len(_xtick_labels))
print("len2:%s"%len(x))
#取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45) #rotaion旋转的度数
# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=font) #rotaion旋转的度数

#
# #添加描述信息，也可以采用fontproperties属性
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟的气温变化情况")

plt.show()