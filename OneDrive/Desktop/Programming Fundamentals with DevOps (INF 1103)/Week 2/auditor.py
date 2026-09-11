##Set inventory to '0'
inventory=0

##User-input
user_input= input("Enter a stock quantity: ")


while user_input != "quit":
    user_input= input("Enter a stock quantity: ")

    if user_input == "quit":
        print("Exiting the program...")
        
    else:
        stock_input = int(user_input)
        inventory = inventory + stock_input