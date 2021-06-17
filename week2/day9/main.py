#Blind Auction
#While 'More Bidders' != N 
import art

cur_data = {}


def auction():
    more_bids = True
    print(art.image)

    while more_bids != False:
        name = input('What is your name?')
        bid = int(input('What is your bid? $'))
        listMaker(name, bid)
        bidders = input('Are there more bidders? "Y" / "N" ?').upper()
        if bidders == 'N':
            print(cur_data)
            maxFinder(cur_data)
            more_bids = False


def listMaker(name, bid):
    cur_data[name] = bid


def maxFinder(dict):
    highest_bid = 0
    winner = ''
    for key in dict:
        if dict[key] > highest_bid:
            highest_bid = dict[key]
            winner = key
    print(f'The winner is{winner}, with a bid of ${highest_bid}!')

auction()