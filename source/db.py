### CONNECTS TO MYSQL DATABASE AND QUERIES/UPDATES DATA ###

import pymysql
import os
from dotenv import load_dotenv
import utils


### DATABASE CONNECTIONS ###

# Connects to the MySQL DB
def connect_to_db():
    # Gets DB location and login credentials
    load_dotenv()
    host = os.environ.get('mysql_host')
    user = os.environ.get('mysql_user')
    password = os.environ.get('mysql_pass')
    database = os.environ.get('mysql_db')
    
    # Establishes a DB connection
    connection = pymysql.connect(host, user, password, database)
    cursor = connection.cursor()
    return cursor, connection


# Commits changes and terminates the DB connection
def disconnect_from_db(cursor, connection):
    cursor.close()
    connection.commit()
    connection.close()


# Rolls back changes to DB in case of error
def roll_back_changes_to_db(connection):
    connection.rollback()
    connection.close()


### FETCHING DATA FROM THE DB ###

# Gets data from database table and stores in a list of dictionaries
def create_list_from_db_table(item_type, col_names, dict_keys):
    temp_list = []
    db_table = utils.get_db_table_name(item_type)
    
    try:
        cursor, connection = connect_to_db()
            
    except:
        print('\nWe\'re sorry, something\'s gone wrong. Unable to connect to the database.')
        raise ConnectionError
    
    sql = f'SELECT {col_names} FROM {db_table}'
    if db_table == 'products':
        sql += f' WHERE product_type = \'{item_type}\''
    
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            temp_dict = {}
            for i in range(len(dict_keys)):
                temp_dict[dict_keys[i]] = row[i]
            temp_list.append(temp_dict)
        
        disconnect_from_db(cursor, connection)
    
    except:
        roll_back_changes_to_db(connection)
        print(f'\nWe\'re sorry, something\'s gone wrong. Unable to retrieve {db_table} data from the database.\n')
        raise ConnectionError
    
    return temp_list


# Gets data from a specific field in the db table and stores in a list
def get_field_from_db_table(db_table, col_name):
    temp_list = []
    
    try:
        cursor, connection = connect_to_db()
            
    except:
        print('\nWe\'re sorry, something\'s gone wrong. Unable to connect to the database.')
        raise ConnectionError
        
    try:
        cursor.execute(f'SELECT {col_name} FROM {db_table}')
        rows = cursor.fetchall()
        for row in rows:
            temp_list.append(row[0])
        
        disconnect_from_db(cursor, connection)

    except:
        roll_back_changes_to_db(connection)
        print(f'\nWe\'re sorry, something\'s gone wrong. Unable to retrieve {db_table} data from the database.\n')
        raise ConnectionError
    
    return temp_list


# Gets the name of an item at specified index in the db table
def get_item_name_from_db_table(db_table, item_id):
    col_name = utils.get_name_col_for_item(db_table)
    
    try:
        cursor, connection = connect_to_db()
            
    except:
        print('\nWe\'re sorry, something\'s gone wrong. Unable to connect to the database.')
        raise ConnectionError
        
    try:
        cursor.execute(f'SELECT {col_name} FROM {db_table} WHERE id = {item_id}')
        item_name = cursor.fetchone()
        disconnect_from_db(cursor, connection)
        return ' '.join(map(str, item_name))

    except:
        roll_back_changes_to_db(connection)
        print(f'\nWe\'re sorry, something\'s gone wrong. Unable to retrieve {db_table} data from the database.\n')
        raise ConnectionError



### UPDATING THE DB ###

# Adds a new record to the specified db table
def create_new_record(db_table, values):
    col_names = utils.get_col_names_for_creating(db_table)
    
    try:
        cursor, connection = connect_to_db()
        
    except:
        print('\nWe\'re sorry, something\'s gone wrong. Unable to connect to the database.')
        raise ConnectionError
        
    try:
        cursor.execute(f'INSERT INTO {db_table} ({col_names}) VALUES ({values})')
        disconnect_from_db(cursor, connection)
        
    except:
        roll_back_changes_to_db(connection)
        print(f'\nWe\'re sorry, something\'s gone wrong. Unable to create a new record in the {db_table} table.\n')
        raise ConnectionError


# Deletes a record at the specified index in the db table
def delete_record_from_db(db_table, item_id):    
    try:
        cursor, connection = connect_to_db()
        
    except:
        print('\nWe\'re sorry, something\'s gone wrong. Unable to connect to the database.')
        raise ConnectionError
        
    try:
        cursor.execute(f'DELETE FROM {db_table} WHERE id = {item_id}')
        disconnect_from_db(cursor, connection)
        
    except:
        roll_back_changes_to_db(connection)
        print(f'\nWe\'re sorry, something\'s gone wrong. Unable to delete data from the {db_table} table.\n')
        raise ConnectionError