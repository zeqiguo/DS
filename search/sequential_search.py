# -*- coding: utf-8 -*-
l = [1,2,3,4,5,6,10]


def sequential_search(val: int, *nums: list) -> bool:
    found = False
    index = 0
    while not found and index<len(nums):
        for x in nums:
            if x == val:
                found = True
                return found
            else:
                index += 1
    return found

def order_sequential_search(val: int, nums: list) -> bool:
    index = 0
    found = False
    stop = False
    while index<len(nums) and not found and not stop:
        if nums[index] == val:
            found = True
        else:
            if nums[index] > val:
                stop = True
            else:
                index += 1

    return found

print(order_sequential_search(val=2, nums=l))


