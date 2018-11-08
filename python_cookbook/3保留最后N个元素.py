'''
    问题：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录
'''
'''
    解决方案：保留有限历史记录 collections.deque
'''
from collections import deque

# 查询前5条记录
def search(lines,pattern,history=5):
    previous_line = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield  li,previous_line
        previous_line.append(li)

'''
    deque新建一个固定大小的队列，当新的元素加入并且这个队列已满时，最老的元素会自动被移除掉
    如果不设置最大队列的大小，就会得到一个无限大小的队列
'''

'''
    复杂度 在队列两端插入或删除元素时间复杂度是o(1),
            在列表的开头插入或删除元素的时间复杂度为o(n)
'''

