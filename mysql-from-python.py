import os
import pymysql
import datetime


# Get username from Cloud9 workspace

# (modify this variable if running on another environment)

username = os.getenv('C9_USER')



# Connect to the database

connection = pymysql.connect(host='localhost',

                             user=username,

                             password='',

                             db='Chinook')



try:

   with connection.cursor() as cursor:

        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",(24, 'bob'))

        connection.commit()

finally:

    # Close the connection, regardless of whether or not the above was successful

    connection.close()
