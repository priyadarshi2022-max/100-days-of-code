from replit import clear
from art import logo

print(logo)
print("Welcome to the SECRET AUCTION PROGRAM.")

bidding = True
auction_dict = {}

while bidding:
  name = input("What's your name? ")
  bid = float(input("What's your bid? $"))
  auction_dict[name] = bid
  other_bidders = input("Are there any other bidders? ")
  if other_bidders.lower() == 'no':
    bidding = False
  clear()

keys_auction = list(auction_dict.keys())
values_auction = list(auction_dict.values())
position = values_auction.index(max(values_auction))
highest_bidder_name = keys_auction[position]

print(f"The winner is {highest_bidder_name} with a bid value of $ {max(values_auction)}")
    
  
