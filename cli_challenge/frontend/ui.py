from PyQt6 import QtWidgets, uic
import sys

from PyQt6.QtWidgets import QTableWidgetItem

from cli_challenge.backend.bin import Bin
from cli_challenge.backend.database import Database
from cli_challenge.backend.order import Order


class Ui(QtWidgets.QMainWindow):

    TREE_DISPLAY_COLUMNS = 2

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('frontend.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

    def populate_table(self, orders: list[Order]):
        self.order_table.setRowCount(len(orders))
        for i in range(len(orders)):
            item0 = QTableWidgetItem(str(orders[i].id))
            item1 = QTableWidgetItem(str(orders[i].status_str()))
            item2 = QTableWidgetItem(str(orders[i].date))
            item3 = QTableWidgetItem(str(orders[i].cost))
            item4 = QTableWidgetItem(str(orders[i].revenue))
            item5 = QTableWidgetItem(str(orders[i].revenue - orders[i].cost))
            self.order_table.setItem(i, 0, item0)
            self.order_table.setItem(i, 1, item1)
            self.order_table.setItem(i, 2, item2)
            self.order_table.setItem(i, 3, item3)
            self.order_table.setItem(i, 4, item4)
            self.order_table.setItem(i, 5, item5)
        self.total_profit.setText(f"Total Profit: ${Order.TOTAL_PROFIT:.2f}")

    def populate_tree(self, bins: list[Bin]):
        self.bins.setColumnCount(Ui.TREE_DISPLAY_COLUMNS)
        for i in range(len(bins)):
            pass



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    window.populate_table(Database.load_database())
    app.exec()  # Start the application
