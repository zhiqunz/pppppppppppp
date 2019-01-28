from src.c1 import *
import sys
import os

a = 'aa'

b = 1

c = False

d = [1,2]
add(d[0], d[1])

f = { "age": 1,
      "name": "zhuzhiqun"
      }


def fun():
    print('dd')
    return "ee"


fun()
# print(aa)
# @fun

file_path = '/Users/zhuzhiqun/PycharmProjects/rbitscostfile/utilforbox1.py'
folder_path = '/Users/zhuzhiqun/PycharmProjects/rbitscostfile1'


if os.access(folder_path, os.R_OK):
    print('ok')
else:
    print('not exist')

print("*"*30)
print(sys.argv)
print("*" * 30)