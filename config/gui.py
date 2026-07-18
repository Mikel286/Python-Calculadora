from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class Window(QWidget):

    def __init__(self, position_x, position_y, width, height):
        
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(position_x, position_y, width, height)

        self.start_gui()

    def show_result(self):
        self.display_label.setText(self.result)

    def _register_value(self, value):
            self.operation += value
            self.display_label.setText(self.operation)

    def _make_operation(self):
            self.result = f"{eval(self.operation)}"
            self.operation = self.result
            self.show_result()

    def create_button(self, text, value):

        button = QPushButton(text)
        button.value = value
        if value == "=":
            button.clicked.connect(lambda: self._make_operation())
        else:
            button.clicked.connect(lambda: self._register_value(button.value))
        return button

    def create_row(self, row):
        button_row = QHBoxLayout()
        for element in row:
            button = self.create_button(text = element, value = element)
            button_row.addWidget(button)
        return button_row

    def create_matrix(self):

        calculator = QVBoxLayout()
        elements = [["7", "8", "9", "/"],
                    ["4", "5", "6", "*"],
                    ["1", "2", "3", "-"],
                    ["0", ".", "=", "+"]]
        
        for row in elements:
            button_row = self.create_row(row)
            calculator.addLayout(button_row)
        return calculator
    
    def create_elements(self):
        
        self.mainbox = QVBoxLayout()

        self.calculator = self.create_matrix()
        self.display_label = QLabel("Welcome to Calculator :)")
        self.display_label.resize(100,50)

        self.mainbox.addLayout(self.calculator)
        self.mainbox.addWidget(self.display_label)
        self.setLayout(self.mainbox)
         

    def start_gui(self):

        self.operation = ""
        self.result = 0

        self.create_elements()
        self.show()
