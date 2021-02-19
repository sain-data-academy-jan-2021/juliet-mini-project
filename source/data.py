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
