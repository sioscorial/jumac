import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from pynput import keyboard
from pynput.keyboard import Controller, Key
import threading
import time

# 키보드 입력을 저장할 리스트
key_log = []

# 녹화 상태를 관리하는 변수
recording = False

# 반복 재생을 관리하는 변수
playing = False
play_thread = None

last_key_time = 0  # 마지막 키 입력 시간을 저장할 전역 변수

def on_press(key):
    global recording
    global last_key_time
    if recording:
        current_time = time.time()
        wait_time = current_time - last_key_time  # 대기 시간 계산
        last_key_time = current_time  # 마지막 키 입력 시간 갱신
        if hasattr(key, 'char') and key.char:
            key_log.append((key.char, wait_time))  # 문자 키의 경우
            print(f"Recorded key: {key.char}")
        else:
            key_log.append((key, wait_time))  # 특수 키의 경우 (예: Key.space)
            print(f"Recorded key: {key}")

def on_release(key):
    global recording
    if recording:
        if hasattr(key, 'char') and key.char:
            key_log.append((key.char, 0))  # 문자 키의 경우
        else:
            key_log.append((key, 0))  # 특수 키의 경우 (예: Key.space)

# 키보드 모니터링을 시작하는 함수
def start_monitoring():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 메인 윈도우 설정
        self.setWindowTitle("Keyboard Recorder")
        self.setGeometry(100, 100, 400, 200)

        # 로그 표시 레이블
        self.log_label = QLabel("", self)
        self.log_label.setGeometry(20, 150, 360, 30)  # 로그 표시 위치 및 크기 설정

        # 버튼 추가
        self.record_button = QPushButton("녹화 시작", self)
        self.record_button.clicked.connect(self.start_recording)
        self.record_button.move(20, 50)

        self.stop_record_button = QPushButton("녹화 종료", self)
        self.stop_record_button.clicked.connect(self.stop_recording)
        self.stop_record_button.move(150, 50)

        self.play_button = QPushButton("반복 시작", self)
        self.play_button.clicked.connect(self.start_playing)
        self.play_button.move(20, 100)

        self.stop_play_button = QPushButton("반복 종료", self)
        self.stop_play_button.clicked.connect(self.stop_playing)
        self.stop_play_button.move(150, 100)

    # 녹화 시작 함수
    def start_recording(self):
        global recording
        global last_key_time
        recording = True
        last_key_time = time.time()  # 녹화 시작 시간 초기화
        key_log.clear()  # 이전 녹화 내용을 지움
        self.log_label.setText("Recording started...")
        print("Recording started...")

    # 녹화 종료 함수
    def stop_recording(self):
        global recording
        recording = False
        self.log_label.setText("Recording stopped. Recorded keys: " + str(key_log))
        print("Recording stopped. Recorded keys:", key_log)

    # 반복 재생 시작 함수
    def start_playing(self):
        global playing
        if not key_log:
            print("No keys recorded.")
            return

        if playing:
            print("Already playing.")
            return

        playing = True

        def playback_thread():
            global playing
            keyboard_controller = Controller()  # 여기에서 keyboard_controller를 정의
            while playing:
                for key, wait_time in key_log:
                    if not playing:
                        break
                    time.sleep(wait_time)
                    if isinstance(key, str):
                        keyboard_controller.press(key)
                        keyboard_controller.release(key)
                    else:
                        keyboard_controller.press(key)
                        keyboard_controller.release(key)

        # 반복 재생 스레드 시작
        play_thread = threading.Thread(target=playback_thread, daemon=True)
        play_thread.start()

    # 반복 재생 종료 함수
    def stop_playing(self):
        global playing
        playing = False

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()

    # 별도의 스레드에서 키보드 모니터링 시작
    thread = threading.Thread(target=start_monitoring, daemon=True)
    thread.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
