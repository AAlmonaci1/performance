menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00}

menu_2 = {"fries": 2.50,
          "chips": 1.00,
          "pretzel": 3.50}


def orderNum1(menu):
    cart = []
    total = 0
    print("-------------------- MENU --------------------")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("----------------------------------------------")

    while True:
        food = input("Select an item (q to quit)").lower()
        if food == "q":
            break
        elif menu.get(food) is not None:
            cart.append(food)

    print("----------------- YOUR ORDER -----------------")
    for food in cart:
        total += menu.get(food)
        print(food, end=" ")

    print()
    print(f"Total is: ${total:.2f}")
    return cart, total

orderNum1(menu)

######## 2nd Order ########

def orderNum2(menu_2):
    cart = []
    total = 0
    print("-------------------- MENU --------------------")
    for key, value in menu_2.items():
        print(f"{key:10}: ${value:.2f}")
    print("----------------------------------------------")

    while True:
        food = input("Select an item (q to quit)").lower()
        if food == "q":
            break
        elif menu_2.get(food) is not None:
            cart.append(food)

    print("----------------- YOUR ORDER -----------------")
    for food in cart:
        total += menu_2.get(food)
        print(food, end=" ")

    print()
    print(f"Total is: ${total:.2f}")

orderNum2(menu_2)