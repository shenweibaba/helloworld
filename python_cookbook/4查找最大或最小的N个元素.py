'''
    问题 查找最大或者最小的N个元素
'''
'''
    解决方案：
    heapq模块有两个函数：nlargest()和nsmallest()
'''
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums)) # 取出列表中最大的三个数字 [42, 37, 23]
print(heapq.nsmallest(3,nums)) # 取出最小的三个数字 [-4, 1, 2]

'''
    可以接受更复杂的数据结构，根据具体的字段进行比较
'''

'''
    场景1 选出价格最大和最小的字典
'''
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3,portfolio,key=lambda a : a["price"])
expensive = heapq.nlargest(3,portfolio,key=lambda a : a['price'])
print("cheap;", cheap)
#cheap; [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]
print("expensive:",expensive)
#expensive: [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]
'''
    重点：底层实现
    1、将集合数据进行堆排序后放入一个列表中
    2、然后通过pop()将最小的元素弹出，以此类推

'''