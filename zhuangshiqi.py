
def makeBold(fn):
    print("BBBBB"*5)
    def wrapped1():   #注意为了演示结果这里讲wrapped函数，分为wrapped1,wrapped2
        print("bbbbb"*5)
        return "<b>" + fn() + "</b>"
    return wrapped1
 
def makeItalic(fn):
    print("IIIII"*5)
    def wrapped2():     #注意为了演示结果这里讲wrapped函数，分为wrapped1,wrapped2
        print("iiiiii" *3)
        return "<i>" + fn() + "</i>"
    return wrapped2
 
#2.使用两个装饰器同时装饰一个函数，可以三个，甚至多个。原理一样
@makeBold   #注意2.其效果等同于test_B_I=makeBold( makeItalic(test_B_I) )
@makeItalic #注意1.其效果等同于test_B_I=makeItalic(test_B_I)
def test_B_I():   
    print("test_B_I"*5)
    return "this is the test_B_I"

print(test_B_I())


class M:
    def __init__(self, x=1):
        self.x = x
        
    def __get__(self, instance, owner):
        print("__get__", instance,owner,self.x)
        return self.x
    
    def __set__(self, instance, value):
        print("__set__", instance, value)
        instance.x=value
        self.x = value

    def __repr__(self):
        return("fgsdggs")
        
# 调用描述器的类
class AA:
    m = M()  # m就是一个描述器
    def __init__(self, x):
        self.x = x
        
aa = AA(5)
bb = M(56)
print(bb)
print(aa.x)
aa.m # 1
aa.m = 2
print(aa.x)
aa.m # 2

class A:
    def __init__(self, name, score):
        self.name = name # 普通属性
        self.score = score
        
    def getscore(self):
        return self._score
    
    def setscore(self, value):
        print('setting score here')
        if isinstance(value, int):
            self._score = value
        else:
            print('please input an int')
            
    score = property(getscore, setscore)
        
a = A('Bob', 90)
b = A('alice', 100)
print(a.name) # 'Bob'
print(a.score) # 90
a.score = 'bob' # please input an int




