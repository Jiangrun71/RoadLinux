#这是我的第一句Python语句
from typing import List

print("hello ,this is my first python program")  #这是当行末尾注释
"""
这是多行注释！！！
"""
#变量赋值
name = "zhang jiang"
age = 18
print(name.title())
print("您的名字是: %s " % name.title())
name = "Eric smith"
print ("hello %s " % name,"Welcome")
print(name.upper())
print(name.lower())
print(name.title())
name = ['zhangjiang','zhangchao','zhangkai','jiangziyi']
message = f"我的名字是{name[2].title()}"
print(message)


names = ['zhangdandan','huanluqian','zhangruifeng']
var1 = f"hello {names[1].upper()}"
print(var1)
names[1] = 'zhangjiang'
print(names)
names.append('zhaoyizhen')
print(names)
names.insert(0,'shuwenhui')
print(names)
del names[3]
print(names)
popped_names = names.pop()
print(names)
print(popped_names)


invitors = ['teacher','boss','parents']
myinvite = f"tonight  I will invite %s " % invitors [1],"to my birthday party"
print(myinvite)
names.sort()
print(names)
print(sorted(names))
names.reverse()
print(names)
len(invitors)
for invitor in invitors:
    print(invitor)
    print(f"{invitor.title()},Welcome to my birthday party")
    print(f"I can`t enjoy it! {invitor.title()}")
print("thank you everyone")
hobbies = ['swim','box','running']
for my_hobby in hobbies:
    print(f'hello, {my_hobby.title()} is my favorite hobby,and you?')
for value in range(1,10):
    print(value)
numbers = list (range(1,5,2))
print(numbers)
cube = []
for value in range (1,5):
    cubes = value ** 2
    cube.append(cubes)

print(cube)
#练习：
squares = []
for value in range (1,6,2):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range (1,9,2):
    squares.append(value ** 2)
print(squares)
#练习：
#使用一个for循环打印数1～20（含）。
for value in range (1,21):
    print(value)
#创建一个包含数1～1 000 000的列表，再使用一个for循环将这些数打印出来。（如果输出的时间太长，按Ctrl + C停止输出或关闭输出窗口。）
list100 = []
for value in range (1,100):
    print(value)
#创建一个包含数1～1 000 000的列表，再使用min()和max()核实该列表确实是从1开始、到1 000 000结束的。
# 另外，对这个列表调用函数sum()，看看Python将一百万个数相加需要多长时间

print(names[0:1])
for name in names[:1]:
    print(name.title())

subjects = ['english','math','chinese']
chao_subje = subjects

subjects.append('biograph')
chao_subje.append('franch')

print("my subjects are:")
print(subjects)

print("chao`s subject are :")
print(chao_subje)

