import sqlite3

connect = sqlite3.connect("mydb.db")

query = """ CREATE TABLE scripts(
        language text,
        users integer,
        complexity text
        ) """
cursor = connect.cursor()
cursor.execute(query) 

connect.commit()
connect.close()
