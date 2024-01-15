from random import choice


def main():
    print(r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    print("Welcome to Blackjack!")
    play_blackjack()


def deck():
    return {
        'A': 11,
        'K': 10,
        'Q': 10,
        'J': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
    }


def deal_card():
    deck_deal = deck()
    return choice(list(deck_deal.keys()))


def card_value(card):
    deck_value = deck()
    return deck_value[card]


def play_blackjack():
    hand = []
    dealer_hand = []
    hand_total = 0
    dealer_total = 0

    game_over = False

    while not game_over:
        if hand_total == 0:
            dealer_hand.append(deal_card())
            dealer_total += card_value(dealer_hand[0])

            hand.append(deal_card())
            hand.append(deal_card())
            hand_total = card_value(hand[0]) + card_value(hand[1])

            print(f"Dealer's hand: {dealer_hand[0]}")
            print(f"Dealer's hand total: {dealer_total}")
            print(f"Your hand: {hand[0]}, {hand[1]}")
            print(f"Your hand total: {hand_total}")
        elif hand_total < 21:
            print(f"Your hand: {', '.join(hand)}")
            print(f"Your hand total: {hand_total}")
        if hand_total > 21:
            if 'A' in hand:
                hand_total -= 10
            else:
                print(f"Your hand: {', '.join(hand)}")
                print(f"Your hand total: {hand_total}")
                print("You busted!")
                game_over = True
        else:
            hit_or_stand = input("Hit or stand? ")
            if hit_or_stand.lower() == 'hit':
                hand.append(deal_card())
                hand_total += card_value(hand[-1])
            elif hit_or_stand.lower() == 'stand':
                dealer_hand.append(deal_card())
                dealer_total = card_value(dealer_hand[0]) + card_value(dealer_hand[1])
                print(f"Dealer's hand: {dealer_hand[0]}, {dealer_hand[1]}")
                print(f"Dealer's hand total: {dealer_total}")
                while dealer_total < 17:
                    if dealer_total > hand_total:
                        print("Dealer wins!")
                        break
                    dealer_hand.append(deal_card())
                    dealer_total += card_value(dealer_hand[-1])
                    print(f"Dealer's hand: {', '.join(dealer_hand)}")
                    print(f"Dealer's hand total: {dealer_total}")
                if dealer_total > 21:
                    if 'A' in dealer_hand:
                        dealer_total -= 10
                    else:
                        print("Dealer busted!")
                        print("You win!")
                elif dealer_total > hand_total:
                    print("Dealer wins!")
                elif dealer_total < hand_total:
                    print("You win!")
                else:
                    print("It's a tie!")
                game_over = True
            else:
                print("Please enter 'hit' or 'stand'.")


if __name__ == '__main__':
    main()
