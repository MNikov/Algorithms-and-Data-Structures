# Interview Question #2
# "A palindrome is a string that reads the same forward and backward"
# For example: radar or madam
# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!

def palindrome_checker_1(string):
    return string == string[::-1]


def palindrome_checker_2(string):
    start_idx = 0
    end_idx = len(string) - 1

    is_palindrome = True

    while end_idx > start_idx:
        if string[start_idx] != string[end_idx]:
            is_palindrome = False
            break
        start_idx += 1
        end_idx -= 1
    return is_palindrome


print(palindrome_checker_1('madam'))
print(palindrome_checker_1('modem'))
print(palindrome_checker_2('madam'))
print(palindrome_checker_2('modem'))
