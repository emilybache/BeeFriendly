"""
Create the db text files based on the production database
"""

connectionString = "DRIVER={MySQL};SERVER=localhost;PORT=3306;DATABASE=users;USER=root;OPTION=3;"

import dbtext
import pyodbc


with pyodbc.connect(connectionString) as conn:
    testdb = dbtext.DBText("users", conn) # the name "dump" doesn't matter, just a temporary name
    testdb.write_data("db_tables", use_master_connection=True) # creates a directory called db_tables
    