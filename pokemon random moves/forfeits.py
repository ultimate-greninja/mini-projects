# forfeits.py
import time
import random

# List of lewd forfeits (you can fill this out)
forfeit_list = [
    "Lock your collar to a heavy object for 60 minutes!",
    "Hold your pee for 30 minutes!",
    "Watch a hypnosis video focused on collaring!",
    "Watch a hypnosis video about bondage and restraint!",
    "Watch a hypnosis video on denial and teasing!",
    "Watch a hypnosis video involving humiliation themes!",
    "Watch a hypnosis video that explores diaper play!",
    "Watch a hypnosis video that explores cucking!",
    "Do 50 squats while wearing your collar!",
    "Do 30 push-ups while wearing your collar!",
    "Hold a plank position for 2 minutes while wearing your collar!",
    "Do 20 jumping jacks while wearing your collar!",
    "Do 15 lunges on each leg while wearing your collar!",
    "Take a picture of yourself while wearing your collar!",
    "Record yourself meowing for 3 minutes!",
    "Record yourself barking for 3 minutes!",
    "Sort out an album for fursuits on phone!",
    "No cumming until the next 5 forfeits are complete!",  # This will now add 5 to the counter
    "hump the couch or teddy until you have edged 10 times don't cum until next forfeit, if you cum type 'cummies sowwy'!"
]

# Counter to keep track of completed forfeits
completed_forfeits = 0
no_cumming_active = False
denial_counter = 0  # Start the counter at 0 to add incrementally

def forfeits():
    global completed_forfeits, no_cumming_active, denial_counter  # Access the global variables
    print("Forfeit activated! Stopping inputs temporarily...")
    time.sleep(2)  # Brief pause before prompting the user

    # Select a random forfeit from the list
    selected_forfeit = random.choice(forfeit_list)
    print(f"Your forfeit is: {selected_forfeit}")

    # Check if the selected forfeit is "No cumming"
    if "No cumming until the next 5 forfeits are complete!" in selected_forfeit:
        no_cumming_active = True
        denial_counter += 5  # Add 5 to the counter
        print(f"You must complete {denial_counter - completed_forfeits} more forfeits before you can cum!")
    
    user_input = input("Please type 'done' when you have completed the forfeit: ")  # Ask for user input

    # Keep prompting until the user enters 'done' or 'cummies sowwy'
    while user_input.lower() not in ['done', 'cummies sowwy']:
        print("That's not it! Please type 'done' when you have completed the forfeit.")
        user_input = input("Your response: ")  # Ask for user input again

    # Check has made to "cummies" 
    if user_input.lower() == 'cummies sowwy':
        denial_counter += 10  # Add 10 more forfeits needed
        print("You made cummies when you wearn't allowed to, 10 more forfeits needed to cum again.")

    # The user completed the forfeit
    if user_input.lower() == 'done':
        completed_forfeits += 1
        remaining_forfeits = denial_counter - completed_forfeits  # Calculate remaining forfeits
        print(f"You have {remaining_forfeits} forfeits left until you can cum!")

        # Check if the condition is satisfied
        if completed_forfeits >= denial_counter:
            print("You can cum now! 🎉")
            completed_forfeits = 0  # Reset the counter for the next round
            no_cumming_active = False  # Deactivate the no cumming condition
            denial_counter = 0  # Reset cum counter to initial value
        else:
            print("Thank you for completing the forfeit!")
