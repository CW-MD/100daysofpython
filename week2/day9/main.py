#Blind Auction
#While 'More Bidders' != N 
import art

cur_data = {}


def auction():
    more_bids = True
    
    print(art.image)

    while more_bids != False:
        name = input('What is your name?')
        bid = input('What is your bid?')
        listMaker(name, bid)
        bidders = input('Are there more bidders? "Y" / "N" ?').upper()
        if bidders == 'N':
            print(cur_data)
            more_bids = False


def listMaker(name, bid):
    cur_data[name] = bid


auction()