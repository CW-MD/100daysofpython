#Blind Auction
#While 'More Bidders' != N 
import art

def auction():
    more_bids = True
    print(art.image)

    while more_bids != False:
        name = input('What is your name?')
        bid = input('What is your bid?')
        bidders = input('Are there more bidders? "Y" / "N" ?').upper()
        if bidders == 'N':
            more_bids = False





auction()