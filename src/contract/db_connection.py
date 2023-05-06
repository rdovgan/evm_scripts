import mysql.connector
from configparser import ConfigParser
import os


def read_db_config(filename='../../resources/config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    filename = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    return db


def insert_record(query: str, record_to_insert):
    connection = None
    cursor = None
    try:
        db_configuration = read_db_config()
        connection = mysql.connector.connect(**db_configuration)

        cursor = connection.cursor()
        cursor.execute(query, record_to_insert)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def read_record(query: str):
    connection = None
    cursor = None
    try:
        db_configuration = read_db_config()
        connection = mysql.connector.connect(**db_configuration)

        cursor = connection.cursor()
        cursor.execute(query)
        # get all records
        records = cursor.fetchone()

        return records

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()


# contract_link [owner, contract_type, contract_link]
def read_contract(owner):
    return read_record(f'SELECT * FROM contract_link WHERE owner = "{owner}"')


def insert_contract(record_to_insert):
    insert_query = """INSERT INTO contract_link (owner, contract_type, contract_address) 
        VALUES (%s, %s, %s) """
    insert_record(insert_query, record_to_insert)
