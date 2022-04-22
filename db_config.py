#-*- coding: utf8 -*-

import sys
import psycopg2


# CREATE THE DATABASE

def creatdb_postgres():
    con = psycopg2.connect(database="testdb", user="postgres",
                  password="1234", host="127.0.0.1", port="5432")
    print( "Create database testdb")

# SET UP THE CONNECTION
try:
    con= psycopg2.connect(database="testdb",user="postgres",password="1234",host="127.0.0.1",port="5432")
    cur=con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print (ver)

except Exception as e:
    print(e)
    sys.exit(1)

creatdb_postgres()
