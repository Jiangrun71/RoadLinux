# 参数赋值
name = input("请输入你的姓名：")
age = int(input("请输入你的年龄："))
weight = float(input("请输入体重，可精确到小数点后两位："))
# 打印信息
print("您的个人信息如下：")
# 引用参数
print("姓名：%s" % name)
print("年龄：%s" % age)
if age >= 18:
    print("您已经成年，可以进去")
# if 判断语句
else:
    print("小屁孩 滚回去学习！")
if weight >= 80:
    print("死胖子，你需要减肥了")
else:
    print("小伙子，身材不错啊！！")
# i = 1
# while i <= 5:
# print("hello 这是循环")
# i = i + 1
sum1 = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum1 += i
    i += 1
print("和为：%d" % sum1)


