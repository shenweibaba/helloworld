
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