import os
import tkinter
import tkinter.simpledialog
import jieba
import math
import re
import pandas as pd
import xlrd

class MyFile:
    # def __init__(self, color,size,direction):
    #     self.color = color
    #     self.size = size
    #     self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction == "up"

    # 对file_name文件，写入content内容
    def write_file(self, file_name,content=""):
        with open(file=file_name, mode='w+', encoding='utf-8') as f:
            f.write('666555')

    # 读出directory里的目录
    def read_file(self, directory, count = 0):
        for file_name in os.listdir(directory):
            # 判断是否为文件，文件的话直接打印名称，目录的话对下一级目录文件
            # 加了目录的文件名
            file_name1 = directory + "\\" + file_name
            # 打印内容
            print_content = "	"*count + file_name1
            if os.path.isfile(file_name1):
                print(print_content)
            if os.path.isdir(file_name1):
                self.read_file(file_name1, count + 1)
                print("------------------------")

    # 弹出输入框,获取含目录的文件名，然后打印全部文件
    def get_window(self):
        root = tkinter.Tk()
        btn = tkinter.Button(root, text='获取', command=self.askname)
        btn.pack()
        root.mainloop()

    # 跟着getWindow混
    def askname(self):
        result = tkinter.simpledialog.askstring(title='信息', prompt='请输入：', initialvalue='初始值')
        self.read_file(result)

    # 计算余弦相似度,输入s1、s2两个字符串，默认分词用，
    # 参考：https://www.cnblogs.com/HankTown/p/12757832.html
    def calculate(self,s1="",s2="",fstop="，"):
        # 读入两个txt文件存入s1,s2字符串中
        # s1 = open('../文本分析/text/2020.txt','r').read()
        # s2 = open('../文本分析/text/2021.txt','r').read()
        # s1 = "好呀，大明，玲玲个fffffffffffffff,"
        # s2 = "好呀，大明，玲玲个fffffffffffffff,"

        # 利用jieba分词与停用词表，将词分好并保存到向量中
        stopwords = []
        fstop = "，"
        for eachWord in fstop:
            eachWord = re.sub("\n", "", eachWord)
            stopwords.append(eachWord)
        s1_cut = [i for i in jieba.cut(s1, cut_all=True) if (i not in stopwords) and i != '']
        s2_cut = [i for i in jieba.cut(s2, cut_all=True) if (i not in stopwords) and i != '']
        word_set = set(s1_cut).union(set(s2_cut))

        # 用字典保存两篇文章中出现的所有词并编上号
        word_dict = dict()
        i = 0
        for word in word_set:
            word_dict[word] = i
            i += 1

        # 根据词袋模型统计词在每篇文档中出现的次数，形成向量
        s1_cut_code = [0] * len(word_dict)

        for word in s1_cut:
            s1_cut_code[word_dict[word]] += 1

        s2_cut_code = [0] * len(word_dict)
        for word in s2_cut:
            s2_cut_code[word_dict[word]] += 1
        # 计算余弦相似度
        sum = 0
        sq1 = 0
        sq2 = 0
        for i in range(len(s1_cut_code)):
            sum += s1_cut_code[i] * s2_cut_code[i]
            sq1 += pow(s1_cut_code[i], 2)
            sq2 += pow(s2_cut_code[i], 2)

        try:
            result = round(float(sum) / (math.sqrt(sq1) * math.sqrt(sq2)), 3)
        except ZeroDivisionError:
            result = 0.0
        print("\n余弦相似度为：%f" % result)

    # def read_excel(self,file_name=""):
        file_name = xlrd.open_workbook(file_name)  # 得到文件
        table = file_name.sheets()[2]  # 得到sheet页
        nrows = table.nrows  # 总行数
        ncols = table.ncols  # 总列数
        i = 0
        while i < nrows:
            cell = table.row_values(i)[1]  # 得到数字列数据
            ctype = table.cell(i, 1).ctype  # 得到数字列数据的格式
            username = table.row_values(i)[0]
            if ctype == 2 and cell % 1 == 0:  # 判断是否是纯数字
                password = int(cell)  # 是纯数字就转化位int类型
                print('用户名：%s' % username, '密码：%s' % password)
            i = i + 1

if __name__ == "__main__":
    file = MyFile()

    # 测试弹窗+读取文件
    # file.getWindow()
    # file.write_file("aa.txt")
    # file.read_file("D:\learn\python")
    # file.get_window()

    # 测试相似度
    s1 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    s2 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    file.calculate(s1, s2)

    # 测试读取excel
    # file.read_excel("D:\work\党建\\202210\工号管理员\系统管理员清单20221123.xlsx")


