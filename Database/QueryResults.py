"""
Author:     Ben Mathew, Email: dbm0204@gmail.com
Project:    SQL Database construction and Query 
            results from the database
Compiler:   Python 3.X
"""

from ContentProvider import shoppingDB

"""
QueryResults manages the query manapulative 
languages and queries required by the problem 
statment.

"""

class QueryResults(shoppingDB):
    
    def __init__(self,fileName):
        shoppingDB.__init__(self,fileName)
    
    def buildSchema(self):
        self.setup_db()
        print("\n")
        self.createTables()
        print("\n")
        self.insertItems()

    def executeQueryOne(self):
        pass
    
    def executeQueryTwo(self):
        pass
    
    def executeQueryThree(self):
        pass

    def executeQueryFour(self):
        pass

    def executeQueryFive(self):
        pass

def main():
    queryList = QueryResults("shopDB.db")
    queryList.buildSchema()
    print("\nStores allowed to sell Alcohol")
    queryList.executeQueryOne()
    print("\nProduct name of the 2 most expensive items based on their price at store id 1")
    queryList.executeQueryTwo()
    print("\nThe products that are not sold in the store id 2")
    queryList.executeQueryThree()
    print("\nThe most popular item sold:")
    queryList.executeQueryFour()
    print("\nUpdating  the line_total field....")

if __name__=='__main__':
    main()

