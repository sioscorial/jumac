import sys
import time
import threading
from pynput.keyboard import Controller, Key, Listener

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from macro import Ui_Jumac  # 여기서 'macro'는 사용자의 UI 모듈 이름입니다.

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.ui = Ui_Jumac()
        self.ui.setupUi(self)

        self.setWindowTitle("JuMac")
        self.setGeometry(300, 300, 600, 400)

        # 이벤트 연결
        self.ui.pushButton.clicked.connect(self.start_recording)
        self.ui.pushButton_2.clicked.connect(self.stop_recording)
        self.ui.pushButton_3.clicked.connect(self.start_playing)
        self.ui.pushButton_4.clicked.connect(self.stop_playing)

        self.ui.retranslateUi(self)
        
        self.log_label = self.ui.log_label

        self.recording = False
        self.playing = False
        self.play_thread = None
        self.last_key_time = 0
        self.key_log = []

    def start_recording(self):
        self.recording = True
        self.last_key_time = time.time()
        self.key_log.clear()
        self.log_label.setText("Recording started...")
        print("Recording started...")

    def stop_recording(self):
        self.recording = False
        self.log_label.setText("Recording stopped. Recorded keys: " + str(self.key_log))
        print("Recording stopped. Recorded keys:", self.key_log)

    def start_playing(self):
        if not self.key_log:
            print("No keys recorded.")
            return

        if self.playing:
            print("Already playing.")
            return

        self.playing = True

        def playback_thread():
            keyboard_controller = Controller()
            while self.playing:
                for key, wait_time in self.key_log:
                    if not self.playing:
                        break
                    time.sleep(wait_time)
                    if isinstance(key, str):
                        keyboard_controller.press(key)
                        keyboard_controller.release(key)
                    else:
                        keyboard_controller.press(key)
                        keyboard_controller.release(key)

        self.play_thread = threading.Thread(target=playback_thread, daemon=True)
        self.play_thread.start()

    def stop_playing(self):
        self.playing = False

    def on_press(self, key):
        if self.recording:
            current_time = time.time()
            wait_time = current_time - self.last_key_time
            self.last_key_time = current_time
            if hasattr(key, 'char') and key.char:
                self.key_log.append((key.char, wait_time))
                print(f"Recorded key: {key.char}")
            else:
                self.key_log.append((key, wait_time))
                print(f"Recorded key: {key}")

    def start_monitoring(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    thread = threading.Thread(target=window.start_monitoring, daemon=True)
    thread.start()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
