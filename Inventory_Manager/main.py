menu = {
    "1.": "Add product",
    "2.": "View inventory",
    "3.": "Search product",
    "4.": "Update stock",
    "5.": "Delete product",
    "6.": "Calculate inventory value",
    "7.": "Exit"
}

products = [
    {
        "name": "Keyboard",
        "price": 1200,
        "quantity": 5
    },
    {
        "name": "Mouse",
        "price": 700,
        "quantity": 8
    },
    {
        "name": "Headphones",
        "price": 1500,
        "quantity": 3
    }
]


def show_menu():

    for options, values in menu.items():
        print(options, values)

    option = input("Enter an option: ").strip()
    return option


def add_product():

    new_product = {}

    new_product["name"] = input("Enter the product name: ").strip()
    if not new_product["name"]:
        print("Enter a valid product name.")
        return

    try:
        new_product["price"] = int(input("Enter the product price: ").strip())
    except ValueError:
        print("That's not a number!")
        return
    if new_product["price"] <= 0:
        print("Enter a valid number!")
        return

    try:
        new_product["quantity"] = int(input("Enter the quantity: ").strip())
    except ValueError:
        print("That's not a number!")
        return
    if new_product["quantity"] < 0:
        print("Enter a valid number!")
        return

    products.append(new_product)


def view_inventory():

    for product in products:
        print(product["name"])
        print(product["price"])
        print(product["quantity"])


def search_product():
    found = False

    search = input("Enter the product name: ").strip()

    for product in products:
        if product["name"] == search:
            print(product["name"])
            print(product["price"])
            print(product["quantity"])
            found = True

    if not found:
        print("Product couldn't be found.")


def update_stock():
    found = False

    search = input("Enter the product name: ").strip()

    for product in products:
        if product["name"] == search:
            print(product["name"])
            print(product["price"])
            print(product["quantity"])
            found = True

            try:
                new_quantity = int(input("What do you want to update the quantity to?: ").strip())
            except ValueError:
                print("That's not a number!")
                return
            if new_quantity < 0:
                print("Enter a valid number!")
                return

            product["quantity"] = new_quantity

    if not found:
        print("Product couldn't be found.")


def delete_product():
    found = False

    search = input("Enter the product name: ").strip()

    for product in products:
        if product["name"] == search:
            products.remove(product)
            found = True

    if not found:
        print("Product couldn't be found.")


def calculate_inventory_value():

    total = 0

    for product in products:
        total = product["price"] * product["quantity"] + total

    print("Total inventory value:", total)


while True:

    option = show_menu()

    if option == "1":
        add_product()

    elif option == "2":
        view_inventory()

    elif option == "3":
        search_product()

    elif option == "4":
        update_stock()

    elif option == "5":
        delete_product()

    elif option == "6":
        calculate_inventory_value()

    elif option == "7":
        break

    else:
        print("That's not a valid option!")