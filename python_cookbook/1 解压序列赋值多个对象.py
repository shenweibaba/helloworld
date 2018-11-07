'''
    一个包含n个元素的元组和序列，怎样将它的值解压后同时赋值给n个变量

'''

#解法 唯一的前提是变量的数量必须和序列元素的值一样
# 否则会出现 ValueError: too many values to unpack (expected 4)
list = [1,2,3,4,5]
a,b,c,d,e =list
print(list)
print(a)#1
print(b)#2
print(c)#3
print(d)#4
print(e)#5
'''
    实际上，这种解压赋值的方式可以用在任何可迭代对象上面，不仅仅是列表或者元祖，包括字符串
    ，文件对象，迭代器和生成器
'''
str = 'apple'
a,b,c,d,f = str
print(a)#a
print(b)#p
print(c)#p
print(d)#l
print(e)#e
'''
    如果你只需要解压一部分,丢弃其他值，可以使用任意变量名去占位，到时候丢掉这些变量就可以了
'''
data = ['abc',50,91.1,(2018,11,7)]
_,s,a,_= data # '_'做占位符
print(a)#91.1

