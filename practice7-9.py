# 练习7-9：五香烟熏牛肉卖完了　使用为完成练习7-8而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
# 在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉（pastrami）卖完了；
# 再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
# 确认最终的列表finished_sandwiches未包含'pastrami'。
sandwich_orders = ['pastrami', 'pastrami', 'tofu', 'tomato', 'fish', 'chicken', 'pastrami']
prompt = "all the pastrami have been sold out"
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(prompt)
print(f"today`s special list:{sandwich_orders}")