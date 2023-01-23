import random

mywordlist = ["table", "chair", "computer", "phone", "car", "red", "door", "window", "mouse", "keyboard", "wire", "light", "water", "hard", "notebook", "shoes", "paper",
              "camera", "hat", "sound", "lock", "screen", "bed", "talk", "run", "bag"]

mynumberlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

pass_word_list = []
for i in range(4):
    pass_word_list.append(random.choice(mywordlist))

pass_number_list = ""
for i in range(6):
    pass_number_list = pass_number_list+(random.choice(mynumberlist))

while True:
    print("Enter [1] for Speech")
    print("Enter [2] for Code")
    choice = input("Enter Choice: ")
    if choice == "1" or choice == "2":
        break


if choice == "1":
    print(pass_word_list)
    counter = 0
    wrong_counter = 0
    while counter < 4:
        password = input("Enter Password: ")
        if password == pass_word_list[counter]:
            print("Next")
            counter += 1
        else:
            wrong_counter += 1
            print("Try Again!")

        if wrong_counter == 3:
            break

    if wrong_counter == 3:
        print("Wrong Password Given!!")
    else:
        print("Unlocked!")

elif choice == "2":
    print(pass_number_list)
    counter = 0
    while counter < 3:
        password = input("Enter Password: ")
        if password == pass_number_list:
            print("Unlocked")
            break
        else:
            print("Try Again")
            counter += 1

    if counter == 3:
        print("Run out of tries")