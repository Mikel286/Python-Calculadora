import sys
from PyQt6.QtWidgets import QApplication
from config.gui import Window

def main():
    
    app = QApplication(sys.argv)

    window = Window(position_x=100, position_y=100, width=400, height=300)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()