import mysql.connector
from configparser import ConfigParser

'''
records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
                         (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                         (6, 'Microsoft Surface', 2330, '2019-07-23')]
'''


def read_db_config(filename='../../resources/config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
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


def insert_records(records_to_insert):
    connection = None
    cursor = None
    try:
        db_configuration = read_db_config()
        connection = mysql.connector.connect(host=db_configuration['host'],
                                             database=db_configuration['database'],
                                             user=db_configuration['user'],
                                             password=db_configuration['password'],
                                             port=db_configuration['port'])

        insert_query = """INSERT INTO land_info (id, coord_x, coord_y, cyber, steampunk, wind, volcano, fire, water, 
                necro, mecha, dragon, meadow, is_shore, is_island, is_mountain_foot, rarity, entropy)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """

        cursor = connection.cursor()
        cursor.executemany(insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def read_all():
    connection = None
    cursor = None
    try:
        db_configuration = read_db_config()
        connection = mysql.connector.connect(**db_configuration)

        sql_select_query = "select * from land_info"
        cursor = connection.cursor()
        cursor.execute(sql_select_query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        return records

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


#read_all()
