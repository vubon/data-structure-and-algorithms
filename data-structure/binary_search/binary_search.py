"""
Python Program for recursive binary search.
Returns index of x in arr if present, else -1
"""


def binary_search(arr, left, right, find_number):
    """
    :param arr:
    :param left:
    :param right:
    :param find_number:
    :return:
    """
    # Check base case
    if right >= left:

        mid = int(left + (right - left) / 2)

        # If element is present at the middle itself 
        if arr[mid] == find_number:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left sub array
        elif arr[mid] > find_number:
            return binary_search(arr, left, mid - 1, find_number)

        # Else the element can only be present
        # in right sub array
        else:
            return binary_search(arr, mid + 1, right, find_number)

    else:
        # Element is not present in the array 
        return -1


# Test array
array = [2, 3, 4, 10, 40, 50]

# Function call 
result = binary_search(array, 0, len(array) - 1, 3)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")


def binary_search_normal(data, find_number):
    """
    :param data:
    :param find_number:
    :return:
    """
    # if the array unsort then , need to sort the arry
    array_sort = sorted(data)
    left = 0
    right = len(array_sort) - 1
    mid = int(left + (right - left) / 2)

    if not right >= left:
        return -1

    if array_sort[mid] == find_number:
        return mid

    elif array_sort[mid] < find_number:
        for num in range(mid + 1, len(array_sort) + 1):
            print(num)
            if num == find_number:
                return num


binary_search_normal([1, 2, 3, 4, 5, 6, 7], 5)
