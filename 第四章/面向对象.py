class car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.c_color=c_color
        self.c_brand=c_brand
        self.c_name=c_name
        print("添加完毕")
c1=car("red","bmw","x7",800000)
print(c1.__dict__)