# -*- coding: utf-8 -*-

def move_t(n, a, b, c):
    if n == 1:
        print(a, " -----> ", c)
    else:
        move_t(n-1, a, c, b)
        print(a, " -----> ", c)
        move_t(n-1, b, a, c)


move_t(10, "a", "b", "c")