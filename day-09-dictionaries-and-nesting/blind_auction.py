def get_bid():
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))
    data = {
        "name": name,
        "bid": bid
    }
    return data


def start_auction():
    bids = []
    auction_over = False
    
    while auction_over == False:
        bid = get_bid()

        bids.append(bid)
        
        should_continue_input = input('Any other people bidding? y/n: ')

        if should_continue_input != 'y':
            auction_over = True
        
    highest_bid = {
        "name": "",
        "bid": 0
    }

    for curr in bids:
        if curr['bid'] > highest_bid['bid']:
            highest_bid = curr
    print(f"{highest_bid['name']} has won")

start_auction()


