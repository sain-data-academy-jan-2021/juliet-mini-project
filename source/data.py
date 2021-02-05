### READS APP DATA FROM AND WRITES DATA TO .CSV FILES ###

import utils
import csv
from io import UnsupportedOperation


### READING APP DATA FROM .CSV AND REFORMATTING ###

# Reads app data from .csv file and stores as list of dictionaries
def get_data_from_csv(filepath):
    temp_list = []
    try:
        with open(filepath, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            for line in data:
                temp_list.append(line)
        return temp_list
    
    except FileNotFoundError:
        utils.clear_terminal()
        utils.app_title()
        print(f'We\'re sorry, something\'s gone wrong.\nApp failed to start. Unable to locate source data file: {filepath}\n')
        exit()
    
    except UnsupportedOperation:
        utils.clear_terminal()
        utils.app_title()
        print(f'We\'re sorry, something\'s gone wrong.\nApp failed to start. Unable to read source data file: {filepath}\n')
        exit()
    
    except Exception as e:
        utils.clear_terminal()
        utils.app_title()
        print(f'We\'re sorry, something\'s gone wrong.\nApp failed to start. An error has occurred: {e}\n')
        exit()


# Converts product prices from strings to floats in product lists
def price_to_float(product_list):
    for product in product_list:
        if 'price' in product:
            product['price'] = float(product['price'])
    return product_list


# Converts string of numbers to a list
def num_str_to_lst(num_str):
    if type(num_str) is str and num_str:
        num_list = num_str.split(',')
        
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        return num_list
    
    else:
        return []


# Converts product values from strings to lists within the orders list (after reading from .csv)
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
def num_lst_to_str(num_lst):
    if type(num_lst) is list and num_lst:
        for i in range(len(num_lst)):
            num_lst[i] = str(num_lst[i])
        
        num_str = ','.join(num_lst)
        return num_str
    
    else:
        return ''


# Converts product values from lists to strings within the orders list (before writing to .csv)
def products_lst_to_str(orders_list):
    for order in orders_list:
        order.update({
            'sandwiches': num_lst_to_str(order['sandwiches']), 
            'cakes': num_lst_to_str(order['cakes']), 
            'drinks': num_lst_to_str(order['drinks'])
            })
    return orders_list


# Writes order data to .csv file from list of dictionaries
def write_data_to_csv(filepath, item_list, item_type):
    item_count = len(item_list)
    try:
        with open(filepath, 'w') as csv_file:
            dict_keys = list(utils.get_field_names(item_type).keys())
            data_file = csv.DictWriter(csv_file, fieldnames = dict_keys)
            data_file.writeheader()
            
            if item_count >= 0:
                for item in item_list:
                    data_file.writerow(item)
                
    except UnsupportedOperation:
        print(f'We\'re sorry, something\'s gone wrong.\nUnable to save changes. Unable to write to file: {filepath}\n')
        exit()
        
    except Exception as e:
        print(f'We\'re sorry, something\'s gone wrong.\nUnable to save changes. An error has occurred: {e}\n')
        exit()