# Program Name: Assignment1.py (use the name the program is saved as)
# Course: IT3883/Section W01(85546)
# Student Name: Tesfaye Woldemariam
# Assignment Number: Assignment 1 
# Due Date: 09/20/ 2026
# Purpose: What does the program do (in a few sentences)? The python code Initializes an empty input buffers and offer a menue user to append data ,clear the buffer ,display its contents or exit the program 
# List Specific resources used to complete the assignment.


# Initialize an empty input buffer
input_buffer =[]

# append data to the input buffer
def append_data():
    user_input = input("Enter a string to append:")
    input_buffer.append(user_input)
    print("Data appended successfully.")

# clear the input buffer
def clear_buffer():
    input_buffer.clear()
    print("Input buffer cleared.")

# display the input buffer
def display_buffer():
    if not input_buffer:
        print("Input buffer is empty.")
    else:
        print("Input buffer:", ', '.join(input_buffer))
# Main program loop
while True:
    print("\nMenu Options:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit")

    # Get user choice
    choice = input("Enter your choice (1-4): ")

    # Process user choice
    if choice == '1':
        append_data()
    elif choice == '2':
        clear_buffer()
    elif choice == '3':
        display_buffer()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1-4.")
