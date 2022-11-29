from typing import List, Any
from utils.misc_utils import timer
from env.logger import CustomLogging

logging = CustomLogging()
logger = logging.get_logger()


@timer
def binary_search(arr: List[int], query, asc=True, first_occurrence=True, debug=False):
    start = 0
    end = len(arr) - 1
    iteration = 0
    while start <= end:
        mid = (start + end) // 2
        first_element = arr[start]
        last_element = arr[end]
        mid_element = arr[mid]
        if debug:
            msg = f"first_element:{first_element},mid_element:{mid_element},last_element:{last_element}\n " \
                  f"first_index:{start},mid_index:{mid},last_index:{end}\n"
            logger.info(msg=msg)
        # Check if Queried element is not getting repeated on next left position while  looking for first_occurrence
        if query in (first_element, mid_element, last_element):

            # Check if query is first_element and if we need to return the first occurrence
            if query == first_element and first_occurrence:
                return {'index': start, 'iteration': iteration}
            # Check if query is last_element and if we need to return the last occurrence OR
            # if mid is end
            elif (query == last_element and not first_occurrence) or (mid == end):
                return {'index': end, 'iteration': iteration}
            # Check if Queried element is not getting repeated on just previous left position while
            # looking for first_occurrence
            elif arr[end - 1] == query and first_occurrence:
                end = end - 1
            elif arr[mid - 1] == query and first_occurrence:
                end = mid - 1

            # Check if Queried element is not getting repeated on next right position while
            # looking for last_occurrence
            elif arr[start + 1] == query and not first_occurrence:
                start = start + 1
            elif arr[mid + 1] == query and not first_occurrence:
                start = mid + 1
            elif query == first_element:
                return {'index': start, 'iteration': iteration}
            elif query == mid_element:
                return {'index': mid, 'iteration': iteration}
            else:
                return {'index': end, 'iteration': iteration}
        # check if
        # Queried element is less than the mid element and order of array is ascending
        # OR
        # Queried element is greater than the mid element and order of array is descending
        elif (mid_element > query > first_element and asc) or \
                (mid_element < query < first_element and not asc):

            end = mid - 1
        # check if
        # Queried element is greater than the mid element and order of array is ascending
        # OR
        # Queried element is less than the mid element and order of array is descending
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
