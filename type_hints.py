from typing import Dict, Tuple, Optional, Union

def is_magic(obj_name: str):
    return obj_name.startswith('__') and obj_name.endswith('__')


def contains(string1: str, string2: str) -> bool:
    return string2.startswith(string1)


# def population(countries: Dict[str, int]):
#     print(countries)
#
#
#
# # print(contains('hello', 'hello world'))
#
# countries = {
#     'China': '2_000_000_000'
# }
# population(countries)


def sum_tuple(values: Tuple[Union[str, int], int]):
    return sum(values)


sum_tuple((2, 2))


# def random(random_number: Optional[int, float] = 100):
#     print(random_number)
#
# random('1000')