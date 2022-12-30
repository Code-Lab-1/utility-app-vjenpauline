import sys 
import time

class colors: # To change the color of text
    INPUT = '\033[95m'
    BLUE = '\033[96m'
    END = '\033[0m'

# The list of products for the vending machine menu
sandwiches = [{'id': '1', 'name': 'smoked turkey loaf', 'price': 20.0, 'stock': 3},
              {'id': '2', 'name': 'tomato and cheese focaccia', 'price': 16.5, 'stock': 5},
              {'id': '3', 'name': 'roasted beef sandwich', 'price': 23.4, 'stock': 3}]

pastries = [{'id': '1', 'name': 'almond croissant', 'price': 8.29, 'stock': 4},
            {'id': '2', 'name': 'carrot cake slice', 'price': 10.5, 'stock': 2},
            {'id': '3', 'name': 'strawberry shortcake', 'price': 10.5, 'stock': 2}]

snacks = [{'id': '1', 'name': 'protein bar', 'price': 4.99, 'stock': 5},
          {'id': '2', 'name': 'bag of pretzels', 'price': 5.25, 'stock': 3},
          {'id': '3', 'name': 'bag of chips', 'price': 3.05, 'stock': 2}]

cold_drinks = [{'id': '1', 'name': 'iced latte', 'price': 12.0, 'stock': 3},
            {'id': '2', 'name': 'iced tea', 'price': 6.35, 'stock': 5},
            {'id': '3', 'name': 'bottled frapuccino', 'price': 9.99, 'stock': 3}]

others = [{'id': '1', 'name': 'cola', 'price': 3.25, 'stock': 2},
          {'id': '2', 'name': 'orange juice', 'price': 4.05, 'stock': 4},
          {'id': '3', 'name': 'bottled water', 'price': 2.99, 'stock': 5}]

list_food = ["Sandwiches", "Pastries", "Snacks"]
list_drinks = ["Cold Drinks", "Others"]
languages = ["English", "Arabic", "Filipino", "english", "filipino", "arabic"] # Languages the user can choose from
bar_design = "==============================================="

def content(text):
    """Centers parameter text in the middle of 60 spaces"""
    print(f"{text}".center(60))

def section(text1, text2):
    """
    Prints formatted section of selection in the vending machine
    
    Parameters:
    text1 - Selection prompt
    text2 - Choices
    """
    content(bar_design)
    print("\n")
    content(text1)
    content(text2)
    print("\n")
    content(bar_design)
 
def intro():
    """Asks user to choose a language before continuing"""
    while True:
        usr_lang = input(colors.INPUT + "THE MACHINE IS CASE SENSITIVE - Enter your language: " + colors.END)
        if usr_lang not in languages:
            print("\tPlease only enter the languages as shown.\n")
        else:
            if usr_lang != "English" and usr_lang != "english": # Denies user from going forward unless the language is English 
                print("\tSorry, that language is still a work-in-progress. Choose a different language.\n")
            else:
                break

def menu(subcat):
    """Presents parameter subcat's information in columns, like a menu"""
    for item in subcat:      
        if item.get("stock") == 0:
            print(f'[{item.get("name").upper()} - OUT OF STOCK]') # Notifies user that product is out of stock
            subcat.remove(item) # Removes a product from the menu if its stock is depleted

    print("# --- PRICE ----- NAME")
    for item in subcat:
        print(item.get("id"), "|", item.get("price"), "AED" " |", item.get("name").title())
    print(" ")

def usr_cat():
    """ 
    Asks user to pick product category to buy from
    Displays all menus of subcategories based on category chosen
    """
    global choice
    choice = str(input(colors.INPUT + "Enter your category: " + colors.END))
    if choice == "Food":
        content(bar_design)
        print("\nFOOD - 3 Sub-categories")
        print("\n" + colors.BLUE + "Sandwiches" + colors.END)
        menu(sandwiches)
        print("\n" + colors.BLUE + "Pastries" + colors.END)
        menu(pastries)
        print("\n" + colors.BLUE + "Snacks" + colors.END)
        menu(snacks)

    elif choice == "Drinks":
        content(bar_design)
        print("\nDRINKS - 2 Sub-categories")
        print("\n" + colors.BLUE + "Cold Drinks" + colors.END)
        menu(cold_drinks)
        print("\n" + colors.BLUE + "Others" + colors.END)
        menu(others)
            
    else:
        print("\tPlease only enter 'Food' or 'Drinks'.\n")
        usr_cat()

