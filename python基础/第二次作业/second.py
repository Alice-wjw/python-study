class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        self.is_running=False

    def start_engine(self):
        if not self.is_running:
            self.is_running=True
            print(f"{self.brand}的引擎启动了")
        else:
            print(f"{self.brand}的引擎已经启动了")
    def drive(self):
        print(f"{self.brand}正在行驶")
class ElectricCar(Car):
    def __init__(self, brand, color,battery_size):
        super().__init__(brand, color)
        self.battery_size=battery_size
    def change(self):
        print(f"{self.brand}正在充电，容量为{self.battery_size}kwH.")

my_car=Car("TESLa","red")
my_car.start_engine()
my_car.start_engine()

my_electriccar=ElectricCar("TELESA",'red',30)
my_electriccar.drive()
my_electriccar.change()

size=0
def add():
    local_var="Add operation"
    global size
    size=size+1
    print(f"size:{size}")
    print(local_var)

def delete():
    local_var="Delete operation"
    global size
    size=size-1
    print(f"size:{size}")
    print(local_var)

from math import pi,sqrt
print ("圆周率pi为",pi)
print(f"25的平方根是{sqrt(25)}")

import datetime as t
now=t.datetime.now()
formtime=now.strftime("%Y-%m-%d %H:%M:%S")
print(f'现在是{now}')
print(f"标准是{formtime}")

with open("greeting.txt","r",encoding='utf-8')as f:
    content=f.read()
    print("---.read()---")
    print(content)
with open('greeting.txt','r',encoding='utf-8')as f:
    lines=f.readlines()
    print('---.readline()---')
    print(lines)
    for line in lines:
        print(line.strip())
if __name__=="__main__":
    add()
    delete()
