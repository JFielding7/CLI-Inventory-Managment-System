from PyQt6 import QtWidgets, uic
import sys

from PyQt6.QtWidgets import QTableWidgetItem, QTreeWidgetItem
from PyQt6.QtWidgets import QTableWidgetItem, QPushButton

from cli_challenge.backend.bin import Bin
from cli_challenge.backend.database import Database
from cli_challenge.backend.order import Order
from cli_challenge.backend.elevator import Elevator

class Ui(QtWidgets.QMainWindow):


    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('frontend.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

    def populate_table(self, orders: list[Order]):
        self.order_table.setRowCount(len(orders))
        for i in range(len(orders)):
            strs = [orders[i].id, orders[i].status_str(), orders[i].date, f"${orders[i].cost:.2f}", f"${orders[i].revenue:.2f}", f"${orders[i].revenue-orders[i].cost:.2f}"]
            for j, p in enumerate(map(lambda i: QTableWidgetItem(str(i)), strs)):
                self.order_table.setItem(i, j, p)
            self.total_profit.setText(f"Total Profit: ${Order.TOTAL_PROFIT:.2f}")

            button = QPushButton("Advance order")
            #button.clicked.connect(self.p)
            self.order_table.setIndexWidget(self.order_table.model().index(i, 0), button)
        self.total_profit.setText(f"Your Total Profit Is: ${Order.TOTAL_PROFIT:.2f}")

    def populate_tree(self, bins: list[Bin]):
        for i in range(len(bins)):
            item = ["bin "+str(i+1), str(bins[i].weight)]
            q = QTreeWidgetItem(item)
            self.bins.addTopLevelItem(q)
            #for item in bins[i].items:


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    orders = Database.load_database()
    window.populate_table(orders)

    elevator = Elevator()
    products = []
    for order in orders:
        for i in range(len(order.items)):
            products.append(order.items[i])
    elevator.receive(products)
    #elevator.send({0: 8.7, 1: 5})
    window.populate_tree(elevator.bins)

    app.exec()  # Start the application
