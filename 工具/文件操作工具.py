import os
import tkinter
import tkinter.simpledialog
import jieba
import math
import re
import pandas as pd
import xlrd2    #xlrd: 对Excel进行读相关操作
import xlwt    #xlwt: 对Excel进行写相关操作，且只能创建一个全新的Excel然后进行写入和保存。

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
        # print("\n余弦相似度为：%f" % result)
        return result

    # python读入文件内容，全部放入一个字典里
    def read_excel(self, file_name=""):
        dictory = {}
        # 获取表格文件
        book = xlrd2.open_workbook(file_name)
        # 获取表格中的所有sheet
        names = book.sheet_names()
        # 获取第一个sheet
        sheet = book.sheet_by_index(0)
        # 获取当前表格的行数
        rows = sheet.nrows
        # 获取当前表格的列数
        cols = sheet.ncols
        # 获取表头文件，即表格第一行
        head = sheet.row_values(0)
        for row in range(rows - 1):
            # 如果当前字典中没有该城市则创建一个
            if not sheet.cell_value(row + 1, 0) in dictory.keys():
                dictory[sheet.cell_value(row + 1, 0)] = {}
            for col in range(cols - 1):
                dictory[sheet.cell_value(row + 1, 0)][head[col + 1]] = sheet.cell_value(row + 1, col + 1)
        return dictory

    # python中，将一个字典，写入到excel里
    def write_excel(self, dic={}, file_name=""):
        wb = xlwt.Workbook()
        sheet = wb.add_sheet('write_test')
        # 先把字典的关键字拿出来
        # 将字典放入列表，把列表内容写入excel
        list = []
        # 处理表头
        head = ['序号']
        for x in dic.get(1).keys():
            head.append(x)
        list.append(head)
        # 逐行处理，list把全部字典内容读取进来
        for i in dic.keys():
            # 每一行一个列表处理
            temp = []
            # 添加序号
            temp.append(i)
            # 添加每一列内容
            item = dic.get(i)
            for j in item.keys():
                temp.append(item.get(j))
            list.append(temp)
            # print(temp)

        # 写入excel中
        for i in range(len(list)):
            for j in range(len(list[i])):
                sheet.write(i, j, list[i][j])
        wb.save(file_name)
        return None

    # python中，将列表，写入到excel里
    def write_excel(self, list=[], file_name="",sheet_name=""):
        wb = xlwt.Workbook()

        sheet = wb.add_sheet(sheet_name)

        # 写入excel中
        for i in range(len(list)):
            for j in range(len(list[i])):
                sheet.write(i, j, list[i][j])

        wb.save(file_name)
        return None

if __name__ == "__main__":
    file = MyFile()

    # 测试弹窗+读取文件
    # file.getWindow()
    # file.write_file("aa.txt")
    # file.read_file("D:\learn\python")
    file.get_window()

    # 测试相似度
    # s1 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    # s2 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    # file.calculate(s1, s2)

    # 测试读取excel
    # file.read_excel("D:\work\党建\\202210\工号管理员\系统管理员清单20221123.xlsx")
    # dictory = file.read_excel("F:\learn\\aa.xls")
    # print(dictory.get(2).get('动作'))

    # 测试写入excel
    # file.write_excel(dic=dictory, file_name="F:\learn\\test.xls")


