import tkinter as tk
from tkinter import simpledialog, messagebox
import pygetwindow as gw

# 창을 연결하는 함수
def connect_window(window_title):
    try:
        # 여기에 창을 연결하는 추가 작업을 수행할 수 있습니다.
        # 성공적으로 연결되었을 때
        messagebox.showinfo("연결 성공", f"{window_title}을(를) 연결했습니다.")
    except Exception as e:
        # 실패했을 때 실패 이유를 메시지로 표시
        messagebox.showerror("연결 실패", f"{window_title} 연결 실패: {str(e)}")

# 모든 창 목록 가져오기
window_list = gw.getAllTitles()

# tkinter 창 생성
root = tk.Tk()
root.title("프로그램 연결")

# 창 목록과 연결하기 버튼을 표시하는 프레임 생성
frame = tk.Frame(root)
frame.pack()

# 창 목록을 리스트 박스에 추가
listbox = tk.Listbox(frame)
for window_title in window_list:
    listbox.insert(tk.END, window_title)
listbox.pack(side=tk.LEFT)

# 연결하기 버튼 생성
connect_button = tk.Button(frame, text="연결하기", command=lambda: connect_window(listbox.get(tk.ACTIVE)))
connect_button.pack(side=tk.LEFT)

# tkinter 창 실행
root.mainloop()
