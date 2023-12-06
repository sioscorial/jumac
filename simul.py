from pynput import keyboard
from pynput.keyboard import Key, Controller
import tkinter as tk
import threading
import time

# 키보드 입력을 저장할 리스트
key_log = []

# 녹화 상태를 관리하는 변수
recording = False

def on_press(key):
    if recording:
        if hasattr(key, 'char') and key.char:
            key_log.append(key.char)  # 문자 키의 경우
            print(f"Recorded key: {key.char}")
        else:
            key_log.append(key)  # 특수 키의 경우 (예: Key.space)
            print(f"Recorded key: {key}")

def simulate_keys():
    keyboard_controller = Controller()
    for key in key_log:
        if isinstance(key, str):
            keyboard_controller.press(key)
            keyboard_controller.release(key)
        else:
            keyboard_controller.press(key)
            keyboard_controller.release(key)


# 키보드 모니터링을 시작하는 함수
def start_monitoring():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# 녹화 시작 버튼 클릭 이벤트
def start_recording():
    global recording
    recording = True
    key_log.clear()  # 이전 녹화 내용을 지움
    status_label.config(text="Recording started...")
    print("Recording started...")

def stop_recording():
    global recording
    recording = False
    print("Recording stopped. Recorded keys:", key_log)

# 반복 재생을 관리하는 변수와 반복 재생 스레드를 관리하기 위한 변수
playing = False
play_thread = None
thread = None  # 키보드 모니터링 스레드를 위한 변수 추가

def start_playing():
    global playing
    global play_thread

    if not key_log:
        print("No keys recorded.")
        return

    if playing:
        print("Already playing.")
        return

    playing = True

    def playback_thread():
        keyboard_controller = Controller()
        while playing:
            for key in key_log:
                if not playing:  # playing 변수가 False이면 반복 종료
                    return
                if isinstance(key, str):
                    keyboard_controller.press(key)
                    time.sleep(0.1)  # 0.1초 대기
                    keyboard_controller.release(key)
                else:
                    keyboard_controller.press(key)
                    time.sleep(0.1)  # 0.1초 대기
                    keyboard_controller.release(key)
                time.sleep(0.1)  # 다음 키 입력을 위해 0.1초 대기

    # 반복 재생 스레드 시작
    play_thread = threading.Thread(target=playback_thread, daemon=True)
    play_thread.start()

def stop_playing():
    global playing, play_thread
    playing = False
    if play_thread:
        play_thread.join()  # 반복 재생 스레드 종료 대기
    play_thread = None
    play_button.config(state=tk.NORMAL)  # 반복 재생이 종료되면 버튼을 다시 활성화



# 종료 버튼 클릭 이벤트
def exit_app():
    global playing
    playing = False
    stop_playing()  # 반복 재생 스레드 종료

# Tkinter GUI 설정
root = tk.Tk()
root.title("Keyboard Recorder")

# Tkinter 인터페이스에 상태 표시 레이블 추가
status_label = tk.Label(root, text="Ready")
status_label.pack()

record_button = tk.Button(root, text="녹화 시작", command=start_recording)
record_button.pack()

stop_record_button = tk.Button(root, text="녹화 종료", command=stop_recording)
stop_record_button.pack()

play_button = tk.Button(root, text="반복 시작", command=start_playing)
play_button.pack()

exit_button = tk.Button(root, text="종료", command=exit_app)
exit_button.pack()

# 별도의 스레드에서 키보드 모니터링 시작
thread = threading.Thread(target=start_monitoring, daemon=True)
thread.start()

root.mainloop()
