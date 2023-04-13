

# 1.
# Доработать класс FlatIterator в коде ниже. Должен получиться итератор,
# который принимает список списков и возвращает их плоское представление,
# т. е. последовательность, состоящую из вложенных элементов. Функция test в
# коде ниже также должна отработать без ошибок.
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.results = iter(self.list_of_list[self.cursor])
        return self

    def __next__(self):
        try:
            item = next(self.results)
        except StopIteration:
            if self.cursor >= len(self.list_of_list) - 1:
                raise StopIteration
            self.cursor += 1
            self.results = iter(self.list_of_list[self.cursor])
            item = next(self.results)
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


# 2. Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков
# и возвращает их плоское представление. Функция test в коде ниже также должна отработать без ошибок.

import types

def flat_generator(list_of_lists):
    cursor = 0
    current_list = iter(list_of_lists[cursor])
    while cursor <= len(list_of_lists) -1 :
        try:
            item = next(current_list)
            yield item
        except StopIteration:
            cursor += 1
            if cursor <= len(list_of_lists) -1 :
                current_list = iter(list_of_lists[cursor])
            else:
                break

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_1()
    test_2()

# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]

# for i in FlatIterator(list_of_lists_1):
#     print(i)

# for i in flat_generator(list_of_lists_1):
#     print(i)
