# import time
from time import sleep
import random
from typing import Any

# print("Hello world!")

a = 5.
LEARNING_RATE = 0.01
b = 'hello world'
c = "hello world"
d = """hello world \
hi
hi"""
e = '''hello world
'''
# print(d)
f = 2 + 5
g = 3 - 1
h = 3 * 2
i = 3 / 2 # floating point number
j = 3 // 2 # integer number

# if a < 5:
#     print('a is less than 5')
# elif a > 5:
#     print('a is greater than 5')
# else:
#     print('a is equal to 5')
    
# for i in range(2, 10, 2):
#     print(i)

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i > 10:
#         break

5 < 10
5 > 10
5 <= 10
5 >= 10
5 == 5
5 != 5

# for i in range(100):
#     # if i >= 25 and i <= 50
#     if 25 <= i <= 50:
#         print(i)

k = [2, 5, 7, 7, 9, 5, 8, 9, 8, 7, 6]
# k = list([2, 5, 7])
l = list(set(k))
# print(l)
k.append(5)
k.append(20)
k.append(16)
k[1] = 8
# print(k)
l = list(set(k))
# print(l)

m = {"e": 5, 7: 3}
n = dict(e=5, d=3)
# o = dict(**m)

# print(m, n)

moves = {1: "e4", 2: "e5", 3: "Nf3"}

o = set([2, 3, 3, 5, 7, 8,8, 89, 9, 5])

q = tuple([2, 3, 4])
r = (2, 3, 4)
s = (2, )
t = 2, 
u = 2, 3, 4
# print(type(u))
# q[1] = 5


# for val in k:
#     print(val)

# for i in range(len(k)):
#     print(k[i])
    
d1 = dict(e=5, d=4, d2=2, d3=4)
d2 = dict(f=4, c=5)
d3 = d1 | d2
# print(d3)
# print(dict(**d1, **d2))

# print(d3["e"])
d3["e"] = 7
# print(d3)
d3["z"] = 50
# print(d3)


def root(name, n):
    for _ in range(n):
        print(f"Hello {name}")
    return name, n


# values = root("John", 3)
# print(type(values))

def something(*args, **kwargs):
    print(args)
    print(kwargs)

# something(2, 3, 4, 5, a=5, b=2)

# loss = 0
# for epoch in range(20):
#     loss += random.random()
#     print(epoch, loss, end="\r")
#     sleep(1)

f = open("read.txt", 'a')
f.write("hello world\n")
f.write("hello\n")
f.close()

print("hello world", file=open("readthis.txt", 'a'))

with open("contextmanager.txt", 'w') as f:
    f.write("hello world\n")
    f.write("hello\n")
    f.close()

# try:
#     a: str | int = 5
# except RuntimeError:
#     pass
# except SyntaxError:
#     pass

with open("contextmanager.txt", 'w') as f:
    try:
        # body
        pass
    except Exception as e:
        print(e)
    finally:
        f.close()

# try:
#     sleep(10)
#     5 / 0
# except ZeroDivisionError as e:
#     print("zero", e)
# except KeyboardInterrupt:
#     pass
# except Exception as e:
#     print("any", e)
# finally:
#     print("done")
    
class Human:
    def __init__(self, name: str, age: int | float, gender: str) -> None:
        self._name = name
        self._age = age
        self._gender = gender
        self._random_list = [random.randint(0, 25) for _ in range(10)]
        self._random_dict = {"e": 25, "g": 325, "er": 325}
    
    @property
    def name(self):
        return self._name
    
    # @name.setter
    # def name(self, value):
    #     self._name = value
    
    @property
    def age(self):
        return self._age
    
    @property
    def gender(self):
        return self._gender
    
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old and gender is {self.gender}"
    
    def __call__(self, message: str) -> Any:
        return message + " " + message
    
    def __getitem__(self, key: str) -> Any:
        return self._random_dict[key]
    
    def __len__(self):
        return len(self._random_list)
    

class Driver(Human):
    def __init__(self, name: str, age: int, gender: str, role: str) -> None:
        super().__init__(name, age, gender)
        self.role = role
        
    # @property
    # def role(self):
    #     return self._role
    
    # @role.setter
    # def role(self, value):
    #     self._role = value

# h1 = Human("John", 25, "male")
# d1 = Driver("Bob", 25, "female", "main driver")
# print(h1)
# print(h1("hi"))
# print(h1["e"])
# print(len(h1))
# print(h1.name)
# # h1.name = "John Smith"
# # print(h1.name)
# print(d1.name)
# h1.name = "Bob Bob"

print(k)
print(k[2:])
print(k[:2])
print(k[::-1])
print(k)
# k.reverse()
k.sort(reverse=True)
print(k)
z = [[5, 7, 9], [2, 5, 6], [3, 5, 7]]

# 5 7 9
# 2 5 6
# 3 5 7
print(z[::])