from Stack.stack import Stack


def dividBy2(decNumber: int):

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    bin_string = ""
    while not remstack.isEmpty():
        bin_string = bin_string + str(remstack.pop_())

    return bin_string

def baseConvert(decNumber, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ''
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop_()]

    return newString
