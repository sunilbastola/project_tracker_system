# import main

# Function to direct to approproate function after user making a choice:
# def validate_user_choice(user_choice):
#     if user_choice == '1':
#         add_team_member()
#     elif user_choice == '2':
#         update_member_score()
#     elif user_choice =='3':
#         calculate_avg_score()
#     elif user_choice =='4':
#         find_highest_lowest()
#     elif user_choice =='5':
#         idenfity_above_target()
#     elif user_choice =='6':
#         exit_program()

members_list = {}

def add_team_member():
    member_name = input("\nEnter team member name: ")
    member_score = float(input(f"Enter {member_name}'s initial score: "))
    print(f"Team member ", member_name, "added successfully with score ", member_score)
    members_list.update({member_name:member_score})

n = 0
while n < 2:
    add_team_member()
    n = n+1

# Pseudocode for Finding the Highest & Lowest Score:
'''
1. Create a function
2. Get list of values from the dictionary
3. Sort the values in the list
4. For minimum, Pick the first value.
5. For maximum, pick the last value
6. Print the lowest valule and highest value
'''

def find_highest_lowest():
    values = list(members_list.values())
    print(values)
    values = sorted(values)
    print(values)

find_highest_lowest()

# Pseudocode for finding the Team Members above the target
'''
1. Define the function & Create a empty list to score the values
2. Get list of values from the dictionary
3. Set the value for performance target with the numeric value
4. Loop through all the values, and compare with Performance target
5. If value > performance target, put it inside the new list created.
6. Extract the keys of the values in the performance target list
7. Print the keys or name from the initial member list.
'''


# print(members_list)
# print(members_list.values())

# def update_member_score():
#     print(f"\nThe users you currently have are: {members_list.keys()}\n")
#     member_name = input("Please enter a user to update the record: ")
#     if member_name in members_list.keys():
#         new_score = float(input(f"Please give a score to update for {member_name}: \n"))
#         members_list[member_name] = new_score
#         print(f"The member {member_name}'s score has been successfully updated to {new_score}\n")
#     else:
#         print("Please enter a valid user from the above list.\n")
#     print(members_list)
# update_member_score()

# def calulate_average_score():
#     total_score = 0
#     for score in members_list.values():
#         total_score = score + total_score
#     avg_score = total_score / len(members_list)
#     # print("Outside of loop")
#     # print(len(members_list))
#     # print(score)
#     print(f"The average score is: {avg_score}")

# calulate_average_score()

