from pywinauto.application import Application
from pywinauto.keyboard import send_keys
import time
import tkinter as tk

# 애플리케이션 시작
app = Application(backend="win32").connect(title="바람의나라")

calc_window = app.window(title="바람의나라")

# Tkinter 애플리케이션 창 생성
root = tk.Tk()
root.title("바람의나라 제어")

def start_program():
    status_label.config(text="프로그램 시작...")
    print("프로그램 시작")

    # 클릭을 3번 반복
    for i in range(100):
        send_keys("{3}")
        log_text = f"F1 키 {i+1}번 누름"
        print(log_text)  # 콘솔에 로그 출력
        status_label.config(text=log_text)  # UI에 로그 표시
        time.sleep(1)  # 1초 대

# 종료 버튼을 눌렀을 때 실행할 함수
def stop_program():
    send_keys("{F5}")
    status_label.config(text="프로그램 종료됨")

# 시작 버튼
start_button = tk.Button(root, text="시작", command=start_program)
start_button.pack()

# 종료 버튼
stop_button = tk.Button(root, text="종료", command=stop_program)
stop_button.pack()

# 상태 표시 레이블
status_label = tk.Label(root, text="")
status_label.pack()

# Tkinter 애플리케이션 시작
root.mainloop()

try:
    # 키를 보내고 작업 수행
    calc_window.type_keys("3")
    time.sleep(1)
    time.sleep(1)
    
    # 결과 가져와서 출력
    result = calc_window.Static2.texts()[0]
    print("결과:", result)
    
    # 창 닫기
    calc_window.close()
    
finally:
    # 예외가 발생하더라도 애플리케이션 종료
    app.kill()
