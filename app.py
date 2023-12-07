from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtUiTools import QUiLoader
from macro import Ui_Jumac

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        # UI 설정
        self.ui = Ui_Jumac()
        self.ui.setupUi(self)

        # 윈도우 설정
        self.setWindowTitle("JuMac")
        self.setGeometry(300, 300, 600, 400)

        # 버튼 클릭 이벤트 연결
        self.ui.pushButton.clicked.connect(self.start_recording)  # 버튼 1에 녹화 시작 연결
        self.ui.pushButton_2.clicked.connect(self.stop_recording)  # 버튼 2에 녹화 종료 연결
        self.ui.pushButton_3.clicked.connect(self.start_playing)  # 버튼 3에 반복 시작 연결
        self.ui.pushButton_4.clicked.connect(self.stop_playing)  # 버튼 4에 반복 종료 연결


    # 버튼 클릭 이벤트 처리 메서드
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
    app.exec()  # 'exec_' 대신 'exec' 사용

if __name__ == "__main__":
    main()