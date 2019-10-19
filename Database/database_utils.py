"""
Author:     Ben Mathew, Email:dbm0204#gmail.com
Project:    SQLite3 Python Implementations 
Compiler:   Python3
"""
#Import Statements
import sqlite3
"""
databse_utlils is a class thats manages
the connection and cursor of the database 
"""
class database_utils():
    def __init__(self,fileName):
        try:
            self.conn = sqlite3.connect(fileName)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(str(e))

    def getConnection(self):
        return self.conn

    def getCursor(self):
        return self.cursor
 
    def setConnection(self,fileName):
        try:
            self.conn = sqlite3.connect(fileName)
        except Exception as e:
            print(str(e))

    def setCursor(self,connect):
        try:
            self.cursor = connect.cursor()
        except Exception as e:
            print(str(e))
    def closeConnection(self):
        try:
            self.con.close()
        except Exception as e:
            print(str(e))
    def commitTransaction(self):
        try:
            self.conn.commit()
        except sqlite3.DatabaseError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def insertRow(self,tableName,data):
        try:
            self.cursor.executemany("INSERT INTO "+
                                    str(tableName)+
                                    " VALUES(?,?,?)",data)
        except sqlite3.DatabaseError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def createTable(self,query):
        try:
            self.cursor.execute(query)
        except sqlite3.DatabaseError as e:
            print(str(e))

    def dropTable(self,tableName):
        try:
            self.cursor.execute("DROP TABLE IF EXISTS " + tableName)
        except sqlite3.DatabaseError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def retrieveResults(self,string):
        results_str = ""
        try:
            self.cursor.execute(string)
            rows = self.cursor.fetchall()
            for row in rows:
                results_str+=str(row)
                results_str+="\n"
            return results_str
        except sqlite3.DatabaseError as e:
            print(str(e))
        except Exception as e:
            print(str(e))

    def delete(self):
        try:
            self.cursor.execute("DROP TABLE *")
        except sqlite3.DatabaseError as e:
            print(str(e))
        except Exception as e:
            print(str(e))
    
def insert_rows(db):
    create_customer_table="""CREATE TABLE cars(id INT,
                                        name TEXT,
                                        price INT )"""
    db.createTable(create_customer_table)
    cars = ((1, 'Audi', 52642),
            (2, 'Mercedes', 57127),
            (3, 'Skoda', 9000),
            (4, 'Volvo', 29000),
            (5, 'Bentley', 350000),
            (6, 'Hummer', 41400),
            (7, 'Volkswagen', 21600))
    db.insertRow("cars",cars)

def main():
    db = database_utils("test1.db")
    db.setCursor(db.getConnection())
    db.dropTable("cars")
    insert_rows(db)
    results_str =db.retrieveResults("""SELECT * FROM cars""")
    print(results_str)

if __name__=='__main__':
    main()