def buy(subcat):
    """Asks user for number of product to buy based on product sub-category (parameter) chosen"""
    global usr_choice
    global price
    
    usr_choice = input(colors.INPUT + "Enter the number that corresponds with the product you want to buy: " + colors.END)
    for item in subcat:
        if usr_choice == item.get("id"):
            usr_choice = item         
            price = usr_choice.get("price")

            # Displays message of the user's selection of product with its price
            print (f'\tYou\'ve selected a/an {usr_choice.get("name")}! This costs {price} AED.\n')
            usr_choice["stock"] -= 1 # Takes off one from the stock of the product
            time.sleep(1)
            break
                
    else:
        print("\tPlease only enter the numbers shown.\n")
        buy(subcat)

def usr_subcat():
    """
    Asks user for sub-category to buy from
    Outputs function that asks user for product ID number after
    """
    global subcat_ask
    subcat_ask = input(colors.INPUT + "\nEnter the sub-category you would like to buy from: " + colors.END)

    if choice == "Food":
        if subcat_ask == "Sandwiches":
            buy(sandwiches)
        elif subcat_ask == "Pastries":
            buy(pastries)
        elif subcat_ask == "Snacks":
            buy(snacks)
        else:
            print("\tPlease only enter the sub-categories as shown.")
            usr_subcat()
    
    else:
        if subcat_ask == "Cold Drinks":
            buy(cold_drinks)
        elif subcat_ask == "Others":
            buy(others)
        else:
            print("\tPlease only enter the sub-categories as shown.")
            usr_subcat()
    
def usr_payment():
    """Compels user to make a payment through two methods available"""
    payment = input(colors.INPUT + "Enter your method of payment: " + colors.END)
    if payment == "1":
        print("Tap your card on the card reader. It will automatically deduct.") 
        time.sleep(1) # Delay to simulate a vending machine contacting the bank before deducting money
    elif payment == "2":
        cash = float(input(colors.INPUT + "Insert your dirhams on the bill acceptor: " + colors.END)) # Asks user to input an amount of money as payment
        if cash >= price:
            change = cash - price # Subtracts price from user's money to return excess
            print(f"{change} AED has been given back to you.")
        else:
            print("\nYou did not put enough money. Your order has been cancelled and refunded.")
            sys.exit() # Forcefully ends program because of insufficient money 
    else:
        print("\tPlease only enter 1 or 2.\n")
        usr_payment()

def starducks():
    """Main function of the vending machine"""
    content("------| WELCOME TO PAULINE'S STARDUCKS! |------")
    content("The First Ready-To-Go Starducks Vending Machine")

    section("Choose Your Language", "English | Arabic | Filipino")

    intro()

    repeat = True
    while repeat == True:
        section("Choose a Category", "Food | Drinks")
        
        usr_cat()
        content(bar_design)
        usr_subcat()
        section("Choose Your Payment", "Credit Card | Card")
        print("\nType 1 for Credit Card, 2 for Cash")

        usr_payment()
        # Message that user's product has been dispensed
        print(f'\tThank you for purchasing! Your {usr_choice.get("name")} has been dispensed.')
        time.sleep(1)
            
        again = input(colors.INPUT + "\nBuy again? Enter 'quit' to stop: " + colors.END)
        # User may buy multiple products until its stock has been depleted
        if again == "quit":
            repeat = False
            print("\nCome back next time!")
            return

        else: # Buying again will display a message that suggests the user to buy from the category not chosen
            if subcat_ask in list_food:
                content("Get a drink to pair with your " + usr_choice.get("name") + "!" + "\n")
            elif subcat_ask in list_drinks:
                content("Buy food to pair with your " + usr_choice.get("name") + "!" + "\n")
            continue

starducks()