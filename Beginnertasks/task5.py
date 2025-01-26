# 1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20
# times).
# Count and print the following statistics:
# How many times you rolled a 6
# How many times you rolled a 1
# How many times you rolled two 6s in a row


# 1. Simulate rolling a six-sided die multiple times and count statistics
import random

roll_6 = 0
roll_1 = 0
two_6_in_a_row_count = 0

for _ in range(20):
    roll = random.randint(1, 6)
    print("Roll:", roll)

    # Counting statistics
    if roll == 6:
        roll_6 += 1
    if roll == 1:
        roll_1 += 1
    if roll == 6 and previous_roll == 6:
        two_6_in_a_row_count += 1

    previous_roll = roll

# Printing statistics
print("Number of times rolled a 6:", roll_6)
print("Number of times rolled a 1:", roll_1)
print("Number of times rolled two 6s in a row:", two_6_in_a_row_count)




# 2. Imagine you are doing a workout routine, and you have to complete 100
# jumping jacks.
# Write a program that:
# Asks you to perform 10 jumping jacks at a time.
# After each set, it asks, "Are you tired?"
# If you reply "yes" or "y," it should ask if you want to skip the remaining sets.
# If you reply "yes" or "y," it should break and print, "You completed a total of
# jumping jacks."


# 2. Workout routine program
total_jumping_jacks = 100
completed_jumping_jacks = 0

while completed_jumping_jacks < total_jumping_jacks:
    remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
    print(f"{remaining_jumping_jacks} jumping jacks remaining.")
    perform = input("Perform 10 jumping jacks? (yes/no): ").strip().lower()
    
    if perform == "no" or perform == "n":
        tired = input("Are you tired? (yes/no): ").strip().lower()
        if tired == "yes" or tired == "y":
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip=="yes" or skip=="y":
                print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
                break
            else:
                continue
        else:
            continue
    elif perform == "yes" or perform == "y":
        completed_jumping_jacks += 10
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
    
    if completed_jumping_jacks == total_jumping_jacks:
        print("Congratulations! You completed the workout!")
        break
