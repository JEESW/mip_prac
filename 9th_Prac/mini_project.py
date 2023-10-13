""" for i in range(1, 6):
    for j in range(i, 6):
        print('*', end='')
    print('') """
    
""" for i in range(1, 6):
    for j in range(6 - i, 6):
        print('*', end='')
    print('') """
    
""" for i in range(1, 6):
    for j in range(i, 6):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print('') """
    
""" for i in range(1, 6):
    for j in range(i, 6):
        print(' ', end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print('')
    
print('***********')

for i in range(1, 6):
    for j in range(6 - i, 6):
        print(' ', end='')
    for j in range(1, 12 - 2 * i):
        print('*', end='')
    print('') """
    
""" list = []

for i in range(0, 5):
    list = []
    for j in range(0, 5):
        list.append(i * 5 + j + 1)
    print(list) """
    
""" list = []

for i in range(0, 5):
    list = []
    for j in range(0, 5):
        list.append(j * 5 + i + 1)
    print(list) """

""" list = []
for i in range(4, -1, -1):
    list = []
    for j in range(4, -1, -1):
        list.append(i * 5 + j + 1)
    print(list) """

""" import random as rd

srp_list = [1, 2, 0]

def random_srp():
    return int(rd.choice(srp_list))

def compare_srp(user_, ai_):
    if user_ == ai_:
        return "Draw"
    elif (user_ == 1 and ai_ == 2) or (user_ == 2 and ai_ == 0) or (user_ == 0 and ai_ == 1):
        return "Lose"
    elif (user_ == 2 and ai_ == 1) or (user_ == 0 and ai_ == 2) or (user_ == 1 and ai_ == 0):
        return "Win"

user = int(input("가위 = 1, 바위 = 2, 보 = 0: "))
ai = random_srp()
print(compare_srp(user, ai)) """

""" file = open("temp.txt", "w")
file.close() """

""" file = open("temp.txt", "r")
file.close() """

""" file = open("temp.txt", "a")
file.close() """

""" file = open("temp.txt", "r+")
file.close() """

""" file = open("temp.txt", "w")

file.write("hello")
file.write("world")

file.close() """

""" file = open("temp.txt", "w")

file.write("hello\n")
file.write("world")

file.close() """

""" file = open("c:/Users/Catholic/temp.txt" , "w")

for i in range(101):
    file.write(f"{i}\n")

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close() """

""" file = open("temp.txt", "r")
res = file.read()
print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")
res = file.read()
print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")
for i in range(103):
    res = file.readline()
    print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")
res = file.readlines()
print(res)

file.close() """

""" file = open("temp.txt", "r")
line = file.readlines()
for l in line:
    print(l)

file.close() """