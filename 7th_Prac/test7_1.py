# Module Practice

import mod.utils as ut
from datetime import datetime as dt
# from pytz import timezone
import os
import sys

# tz = timezone("UTC")

print(dt.now())
# print(dt.now(tz))
print(ut.dt_now())

data_string = "2023-09-25"
# data_object = dt.strptime(data_string, "%Y-%m-%d")
data_object = ut.dt_strptime(data_string)
print(data_object)

data_object = dt.now()
#data_string = data_object.strftime("%Y-%m-%d")
data_string = ut.dt_strftime(data_object)
print(data_string)

print(os.getcwd())
os.chdir("../")
print(os.getcwd())
print(os.listdir())
os.mkdir("new_directory")
print(os.listdir())
os.rmdir("new_directory")
print(os.listdir())

print(ut.os_getcwd())
ut.os_chdir("../")
print(ut.os_getcwd())
print(ut.os_listdir())
ut.os_mkdir("new_directory")
print(ut.os_listdir())
ut.os_rmdir("new_directory")
print(ut.os_listdir())

print(sys.version)
print(sys.argv)
print(ut.sys_version)
print(ut.sys_argv)

# Data Structure
# STACK in Python

stack = []

for i in range(5):
    a = input()
    stack.append(a)
    
print(stack)

for i in range(5):
    top = stack.pop()
    print(top)
    
# QUEUE in Python

queue = []

for i in range(5):
    a = input()
    queue.append(a)
    
print(queue)

for i in range(5):
    front = queue.pop(0)
    print(front)