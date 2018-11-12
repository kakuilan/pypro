#!/usr/bin/python3
# coding: UTF-8
# list常用操作

print('list定义')
li = ['a','b','mpilgrim','z','example']
print(li)
print(li[1])

print('list负数索引')
print(li[-1])
print(li[-3])
print(li[1:3])
print(li[1:-1])
print(li[0:3])

print('list增加元素')
li.append('new')
li.insert(2, 'new')
li.extend(['tow','elemnets'])
print(li)

print('list搜索')
print(li.index('example'))
print(li.index('new'))
#print(li.index('c')) #会抛一个异常
print('c' in li)

print('list删除元素')
li.remove('z')
li.remove('new') #删除首次出现的一个值
#li.remove('c') #list中没有找到值,python会引发一个异常
li.pop() #pop会做2件事：删除list的最后一个元素,然后返回被删除元素的值
print(li)

print('list运算符')
li = ['a','b','mpilgrim']
li = li + ['example','new']
li += ['two']
print(li)
li = [1,2] * 3
print(li)

print('使用join链接list成为字符串')
params = {'server':'mpilgrim','database':'master','uid':'sa','pwd':'secret'}
print(["%s=%s" % (k,v) for k,v in params.items()])
print(";".join(["%s=%s" % (k,v) for k,v in params.items()]))

print('list分割字符串')
li = ['server=mpilgrim','uid=sa','database=master','pwd=secret']
s = ';'.join(li)
print(s)
s.split(';')
s.split(';', 1)

print('list的映射解析')
li = [1,9,8,4]
print([elem*2 for elem in li])
li = [elem*2 for elem in li]
print(li)

print('dictionary中的解析')
params = {'server':'mpilgrim','database':'master','uid':'sa','pwd':'secret'}
print(params.keys())
print(params.values())
print(params.items())
print([k for k,v in params.items()])
print([v for k,v in params.items()])
print(["%s=%s" % (k,v) for k,v in params.items()])

print('list过滤')
li = ['a', 'mpilgrim','foo','b','c','b','d','d']
print([elem for elem in li if len(elem)>1])
print([elem for elem in li if elem!='b'])
print([elem for elem in li if li.count(elem)==1])



