import dbtext, os
import pyodbc
    
testdbname = "ttdb_" + str(os.getpid()) # some temporary name not to clash with other tests
with dbtext.DBText(testdbname) as db: # the name you use here will be used for the directory name in the current working directory
    # You need a script 'create_empty.sql' that sets up the schema but no data
    # db.create will set up the schema and read the test data from a directory here called "db_tables"
    db.create(sqlfile="empty_db.sql")
     
    # Then it should take the testdbname and configure your system to start a server against the new database
    # ...
    #do_some_setup()
    #db.update_start_rv() # tell it the test is starting for real now
    # do whatever it is the test does

    connectionString = f"DRIVER={{MySQL}};SERVER=localhost;PORT=3306;DATABASE={testdbname};USER=root;OPTION=3;"

    with pyodbc.connect(connectionString) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM people WHERE name LIKE 'Charles Darwin';")
        cursor.commit()


    db.dumptables("users", "*", usemaxcol="") # dump changes in all the tables you're interested in. "myext" is whatever extension you want to use, probably the TextTest one 
