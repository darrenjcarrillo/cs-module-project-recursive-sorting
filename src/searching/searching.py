# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start is None:
        start = 0

    if end is None:
        end = len(arr) - 1

    # base case
    if start > end:
        return -1

    # calculate the index by adding high and low and floor divide by 2 --> floor division results in a whole number.
    mid = (start + end) // 2
    # check if mid index is equal to the target
    if arr[mid] == target:
        # return mid point
        return mid
    # check if mid target is less than the mid
    if target < arr[mid]:
        # decrement mid point by 1 and recursive call
        return binary_search(arr, target, start, mid-1)
    # otherwise, target is greater than mid point
    else:
        # increment the mid point by 1 and recursive call
        return binary_search(arr, target, mid+1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
