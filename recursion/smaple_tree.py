# -*- coding: utf-8 -*-

import turtle


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

ttl = turtle.Turtle()
myWin = turtle.Screen()
tree(75,ttl)
myWin.exitonclick()
