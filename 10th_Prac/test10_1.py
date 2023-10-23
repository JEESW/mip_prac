""" import os

# fp = "test.py"
fp = "temp.txt"

file = open(fp, "w")

if os.path.exists(fp):
    print("ok")
else:
    print("error")

file.close() """


""" import os

fp = "temp.txt"

if os.path.exists(fp):
    f = open(fp,"r")
    for line in f:
        print(line)
else:
    f = open(fp, "w")
    for i in range(100):
        f.write(str(i) + "\n")
        
f.close() """


""" import os

def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)

fp = "new.txt"
 
f = open(fp, "w")
f.close()

dir_print("./")

os.remove(fp)
print("-----------------------------------------\n\n")
dir_print("./")
print("complete") """


""" import os

def dir_print(p):
    files = os.listdir(p)
    for f in files:
        print(f)

fp = "new.txt"
tp = "new1.txt"
 
f = open(fp, "w")
f.close()

dir_print("./")
print("-----------------------------------------\n\n")

if os.path.exists(tp):
    os.remove(tp)
    dir_print("./")
    print("exist, same name file)
else:
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete") """


""" f = open("temp.txt", "r")
with open("temp.txt", "r") as f:
    print(f.read())
    
    for i in range(110):
        res = f.readline()
        print(res) """