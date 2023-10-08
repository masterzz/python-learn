import os
import tkinter
import tkinter.simpledialog
import jieba
import math
import re
import pandas as pd
import xlrd2  # xlrd: 对Excel进行读相关操作
import xlwt  # xlwt: 对Excel进行写相关操作，且只能创建一个全新的Excel然后进行写入和保存。


class MyFile:
    # def __init__(self, color,size,direction):
    #     self.color = color
    #     self.size = size
    #     self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction == "up"

    # 对file_name文件，写入content内容
    def write_file(self, file_name, content=""):
        with open(file=file_name, mode='w+', encoding='utf-8') as f:
            f.write('666555')

    # 默认读出directory里的所有文件
    def read_file(self, directory, count=0, type=None):
        for file_name in os.listdir(directory):
            # 判断是否为文件，文件的话直接打印名称，目录的话对下一级目录文件
            # 加了目录的文件名
            file_name1 = directory + "\\" + file_name
            # 打印内容，默认None
            print_content = "	" * count + file_name1
            if type is None:
                print(print_content)
            # type为file时打印全部文件
            if type == "file":
                if os.path.isfile(file_name1):
                    print(print_content)
                    # pass
                if os.path.isdir(file_name1):
                    self.read_file(file_name1, count + 1)
                    # print(file_name1)
                    print("------------------------")

    # 弹出输入框,获取含目录的文件名，然后打印全部文件
    def get_window(self, type=None):
        root = tkinter.Tk()
        # 默认读全部文件
        if type is None:
            btn = tkinter.Button(root, text='获取', command=self.askname)
        btn.pack()
        root.mainloop()

    # 根据文件名，在路径dir中，根据list创建目录
    def mkdirs(self, dir="", list=None):
        if os.path.isdir(dir):
            if list is not None:
                for d in list:
                    filename = dir + "\\" + d
                    if not os.path.exists(filename):
                        os.mkdir(filename)
        pass

    # 跟着getWindow混
    def askname(self):
        result = tkinter.simpledialog.askstring(title='信息', prompt='请输入：', initialvalue='初始值')
        self.read_file(result)

    # 计算余弦相似度,输入s1、s2两个字符串，默认分词用，
    # 参考：https://www.cnblogs.com/HankTown/p/12757832.html
    def calculate(self, s1="", s2="", fstop="，"):
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

    # python读入文件内容，全部放入一个字典里，并返回字典
    def read_excel(self, file_name=""):
        dictory = {}
        # 获取表格文件
        book = xlrd2.open_workbook(file_name)
        # 获取表格中的所有sheet
        names = book.sheet_names()
        # 获取第一个sheet
        sheet = book.sheet_by_name('Sheet1')
        # sheet = book.sheet_by_index(0)
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
    def write_excel(self, list=[], file_name="", sheet_name=""):
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
    # 先读出excel中的全量单位名称
    dict1 = file.read_excel("D:\work\政企BG\肇庆-交流\政数局驻场\\202307\首席数据官\首席数据官反馈统计.xlsx")
    print(dict1)
    # 测试弹窗+读取文件
    # file.write_file("aa.txt")
    # file.read_file("D:\learn\python")
    # file.get_window()

    # 测试相似度
#     s1 = """11:10谈话后拒绝告知抢救查处申请书
# 云浮市卫健局:
# 袁婉芳新生儿医疗纠纷中，在2016年8月25日11:10谈话后，黄谏珍、黄观丽、黄燕华已经知悉新生儿病情:新生儿肺炎、新生儿窒息、新生儿缺氧缺血性脑病，却拒绝对家属告知新生儿须抢救，令家属痛失挽救新生儿生命的机会。该不作为侵犯患者生命健康权，故意人为缩短新生儿生命，涉嫌不作为故意杀人。
# 《医疗事故处理条例》第三十八条患者死亡的，县级人民政府卫生行政部门应当自接到医疗机构的报告或者当事人提出医疗事故争议处理申请之日起7日内移送上一级人民政府卫生行政部门处理。
# 现我们依据《医疗事故处理条例》第三十八条向云浮市卫健局申请查处郁南县人民医院黄谏珍、黄观丽、黄燕华在8月25日11:10谈话后拒绝向家属告知新生儿须抢救，涉嫌不作为故意杀人。
# 患者家属:李翼
# 2022年8月6日
# 电话:13826806051
# 地址:郁南县都城镇商贸二路41号
# 你好！根据云浮市12345政府服务热线管理办法（试行）第二章受理范围第七条规定：内容重复的诉求列入12345政府热线非受理范围。根据你的投诉“反映新生儿医疗纠纷事件的问题”已由省高院终审，同时云浮市卫生健康局也多次调查处理并回复，你现反映的问题没有新理由、新情况，属重复投诉 ，不予受理。"""
#     s2 = """11:10谈话后拒绝下达《抢救通知》查处申请书
# 云浮市卫健局:
# 袁婉芳新生儿医疗纠纷中，在2016年8月25日 11:10谈话后 ，黄谏珍、黄观丽、黄燕华已经知悉新生儿病情:新生儿肺炎、新生儿窒息、新生儿缺氧缺血性脑病，却拒绝对家属下达《抢救通知》，令家属痛失挽救新生儿生命的机会。该不作为侵犯患者生命健康权，故意人为缩短新生儿生命，涉嫌不作为故意杀人。
# 《医疗事故处理条例》第三十八条患者死亡的，县级人民政府卫生行政部门应当自接到医疗机构的报告或者当事人提出医疗事故争议处理申请之日起7日内移送上一级人民政府卫生行政部门处理。
# 现我们依据《医疗事故处理条例》第三十八条向云浮市卫健局申请查处郁南县人民医院黄谏珍、黄观丽、黄燕华在8月25日11:10谈话后拒绝向家属下达《抢救通知》，涉嫌不作为故意杀人。
# 患者家属:李翼
# 2022年8月6日
# 电话:13826806051
# 地址:郁南县都城镇商贸二路41号
# 你好！根据云浮市12345政府服务热线管理办法（试行）第二章受理范围第七条规定：内容重复的诉求列入12345政府热线非受理范围。根据你的投诉“反映新生儿医疗纠纷事件的问题”已由省高院终审，同时云浮市卫生健康局也多次调查处理并回复，你现反映的问题没有新理由、新情况，属重复投诉 ，不予受理。"""
#     cal = file.calculate(s1, s2)
#     print(cal)

# 测试读取excel
# file.read_excel("D:\work\党建\\202210\工号管理员\系统管理员清单20221123.xlsx")
# dictory = file.read_excel("F:\learn\\aa.xls")
# print(dictory.get(2).get('动作'))

# 测试写入excel
# file.write_excel(dic=dictory, file_name="F:\learn\\test.xls")
