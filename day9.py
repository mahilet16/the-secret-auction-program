

#the secret auction program
import bidlogo
print(bidlogo.logo)
print("Welcome to the secret auction program.")
def my_function(auction_data):
    highest_bid=0
    the_name=""
    for name in auction_data:
        value=auction_data[name]
        if value>highest_bid:
            highest_bid=value
            the_name=name
    print(f"the winner is {the_name} with a bid of {highest_bid}$ ")
again="yes"
blind_auction={}
while again=="yes":
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: $"))
    blind_auction[name]= bid
    again=input("are there any other bidders? Type 'yes' or 'No'")
    if again=="no":
        my_function(blind_auction)







        
