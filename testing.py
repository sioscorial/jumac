import time
import threading
from pynput import keyboard
from pywinauto.application import Application
import pywinauto
import pyautogui
from pywinauto.keyboard import SendKeys

# 반복 실행을 제어하는 플래그
stop_thread = False

# 키 입력을 반복적으로 실행하는 함수
def type_keys_repeatedly():
    global stop_thread
    while not stop_thread:
        pyautogui.press('3')  # 3번 키를 누름
        time.sleep(1)

# 키보드 리스너에서 호출되는 콜백 함수
def on_press(key):
    global stop_thread
    if key == keyboard.Key.esc:
        stop_thread = True
        return False

# 윈도우에 연결
app = Application().connect(title='바람의나라')
window = app.window(title='바람의나라')

# 키 입력 반복을 위한 스레드 생성 및 시작
thread = threading.Thread(target=type_keys_repeatedly, args=(window,))
thread.start()

# 키보드 리스너 시작
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# 스레드가 종료될 때까지 대기
thread.join()
