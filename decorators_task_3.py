from decorators_task_2 import logger

@logger('main_test.log')
def flat_generator(list_of_lists):
    ls = iter(list_of_lists)
    while True:
        try:
            for item in iter(next(ls)):
                yield item
        except StopIteration:
            break


test_list = [['a', 'b', 'c'],
             ['d', 'e', 'f', 'h', False],
             [1, 2, None]]

for item in flat_generator(test_list):
    print(item)