class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = 0      
        self.inner_cursor = 0  

    def __iter__(self):
        return self

    def __next__(self):
        
        while self.cursor < len(self.list_of_list):
            nested = self.list_of_list[self.cursor]
            if self.inner_cursor < len(nested):
                item = nested[self.inner_cursor]
                self.inner_cursor += 1
                return item
            
            self.cursor += 1
            self.inner_cursor = 0
        raise StopIteration


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


if __name__ == '__main__':
    test_1()
