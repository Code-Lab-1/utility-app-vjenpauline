import sys
import time

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

languages = ["English", "Arabic", "Filipino", "english", "filipino", "arabic"]
bar_design = "-----------------------------------------------"

list_food = ["Sandwiches", "Pastries", "Snacks"]
list_drinks = ["Cold Drinks", "Others"]

def content(text):
    print(f"{text}".center(60))

def section(text1, text2):
    content(bar_design)
    print("\n")
    content(text1)
    content(text2)
    print("\n")
    content(bar_design)
 
def intro():
    while True:
        usr_lang = input("(THE MACHINE IS CASE SENSITIVE) Enter your language: ")
        if usr_lang not in languages:
            print("\tPlease only enter the languages as shown.\n")
        else:
            if usr_lang != "English" and usr_lang != "english":
                print("\tSorry, that language is still a work-in-progress. Choose a different language.\n")
            else:
                break

def menu(subcat):
    print("# --- PRICE ----- NAME")
    for item in subcat:      
        if item.get("stock") == 0:
            subcat.remove(item)

    for item in subcat:
        print(item.get("id"), " |", item.get("price"), " |", item.get("name").title())

def usr_cat():
    choice = str(input("Enter your category: "))
    if choice == "Food":
        content(bar_design)
        print("\nFOOD (3 Sub-categories)")
        print("\nSandwiches")
        menu(sandwiches)
        print("\nPastries")
        menu(pastries)
        print("\nSnacks")
        menu(snacks)

    elif choice == "Drinks":
        content(bar_design)
        print("DRINKS (2 Sub-categories)")
        print("\nCold Drinks")
        menu(cold_drinks)
        print("\nOthers")
        menu(others)
            
    else:
        print("\tPlease only enter 'Food' or 'Drinks'.\n")
        usr_cat()

def buy(subcat):
    global usr_choice
    global price
    
    usr_choice = input("Enter the number that corresponds with the product you want to buy: ")
    for item in subcat:
        if usr_choice == item.get("id"):
            usr_choice = item         
            price = usr_choice.get("price")

            print (f'\tYou\'ve selected a/an {usr_choice.get("name")}! This costs {price} AED.\n')
            usr_choice["stock"] -= 1
            time.sleep(1)
            break
                
    else:
        print("\tPlease only enter the numbers shown.\n")
        buy(subcat)

def usr_subcat():
    global subcat_ask 
    subcat_ask = input("\nEnter the sub-category you would like to buy from: ")

    if subcat_ask == "Sandwiches":
        buy(sandwiches)
    elif subcat_ask == "Pastries":
        buy(pastries)
    elif subcat_ask == "Snacks":
        buy(snacks)
    elif subcat_ask == "Cold Drinks":
        buy(cold_drinks)
    elif subcat_ask == "Others":
        buy(others)
    else:
        print("\tPlease only enter the sub-categories as shown.")
        usr_subcat()
    
def usr_payment():
    payment = input("Enter your method of payment: ")
    if payment == "1":
        print("Tap your card on the card reader. It will automatically deduct.")
        time.sleep(1)
    elif payment == "2":
        cash = float(input("Insert your cash on the bill acceptor: "))
        if cash >= price:
            change = cash - price
            print(f"{change} AED has been given back to you.")
        else:
            print("\nYou did not put enough money. Your order has been cancelled.")
            sys.exit()
    else:
        print("\tPlease only enter 1 or 2.\n")
        usr_payment()

def starducks():
    content("------| WELCOME TO PAULINE'S STARDUCKS! |------")
    content("The First Ready-To-Go Starducks Vending Machine")

    section("Choose Your Language", "English | Arabic | Filipino")

    intro()

    repeat = True
    while repeat == True:
        section("Choose a Category", "Food | Drinks")
        
        usr_cat()
        usr_subcat()
        section("Choose Your Payment", "Credit Card | Card")
        print("Type 1 for Credit Card, 2 for Cash")

        usr_payment()
        print(f'\tThank you for purchasing! Your {usr_choice.get("name")} has been dispensed.')
        time.sleep(1)
            
        again = input("\nBuy again? Enter 'quit' to stop: ")
        if again == "quit":
            repeat = False
            return

        else:
            if subcat_ask in list_food:
                content("Get a drink to pair with your " + usr_choice.get("name") + "!")
            elif subcat_ask in list_drinks:
                content("Buy food to pair with your " + usr_choice.get("name") + "!")
            continue

starducks()