# Interview Question #3
# Our task is to design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.


def reverse_int_1(num):
    reversed_int_arr = []
    for n in str(num)[::-1]:
        reversed_int_arr.append(n)

    return int(''.join(reversed_int_arr))


def reverse_int_2(num):
    return int(str(num)[::-1])


# Course implementation
def reverse_int_3(num):
    reversed_num = 0
    while num:
        curr_digit = num % 10
        reversed_num = reversed_num * 10 + curr_digit
        num //= 10

    return reversed_num


print(reverse_int_1(123))
print(reverse_int_2(456))
print(reverse_int_3(789))
