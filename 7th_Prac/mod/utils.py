import math
import random
from datetime import datetime
import os
import sys

def mt_sqrt(x):
    return math.sqrt(x)

def mt_sinpi():
    return math.sin(math.pi / 2)

def mt_log():
    return math.log(math.e)

def mt_exp(x):
    return math.exp(x)

def mt_pi():
    return math.pi

def rd_randrange(a, b):
    return random.randrange(a, b)

def rd_choice(ls):
    return random.choice(ls)

def rd_random():
    return random.random()

def rd_normalvariate():
    return random.normalvariate()

def dt_now():
    return datetime.now()

def dt_strptime(objtime):
    return datetime.strptime(objtime, "%Y-%m-%d")

def dt_strftime(strtime):
    return strtime.strftime("%Y-%m-%d")

def os_getcwd():
    return os.getcwd()

def os_chdir(path_):
    return os.chdir(path_)

def os_listdir():
    return os.listdir()

def os_mkdir(filename_):
    return os.mkdir(filename_)

def os_rmdir(filename_):
    return os.rmdir(filename_)

sys_version = sys.version
sys_argv = sys.argv