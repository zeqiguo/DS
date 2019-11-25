# -*- coding: utf-8 -*-

def phibo_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return phibo_recursion(n-1) + phibo_recursion(n-2)


print(phibo_recursion(3))