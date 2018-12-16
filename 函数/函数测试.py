# 1,多个返回值
'''
def test1(a,b):
    print(a)
    print(b)
    return a,b

print(test1(b=11,a=22))
'''

'''
# 2，缺省参数
def printinfo(name, age=35,sex='male'):
    # 打印任何传⼊的字符串
    print("Name: ", name)
    print("Age ", age)

#printinfo('zhangsan',age=22,sex='male')
'''

# 3, 不定长参数
def fun(a,b,*arg, **kwargs):
    print('a= ' , a)
    print('b= ' , b)
    print('args= ' , arg)
    print('kwargs= ' , kwargs)


A=[3,4,5,6]
B={'c':'cc','d':'dd'}
fun(22,33,44,55,*A,**B)

