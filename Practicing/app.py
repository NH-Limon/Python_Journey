# import app2
# print(app2.add(10,20));
# print(app2.subtract(10,20));
# print(app2.name)

# Specific import: 😀
# from app2 import add, name
# print(add(10,30))
# print(name)

# All import: 😀
# from app2 import *
# print(name)
# print(add(100,5))
# print(subtract(10,2))

# Built-in module import: 😀
# import sys
# print(sys.path)

# Renaming module: 😀
# import app2 as a
# from app2 import add as a
# print(a(100,200))

# dir(): 😀
# import app2
# print(dir(app2))

# Using some builtin modules of pyhton:😀
# import math
# print(math.pi)
# print(int(math.sqrt(100)))
# print(math.sin(90))
# print(math.pow(5,3))
# import random
# print(random.random()) # 0 - 1 Floating Random Numbers
# print(random.randint(10, 20)) # 10-20 Integer Random Numbers
# fruits = ["Lichi", "Mango", "Banana"]
# print(random.choice(fruits))
# import datetime as dt
# from datetime import date
# import time
# print(time.time())

# Using packages: 😀
# from MyPythonPackage import mod1
# mod1.showName()
# mod1.showAge()
# import MyPythonPackage
# MyPythonPackage.mod1.showName()
import MyPythonPackage.mod1 as m1
# print(sum(100, 20))
m1.showAge()