# Formats status in uppercase and updates order_status value in dictionary

def update_order_status(o_dict, o_status):
    try:
        if type(o_dict) == dict and type(o_status) == str:
            o_dict['order_status'] = o_status.upper()
            return o_dict
        else:
            print('TypeError (Invalid input: o_dict must be a dictionary and o_status must be a string.)')
            return TypeError
    
    except Exception as e:
        return Exception