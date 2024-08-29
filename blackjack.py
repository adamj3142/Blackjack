import random

def draw_card(hand, deck):
    random_card_index = random.randint(0,len(deck)-1)
    hand.append(deck_of_cards[random_card_index])
    deck.pop(random_card_index)
    return(hand,deck)

def print_hands(results=False):
    print("Player: ")
    print(player_hand)
    print("total:")
    print(hand_value(player_hand))
    print("Dealer: ")
    print(dealer_hand)
    print("total:")
    print(hand_value(dealer_hand))
    if results == False:
        print("--------------\n")

def hand_value(hand):
    hand_value = 0
    num_of_aces = 0
    for card in hand:
        if card[0] == "J":
            hand_value += 10
        elif card[0] == "Q":
            hand_value += 10
        elif card[0] == "K":
            hand_value += 10
        elif card[0] == "A":
            hand_value += 11
            num_of_aces += 1
        elif card[0] == "1":
            hand_value += 10
        else:
            hand_value += int(card[0])
        while num_of_aces > 0 and hand_value > 21:
            hand_value -= 10
            num_of_aces -= 1
    return hand_value

def create_deck():
    suit_of_cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits = ["H","D","S","C"]
    deck_of_cards = []

    #6 decks
    for i in range (0,6):
        #4 suits
        for i in range(0,4):
            for card_number in suit_of_cards:
                new_card = card_number + suits[i]
                deck_of_cards.append(new_card)
    return deck_of_cards

########################################################
play_again = "Y"

player_credits = int(input("How many credits would you like to start with? "))

while play_again == "Y":

    deck_of_cards = create_deck()

    player_hand = []
    dealer_hand = []

    number_of_hands = -1
    next_hand = []
    current_hand = -1

    player_hands = []

    bet = int(input("How much would you like to bet? "))
    original_bet = bet

    player_hand, deck_of_cards = draw_card(player_hand, deck_of_cards)
    dealer_hand, deck_of_cards = draw_card(dealer_hand, deck_of_cards)

    while current_hand <= number_of_hands:
        if len(next_hand) > 0:
            player_hand = []
            print("Because you split, you still have another hand...!")
            player_hand.append(next_hand[current_hand])
            bet = original_bet
        
        player_hand, deck_of_cards = draw_card(player_hand, deck_of_cards)
        print_hands()

        player_choice = "Sp"
        asked = False
        while player_hand[0][0] == player_hand[1][0] and player_choice == "Sp":
            player_choice = str(input("Hit or Stand or Double or Split? [H/S/D/Sp]"))
            asked = True
            if player_hand[0][0] == player_hand[1][0] and player_choice == "Sp":
                number_of_hands += 1
                next_hand.append(player_hand[1])
                player_hand.pop(1)
                player_hand, deck_of_cards = draw_card(player_hand, deck_of_cards)
                print_hands()
                asked = False

        if asked == False:
            player_choice = str(input("Hit or Stand or Double? [H/S/D] "))            

        while player_choice == "H" or player_choice == "D":
            

            player_hand, deck_of_cards = draw_card(player_hand, deck_of_cards)
            print_hands()
            if len(player_hand) == 3 and player_choice == "D":
                bet = bet * 2
                player_choice = "DD"
            else:
                if hand_value(player_hand) > 21:
                    player_choice = "B"
                    print("BUST")
                else:
                    player_choice = str(input("Hit or Stand? [H/S]"))

        player_hands.append(player_hand)
            
        current_hand += 1
    
    print("\n\nROUND OVER\nRESULTS:")
    hand_num = 0
    for hand in player_hands:
        player_hand = hand
        hand_num += 1
        print("---\n")
        print("Result for hand num ", str(hand_num), ": ")

        if hand_value(player_hand) > 21:
            print("BUST")
            player_credits -= bet
            print("New balance:")
            print(player_credits)
        elif (hand_value(player_hand) == 21 and len(player_hand) == 2) and (hand_value(dealer_hand) != 21 or len(dealer_hand != 2)):
            print("WINNER - 2.5x BLACKJACK BONUS")
            player_credits += bet * 1.5
            print("New balance:")
            print(player_credits)
        else:
            while hand_value(dealer_hand) < 17:
                dealer_hand, deck_of_cards = draw_card(dealer_hand, deck_of_cards)
            print_hands()
            if hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
                print("WINNER\n")
                player_credits += bet
                print("New balance:")
                print(player_credits)
            elif hand_value(player_hand) == hand_value(dealer_hand):
                print("DRAW\n")
                print("Balance:")
                print(player_credits)
            else:
                print("LOSER\n")
                player_credits -= bet
                print("New balance:")
                print(player_credits)
        
        
    play_again = str(input("Play again? [Y/N]"))

print("GAME OVER")
print("Credits: ", str(player_credits))
        
