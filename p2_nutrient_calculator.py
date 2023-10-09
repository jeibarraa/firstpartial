https://replit.com/join/cutkaonkiy-jose-emilioem22

# Function 1
total_calories = 0
total_protein = 0
total_carbohydrates = 0
total_fat = 0

# Information
num_ingredients = int(input("Enter the number of ingredients: "))

for _ in range(num_ingredients):
    ingredient_name = input("Enter the ingredient name: ")
    quantity = float(input(f"Enter the quantity of {ingredient_name} (in grams): "))
    calories_per_100g = float(input(f"Enter calories per 100 grams of {ingredient_name}: "))
    protein_per_100g = float(input(f"Enter protein per 100 grams of {ingredient_name} (in grams): "))
    carbohydrates_per_100g = float(input(f"Enter carbohydrates per 100 grams of {ingredient_name} (in grams): "))
    fat_per_100g = float(input(f"Enter fat per 100 grams of {ingredient_name} (in grams): "))
    
    # Calculate the contribution of this ingredient to the total nutrients
    total_calories += (calories_per_100g / 100) * quantity
    total_protein += (protein_per_100g / 100) * quantity
    total_carbohydrates += (carbohydrates_per_100g / 100) * quantity
    total_fat += (fat_per_100g / 100) * quantity

# Display the total nutritional information for the recipe
print("\nTotal Nutritional Information for the Recipe:")
print(f"Total Calories: {total_calories} calories")
print(f"Total Protein: {total_protein} grams")
print(f"Total Carbohydrates: {total_carbohydrates} grams")
print(f"Total Fat: {total_fat} grams")
