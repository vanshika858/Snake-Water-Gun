# Exercise6 : Snake Water Gun
import random
print("Number of Round you want to play : ")
round = int(input())
draw_round = 0
c_point = 0
p_point= 0
while(round > 0):
    cpu = ["Snake" , "Water" , "Gun"]
    cpu_choice = random.choice(cpu)

    print("Enter player choice")
    player_choice = input()

    print("cpu choice is : " , cpu_choice)
    if player_choice == "Snake":
        if cpu_choice == "Snake":
            print("Draw!!")
            draw_round =+ 1
        elif cpu_choice == "Water":
            print("Won!!")
            p_point =+ 1
        else:
            print("Loss")
            c_point =+ 1
    elif player_choice == "Water":
        if cpu_choice == "Snake":
            print("Loss!!")
            c_point =+ 1
        elif cpu_choice == "Water":
            print("Draw!!")
            draw_round =+ 1
        else:
            print("Won")
            p_point =+ 1
    else:
        if cpu_choice == "Gun":
            print("Draw!!")
            draw_round =+ 1 
        elif cpu_choice == "Water":
            print("Loss!!")
            c_point =+ 1
        else:
            print("Won")
            p_point =+ 1

        round =- 1

print("Total score at the end of round")
print("Number of Matches draw between cpu and player ")
print(f"{draw_round} rounds")
print("Number of matches cpu wins")
print(f"{c_point} rounds")
print("number of matches player won")
print(f"{p_point} round")