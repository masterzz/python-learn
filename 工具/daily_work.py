import os

from 文件操作工具 import MyFile


# 只要是有反馈工作方案的，就创建一个目录
def mkdirs():
    file = MyFile()
    dict1 = file.read_excel("D:\work\政企BG\肇庆-交流\政数局驻场\\202307\首席数据官\首席数据官反馈统计.xlsx")
    # 读出所有有反馈工作方案的单位
    # print(dict1)
    l = len(dict1.values())
    area = []
    for i in range(1, l + 1):
        temp = dict1.get(i)
        if temp.get("是否反馈工作方案") == "是":
            area.append(temp.get("单位名称"))
    # 根据单位名称创建目录
    dire = "D:\\work\\政企BG\\肇庆-交流\\政数局驻场\\202307\\首席数据官\\方案\\各单位方案"
    filenames = []
    for i in area:
        filenames.append(i)
    file.mkdirs(dir=dire, list=filenames)
    # 将类似名称文件放入文件夹
    # 先拿到所有文件
    get_files = []
    for i in os.listdir(dire):
        if os.path.isfile(dire + "\\" + i):
            get_files.append(i)
    print(get_files)
    # 判断文件名是否匹配
    for i in filenames:
        for j in get_files:
            if i.replace("区府办", "").replace("县府办", "").replace("市府办", "") in j:
                os.replace(dire + "\\" + j, dire + "\\" +i + "\\" + j)


if __name__ == '__main__':
    mkdirs()
