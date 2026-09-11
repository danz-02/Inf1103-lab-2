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

    ##Trigger Overstock Alert
        if (inventory+stock_input) > max_inventory:
                print("Warning! Inventory exceed 500.")
                failed_entries = failed_entries + 1
                break
        inventory += stock_input
    else:
        print("Error! invalid input")
        failed_entries = failed_entries + 1

        
print("\n Final Inventory Report")
print(f"Total Units Processed (Final Stock): {inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
