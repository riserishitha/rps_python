print("Start Game!!")
print("How to play: Enter 1 for rock or Enter 2 for paper or Enter 3 for scissor.")
user_input1=input("Enter 1 or 2 or 3 - ")
user_input2=input("Enter 1 or 2 or 3 - ")
if len(user_input1)==1 and len(user_input2)==1:
    if user_input1==user_input2:
        print("it's tie, play again")
    elif user_input1=="2" and user_input2=="1" or user_input1=="3" and user_input2=="2" or user_input1=="1" and user_input2=="3":
        print("User1 won!")
    elif user_input1=="3" and user_input2=="1" or user_input1=="2" and user_input2=="3" or user_input1=="1" and user_input2=="2":
        print("User2 won!")
else:
    print("No Input")
print("Play again")