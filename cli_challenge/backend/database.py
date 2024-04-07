import sqlite3

from cli_challenge.backend.product import Product
from order import Order


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
                        STATUS INT
                        )""")
    cursor.execute("INSERT INTO ORDERS_TO_INFO (ORDER_ID, ORDER_DATE, STATUS) VALUES (?, ?, ?)", (64, "Feb 26 2019 12:00:00 GMT", 3))
    cursor.execute("INSERT INTO ORDERS_TO_INFO (ORDER_ID, ORDER_DATE, STATUS) VALUES (?, ?, ?)", (123, "Feb 26 2019 12:00:00 GMT", 0))

    connection.commit()
    connection.close()


def load_database():
    connection = sqlite3.connect('cli.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ORDERS_TO_INFO")

    query = cursor.fetchall()

    orders = {}
    for order in query:
        orders[order[0]] = Order(order[1], order[0], order[2])

    cursor.execute("SELECT * FROM ORDERS_TO_PRODUCTS")
    query = cursor.fetchall()
    for order in query:
        orders[order[0]].items.append(Product(order[2], order[1], Product.get_BPMT(order[0])))

    connection.commit()
    connection.close()
    return orders


create_db()
orders = load_database()
for order in orders.values():
    print(order.items)
