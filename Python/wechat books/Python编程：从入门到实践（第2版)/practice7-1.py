#编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，下面是一个例子
#Let me see if I can find you a Subaru.
cars = (input("which kind of cars will you rent:\n"))
print(f"Let me see if I can find you a {cars}")
people_num = int(input("how many are you will for lunch:\n"))
if people_num > 8:
    print(f"there are no enough desks for you guys")
else:
    print(f"{people_num} desks are enough")

input_num = int(input("please input an number:\n"))
if input_num % 100 == 0:
    print(f"the number {input_num} is double than 100")
else:
    print(f"the number {input_num} is an odd" )