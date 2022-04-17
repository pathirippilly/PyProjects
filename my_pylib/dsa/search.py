from typing import List, Any
from utils.misc_utils import timer
from env.logger import CustomLogging


@timer
def binary_search(arr: List[int], query, asc=True):
    start = 0
    end = len(arr) - 1
    iteration = 0
    while start <= end:
        mid = (start + end) // 2
        mid_element = arr[mid]
        if mid_element == query:
            return {'index': mid, 'iteration': iteration}
        elif (mid_element > query and asc) or (mid_element < query and not asc):
            end = mid - 1
        else:
            start = mid + 1
        iteration = iteration + 1

    return {'index': -1, 'iteration': iteration}


@timer
def linear_search(arr: List[int], query: int):
    iteration = 0
    for num in arr:
        if query == num:
            return {'index': iteration, 'iteration': iteration}
        iteration = iteration + 1

    return {'index': -1, 'iteration': iteration - 1}
