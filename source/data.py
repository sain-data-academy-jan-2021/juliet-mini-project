### READS APP DATA FROM AND WRITES DATA TO .CSV FILES ###

import utils


# # Converts product and courier ids from strings to integers
# def id_to_integer(item_list):
#     for item in item_list:
#         if 'id' in item:
#             item['id'] = int(item['id'])
#     return item_list


# # Converts product prices from strings to floats in product lists
# def price_to_float(product_list):
#     for product in product_list:
#         if 'price' in product:
#             product['price'] = float(product['price'])
#     return product_list


# Converts string of numbers to a list
# ***DELETE WHEN ORDER DATA IS MIGRATED TO DB***
def num_str_to_lst(num_str):
    if type(num_str) is str and num_str:
        num_list = num_str.split(',')
        
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        return num_list
    
    else:
        return []


# Converts product values from strings to lists within the orders list (after reading from .csv)
# ***DELETE WHEN ORDER DATA IS MIGRATED TO DB***
def products_str_to_lst(orders_list):
    for order in orders_list:
        if 'sandwiches' in order:
            order['sandwiches'] = num_str_to_lst(order['sandwiches'])
            
        if 'cakes' in order:
            order['cakes'] = num_str_to_lst(order['cakes'])
            
        if 'drinks' in order:
            order['drinks'] = num_str_to_lst(order['drinks'])
            
    return orders_list


### REFORMATTING AND WRITING APP DATA TO .CSV ###
# Converts list of numbers to a string
# ***DELETE WHEN ORDER DATA IS MIGRATED TO DB***
def num_lst_to_str(num_lst):
    if type(num_lst) is list and num_lst:
        for i in range(len(num_lst)):
            num_lst[i] = str(num_lst[i])
        
        num_str = ','.join(num_lst)
        return num_str
    
    else:
        return ''


# Converts product values from lists to strings within the orders list (before writing to .csv)
# ***DELETE WHEN ORDER DATA IS MIGRATED TO DB***
def products_lst_to_str(orders_list):
    for order in orders_list:
        order.update({
            'sandwiches': num_lst_to_str(order['sandwiches']), 
            'cakes': num_lst_to_str(order['cakes']), 
            'drinks': num_lst_to_str(order['drinks'])
            })
    return orders_list
