import random
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


# Create a stack instance
stack = Stack()
nums = [random.randint(1, 100) for i in range(7)]
# a. Insert 7 elements into the stack
for element in nums:
    stack.push(element)

print("Stack after pushing 7 elements:", stack)

# b. Delete the 2nd, 3rd, and 6th elements (1-based index)
to_delete = [1, 2, 5]
for i in sorted(to_delete, reverse=True):
    stack.items.pop(i)

print("Stack after deleting 2nd, 3rd, and 6th elements:", stack)
# c. Check whether the stack is empty
print("Is the stack empty?", stack.is_empty())
