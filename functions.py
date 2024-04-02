# def multiply(x, y):
#     result = x * y
#     return result


# answer = multiply(10, 9)
# print(answer)
#
# for i in range(1,5):
#     answers = multiply(i, 2)
#     print(answers)


# def is_palindrome(string):
#     backward = string[::-1]
#     return backward.casefold() == string.casefold()
#
#
# def palindrome_sentence(sentence):
#     string = ''
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     print(string)
#     return string[::-1].casefold() == string.casefold()
#
#
# word = input("Please input the word ")
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


# word = str.casefold(input("Please enter the word "))
# backward = word[::-1]
# if backward == word:
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


# def sum_eo(n, t):
#     if t == "e":
#         start = 2
#     elif t == "o":
#         start = 1
#     else:
#         return -1
#
#     total = 0
#     for i in range(start, n, 2):
#         total += i
#     return total
#
#
# a = int(input("Enter the value of n "))
# b = input("Enter the value of t ")
# x = sum_eo(a, b)
# print(x)


# n0 = 0
# n1 = 1
# x = int(input("Enter the number of Fibonacci sequence: "))
# print(n0)
# print(n1)
# for i in range(2, x):
#     result = n1 + n0
#     n0 = n1
#     n1 = result
#     print(result)

# def fibonacci(n):
#     if 0 <= n <= 1:
#         return n
#
#     n0, n1 = 0, 1
#
#     result = None
#     for f in range(n):
#         result = n0 + n1
#         n0 = n1
#         n1 = result
#     return result
#
#
# n_turns = int(input("Enter the number of turns: "))
# for i in range(n_turns-1):
#     print(i, fibonacci(i))
