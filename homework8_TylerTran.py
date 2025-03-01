#1 Create a function that accepts a list of sandwich ingredients.
#2 The function should have one parameter that can collect as many arguments as the function call provides.
#3 The function should print a summary of the sandwich being ordered

def order_sandwich(*ingredients):
    if ingredients:
        print("\nYour sandwich has these ingredients:")
        for ingredient in ingredients:
            print(f"{ingredient}")
    else:
        print("\nYou ordered a sandwich with no ingredients.")

#4 Call the function two times with different arguments
order_sandwich("bacon", "lettuce", "tomato")
order_sandwich("meatballs", "marinara")
 