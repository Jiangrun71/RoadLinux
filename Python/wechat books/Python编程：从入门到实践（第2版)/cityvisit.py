prompt = "\n请输入一个城市名："
prompt += "\n如果你想退出，请键入quit\n"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would like to visit {city.title()} again")