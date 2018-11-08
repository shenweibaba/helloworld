
'''
    当可迭代对象的元素个数大于接受变量的个数时，会抛出valueError，怎么才能
    从这个可迭代对象中解压出N个元素


'''
'''
    解决方案 使用python的星号表达式
'''
'''
场景1 期末时，公布了6门考试成绩，如果需要去掉第一个 和最后一个，然后计算平均分

'''
def avg(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

def get_avgGrade(grades):
    first,*middle,last = grades
    return avg(middle)
grades = [88,77,55,66,100]
print(get_avgGrade(grades)) # 66.0

'''
场景2 有一些用户的记录，每条记录包含一个名字，邮件以及不确定数量的电话号码
'''
record = ['mike','mike@email.com','110','120','119']
name,email,*phone = record
print(name) #mike
print(email) #mike@email.com
print(phone) #['110', '120', '119']
'''
注意 解压出来的 *表达式变量永远是列表类型，不管解压出来的数量是多少个(包括0个)
'''

'''
    扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的
'''
'''
    场景3 迭代可变长元组
'''
records = [
    ('foo','1','2'),
    ('too','3')
]

for i , *j in records:
    print(i + ":", end='')
    print(j)
'''
    输出 foo:['1', '2']
         too:['3']
'''

'''
    由于语言的限制 递归不是python 擅长的 什么意思？
    
'''

