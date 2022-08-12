"""练习9-1：餐馆　创建一个名为Restaurant的类，为其方法__init__()设置属性restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法."""


class Restaurant:
    def __init__(self, res_name, res_type):
        self.res_name = res_name
        self.res_type = res_type

    def describe_restaurant(self):
        print(f"The restaurant {self.res_name} is open")

    def open_restaurant(self):
        print(f"The restaurant {self.res_name} is {self.res_type}")


my_restaurant = Restaurant('restaurant', 'close')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
