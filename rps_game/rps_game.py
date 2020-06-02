import random


user = int(input("Enter a number from 0-2: "))
computer = random.randint(0, 2)


def get_hand(hand_number):
    outcome = {0: "rock", 1: "paper", 2: "scissors"}
    return outcome.get(hand_number)


def determine_winner(player_hand, comp_hand):
    if player_hand == comp_hand:
        return "Tie"
    if player_hand == "rock":
        if comp_hand == "paper":
            return "You lose"
        if comp_hand == "scissors":
            return "You win"
    if player_hand == "paper":
        if comp_hand == "rock":
            return "You win"
        if comp_hand == "scissors":
            return "You lose"
    if player_hand == "scissors":
        if comp_hand == "rock":
            return "You lose"
        if comp_hand == "paper":
            return "You win"
            

print(f"User: {get_hand(user)}")
print(f"Computer: {get_hand(computer)}")
print(determine_winner(get_hand(user), get_hand(computer)))
