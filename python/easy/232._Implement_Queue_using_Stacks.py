# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
#
# Implement the MyQueue class:
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]


class MyQueue:

    def __init__(self):
        self.queue = list()

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return False if self.queue else True


if __name__ == '__main__':
    x = 10
    obj = MyQueue()
    obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
