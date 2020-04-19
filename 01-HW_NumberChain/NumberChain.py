# Initial variable to track game play
user_play = "y"
start_number = 0

# While we are still playing...
while user_play == "y":
    
    # Ask the user how many numbers to loop through
    x = int(input("How many numbers? "))
    x = start_number + x
    

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for i in range(start_number, x):

        # Print each number in the range
        print(i)
        
        start_number = start_number+1

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")
    
    if user_play == "y":
        continue
    elif user_play =="n":
        break
    else: 
        break
    
    