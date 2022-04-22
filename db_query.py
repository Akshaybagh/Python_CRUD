#-*- coding: utf8 -*-

''' MYSQL CRUD '''

import psycopg2 as pdb
import warnings
import psycopg2.extras
import sys
import update as upd

global list_tables

# CREATE A NEW TABLE


def createTable(con):
    with con:

        cur = con.cursor()
        tbl_name=input("Enter table name")
        cur.execute("DROP TABLE IF EXISTS Emp")
        cur.execute(
            "CREATE table " + tbl_name + " (Id SERIAL PRIMARY KEY, Name VARCHAR(25), Company_Name VARCHAR(25), Designation VARCHAR(25), Age VARCHAR(25), City VARCHAR(25));")
        print (tbl_name + ' Table created')

# INSERT VALUES
def GetTableList(t_schema,con):
    # Retrieve the table list

    get_table_names=   "SELECT table_name  FROM information_schema.tables  WHERE (table_schema='public') ORDER BY table_schema, table_name;"
    cur=con.cursor()
    # Retrieve all the rows from the cursor
    cur.execute(get_table_names)

    list_tables = cur.fetchall()

    # Print the names of the tables
    return list_tables
def column_list(con,tbl_name):
     cur = con.cursor()
     get_columns="""select column_name from information_schema.columns where
                                table_schema = 'public' and table_name='{}'""".format(tbl_name)
     cur.execute(get_columns)
     column_names = [row[0] for row in cur]

     print("Column names: {}\n".format(column_names))
     return list(column_names)

def insertTable(con):
    with con:

        try:
            cur = con.cursor()

            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                print("Select a table from the table names given below: ")
                warnings.filterwarnings('ignore', 'unknown table')
                GetTableList('public',con)
                tbl_name=input(("Enter table name: "))
                get_columns="""select column_name from information_schema.columns where
                                table_schema = 'public' and table_name='{}'""".format(tbl_name)
                cur.execute(get_columns)
                column_names = [row[0] for row in cur]

            print("Column names: {}\n".format(column_names))
            print("Enter data accordingly:e.g  {Key value} = name akshay")
            print("How many values do you want to enter?")
            #n=int(input())
            d=list(input("Enter {} values\n".format(len(column_names))).split())
            base_query = "insert into " + tbl_name + " values("
            for i in range(len(d)):
                if (i == len(d) - 1):
                    base_query += "'" + d[i] + "'"
                else:

                    base_query += "'" + d[i] + "'"","
            base_query += ")"
            print(base_query)
            cur.execute(base_query)
            print("Inserted")
        except Exception as e:
            print (e)




# RETRIEVE TABLE ROWS
def retrieveTable(con):
    with con:

        cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
        print("Select a table from the table names given below: ")
        l=GetTableList('public',con)
        print(l)
        tbl_name=input("Enter table name: ")
        l1=column_list(con,tbl_name)
        try:
            q="Select * from "+tbl_name
            cur.execute(q)
            rows = cur.fetchall()
            print("Table Values: ")
            for row in range(len(rows)):
                if rows == None:
                    print ('Table is Empty')
                    break
                else:
                    print(rows[row])
        except Exception as e:
                print("Invalid table name")


def update(con):
    with con:
        cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
        l=GetTableList('public',con)
        print("Available tables: ")
        print(l)
        tbl_name=input("Enter table name: ")
        set_val=(input("Enter values that need to be set: ").split())
        cond=(input("Enter where conditions: ").split())          
        r=upd.update(tbl_name,set_val,cond)
        print(r)
        print(type(r))
        cur.execute(r)
        print ( "Number of rows updated:",cur.rowcount)
        if cur.rowcount == 0:
                print ('Record Not Updated')
        

# UPDATE ROW
def updateRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            q="Select *  "
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            e_id = input("Enter id You want to update")
            name = input("Enter Name for Update Record")
            cname = input("Enter Company Name for Update Record")
            deg = input("Enter Designation for Update Record")
            age = input("Enter Age for Update Record")
            city = input('Enter City Name For Update record')

            cur.execute("UPDATE Emp SET name =%s, Company_Name = %s, Designation = %s, Age = %s, City = %s WHERE Id = %s",
                        (name, cname, deg, age, city, e_id))

            print ( "Number of rows updated:"),  cur.rowcount
            if cur.rowcount == 0:
                print ('Record Not Updated')
        except TypeError as e:
            print ('ID Not Exist ')

#  # DELETE ROW


def deleteRow(con):
    with con:

        try:
            cur = con.cursor()
            cur = con.cursor(cursor_factory=pdb.extras.DictCursor)
            cur.execute("SELECT * FROM Emp")
            rows = cur.fetchall()
            for row in rows:
                print('ID: {0} Name: {1} Company Name: {2} Designation: {3} Age: {4} City: {5}'.format(
                    row[0], row[1], row[2], row[3], row[4], row[5]))

            id = input("Enter ID for Delete Record")
            cur.execute("DELETE FROM Emp WHERE Id = %s", id)
            print ("Number of rows deleted:"), cur.rowcount

        except TypeError as e:
            print ('ID Not Exist ')
