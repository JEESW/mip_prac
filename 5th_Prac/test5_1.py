num = input("숫자를 입력하세요!!")
print("number ", num)
print("number ", int(num))

a = 12
print(type(a))

a = 12.01
print(type(a))

a = "a"
print(type(a))

a = "abcd"
print(type(a))

a = [3, 2, 1]
print(type(a))

a = 65
# a = "65"
print(int(a))
print(str(a))
print(hex(a))
print(oct(a))
print(chr(a))
print(ord("A"))

print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4)

print(divmod(10, 3))

print(round(3.141))

a = (3, 5, 7)
b = list(a)
c = tuple(b)

print(b)
print(c)

print(type(b))
print(type(c))

for i in range(2, 7):
    print(i)

for i in range(6):
    print(i)
    
for i in range(1, 20, 3):
    print(i)
    
a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a))

print(abs(-3))
print(abs(3.0))
print(abs(-3.0))

a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True))

a = [5, 3.14, False, 9, "string"]
print(enumerate(a))
print(*enumerate(a))

a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(*zip(a, b))

a = [True, True, False]
print(any(a))
print(all(a))

a = 20
b = 23
c = "a 는 {}, b 는 {}, {}".format(a, b, "python")

print(c)

a = 3
print(globals())
print(locals())

print(dir(a))

print(callable(a))

add = lambda a, b : a + b
print(add(2, 3))

sub = lambda a, b : a - b
print(sub(2, 3))

mul = lambda a, b : a * b
print(mul(2, 3))

div = lambda a, b : a / b
print(div(2, 3))

def add_numbers(x, y):
    return x + y

result = add_numbers(4, 5)
print(result)

def greet(name):
    print(name)
    print("Hello, " + name + ". How are you?")

greet("Python")

def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
print(sub(3, 5))
print(mul())
div()

#1
def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
x =  int(input())
print(isEven(x))

#2
def revstr(s):
    print(*reversed(s))
    
s = "Python"
revstr(s)

#3
def cal_add():
    x = int(input())
    y = int(input())
    print(x + y)
def cal_sub():
    x = int(input())
    y = int(input())
    print(x - y)
def cal_mul():
    x = int(input())
    y = int(input())
    print(x * y)
def cal_div():
    x = int(input())
    y = int(input())
    print(x / y)


cal_add()
cal_sub()
cal_mul()
cal_div()

#4
def sum_5():
    ss = 0
    for i in range(5):
        a = int(input())
        ss += a 
    print(ss)
    
sum_5()