import random  #import random esliye use kiye hai becz random value assign hongi 

player=input("Enter rock,Enter scissors,Enter paper   :  ")
computer=random.choice(["rock","scissors","paper"]) #syntax random.choice([])

if player==computer:
  print("draw")

elif player=="rock" and computer=="scissors":
  print("player wins")

elif player=="paper" and computer=="rock":
  print("player wins")

elif player=="scissors" and computer=="paper":
  print("player wins")

else:
  print("Computer wins")
