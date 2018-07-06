'''
队列：
    先进先出
'''

import collections

# 创建一个队列
queue = collections.deque()

# 压入数据
queue.append("A")
queue.append("B")

# 取出数据
queue.popleft()