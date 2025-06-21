import random
count = 0
while True:

    a = random.randint(1,10)
    b = random.randint(1,10)

    user_choice = input("Roll the dice? (y/n): ").lower()
   
    if user_choice == "y":
        no_of_dice = int(input("How many dice you want to roll? (1/2) "))

        if no_of_dice == 1:
            print(a)
            count += 1
        else:
            print (f' ({a}, {b})')
            count += 2

    elif user_choice == "n":
        print("Thanks for playing!")
        print(f'you have rolled {count} times')
        break

    else:
        print("Invalid Choice")
        
