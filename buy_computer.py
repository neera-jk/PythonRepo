available_parts = {
    "1": "Computer",
    "2": "Monitor",
    "3": "Keyboard",
    "4": "Mouse",
    "5": "HDMI Cable",
    "6": "DVD Drive",
}

current_choice = None
computer_parts = {}

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list:")
        for keys, value in available_parts.items():
            print(f"{keys}: {value}")
        print("0: to finish")

    current_choice = input("> ")