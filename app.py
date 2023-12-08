import sys
import psutil
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel, QVBoxLayout, QWidget

class ProcessController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Program Controller")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.program_list_label = QLabel("Select a program:")
        self.program_list = QComboBox()
        layout.addWidget(self.program_list_label)
        layout.addWidget(self.program_list)

        self.control_button = QPushButton("Control Selected Program")
        layout.addWidget(self.control_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.control_button.clicked.connect(self.control_selected_program)

        self.populate_program_list()

    def populate_program_list(self):
        program_set = set()
        for process in psutil.process_iter(attrs=['name']):
            program_name = process.info['name']
            program_set.add(program_name)

        self.program_list.addItems(sorted(program_set))

    def control_selected_program(self):
        selected_program = self.program_list.currentText()

        # Add your code to control the selected program here
        # You can use psutil or other libraries to interact with the program

def main():
    app = QApplication(sys.argv)
    window = ProcessController()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
