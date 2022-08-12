# 练习7-4：比萨配料　编写一个循环，提示用户输入一系列比萨配料，并在用户输入quit'时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料
prompt = "\n请输入需要添加的配料名称："
prompt += "\n请键入quit结束输入\n"
mixture = []

while True:
    spels = input(prompt)
    if spels == 'quit':
        print(f"您的配料如下：{mixture}请让我们开始制作大餐吧")
        break

    else:
        mixture.append(spels)
        print(f"{spels.title()} 已添加，请继续输入")
