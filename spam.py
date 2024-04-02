# menu = [
#     ["egg", "bacon"],
#     ["egg", "sausage", "bacon"],
#     ["egg", "spam"],
#     ["egg", "bacon", "spam"],
#     ["egg", "bacon", "sausage", "spam"],
#     ["spam", "bacon", "sausage", "spam"],
#     ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
#     ["spam", "egg", "spam", "spam", "bacon", "spam"],
# ]
#
# for i in menu:
#     for j in i:
#         if j != "spam":
#             print(j)
#     print()

# cars = [
#     "BMW",
#     "Audi",
#     "Mercedes",
#     "Volkswagen",
#     "Hyundai",
#     "Kia",
#     "Skoda"
# ]
#
# print(" | ".join(cars))

# input_value = input("Please enter 3 numbers")
# split_value = input_value.split(",")
# print(split_value)
#
# int_tokens = []
# for st in split_value:
#     int_tokens.append(int(st))
# print(int_tokens)
#
# a = int_tokens[0]
# b = int_tokens[1]
# c = int_tokens[2]
#
# print(a+b-c)

coldplay = "Speed of Sound", "X&Y", "2012"
song, album, year = coldplay
print(song)
print(album)
print(year)