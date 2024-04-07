from PyQt5 import QtWidgets, uic
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidgetItem

from cli_challenge.backend.order import Order


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('frontend.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
    def populate_table(self, orders: list[Order]):
        orders.append(Order({0: 50},"Jan 2", 1))
        self.order_table.setRowCount(len(orders))
        for i in range(len(orders)):

            item1 = QTableWidgetItem(str(orders[i].num))
            item2 = QTableWidgetItem(str(orders[i].state))
            item3 = QTableWidgetItem(str(orders[i].date))
            self.order_table.setItem(i, 0, item1)
            self.order_table.setItem(i, 1, item2)
            self.order_table.setItem(i, 2, item3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    window.populate_table([])
    app.exec()  # Start the application
