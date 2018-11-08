'''
怎样实现一个按优先级排序的队列？并且在这个队列上面每次 pop 操作总是返回
优先级最高的那个元素
'''
import heapq
class PriorityQueue:
    def __init__(self):
        self.queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self.queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self.queue)[-1] #heappop弹出堆中最小的元素

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q.queue)
print(q.pop()) #Item('bar')
print(q.pop()) #Item('spam')
print(q.pop()) #Item('foo')
print(q.pop()) #Item('grok')

'''
    解析 队列中包含一个元祖 其中 priority代表优先级，负数使得队列中的元素
    按照优先级由高到低排列
    index 记录插入的顺序，同优先级的元素通过这个变量比较
'''