from PyQt5 import QtWidgets, uic
import sys
from cli_challenge.backend.order import Order

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('frontend.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
    def populate_table(self, orders: list[Order]):
        self.orderTable.setRowCount(len(orders))
        for i in range(len(orders)):
            self.orderTable.itemAt(i, 0).widget().setText(orders[i].num)
            self.orderTable.itemAt(i, 1).widget().setText(orders[i].state)
            self.orderTable.itemAt(i, 2).widget().setText(orders[i].date)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    app.exec()  # Start the application
