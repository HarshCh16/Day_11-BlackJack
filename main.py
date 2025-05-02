import random
from ascii_art import logo


cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]


def score_update():
        print(f"Your cards : {user_hand} , current score : {sum(user_hand)}")
        print(f"Dealer\'s cards : {dealer_hand[0]} , dealer\'s score : {dealer_hand[0]}")

def user_ace_check():
    while 11 in user_hand:
        value = input("You got an ace, would you like to change it\'s value to 1 or keep it to 11? Type \'y' for 1 and \'n' for 11. ").lower()
        if value == "y":
            user_hand[user_hand.index(11)] = 1
            score_update()
        else :
            break
        
def dealer_ace_check():
    while 11 in dealer_hand:
        if sum(dealer_hand) > 21:
            dealer_hand[dealer_hand.index(11)] = 1
        else :
            break


def deal():
    for _ in range(2):
        user_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

    while sum(dealer_hand) <= 16:
        dealer_hand.append(random.choice(cards))
    
    dealer_ace_check()
    score_update()
    user_ace_check()
    # print(dealer_hand)


def final_score_update():
    print("Result : ")
    print(f"Your cards : {user_hand} , current score : {sum(user_hand)}")
    print(f"Dealer\'s cards : {dealer_hand} , dealer\'s score : {sum(dealer_hand)}")

    
def hit():
    user_hand.append(random.choice(cards))
    user_ace_check()

def blackjack_check():
    if sum(user_hand) == 21 or sum(dealer_hand) == 21:
        final_score_update()
        if sum(user_hand) == 21 and sum(dealer_hand) == 21:
            print("You both have Blackjack. It\'s a draw.")
        elif sum(user_hand) == 21:
            print("You have BlackJack. You won!")
        elif sum(dealer_hand) == 21:
            print("The dealer has BlackJack. You lose.")
        return True

    elif sum(user_hand) > 21 or sum(dealer_hand) > 21:
        final_score_update()
        if sum(user_hand) > sum(dealer_hand):
            print("You overwent, Dealer won.")
        elif sum(user_hand) < sum(dealer_hand):
                print("The Dealer overwent. You Won!")
        if sum(user_hand) > 21 and sum(dealer_hand) > 21:
            print("You both overwent. Its a draw")
        return True

    else :
        return False 

def winner_check():
    if sum(user_hand) < 22 and sum(dealer_hand) < 22:
        final_score_update()
        if sum(user_hand) > sum(dealer_hand):
            print("You Won!")
        elif sum(user_hand) < sum(dealer_hand):
            print("You Lose.")
        elif sum(user_hand) == sum(dealer_hand):
            print("It\'s a Draw.")

another_game = True

while another_game == True:

    game = input("Do you want to play a game of Blackjack? Type \'y' or \'n'. ").lower()

    if game == "y":
        print(logo)
        should_continue = True
        user_hand = []
        dealer_hand = []

        deal()
        
        if blackjack_check():
            should_continue = False
            print("\n" * 2)
        
        while should_continue == True:
            another_card = input("Type \'y' to hit another card, type \'n' to stand. ").lower()
            if another_card == "y":
                hit()
                if blackjack_check():
                    should_continue = False
                    print("\n" * 2)
                else:
                    score_update()
            elif another_card == "n":
                if not blackjack_check():
                    winner_check()
                    should_continue = False
                    print("\n" * 2)

    
    elif game == "n":
        another_game = False
        print("Bye")

    else :
        another_game = False
        print("Invalid input")