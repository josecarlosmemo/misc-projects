from PyQt5.QtWidgets import *
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()



    def loadUI(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()

    sys.exit(app.exec_())

