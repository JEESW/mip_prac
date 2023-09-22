# import calc

# add_res = calc.add(3, 2)
# sub_res = calc.sub(3, 2)
# mul_res = calc.mul(3, 2)
# div_res = calc.div(3, 2)

import calc as cl

add_res = cl.add(3, 2)
sub_res = cl.sub(3, 2)
mul_res = cl.mul(3, 2)
div_res = cl.div(3, 2)

print(add_res)
print(sub_res)
print(mul_res)
print(div_res)

import mod.circle_mod as cmod

print(cmod.pi)
print(cmod.circum(4))
print(cmod.cir_area(4))

import mod.str_util as smod

url = "https://www.notion.so/test/4-1/a1fe5ef0df1/41f7a1aa9ec01/3a859a"
res = smod.cutword(url, "/", 3)

print(res)

import math
import random
import mod.utils as ut

print(math.sqrt(6))
print(math.sin(math.pi / 2))
print(math.log(math.e))
print(math.exp(3))
print(math.pi)

print(ut.mt_sqrt(6))
print(ut.mt_sinpi())
print(ut.mt_log())
print(ut.mt_exp(3))
print(ut.mt_pi())

fruits = ["apple", "banana", "cherry"]

print(random.randrange(1, 11))
print(random.choice(fruits))
print(random.random())
print(random.normalvariate())

print(ut.rd_randrange(1, 11))
print(ut.rd_choice(fruits))
print(ut.rd_random())
print(ut.rd_normalvariate())