# 创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字，
# 再创建一个名为finished_sandwiches的空列表。遍历列表sandwich_orders，
# 对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich，
# 并将其移到列表finished_sandwiches中。所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['duck','fish','cache','tofu']
finished_sandwiches = []
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)
print(f"all the sandwich finished {finished_sandwiches}")
