# -*- coding: utf-8 -*-
from pythonds.basic.stack import Stack


# 当在 Python 中调用函数时，会分配一个栈来处理函数的局部变量。
def to_string_recursion(n, base):
    convert_string = "0123456789ABCDEF"
    if n<base:
        return convert_string[0]
    else:
        return to_string_recursion(n//base, base) + convert_string[n%base]

# print(to_string_recursion(1234, 16))

r_stack = Stack()
def to_string_stack(n, base):
    convert_string = "0123456789ABCDEF"
    while n>0:
        if n<base:
            r_stack.push(convert_string[0])
        else:
            r_stack.push(convert_string[n%base])
        n = n // base
    res = ""
    while not r_stack.isEmpty():
        res += str(r_stack.pop())
    return res
# print(to_string_stack(1234, 16))


import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def drawSpiral(my_turtle, linLen):
    if linLen>0:
        my_turtle.forward(linLen)
        my_turtle.right(90)
        drawSpiral(my_turtle, linLen-5)

drawSpiral(my_turtle, 200)
my_win.exitonclick()
