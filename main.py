# Initial Pseudocode
'''
1. Display the Home Page to the User
2. Ask User to Enter the Choice
3. Get the input from the User
4. Give the relevant output to User based on the choice
5. Get Information from the User
6. Update the Information to the System
7. Give the confirmation to the user.
8. Again show the Same Homepage to give the choice to the Program
9. Repeat the Program.
'''

# Initial Screen of the Terminal:
def default_ui():
    print("\nWelcome to the Project Score Tracker:")

    print(
        '''
    --- Project Score Tracker Menu ---
    1. Add Team Member Record
    2. Update Team Member Score
    3. Calculate Team Average Score
    4. Find Highest and Lowest Score
    5. Identify Team mambers above Target
    6. Exit
    --------------------------------
    '''
    )

# For initial Page of the Screen
default_ui()

# Create an empty dictionary to add the member data
members_list = {}

# Create the function to get the choice between 1-6 from the user
def get_user_choice():
    # Save the user input to the user_choice variable
    user_choice = input("Enter your choice: ")
    if user_choice == '1':
        add_team_member()
    elif user_choice == '2':
        update_member_score()
    elif user_choice =='3':
        calculate_average_score()
    elif user_choice =='4':
        find_highest_lowest()
    elif user_choice =='5':
        identify_performance_target()
    elif user_choice == "6":
        return False
    else:
        default_ui()

# 1. Fuction to add team member i.e. (user_choice == 1):
def add_team_member():
    member_count = int(input("\n Enter the number of members that you want to set: "))
    for member in range(0, member_count):
        member_name = input("\nEnter team member name: ")
        member_score = float(input(f"Enter {member_name}'s initial score: "))
        print(f"Team member ", member_name, "added successfully with score ", member_score)
        members_list.update({member_name:member_score})
        member_count = member_count + 1
    print("\n")
    default_ui()
    get_user_choice()

# 2. Function to update team member i.e. (user choice == 2):
def update_member_score():
    print(f"\nThe users you currently have are: {members_list.keys()}\n")
    member_name = input("Please enter a user to update the record: ")
    if member_name in members_list.keys():
        new_score = float(input(f"Please give a score to update for {member_name}: \n"))
        members_list[member_name] = new_score
        print(f"The member {member_name}'s score has been successfully updated to {new_score}\n")
    else:
        print("Please enter a valid user from the above list.\n")
    print(members_list)
    print("\n")
    default_ui()
    get_user_choice()

# 3. Function to add the team average score i.e. (user choice == 3):
def calculate_average_score():
    total_score = 0
    for score in members_list.values():
        total_score = score + total_score
    avg_score = total_score / len(members_list)
    # print("Outside of loop")
    # print(len(members_list))
    # print(score)
    print(f"The average score is: {avg_score}")
    print("\n")
    default_ui()
    get_user_choice()    

# 4. Pseudocode for Finding the Maximum & Minimum Score:
'''
1. Create a function
2. Get list of values from the dictionary
3. Sort the values in the list
4. For minimum, Pick the first value.
5. For maximum, pick the last value
6. Print the lowest valule and highest value
'''

# Implement the logic to calculate the maximum & minimum score
def find_highest_lowest():
    values = list(members_list.values())
    print(values)
    values = sorted(values)
    print(f"The lowest score is {values[0]}")
    print(f"The highest score is {values[-1]}")
    print("\n")
    default_ui()
    get_user_choice()

# 5. # Pseudocode for finding the Team Members above the target
'''
1. Define the function & Create a empty list to score the values
2. Get list of values from the dictionary
3. Set the value for performance target with the numeric value
4. Loop through all the values, and compare with Performance target
5. If value > performance target, put it inside the new list created.
6. Extract the keys of the values in the performance target list
7. Print the keys or name from the initial member list.
'''

# Create a function that identifies the values above the performance target.
def identify_performance_target():
    performance_values = []
    performance_target = 80
    performance_members = []
    member_scores = list(members_list.values())

    for key,value in members_list.items():
        if value >= performance_target:

            performance_values.append(value)
            performance_members.append(key)
    print(f" The members above the performance score are: {performance_members}")
    print(f"Their respective scores are: {performance_values}")
    print("\n")
    default_ui()
    get_user_choice()

# Run the Overall Function:
get_user_choice()