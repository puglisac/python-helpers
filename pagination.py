"""
This method takes an array of items, a page number, and page size and returns a smaller array

>>> pagination([1,2,3,4,5,6,7,8,9,10,11,12], 1, 6)
[1, 2, 3, 4, 5, 6]
>>> pagination([1,2,3,4,5,6,7,8,9,10,11,12], 2, 6)
[7, 8, 9, 10, 11, 12]
>>> pagination([1,2,3,4,5,6,7,8,9,10,11,12], 4, 6)
[7, 8, 9, 10, 11, 12]
>>> pagination([1,2,3,4,5,6,7,8,9,10,11,12], 0, 3)
[1, 2, 3]
>>> pagination([1,2,3,4,5,6,7,8,9,10,11,12], 3, 3)
[7, 8, 9]
"""

import math

def pagination(arr, page_number, page_size):    
    size = math.ceil(len(arr)/page_size)
    if page_number > size:
        page_number = size
    if page_number < 1:
        page_number = 1
    start_index = (page_number-1)*page_size
    paginated_array = arr[start_index:start_index+page_size]
    return paginated_array