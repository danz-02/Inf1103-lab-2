##Set inventory to '0'
inventory=0
max_inventory=500
failed_entries=0



while True:
    ##User-input
    user_input= input("Enter a stock quantity: ")

    if user_input == "quit":
        print("Exiting the program...")
        break
    ##Check for valid-input
    elif user_input.isdigit():
    
        stock_input = int(user_input)

        