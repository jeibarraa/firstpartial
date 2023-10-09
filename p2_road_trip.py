https://replit.com/join/zoclwlmtym-jose-emilioem22
def calculate_trip_cost():
    #  distance in miles
    distance = float(input("Enter the distance in miles: "))
    
    # (MPG)
    mpg = float(input("Enter the car's MPG: "))
    
    # current price of gasoline 
    current_gas_price = float(input("Enter the current price of gasoline per gallon: "))
    
    #  days 
    days = int(input("Enter the number of days you plan to travel: "))
    
    # total cost
    total_cost = 0
    
    # Calculate
    for day in range(1, days + 1):
        # Calculate 
        cost_for_day = (distance / mpg) * current_gas_price
        
        # Add the cost to the total cost
        total_cost += cost_for_day
        
        #new price
        if day < days:
            new_gas_price = float(input(f"Enter the gas price for day {day + 1}: "))
            current_gas_price = new_gas_price
    
    # new cost
    print(f"Total cost of the trip for {days} days: ${total_cost:.2f}")

# calculate final cost
calculate_trip_cost()
