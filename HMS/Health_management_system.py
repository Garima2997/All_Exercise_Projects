import datetime

def getdate():
    today_date = datetime.datetime.now()
    date = today_date.strftime("%Y-%m-%d")
    time = today_date.strftime("%H:%M:%S")
    return date, time;

def write(client_name):
    if client_name == 1:
        choice = int(input("You want to log into: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            food_value = input("Enter food: ")
            with open ("Harry_food.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {food_value} at {time} \n")
        else:
            exercise_name = input("Enter Exercise: ")
            with open ("Harry_exc.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {exercise_name} at {time} \n")
    elif client_name == 2:
        choice = int(input("You want to log into: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            food_value = input("Enter food: ")
            with open("Rohan_food.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {food_value} at {time} \n")
        else :
            exercise_name = input("Enter Exercise: ")
            with open("Rohan_exc.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {exercise_name} at {time} \n")
    elif client_name == 3:
        choice = int(input("You want to log into: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            food_value = input("Enter food: ")
            with open("Gaurav_food.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {food_value} at {time} \n")
        else:
            exercise_name = input("Enter Exercise: ")
            with open("Gaurav_exc.txt", "a") as f:
                date, time = getdate()
                f.write(f"{date}:  {exercise_name} at {time} \n")
    else:
        print("Invalid Input! Try again!!")


def read(client_name):
    if client_name == 1:
        choice = int(input("You want to read: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            with open("Harry_food.txt", "r") as f:
                print(f.read())
        else:
            with open("Harry_exc.txt", "r") as f:
                print(f.read())
    elif client_name == 2:
        choice = int(input("You want to read: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            with open("Rohan_food.txt", "r") as f:
                print(f.read())
        else:
            with open("Rohan_exc.txt", "r") as f:
                print(f.read())
    elif client_name == 3:
        choice = int(input("You want to read: \n 1.Food \n 2.Exercise \n"))
        if choice == 1:
            with open("Gaurav_food.txt", "r") as f:
                print(f.read())
        else:
            with open("Gaurav_exc.txt", "r") as f:
                print(f.read())
    else:
        print("Invalid Input! Try again!!")


redo_action = "True"
print(redo_action)
while redo_action == "True":
    print(redo_action)
    action = int(input("You want to Write or Read: \n 1.Write \n 2.Read \n"))
    client_name = int(input("Enter the Client Name: \n 1.Harry \n 2.Rohan \n 3.Gaurav \n"))
    if action == 1:
        write(client_name)
    elif action == 2:
        read(client_name)
    redo_action = input("You want to Write or Read again: \n True \n False \n")
    print (redo_action)
else:
    print("No Redo -Thank you!!")
