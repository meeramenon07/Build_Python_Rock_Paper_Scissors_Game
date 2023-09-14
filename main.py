import getpass
from getpass import getpass as input
import emoji

print(emoji.emojize("Welcome to the game of :rock: and :paper: and :scissors:"))
print(emoji.emojize("R stands for Rock :rock:"))
print(emoji.emojize("P stands for Paper :paper:"))
print(emoji.emojize("S stands for Scissors :scissors:"))
print()
possible_actions = ["R", "P", "S"]
print("Choose your actions",possible_actions)
print()
score_player1 = 0
score_player2 = 0

while True:
  player1_action = input("Player1 > ")
  print()
  player2_action = input("Player2 > ")
  print()
  if(player1_action== "R"):
    if(player2_action == "R"):
      print("You both chose Rock, it is a tie!")
    elif(player2_action == "S"):
      print("Player1's Rock hits Player2's Scissors! Player1 wins!")
      score_player1 += 1
    elif(player2_action == "P"):
      
      print("Player2's Paper covers Player1's Rock! Player2 wins!")
    score_player2 += 1
  elif(player1_action == "P"):
    if(player2_action == "R"):
     print("Player1's Paper covers Player2's Rock! Player1 wins!")
     score_player1 += 1
    elif(player2_action == "S"):
      print("Player2's Scissors cuts Player1's Paper! Player2 wins!")
      score_player2 += 1
    elif(player2_action == "P"):
     print("Both chose Paper, it is a tie!")
  elif(player1_action == "S"):
    if(player2_action == "R"):
      print("Player2's Rock hits Player1's Scissors! Player2 wins!")
      score_player2 += 1
    elif(player2_action == "P"):
      print("Player1's Scissors cuts Player2's Paper, Player1 wins! ")
      score_player1 += 1
    elif(player2_action == "S"):
      print("Both chose Scissors! It is a tie!")
      print("Player1 has", score_player1, "wins!")
      print("Player2 has", score_player2, "wins!" )
      if score_player1 == 3 and score_player2 == 3:
        print("Thanks for playing a fantastic game!")
        exit()
      else:
        continue
      
