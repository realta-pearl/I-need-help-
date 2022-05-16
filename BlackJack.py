import random
from sys import exit


def generate_deck(list_of_cards_drawn):
    ranks = ("Hearts", "Spades", "Cloves", "Diamonds")
    suits = (
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "King",
        "Queen",
        "Joker",
        "Jack",
    )

    result = ""
    while result == "" or result in list_of_cards_drawn:
        generated_rank = random.choice(ranks)
        generated_suit = random.choice(suits)
        if generated_suit == "Joker":
            result = generated_suit
        else:
            result = generated_suit + " of " + generated_rank
    list_of_cards_drawn.add(result)


def derive_card_total_value(list_of_cards_drawn):
    power_value_card = {"King", "Queen", "Jack"}
    suit = list()
    for card in list_of_cards_drawn:
        suit.append(card.split(" ")[0])
    total_sum = 0
    for s in suit:
        if "Joker" != s:
            if "Ace" == s:
                if power_value_card.intersection(suit):
                    total_sum += 11
                else:
                    total_sum += 1
            elif s in power_value_card:
                total_sum += 10
            else:
                total_sum += int(s)
    return total_sum


def byebye():
    print("Game discontinued.")
    exit()


def draw_two(list_of_cards_drawn):
    # draw two cards first
    for i in range(2):
        current_drawn_card = generate_deck(list_of_cards_drawn)
    return current_drawn_card


def show_hands(label, list_of_cards_drawn):
    total_card_value = derive_card_total_value(list_of_cards_drawn)
    print("Current hand of " + label + " (" + str(total_card_value) + "):")
    for card in list_of_cards_drawn:
        print(card)
    print("-------------------------")


def check_game_state(player_value_of_cards_drawn, house_value_of_cards_drawn):
    player_current_total_sum = derive_card_total_value(player_value_of_cards_drawn)
    house_current_total_sum = derive_card_total_value(house_value_of_cards_drawn)
    if player_current_total_sum < 21 and house_current_total_sum < 21:
        print("Both player and house still in the money.")
        if player_current_total_sum < house_current_total_sum:
            print("Player is winner.")
        else:
            print("House is winner.")
        # we have yet to reach the end of game situation
        return

    if player_current_total_sum > 21 and house_current_total_sum > 21:
        print("Draw. Both lost.")
    if player_current_total_sum != 21 and house_current_total_sum == 21:
        print("House wins. Player lose.")
    if player_current_total_sum == 21 and house_current_total_sum != 21:
        print("Player wins. House lose.")
    if player_current_total_sum > 21 and house_current_total_sum < 21:
        print("House wins. Player lose.")
    if player_current_total_sum < 21 and house_current_total_sum > 21:
        print("Player wins. House lose.")
    # regardless the game should end here
    byebye()


def playgame():
    check_00 = input("Would you like to play? (Y/N) ")
    # start of the game
    player_list_of_cards_drawn = set()
    house_list_of_cards_drawn = set()

    if check_00.upper() == "Y":
        # draw two cards first
        draw_two(player_list_of_cards_drawn)
        show_hands("Player", player_list_of_cards_drawn)
        draw_two(house_list_of_cards_drawn)
        show_hands("House", house_list_of_cards_drawn)
        check_game_state(player_list_of_cards_drawn, house_list_of_cards_drawn)

        # the second round of drawing, draw one card at a time
        while True:
            check_01 = input("Would you like to draw another card? ")
            if check_01.upper() == "Y":
                generate_deck(player_list_of_cards_drawn)
                show_hands("Player", player_list_of_cards_drawn)
                generate_deck(house_list_of_cards_drawn)
                show_hands("House", house_list_of_cards_drawn)
            else:
                byebye()
            check_game_state(player_list_of_cards_drawn, house_list_of_cards_drawn)
    else:
        byebye()


if __name__ == "__main__":
    playgame()
