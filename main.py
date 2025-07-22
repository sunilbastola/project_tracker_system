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
print("Welcome to the Project Score Tracker:\n")

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

# Create the function to get the choice between 1-6 from the user
def get_user_choice(user_choice):
    # Save the user input to the user_choice variable
    user_choice = input("Enter your choice: ")
    return user_choice

# Save the output to the variable user_choice
user_choice = get_user_choice()

# Function to direct to approproate function after user making a choice:
def validate_user_choice(user_choice):

    if user_choice == '1':
        add_team_member()
    elif user_choice == '2':
        update_member_score()
    elif user_choice =='3':
        calculate_avg_score()
    elif user_choice =='4':
        find_highest_lowest()
    elif user_choice =='5':
        idenfity_above_target()
    elif user_choice =='6':
        exit_program()
    













    # # Initialize the self method.
    # def __init__(self, user_choice):
    #     self.user_choice = user_choice
    
    # def get_user_input():
    #     input


# Function to add member recodrs:
# def add_member_records():
#     def __init__(self, member, name)
