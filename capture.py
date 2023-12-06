import pywinauto
import tkinter as tk
from tkinter import Listbox, messagebox
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import pythoncom
import time
import os
from pywinauto.application import Application



# 현재 스크립트의 절대 경로를 얻고, 그 경로에 스크린샷 폴더를 생성
# current_directory = os.path.dirname(os.path.abspath(__file__))
# screenshot_folder = os.path.join(current_directory, "screenshot")

# if not os.path.exists(screenshot_folder):
#     os.makedirs(screenshot_folder)

app = Application(backend="win32").connect(title="바람의나라")

calc_window = app.window(title="바람의나라")
# PyQt5 화면 캡처 클래스
class CaptureScreen(QtWidgets.QLabel):
    def __init__(self, screenshot_path):
        super().__init__()
        self.pixmap = QtGui.QPixmap(screenshot_path)
        self.initUI()

    def initUI(self):
        self.setPixmap(self.pixmap)
        self.setWindowOpacity(1.0)  # 투명도 설정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.showFullScreen()

        self.start_x, self.start_y, self.end_x, self.end_y = 0, 0, 0, 0
        self.is_mouse_pressed = False

    def mousePressEvent(self, event):
        self.start_x = event.x()
        self.start_y = event.y()
        self.is_mouse_pressed = True

    def mouseReleaseEvent(self, event):
        self.is_mouse_pressed = False
        self.takeScreenshot()
        self.close()

    def mouseMoveEvent(self, event):
        if self.is_mouse_pressed:
            self.end_x = event.x()
            self.end_y = event.y()
            self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.rect(), self.pixmap)  # 전체 화면에 이미지 그리기

        if self.is_mouse_pressed:
        # 드래그 영역 표시 로직
            pen = QtGui.QPen(QtGui.QColor(255, 0, 0), 2, QtCore.Qt.DashLine)
            painter.setPen(pen)
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawRect(QtCore.QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y))

    def takeScreenshot(self):
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)

        cropped_image = self.pixmap.copy(x1, y1, x2 - x1, y2 - y1)
        cropped_image.save("captured_area.png", "png")

# 연결된 프로그램의 화면 캡처 함수
def capture_connected_program(program_name):
    try:
        pythoncom.CoInitialize()
        app = pywinauto.Application().connect(title=program_name)
        main_window = app.window(title=program_name)
        rect = main_window.rectangle()
        screenshot_path = os.path.join(screenshot_folder, "temp_screenshot.png")
        screenshot = pyautogui.screenshot(region=(rect.left, rect.top, rect.width(), rect.height()))
        time.sleep(2)
        screenshot.save(screenshot_path)
        pythoncom.CoUninitialize()
        return screenshot_path
    except Exception as e:
        print("Error: ", e)
        return None

# PyQt5 캡처 기능 시작 함수
def start_pyqt_capture(screenshot_path):
    if screenshot_path:
        app = QtWidgets.QApplication(sys.argv)
        capture_screen = CaptureScreen(screenshot_path)
        app.exec_()


# Tkinter GUI 함수
def get_running_windows():
    desktop = pywinauto.Desktop(backend="uia")
    windows = desktop.windows()
    return [w.window_text() for w in windows if w.window_text()]

def on_button_click():
    windows_list = get_running_windows()
    listbox.delete(0, tk.END)
    for item in windows_list:
        listbox.insert(tk.END, item)

def on_listbox_select(event):
    selected_program = listbox.get(listbox.curselection())
    if not selected_program:
        messagebox.showwarning("경고", "프로그램이 선택되지 않았습니다.")
        return

    if capture_connected_program(selected_program):
        messagebox.showinfo("연결 상태", f"{selected_program}에 연결되었습니다.")
    else:
        messagebox.showerror("연결 오류", f"{selected_program}에 연결할 수 없습니다.")

# "캡쳐하기" 버튼의 클릭 이벤트를 처리하는 함수
def start_capture():
    selected_program = listbox.get(listbox.curselection())
    if selected_program:
        screenshot_path = capture_connected_program(selected_program)
        if screenshot_path:
            root.withdraw()
            start_pyqt_capture(screenshot_path)
            root.deiconify()
        else:
            messagebox.showerror("캡처 오류", "화면 캡처에 실패했습니다.")
    else:
        messagebox.showwarning("경고", "프로그램이 선택되지 않았습니다.")

# Tkinter GUI 인터페이스 설정
root = tk.Tk()

button = tk.Button(root, text="List Running Programs", command=on_button_click)
button.pack()

listbox = Listbox(root)
listbox.pack()
listbox.bind('<<ListboxSelect>>', on_listbox_select)

capture_button = tk.Button(root, text="캡쳐하기", command=start_capture)
capture_button.pack()

root.mainloop()