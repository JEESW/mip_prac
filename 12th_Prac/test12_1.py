""" class MyClass:
    count = 0
    
    def __init__(self, num):
        self.count = num
    
    @classmethod
    def clsMethod(cls):
        cls.count += 1
        print(f"instance = {cls.count}")
    
    def instMethod(self):
        self.count += 1
        print(f"instance = {self.count}")

MyClass.clsMethod()

obj = MyClass(10)

obj.instMethod()
print(obj.count)

print(MyClass.count)
print(MyClass.count) """



""" class Champion:
    name_ = ""
    hp_ = 0
    lev_ = 0
    speed_ = 0.0
    attackspeed_ = 0.0
    skill = []
    
    def __init__(self, name, speed):
        self.hp = 100
        self.name_ = name
        self.lev_ = 1
        self.speed = 300.0
        self.setSpeed(speed)
        self.setAtkSpd()
        self.setMovSpd()
    
    def setAtkSpd(self):
        self.attackspeed = 0.658*((1.0334)**(Champion.lev_ - 1))
    
    def beAtk(self, dam):
        print("be attack", dam, 1-100.0/(100.0+100))
        self.dam = dam*(100.0/(100.0 +100))
        print(self.dam)
        self.hp = self.hp - self.dam
    
    def setSpeed(self, sp):
        if (sp == 1):
            self.speed_ = 50
        else:
            self.speed_ = 0
    
    def setMovSpd(self):
        print("set Mov Spd")
        self.setMovSpd = (20 + self.speed_) * 1.00 * 100
    
    def printStatus(self):
        print("champion: %s, hp: %f, lev: %d, mvSpd: %f, atkSpd: %f" % {self.name_, self.hp_, self.lev_, self.speed_, self.attackspeed_})
    
ashe = Champion("ashe", 474)
mipo = Champion("mipo", 600)

ashe.printStatus()
ashe.printStatus()

mipo.beAtk(63.0)
mipo.printStatus() """



# Inheritance
""" class Champion:
    def __init__(self, name):
        self.name = name
        self.level = 1
        
    def attack(self, key):
        print(f"attack = {key}")
    
    def levelup(self):
        self.level += 1
    
    def getLevel(self):
        print(self.level)
   
class Yasuo(Champion):
    def attack(self, key):
        print(f"attack - {key} steel tempest")
        return

class Garen(Champion):
    def attack(self, key):
        print(f"attack - {key} demacian justice")
        return

user1 = Yasuo("python")
user2 = Garen("hello")

user1.getLevel()
uesr2.getLevel()

user1.attack(user2.name)
user2.attack(user1.name)

user1.levelup()
user2.levelup()

user1.getLevel()
uesr2.getLevel() """



# Abstraction
""" from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


circ = Circle(5)
rect = Rectangle(4, 6)

print(circ.area())
print(rect.area())

sett = [circ, rect]
for st in sett:
    print(st.area()) """



# Infomation property
""" class Person:
    def __init__(self, name, age, number):
        self._name = name
        self._age = age
        self._number = number
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    def number(self):
        return self._number
    
    @name.setter
    def name(self, nName):
        self._name = nName
    
    @age.setter
    def age(self, nAge):
        self._age = nAge

user1 = Person("Alice", 30, "01011112222")

print(user1.age)
print(user1._age)
print(user1.name)
print(user1._name)
print(user1.number)
print(user1._number) """



# Polyform
""" class Person:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getNumber(self):
        return self.number

class Student(Person):  ()
class Teacher(Person):  ()

def getPersonName(person):
    return person.getName()

user1 = Student("alice", 23, "01011112222")
user2 = Teacher("bob", 25, "01033334444")

print(getPersonName(user1))
print(getPersonName(user2)) """



# Capsule
""" class Person:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.number = num
    
    def getName(self):
        return self.name
    
    def setName(self, new):
        self.name = new
        return
    
    def getNumber(self):
        return self.number
    
    def setNumber(self, new):
        self.number = new
        return        

p1 = Person("alice", 23, "01011112222")
p2 = Person("bob", 25, "01033334444")

print(p1.getName())
print(p2.getName())
print(p1.getNumber())
print(p2.getNumber())

p1.setName("A")
p2.setName("B")
p1.setNumber("11111111111")
p2.setNumber("22222222222")

print(p1.getName())
print(p2.getName())
print(p1.getNumber())
print(p2.getNumber()) """