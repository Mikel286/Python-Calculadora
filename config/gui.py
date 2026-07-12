from PyQt6.QtWidgets import QWidget

class Window(QWidget):

    def __init__(self, position_x, position_y, width, height):
        
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(position_x, position_y, width, height)

        self.start_gui()

    def start_gui(self):

        self.show()
