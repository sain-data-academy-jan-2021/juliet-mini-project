# from source.ordstatus import update_order_status

# # Test 1: update order_status of fully populated dictionary

# def test_one():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }
#     o_status = 'pending'
#     expected = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'PENDING'
#     }
    
#     result = update_order_status(o_dict, o_status)
    
#     assert result == expected
#     print('Passed test one')

# test_one()


# # Test 2: update order_status of dictionary when order_status value is empty string

# def test_two():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': ''
#     }
#     o_status = 'cancelled'
#     expected = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'CANCELLED'
#     }
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test two')

# test_two()


# # Test 3: update order_status of dictionary when order_status value is None

# def test_three():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': None
#     }
#     o_status = 'cancelled'
#     expected = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'CANCELLED'
#     }
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test three')

# test_three()


# # Test 4: update order_status of dictionary when order_status key-value pair is missing from o_dict

# def test_four():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#     }
#     o_status = 'cancelled'
#     expected = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'CANCELLED'
#     }
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test four')

# # test_four()


# # Test 5: update order_status of dictionary when o_dict is an empty dictionary

# def test_five():
#     o_dict = {}
#     o_status = 'cancelled'
#     expected = {'order_status': 'CANCELLED'}
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test five')

# # test_five()


# # Test 6: update order_status when o_status is an empty string

# def test_six():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }
#     o_status = ''
#     expected = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': ''
#     }
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test six')

# # test_six()


# # Test 7: update order_status when o_status is Boolean. TypeError expected as o_status must be a string.

# def test_seven():
#     o_dict = {
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }
#     o_status = True
#     expected = TypeError
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test seven')

# # test_seven()


# # Test 8: update order status when o_dict dictionary is inside a list. TypeError expected as o_dict must be a dictionary.

# def test_eight():
#     o_dict = [{
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }]
#     o_status = 'Cancelled'
#     expected = TypeError
    
#     result = update_order_status(o_dict, o_status)

#     assert result == expected
#     print('Passed test eight')

# # test_eight()


# # Test 9: update order status when o_dict and o_status are passed in the wrong order. TypeError expected as both arguments are wrong data type.

# def test_nine():
#     o_dict = [{
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }]
#     o_status = 'Cancelled'
#     expected = TypeError
    
#     result = update_order_status(o_status, o_dict)

#     assert result == expected
#     print('Passed test nine')

# # test_nine()


# # Test 10: update order status when both function arguments are missing. TypeError expected as function arguments missing.

# def test_ten():
#     o_dict = [{
#         'order_number': 'JAM-1', 
#         'order_date': '20/01/2021 11:59',
#         'customer_name': 'Chloe Brennan', 
#         'customer_address': '24 Ramsay Street, Erinsborough, MK16 9ET', 
#         'customer_phone': '01234 711578',
#         'preferred_courier': 'Thomas', 
#         'order_status': 'DELIVERED'
#     }]
#     o_status = 'Cancelled'
#     expected = TypeError
    
#     result = update_order_status()

#     assert result == expected
#     print('Passed test ten')

# # test_ten()