1.stack using the list(last in first out)
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())
print(stack)

2.stack using the deque
from collections import deque
stack=deque()
stack.append(100)
stack.append(200)
stack.append(300)
print(stack)
print(stack.pop())

3.queue using the list(first in first out)
queue=[]
queue.append(34)
queue.append(20)
queue.append(18)
print(queue)
print(queue.pop())
print(queue)

4.queue using the dequeue
from collections import deque
queue=deque()
queue.append(10)
queue.append(11)
queue.append(12)
print(queue)
print(queue.pop())
print(queue)
