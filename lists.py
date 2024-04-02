available_parts = ["computer",
                   "monitor",
                   "CPU",
                   "mouse",
                   "speaker",
                   "keyboard"
                   ]
valid_choice = []

for i in range(1, len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)

current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choice:
        print("Adding {}". format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
    else:
        print("Please add options from the list:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}". format(number+1, part))
    current_choice = input()

print(computer_parts)

# names = ["kamal",
#          "Neil",
#          "harris",
#          "Sita",
#          "badri",
#          "prakash"
#         ]
#
# names.sort(key=str.casefold)
# print(names)

# a = "123456789"
# print(a[1:7:2])
# for index, character in enumerate("abcdefgh"):
#     print(index, character)

