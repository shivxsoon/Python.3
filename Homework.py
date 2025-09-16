try:
    age = int(input("Enter your age: "))

    if 0 < age <=120:
        print("Your age is valid")

        if age % 2 == 0:
            print("You age is even.")
        else:
            print("Your age is odd.")
    else:
        print("Error: Age entered is not realistic.")
except ValueError:
    print("Error: Please enter a valid number for age.")