# my_string = "2,5,7"
# my_list = my_string.split(',')
# print(my_list)

# string_again = ','.join(my_list)
# print(string_again)

import tabulate
import utils

orders = [
    {'order_number': 'JAM-1', 
     'order_date': '20/01/2021 11:59', 
     'customer_name': 'Chloe Brennan', 
     'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
     'customer_phone': '01234 711578', 
     'courier': 'Thomas', 
     'order_status': 'COMPLETED', 
     'sandwiches': '0,2,3', 
     'cakes': '1,13', 
     'drinks': '1,12,13'
     }, 
    {'order_number': 'JAM-2', 
     'order_date': '20/01/2021 12:14', 
     'customer_name': 'Sherlock Holmes', 
     'customer_address': '221B Baker Street, Bedford, MK14 8IP', 
     'customer_phone': '01234 721546', 
     'courier': 'Ethan', 'order_status': 'COMPLETED', 
     'sandwiches': None, 
     'cakes': '', 
     'drinks': '5,8,9,13'
     }, 
    {'order_number': 'JAM-3', 
     'order_date': '22/01/2021 09:48', 
     'customer_name': 'Rachel Mason', 
     'customer_address': '9 Waterloo Road, Rochdale, MK14 8IR', 
     'customer_phone': '01908 898764', 
     'courier': '', 
     'order_status': 'CANCELLED', 
     'sandwiches': '5,6', 
     'cakes': '3,5,9', 
     'drinks': '0,5,6'}
]

# def tabulate_test(lst):
#     dict_keys = list(lst[0])
#     data = [item.values() for item in lst]
#     print(tabulate.tabulate(data, dict_keys, tablefmt = 'psql'))

# tabulate_test(orders)


# # Converts string of numbers to a list
# def num_str_to_lst(num_str):
#     if type(num_str) is str and num_str:
#         num_list = num_str.split(',')
        
#         for i in range(len(num_list)):
#             num_list[i] = int(num_list[i])
#         return num_list
    
#     else:
#         return []


# # Converts product values from strings to lists within the orders list (after reading from .csv)
# def products_str_to_lst(orders_list):
#     for order in orders_list:
#         order.update(
#             {
#             'sandwiches': num_str_to_lst(order['sandwiches']), 
#             'cakes': num_str_to_lst(order['cakes']), 
#             'drinks': num_str_to_lst(order['drinks'])
#             }
#             )
#     return orders_list

# products_str_to_lst(orders)
# print(orders)


# # Converts list of numbers to a string
# def num_lst_to_str(num_lst):
#     if type(num_lst) is list and num_lst:
#         for i in range(len(num_lst)):
#             num_lst[i] = str(num_lst[i])
        
#         num_str = ','.join(num_lst)
#         return num_str
    
#     else:
#         return ''

# # Converts product values from lists to strings within the orders list (before writing to .csv)
# def products_lst_to_str(orders_list):
#     for order in orders_list:
#         order.update({
#             'sandwiches': num_lst_to_str(order['sandwiches']), 
#             'cakes': num_lst_to_str(order['cakes']), 
#             'drinks': num_lst_to_str(order['drinks'])
#             })
#     return orders_list

# products_lst_to_str(orders)
# print()
# print(orders)


my_dict = {'order_number': 'JAM-1', 
            'order_date': '20/01/2021 11:59', 
            'customer_name': 'Chloe Brennan', 
            'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
            'customer_phone': '01234 711578', 
            'courier': 'Thomas', 
            'order_status': 'COMPLETED', 
            'sandwiches': '0,2,3', 
            'cakes': '1,13', 
            'drinks': '1,12,13'
            }

# headers = list(my_dict.keys())
# print(headers)

# dict_keys = list(utils.get_dict_keys('order').keys())
# print(dict_keys)

# item_list = []
# if not item_list:
#     print(f'The list is currently empty.')


# # Gets a list of product/courier strings from the global lists of dictionaries
# def get_list_of_strings(item_list):
#     temp_list = []
#     for item in item_list:
#         temp_list.append(item.get('name'))
    
#     return temp_list

# test_cakes = [{'name': 'Lemon drizzle cake', 'price': '2.45'}, {'name': 'Chocolate brownie', 'price': '2.25'}, {'name': "Millionaire's shortbread", 'price': '2.4'}, 
#               {'name': 'Carrot & walnut cake', 'price': '2.9'}, {'name': 'Blueberry muffin', 'price': '2.1'}, {'name': 'White chocolate cookie', 'price': '1.85'}, 
#               {'name': 'Peanut butter cookie', 'price': '1.85'}, {'name': 'Apple crumble muffin', 'price': '2.1'}, {'name': 'Fruity flapjack', 'price': '1.75'}, 
#               {'name': 'Pain au chocolat', 'price': '2.2'}, {'name': 'Pain aux raisins', 'price': '2.2'}, {'name': 'Almond croissant', 'price': '2.3'}, 
#               {'name': 'Lemon square', 'price': '2.25'}]

# # print(test_cakes)
# # print()

# print(test_cakes[0]['name'])

# def test_func(item_id, max_item_id):
#     if -1 < item_id < max_item_id:
#         print('passed')
#     print(item_id)

# test_func(2, 14)

# def inner_func():
#     try:
#         my_list = [1]
#         # print(my_list[2])
#         my_list = my_list + 1
    
#     except IndexError:
#         print('index doesn\'t exist')
#         raise IndexError
    
#     except TypeError:
#         print('you cant do that to a list')
#         raise TypeError

#     return 'bananas'

# def middle_func():
#     inner_func()

# def outer_func():
#     try:
#         middle_func()
#     except:
#         print('something went wrong')
#         # pass

# # middle_func()
# # outer_func()

# print(len("Flat 368, Nelson Mandela House, Peckham, MK48 3ET"))

# o_courier = 1
# o_sandwiches = '3, 4, 5'
# o_cakes = ''
# o_drinks = '5'

# optional_fields = [o_courier, o_sandwiches, o_cakes, o_drinks]
# order_data = f'Jam-15, 27/June/20, \'PREPARING\', Pip'
# for field in optional_fields:
#     if field:
#         if type(field) is int:
#             order_data = order_data + f', {field}'
#         else:
#             order_data = order_data + f', \'{field}\''

# print(order_data)

if 0:
    print('truthy')
else:
    print('falsy')