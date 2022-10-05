from replit import clear
#call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_completed = False

def highest_bidder(bidding_history):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_history:
        bid_amount = bidding_history[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        

while not bidding_completed:
    name = input("What is your name?")
    bid_price = int(input("What is your bid? $"))
    bids[name] = bid_price
    continue_bidding = input("Are there anymore bidders?  Type 'yes' or 'no'.\n")
    if continue_bidding == "no":
        bidding_completed = True
        highest_bidder(bids)
    elif continue_bidding =="yes":
        clear()
