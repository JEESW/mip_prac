""" def prt_func(n) :
    print("hello", n)

def callfunc(fx) :
    for i in range(5):
        fx(i)

callfunc(prt_func) """


""" def update_msg(name: str) -> list:
    msg = []
    msg.append("Hello, " + name)
    msg.append("Bye, " + name)
    return msg

def greeting(in_name: str) -> list:
    gt_msg = None
    gt_msg = update_msg(in_name)
    return gt_msg 

res = greeting("Python")

for messege in res:
    print(messege) """
    
def fun(n) :
    if n == 5 :
        return
    
    print(1, n)
    fun(n+1)
    
fun(1)

def ploop(n):
    if n==0:
        return 1
    else:
        return n * ploop(n-1)
    
print(ploop(5))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

res = fibo(4)
print("res =", res)