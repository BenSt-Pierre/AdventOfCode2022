__author__ = "BenSt-Pierre"
__date__ = "2022-12-01"

# General Variables
input_file_path = "input.txt"
debug = False

# Open File
input = open(input_file_path, "r")

# Read all lines
all_lines = input.readlines()
print(all_lines) if debug is True else None

# Remove \n from all lines, make a list of int
list_of_calories = []
for every_line in all_lines:
    calorie_amount = every_line.split("\n")[0]
    if calorie_amount == "":
        calorie_amount = 0
    print(calorie_amount) if debug is True else None

    list_of_calories.append(int(calorie_amount))

# Get total carried calories per elf
total_calories_per_elf = []
current_sum = 0
elf_number = 1
master_list = []
for every_snack in list_of_calories:
    if every_snack != 0:
        current_sum += every_snack
    else:
        total_calories_per_elf.append(current_sum)
        print(f"Total carried calories for elf {elf_number} is {current_sum}") if debug is True else None
        master_list.append([current_sum, elf_number])
        elf_number += 1
        current_sum = 0

# Sort master list
master_list.sort(reverse=True)
print(master_list)if debug is True else None

# Get results
print(f"Elf #{master_list[0][1]} is carrying the most calories, {master_list[0][0]} to be exact.")
print(f"Elf #{master_list[1][1]} is second in line, carrying {master_list[1][0]} calories.")
print(f"Closely followed by Elf #{master_list[2][1]}, carrying {master_list[2][0]} calories.")
print(f"The top three Elfs carry {(master_list[0][0]+master_list[1][0])+master_list[2][0]} calories together!")

# # Get maximum calories carried by an elf and its number
# max_carried_calories = 0
# max_carried_elf_number = 0
# for elf_number, carried_calories in enumerate(total_calories_per_elf, start=1):
#     if carried_calories > max_carried_calories:
#         max_carried_calories = carried_calories
#         max_carried_elf_number = elf_number

# print(f"Elf #{max_carried_elf_number} is carrying the most calories, {max_carried_calories} to be exact")