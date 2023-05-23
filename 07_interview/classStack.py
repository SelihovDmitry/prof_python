

# Задание 1
class Stack:

    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        return not bool(self.stack_list)

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        return self.stack_list.pop() if len(self.stack_list) else 'Стек пустой'

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def content(self):
        return self.stack_list


if __name__ == "__main__":

    stack1 = Stack()

    print(stack1.pop())
    print(stack1.is_empty())
    stack1.push(')')
    stack1.push('(')
    stack1.push('[')
    print(stack1.pop())
    print(stack1.is_empty())
    print(stack1.size())
    print(stack1.content())
    print(stack1.peek())

