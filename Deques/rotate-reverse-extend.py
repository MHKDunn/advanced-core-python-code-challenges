from collections import deque
my_deque = deque([1,2,3,4,5])
my_deque.rotate(2)
print(my_deque)
my_deque.reverse()
print(my_deque)
my_deque.extend([6,7,8])
print(my_deque)