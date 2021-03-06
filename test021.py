#!/usr/bin/python3
#多继承实例

class people:
  #定义基本属性
  name = ''
  age = 0
  #定义私有属性,私有属性在类外部无法直接进行访问
  __weight = 0
  #定义构造方法
  def __init__(self,n,a,w):
    self.name = n
    self.age = a
    self.__wight = w
  def speak(self):
    print("%s is speaking:I am %d years old" %(self.name, self.age))

class student(people):
  grade = ''
  def __init__(self,n,a,w,g):
    #调用父类的构造函数
    people.__init__(self,n,a,w)
    self.grade = g

  #覆写父类的方法
  def speak(self):
    print("%s is speaking:I am %d years old,and I am in grade %d" %(self.name, self.age, self.grade))

class speaker():
  topic = ''
  name = ''
  def __init__(self,n,t):
    self.name = n
    self.topic =t
  def speak(self):
    print("I am %s,I aam a speaker!My topic is %s" %(self.name, self.topic))

class sample(speaker, student):
  a = ''
  def __init__(self,n,a,w,g,t):
    student.__init__(self,n,a,w,g)
    speaker.__init__(self,n,t)

test = sample("Tim", 25, 89, 4, "Python")
test.speak()
