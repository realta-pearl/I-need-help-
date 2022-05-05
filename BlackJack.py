import random 

def generate_deck(list_of_cards_drawn):
    ranks = ("Hearts", "Spades", "Cloves", "Diamonds")
    suits = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "King", "Queen", "Joker", "Jack")
    
    result = ""
    while result == "" or result in list_of_cards_drawn:
        generated_rank = random.choice(ranks)
        generated_suit = random.choice(suits)
        if generated_suit == "Joker":
            result = generated_suit
        else:
            result = generated_suit + " of "+ generated_rank

    list_of_cards_drawn.add(result)
    #print("Current set: " + str(list_of_cards_drawn))
    return result

def byebye():
    print("Game discontinued.")
    exit()    

def playgame():
    check_00 = input("Would you like to play? (Y/N) ")
    #start of the game 
    list_of_cards_drawn = set()
    if check_00.upper() == "Y": 
        # draw two cards first
        for i in range(2):
            current_drawn_card = generate_deck(list_of_cards_drawn)
            print(current_drawn_card)

        #the second round of drawing, draw one card at a time
        while True: 
            check_01 = input("Would you like to draw another card? ")
            if check_01.upper() == "Y":
                current_drawn_card = generate_deck(list_of_cards_drawn)
                print(current_drawn_card) 
            else:
                byebye()
    else:
        byebye()

    
if __name__ == '__main__':
    playgame()