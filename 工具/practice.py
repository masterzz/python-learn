from 工具.文件操作工具 import MyFile

if __name__ == "__main__":
    file = MyFile()
    # file.getWindow()
    # file.write_file("aa.txt")
    # file.read_file("D:\learn\python")
    # file.get_window()
    s1 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    s2 = "同志坚决拥护中国共产党的领导，能不折不扣贯彻落实党中央和上级党组织各项决策部署；坚决执行公司规章制度，工号创建变更按照规范流程开展，对于离职的员工或者第三方人员及时清理。"
    file.calculate(s1, s2)
