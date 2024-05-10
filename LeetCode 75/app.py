def calculate_coins(decimal_part):
    # Initialize variables to count the number of each coin
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    
    # Convert the decimal part to cents
    cents = int(decimal_part * 100)
    
    # Calculate the number of quarters
    quarters = cents // 25
    cents %= 25
    
    # Calculate the number of dimes
    dimes = cents // 10
    cents %= 10
    
    # Calculate the number of nickels
    nickels = cents // 5
    cents %= 5
    
    # The remaining cents are pennies
    pennies = cents
    
    # Return the counts of each coin
    return quarters, dimes, nickels, pennies

def main():
    # Prompt the user to enter the amount of change owed in dollars
    change_owed = float(input("How much change is owed (in dollars)? "))
    
    # If the user enters a negative number, prompt again until a positive number is entered
    while change_owed < 0:
        print("Please enter a positive number.")
        change_owed = float(input("How much change is owed (in dollars)? "))
    
    # Extract the decimal part
    decimal_part = change_owed - int(change_owed)
    
    # Calculate the number of coins
    quarters, dimes, nickels, pennies = calculate_coins(decimal_part)
    
    # Calculate the total number of coins
    total_coins = quarters + dimes + nickels + pennies
    
    # Display the minimum number of coins required
    print(total_coins)

if __name__ == "__main__":
    main()
