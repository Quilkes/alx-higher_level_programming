#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = []
    end_sum = 0
    length = len(roman_string)

    for i in range(0, length):
        for k, v in roman.items():
            if roman_string[i] == k:
                numbers.append(v)

    current_sum = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i - 1] == numbers[i]:
            current_sum += numbers[i]
        elif numbers[i - 1] > numbers[i]:
            end_sum += current_sum
            current_sum = numbers[i]
        elif numbers[i - 1] < numbers[i]:
            end_sum -= current_sum
            current_sum = numbers[i]
    return (current_sum + end_sum)

"""def roman_to_int(roman_string):
    if type(roman_string) != str:
        return 0

    roman = {"I" : 1,"V" : 5,"X" : 10,"L" : 50,"C" : 100,"D" : 500,"M" : 1000}

    r = 0
    Prev_no = 0
    curr_no = 0

    for letter in (roman_string[::-1]):
        prev_no = curr_no
        curr_no = roman[letter]

       # r += (curr_num if curr_num >= prev_num else -curr_num)
        if curr_no >= prev_no:
            r += curr_no
        else:
            r += -curr_no

    return r"""

