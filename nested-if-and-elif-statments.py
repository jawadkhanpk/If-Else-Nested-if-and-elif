print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
    print("you can ride the rollercoaster")

    age = int(input("What is your age"))

    if age <=12:
        bill = 5
        print("Child Tickets are $5")
    elif age <=18:
        bill = 18
        print("Youth Tickets are $7")
    elif age <= 44:
        bill = 12
        print("Adults Tickets are $12")
    elif age >=45 and age<=55:
        bill = 0
        print("Have a free ride on us")

    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")