from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

class Window(QWidget):

    def __init__(self, position_x, position_y, width, height):
        
        super().__init__()
        self.setWindowTitle("Cross Calculator")
        self.setGeometry(position_x, position_y, width, height)

        self.start_gui()

    def show_result(self):
        self.display_label.setText(self._result)

    def _register_value(self, value):
            self._operation += value
            self.display_label.setText(self._operation)

    def _make_operation(self):
        try:
            self._result = f"{eval(self._operation)}"
            self._operation = self._result
            self.show_result()
        except SyntaxError:
            self.display_label.setText("Operación invalida...")
            self._operation = ""
            self._result = ""

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
    
    def create_label(self):
        display_label = QLabel("Welcome to Calculator :)")
        return display_label
    
    def create_elements(self):
        
        self.mainbox = QVBoxLayout()

        self.calculator = self.create_matrix()
        self.display_label = self.create_label()

        self.mainbox.addWidget(self.display_label)
        self.mainbox.addLayout(self.calculator)
        self.setLayout(self.mainbox)
         

    def start_gui(self):

        self._operation = ""
        self._result = 0

        self.create_elements()
        self.show()
