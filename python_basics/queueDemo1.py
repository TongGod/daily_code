# 队列
import collections

# 创建一个空队列
queue = collections.deque()
print(queue)

# 入队【向队列中添加数据】：append
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)
queue.append(4)
print(queue)

# 出队【向队列中获取数据】：popleft:表头/ pop:表尾
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)


"""
特点： 先进先出，后进后出
"""