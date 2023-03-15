#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    lib = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    ans = 0
    for i in range(len(roman_string)):
        value = lib[roman_string[i]]
        if i < len(roman_string) - 1 and lib[roman_string[i + 1]] > value:
            ans -= value
        else:
            ans += value
        return ans
