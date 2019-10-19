"""
Author:     Ben Mathew, Email: dbm0204@gmail.com
Project:    Building SQL Database and query resultsl
Compiler:   Python 3.X
"""
from  database_utils import database_utils 

"""
ShoppingDB is a class that handes the data declarative 
languages and data insertion.

"""
class shoppingDB(database_utils):

    def __init__(self,fileName):
        database_utils.__init__(self,fileName)

    
    def setup_db(self):
        self.setCursor(self.getConnection())

    def createTables(self):
        stores_str = """CREATE TABLE IF NOT EXISTS stores(id INT,
                        name TEXT,allowed_alcohol TEXT)"""
        self.createTable(stores_str)
        print("Table Creation: stores created...")


        product_str = """CREATE TABLE IF NOT EXISTS products(
                         id INT,name TEXT,upc TEXT,
                         create_at_date TEXT)"""
        self.createTable(product_str)
        print("Table Creation: products created...")


        store_price ="""CREATE TABLE IF NOT EXISTS store_prices(
                        id INT,product_id INT,store_id INT,
                        price FLOAT)"""
        self.createTable(store_price)
        print("Table Creation: store_prices created...")


        order_line_str = """CREATE TABLE IF NOT EXISTS
                            order_line(id INT,
                            product_id INT,store_id INT,qty INT,
                            line_total TEXT)"""
        self.createTable(order_line_str)
        print("Table Creation: order_line created....")

    def insertItems(self):
        stores   = ((1,'Gettar','true'),
                    (2,'Waysafe','false'))
        self.insertRow("stores",stores)
        print("Data Insertion: Data inserted into 'Stores' Table")
        
        products = ((1,'Apple','123','2018-01-01'),
                    (2,'Banana','456','2018-01-02'),
                    (3,'Grapes','789','2018-01-03'),
                    (4,'Golden Banana','456','2018-02-04'),
                    (5,'Bouquet Flowers', '9213123', '2018-02-05'))
        self.insertRow("products",products)
        print("Data Insertion: Data inserted into 'products' table")

        
        store_prices= ((1,3,1,2.59),
                       (2,2,1,3.32),
                       (3,4,1,3.59),
                       (4,3,2,2.34),
                       (5,1,2,1.56))
        self.insertRow("store_prices",store_prices)
        print("Data insertion: Data inserted into 'store_prices' table")

        order_lines= ((1,1,2,3,"NULL"),
                      (2,2,1,50,"NULL"),
                      (3,2,1,1,"NULL"),
                      (4,3,2,4,"NULL"))
        self.insertRow("order_lines",order_lines)
        print("Data insertion: Data inserted into 'order_lines' table")


def main():
    db = shoppingDB("shopDB.db")
    db.setup_db()
    db.createTables()
    db.insertItems()

if __name__=="__main__":
    main()

