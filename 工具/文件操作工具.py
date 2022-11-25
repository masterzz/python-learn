import tkinter
import tkinter.simpledialog

class MyFile:
    # def __init__(self, color,size,direction):
    #     self.color = color
    #     self.size = size
    #     self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction == "up"

    def readFile(self, fileName):
        with open(file=fileName, mode='w+', encoding='utf-8') as f:
            f.write('666')

    # 弹出输入框
    def getWindow(self):
        root = tkinter.Tk()
        btn = tkinter.Button(root, text='获取', command=self.askname)
        btn.pack()
        root.mainloop()

    def askname(self):
        result = tkinter.simpledialog.askstring(title='信息', prompt='请输入：', initialvalue='初始值')
        print(result)




if __name__ == "__main__":
    # myball = MyFile()
    # myball.direction = "down"
    # myball.color = "red"
    # myball.size = "small"
    # mylinear()
    print("test")
    file = MyFile()
    file.getWindow()



