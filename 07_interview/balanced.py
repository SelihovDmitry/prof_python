from classStack import Stack

def balanced(my_str: str) -> bool:

    if len(my_str) == 0:
        return True
    elif my_str[0] in ']})':
        return False

    my_stack = Stack()
    pairs = {'(': ')',
             '[': ']',
             '{': '}'}

    # print(my_str)
    for symbol in my_str:
        if symbol in '[{(':
            my_stack.push(symbol)
        elif symbol in ']})':
            if pairs[my_stack.pop()] == symbol:
                continue
            else:
                return False

    if my_stack.size() == 0:
        return True



if __name__ == "__main__":

    lines = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]', '', ']']
    for line in lines:
        if balanced(line):
            print('Сбалансировано')
        else:
            print('Несбалансировано')


