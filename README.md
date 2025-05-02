# 🃁 BlackJack

Blackjack is a popular card game where players aim to get as close to a score of 21 as possible without exceeding it. Players are dealt two cards, and they can choose to 'hit' for more cards or 'stand' to keep their current hand. The dealer plays according to fixed rules and the winner is determined based on the final scores.

## How it Works

Starting the Game: When the game starts, the player is prompted with a message asking if they want to play. If the player types 'y', the game proceeds; otherwise, it ends.

Dealing Cards: Both the player and the dealer are dealt two cards randomly from a set of card values (11 for Ace, 2, and 3). The player's and dealer's hands are displayed, with the dealer's second card hidden for now.

Player's Turn: The player can choose to 'hit' (draw another card) or 'stand' (keep their current hand). If the player exceeds 21 points (busted), they lose the game. Additionally, Aces can be adjusted between 1 or 11 to avoid going over 21.

Dealer's Turn: The dealer draws cards automatically until their total score is 17 or higher. If the dealer's score exceeds 21, they bust, and the player wins.

Endgame Conditions: The game ends when the player or dealer reaches a Blackjack (score of 21), busts, or when both hands are compared to determine the winner.

Ace Handling: The program checks if either the player or the dealer has an Ace (value of 11). If the total score exceeds 21, the Ace’s value is automatically changed to 1.

## 🛠️ Features

Player vs Dealer: The player competes against the dealer in this game.

Card Drawing Mechanism: The player can choose to hit or stand.

## 🐛Bugs and improvements

If you find an issue or have a suggestion for improvement, please submit it using the 'Issues' tab above. If you’re submitting a pull request (PR) with a fix, make sure to reference the related issue in the PR description.

Ace Value Adjustment: The game adjusts the value of Aces if necessary.

Blackjack Check: The game automatically checks if either the player or dealer has Blackjack (21 points).

Score Display: The current score of the player and dealer is displayed after each action.
