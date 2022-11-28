from 工具.文件操作工具 import MyFile

# 计算每个人意见的相似度
def calculate():
    # 1、完成原始文件的读取、处理
    mf = MyFile()
    dic = mf.read_excel("D:\work\党建\\202210\工号管理员\\校验.xls")

    # 定义最终要写出去的dic1，加上每一项意见相似度最高的情况
    # 定义四个列表代表4类意见
    # list1:品德方面意见;list2:能力方面意见;list3:勤勉方面意见;list4:业绩方面意见
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for i in range(len(dic.keys())):
        list1.append(dic.get(i+1).get("品德方面意见"))
        list2.append(dic.get(i + 1).get("能力方面意见"))
        list3.append(dic.get(i + 1).get("勤勉方面意见"))
        list4.append(dic.get(i + 1).get("业绩方面意见"))

    # 2、计算出每一项最大相似的意见
    # 定义一个系数说明相似度,以及如果算出来最相似的就记录下来编号为key
    # 品德方面意见
    for i in range(len(list1)):
        num = -1
        key = -1
        for j in range(len(list1)):
            if i == j:
                continue
            cal = mf.calculate(list1[i],list1[j])
            if num < cal:
                num = cal
                key = j
        # print(i+1,key+1,num)
        # pass

    # 能力方面意见
    for i in range(len(list2)):
        num = -1
        key = -1
        for j in range(len(list2)):
            if i == j:
                continue
            cal = mf.calculate(list2[i],list2[j])
            if num < cal:
                num = cal
                key = j
        # print(i+1,key+1,num)
        # pass

    # 勤勉方面意见
    for i in range(len(list3)):
        num = -1
        key = -1
        for j in range(len(list3)):
            if i == j:
                continue
            cal = mf.calculate(list3[i],list3[j])
            if num < cal:
                num = cal
                key = j
        # print(i+1,key+1,num)
        # pass
    i = 1

    # 业绩方面意见
    for i in range(len(list4)):
        num = -1
        key = -1
        for j in range(len(list4)):
            if i == j:
                continue
            cal = mf.calculate(list4[i],list4[j])
            if num < cal:
                num = cal
                key = j
        print(i+1,key+1,num)
        # pass
    i = 1

    # 取出list1-4中的每一项比对，拿到最大值放进去，包括姓名、相似意见、相似度
    for i in range(len(dic.keys())):
        # print(i)
        pass

    # 将处理完的dic1做整理
    dic1 = {}
    # 3、整理进dic1进行输出

    mf.write_excel(dic,"D:\work\党建\\202210\工号管理员\\tt.xls" )
    return None

if __name__ == "__main__":
    calculate()