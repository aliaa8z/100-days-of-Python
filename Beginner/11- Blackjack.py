# Demo:
# https://appbrewery.github.io/python-day11-demo/

import random

def calc_score(cards):
    if (sum(cards) == 21) and (len(cards) == 2):
        return 0
    if (11 in cards) and (sum(cards) > 21):
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(u_score, computer_score):
    if u_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "lose, computer has blackjack"
    elif u_score == 0:
        return "win, you hava blackjack"
    elif u_score > 21:
        return "lose, you went over 21"
    elif computer_score > 21:
        return "win, compuuter went over 21"
    elif u_score > computer_score:
        return "win, you have higher hand"
    else:
        return "lose, you have lower hand"


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)
        print(f"your cards: {user_cards}, current score: {user_score}")
        print(f"dealer's first hand: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            choice = input("type 'y' to get another card, otherwise type 'n' to pass: ").lower()
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)


    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"dealer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print('\n' * 20)
    play_game()

