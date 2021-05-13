# 栈： 列表的底层维护了一个栈结构

stack = []
print(stack)

# 入栈【向栈中存数据】  ： append
stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)
stack.append(4)
print(stack)

# 出栈【从栈中取数据】：pop
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

"""
特点：先进后出，后进先出
"""