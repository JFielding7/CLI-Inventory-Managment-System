import sqlite3

from cli_challenge.backend.product import Product
from cli_challenge.backend.order import Order


class Database:
    @staticmethod
    def create_db():
        connection = sqlite3.connect('cli.db')

        # cursor object
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS ORDERS_TO_PRODUCTS")
        cursor.execute("DROP TABLE IF EXISTS ORDERS_TO_INFO")

        cursor.execute("""CREATE TABLE IF NOT EXISTS ORDERS_TO_PRODUCTS(
                            ORDER_ID INT,
                            PRODUCT_ID INT,
                            BUSHELS DOUBLE
                            )""")
        cursor.execute("INSERT INTO ORDERS_TO_PRODUCTS VALUES (64, 0, 8.7)")
        cursor.execute("INSERT INTO ORDERS_TO_PRODUCTS VALUES (123, 2, 16.34)")
        cursor.execute("INSERT INTO ORDERS_TO_PRODUCTS VALUES (64, 1, 5)")

        cursor.execute("""CREATE TABLE IF NOT EXISTS ORDERS_TO_INFO(
                            ORDER_ID INT,
                            ORDER_DATE TEXT,
                            STATUS INT,
                            COST DOUBLE,
                            REVENUE DOUBLE
                            )""")
        cursor.execute("""INSERT INTO ORDERS_TO_INFO (ORDER_ID, ORDER_DATE, STATUS, COST, REVENUE) 
                            VALUES (?, ?, ?, ?, ?)""", (64, "Feb 26 2019", 3, 350, 669))
        cursor.execute("""INSERT INTO ORDERS_TO_INFO (ORDER_ID, ORDER_DATE, STATUS, COST, REVENUE) 
                            VALUES (?, ?, ?, ?, ?)""", (123, "Feb 26 2019", 0, 250.98, 1760))

        connection.commit()
        connection.close()

    @staticmethod
    def load_database():
        connection = sqlite3.connect('cli.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ORDERS_TO_INFO")

        query = cursor.fetchall()

        orders_dict = {}
        for curr_order in query:
            orders_dict[curr_order[0]] = order = Order(curr_order[1], curr_order[0], curr_order[3], curr_order[4], curr_order[2])
            Order.TOTAL_PROFIT += order.profit()
        cursor.execute("SELECT * FROM ORDERS_TO_PRODUCTS")
        query = cursor.fetchall()
        for curr_order in query:
            orders_dict[curr_order[0]].items.append(Product(curr_order[2], curr_order[1], Product.get_BPMT(curr_order[0])))

        connection.commit()
        connection.close()
        return [*orders_dict.values()]

    create_db()
    # orders = load_database()
    # for order in orders.values():
    #    print(order.items)
