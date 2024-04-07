from PyQt6 import QtWidgets, uic
import sys

from PyQt6.QtWidgets import QTreeWidgetItem
from PyQt6.QtWidgets import QTableWidgetItem, QPushButton

from cli_challenge.backend.bin import Bin
from cli_challenge.backend.database import Database
from cli_challenge.backend.order import Order
from cli_challenge.backend.elevator import Elevator
from cli_challenge.backend.product import Product
from cli_challenge.backend.rail_system import RailSystem


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('frontend.ui', self)  # Load the .ui file
        self.show()  # Show the GUI

    def construct_button(self, order, window, status_widget):
        button = QPushButton("Advance order")
        def click_function():
            order.advance_state(window)
            status_widget.setText(order.status_str())
            if order.state == Order.DELIVERED:
                self.total_profit.setText(f"Your Total Profit Is: ${Order.TOTAL_PROFIT:.2f}")
            if order.state == Order.ON_RAIL_CAR:
                window.elevator.send(order.map_product_id_to_weight())
                window.update_tree(window.elevator.bins)

        button.clicked.connect(click_function)
        return button

    def populate_table(self, orders: list[Order], window: QtWidgets.QMainWindow):
        self.order_table.setRowCount(len(orders))
        for i, order in enumerate(orders):

            strs = [orders[i].id, orders[i].status_str(), orders[i].date, f"${orders[i].cost:.2f}",
                    f"${orders[i].revenue:.2f}", f"${orders[i].revenue - orders[i].cost:.2f}"]
            widgets = [*map(lambda i: QTableWidgetItem(str(i)), strs)]
            for j, p in enumerate(widgets, 1):
                self.order_table.setItem(i, j, p)
            self.order_table.setIndexWidget(self.order_table.model().index(i, 0),
                                            self.construct_button(order, window, widgets[1]))

        self.total_profit.setText(f"Your Total Profit Is: ${Order.TOTAL_PROFIT:.2f}")

    def populate_tree(self, bins: list[Bin]):
        self.bin_widgets = []
        for i in range(len(bins)):
            weight = bins[i].weight
            if abs(weight) < 1e-6:
                weight = 0
            parent = QTreeWidgetItem(["Bin " + str(i + 1), "0" if weight == 0 else f"{weight:.4f} MT"])
            self.bins.addTopLevelItem(parent)
            self.bin_widgets.append(parent)
            for item in bins[i].items:
                weight = bins[i].items[item]
                parent.addChild(QTreeWidgetItem([Product.product_name(item), "0" if weight == 0 else f"{weight:.4f} MT"]))

    def update_tree(self, bins: list[Bin]):
        for i in range(15):
            self.bins.takeTopLevelItem(1)
        self.populate_tree(bins)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Create an instance of QtWidgets.QApplication
    window = Ui()  # Create an instance of our class
    elevator = window.elevator = Elevator()
    railSystem = window.rail_system = RailSystem()
    orders = Database.load_database()
    window.populate_table(orders, window)

    products = []
    for order in filter(lambda o: o.state == Order.IN_BIN, orders):
        for i in range(len(order.items)):
            products.append(order.items[i])
    elevator.receive(products)
    window.populate_tree(elevator.bins)

    app.exec()  # Start the application
