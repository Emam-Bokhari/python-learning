from collections import deque

# Stack: LIFO
# Queue: FIFO


# print(stack[-1])

# print(stack.pop())

# print(stack)

# stack.popleft()

# print(stack)
stack = [10, 20, 30]

queue_example=deque(stack)

queue_example.popleft()
print(queue_example)