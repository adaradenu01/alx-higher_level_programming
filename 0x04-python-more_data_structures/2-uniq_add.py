#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniqueNum = set(my_list)
    num = 0
    for x in uniqueNum:
        num += x
    return num
