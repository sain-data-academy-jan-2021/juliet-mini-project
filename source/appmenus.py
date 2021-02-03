### APP MENU SCREENS ###

# Get menu option selected by user
def get_option(input):
    return input('Please enter a number to select an option: ')


# Displays app's main menu and gets user selection
def display_main_menu():
    print(\
'''--------- MAIN MENU ---------\n
What would you like to do?
1 - View or update our product lists
2 - View or update our courier list
3 - Place or update an order
0 - Exit app
''')
    return get_option(input)


# Displays product type menu and gets user selection
def product_type_menu():
    print(\
f'''--------- PRODUCT TYPE MENU ---------\n
Which product type would you like to view/update?
1 - Sandwiches
2 - Cakes
3 - Drinks
4 - Return to the main menu
0 - Exit app
''')
    return get_option(input)


# Displays product menus and gets user selection
def product_menu(product_type):
    print(\
f'''--------- {product_type.upper()} MENU ---------\n
What would you like to do?
1 - View our {product_type} list
2 - Add a new {product_type}
3 - Update an existing {product_type}
4 - Remove an existing {product_type}
5 - Return to the product type menu
6 - Return to the main menu
0 - Exit app
''')
    return get_option(input)


# Displays courier menu and gets user selection
def courier_menu():
    print(\
'''--------- COURIER MENU ---------\n
What would you like to do?
1 - View our courier list
2 - Add a new courier
3 - Update an existing courier
4 - Remove an existing courier
5 - Return to the main menu
0 - Exit app
''')
    return get_option(input)


# Displays order menu and gets user selection
def order_menu():
    print(\
'''--------- ORDER MENU ---------\n
What would you like to do?
1 - View all orders
2 - Place a new order
3 - Update status of an order
4 - Update an order
5 - Delete an order
6 - Return to the main menu
0 - Exit app
''')
    return get_option(input)
