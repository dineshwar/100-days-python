import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

def print_highest_bid(bids):
    highest_bid = 0
    highest_bidder = ''
    for bid in bids:
        if (bids[bid] > highest_bid):
            highest_bidder = bid
            highest_bid = bids[bid]

    print(f'The winner is {highest_bidder} with a bid of ${highest_bid}')
auction_active = True
all_bids = {}
print("Welcome to the secret auction program.")
while auction_active:
    name =  input("What is your name? ")
    if (all_bids.get(name) is not None):
        print("Name already exist, enter a unique name.")
        continue
    amount = int(input("What's your bid? "))
    all_bids[name] = amount
    ans = input("Are there any other bidders? Type 'yes' or 'no': ")
    if ans == 'yes':
        os.system('clear')
    else:
        auction_active = False
        print_highest_bid(all_bids)


