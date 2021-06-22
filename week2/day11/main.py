import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10,11]
game_over = False
player_hand = []

dealer_hand = []

def deal_card():
    card = random.choice(cards)
    print(card)
    return card 

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

i = 0
while (i < 2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    i+=1
while not game_over:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    print(dealer_score)
    print(player_score)

if player_score == 0 or dealer_score == 0 or player_score > 21:
    game_over = True
else:
    player_deal = input("'y' for another card; 'n' to pass: ")
    if player_deal == 'y':
       player_hand.append(deal_card())
    else:
        game_over = True
