import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10,11]

player_hand = []

dealer_hand = []

#def hit(target_hand):
    #todo


def play():
    i = 0
    while (i < 2):
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
        i+=1
print(random.choice(cards))
play()
print(dealer_hand, 'dealer')
print(player_hand, 'player')