prompt = "\n请输入一个城市名："
prompt += "\n如果你想退出，请键入quit\n"
citys = []
while True:
    city = input(prompt)
    if city == 'quit':
        print(f"你喜欢的城市如下：{citys}")
        print("this is a new grammar")
        break
    else:
        citys.append(city)
        print(f'I would like to visit {city.title()} again')
