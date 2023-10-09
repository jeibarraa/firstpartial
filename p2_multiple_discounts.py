https://replit.com/join/rkgucjkzzg-jose-emilioem22
def calculate_discounted_price(price, category, units):
    category_discounts = {'A': 0.10, 'B': 0.05, 'C': 0.02}
    base_discount = price * category_discounts.get(category, 0)
    additional_discount = 0.05 if units > 10 else 0
    total_discount = base_discount + additional_discount
    discounted_price = price - total_discount
    return discounted_price

price = float(input("Enter the price of the product: "))
category = input("Enter the category (A, B, or C): ").upper()
units = int(input("Enter the number of units purchased: "))

discounted_price = calculate_discounted_price(price, category, units)

print(f"Final price after discounts: ${discounted_price}")
