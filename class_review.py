
"""
class很自由，三種定義屬性的方法
"""
class TestInitAttr:
    hello = 'hello at fitrst line!' # 可以在init外
    def __init__(self):
        self.hello__init__ = 'hello in __init__'

TestInitAttr.hello # 在init外宣告，就不需要初始話就可以讀取
ta = TestInitAttr()
print(ta.hello)
print(ta.hello__init__)
ta.hello__send__ = 'hello outside.' # 也可以在class外另外輸入給instance
print(ta.hello__send__)

"""
Class有三個主要特性:
1. 封裝(encapsulation)
2. 繼承(inheritance)
3. 多型(polymorphism)
"""

"""
1. 繼承
"""
class Employee:
    """
    這是一個__doc__會跑出來的資訊
    """
    def __init__(self):
        self.base_skill = 'cut_tree'

class Andy(Employee):
    def __init__(self):
        super().__init__() # 呼叫父類別，將繼承父類所有屬性和方法。如果子類別有重複的，子類別將會替代父類。
        self.more_skill = 'can_swim'

    def intro(self):
        print('----intro----')
        print(self.base_skill)
        print(self.more_skill)

    def working(self, t=10):
        print(f'working for {t}')
        print('calling sleep mtehod.')
        self.__sleep()

    def __sleep(self): #
        print(f'sleeping for 10')

andy = Andy()
andy.intro()
andy.working(10)
andy.__sleep()

"""
多型: 一樣名字的方法，卻做不同的事情
"""
class Ken(Employee):
    def __init__(self):
        super().__init__()
        self.more_skill = 'can_hiking'

    def working(self, t):
        print(f'working for {t} hiking')
ken = Ken()
ken.working(10)

print(Employee.__doc__)
print(ken.__doc__) # __doc__不會被繼承

print(Employee.__class__)
print(ken.__class__)

print(Employee.__dict__)

"""
StaticMethods 使用方法：
    在 def 函式上加上 @staticmethod
    不用傳入 self 參數

    ▍StaticMethods 使用時機：
    不在需要將 class 實例後才能使用函式，直接像以下範例呼叫 People_StaticMethods.work(4) 即可使用
"""
class EmployeeWork:
    def __init__(self):
        pass

    def sleep(self, time):
        print(f'sleep for {time}')

    @staticmethod
    def working(time):
        print(f'working for {time}')

e = EmployeeWork()
e.sleep(10)
e.working(10)
# staticmethod 可以不用宣告實例就可以用
EmployeeWork.working(10)

"""
ClassMethods 使用方法：
    在 def 函式上加上 @classmethod
    必須傳入 class 本身參數，通常大家都會命名為 cls
    如果要引入 class 其他函式，可以使用 cls().sleep(6)

    ▍ClassMethods 使用時機：
    1. 不在需要將 class 實例後才能使用函式，直接像以下範例呼叫 People_ClassMethods.work(5) 即可使用
    2. 不同於 StaticMethods，因為多引入了 class 本身參數為 cls，可以利用 cls 來 access 其他 class 內的函式
"""
class Employee_ClassMethods:
    def __init__(self):
        pass

    def sleep(self, time):
        print(f'sleep for {time}')

    @classmethod
    def working(this_cls, time):
        print(f'work for {time}')
        this_cls().sleep(10)

ec = Employee_ClassMethods()
ec.sleep(10)
ec.working(20)
Employee_ClassMethods.working(100)
# 可以加上classmethod
ec.eating = classmethod()



class Student:
    # creating a variable
    name = "Geeksforgeeks"

    # creating a function
    def print_name(obj):
        print("The name is:", obj.name) 

Student.__dict__
# creating print_name classmethod
# before creating this line print_name()
# can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be call as classmethod
# print_name() method is called as class method
Student.print_name()
