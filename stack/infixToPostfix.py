# -*- coding: utf-8 -*-

from Stack.stack import Stack
import string

def infixToPostfix(infixexpr):
    prec = {
        '*' : 3,
        '/' : 3,
        '+' : 2,
        '-' : 2,
        '(' : 1
    }

    opSrack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and string.digits:
            postfixList.append(token)
        elif token == '(':
            opSrack.push(token)
        elif token == ')':
            topToken = opSrack.pop_()
            postfixList.append(topToken)
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opSrack.pop_()
        else:
            while (not opSrack.isEmpty()) and (prec[opSrack.peak()] >= prec[token]):
                postfixList.append((opSrack.pop_()))
            opSrack.push(token)

    while not opSrack.isEmpty():
        postfixList.append(opSrack.pop_())
    return " ".join(postfixList)

print(infixToPostfix('A + B) * (C + D)'))