from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtUiTools import QUiLoader
from ui_code import Ui_Ju

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        try:
            loader = QUiLoader()
            self.ui = Ui_Ju()
            self.ui.setupUi(self)
        except Exception as e:
            print(f"Error loading UI: {e}")

        self.setCentralWidget(self.ui)
        self.setWindowTitle("My Window")
        self.setGeometry(100, 100, 400, 200)

        self.ui.pushButton_4.clicked.connect(self.button4_clicked)
        self.ui.pushButton_3.clicked.connect(self.button3_clicked)
        self.ui.pushButton_2.clicked.connect(self.button2_clicked)
        self.ui.pushButton.clicked.connect(self.button_clicked)
        self.ui.pushButton_5.clicked.connect(self.button5_clicked)

    def button4_clicked(self):
        print("버튼 4를 클릭했습니다.")

    def button3_clicked(self):
        print("버튼 3을 클릭했습니다.")

    def button2_clicked(self):
        print("버튼 2를 클릭했습니다.")

    def button_clicked(self):
        print("버튼 1을 클릭했습니다.")

    def button5_clicked(self):
        print("버튼 5를 클릭했습니다.")

def main():
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
