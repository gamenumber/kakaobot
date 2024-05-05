import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtCore import Qt
import time
import pyautogui
import cv2
import numpy as np
import pyperclip
from datetime import datetime

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("상태 선택")

        layout = QVBoxLayout()

        self.status_dropdown = QComboBox()
        self.status_dropdown.addItems(status_messages.keys())
        layout.addWidget(self.status_dropdown)

        self.start_button = QPushButton("프로그램 시작")
        self.start_button.clicked.connect(self.start_program)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_program(self):
        selected_status = self.status_dropdown.currentText()
        response_message = status_messages[selected_status]
        print("Selected status:", selected_status)
        print("Response message:", response_message)
        # 감지 및 응답 기능 추가하기
        while True:
            find_and_respond("notification_banner.png", response_message)
            time.sleep(6)  # 다음 확인까지 대기

def send_auto_response(message):
    kakao_icon_position = (550, 900)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.
    pyautogui.moveTo(kakao_icon_position, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    first_chat_position = (600, 220)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.
    pyautogui.moveTo(first_chat_position, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    left_scroll_position = (300, 600)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.
    pyautogui.moveTo(left_scroll_position, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    left_bottom_scroll_position = (300, 750)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.
    pyautogui.moveTo(left_bottom_scroll_position, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    pyperclip.copy(message)
    pyautogui.hotkey('command', 'v')
    pyautogui.sleep(0.1)
    pyautogui.press('return')

    toptop_bottom_scroll_position = (180, 200)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.
    pyautogui.moveTo(toptop_bottom_scroll_position, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.1)

    print("메시지를 성공적으로 전송했습니다.")

def generate_notification_id(notification_image):
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    combined_info = f"{hash(notification_image.tobytes())}_{current_time}"
    return hash(combined_info)

processed_notifications = set()

def find_and_respond(target_image, response_message):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    target = cv2.imread(target_image)
    result = cv2.matchTemplate(screenshot, target, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    if max_val > 0.4:
        notification_id = generate_notification_id(target)
        if notification_id not in processed_notifications:
            print("새로운 알림 감지!")
            send_auto_response(response_message)
            processed_notifications.add(notification_id)
        else:
            print("이미 처리된 알림입니다.")
    else:
        print("알림 감지되지 않음.")

# 사용자 상태에 따른 자동 회신 메시지
status_messages = {
    "샤워중": "(자동회신)현재 주인장이 샤워중입니다. 나중에 꼼꼼하게 읽고 꼭 답변 드리겠습니다 (@_@)",
    "테스트중": "(자동회신)프로그램 테스트 중입니다 (@_@)",
    "외출중": "(자동회신)현재 주인장이 외출중입니다. 나중에 꼼꼼하게 읽고 꼭 답변 드리겠습니다 (@_@)",
    "식사중": "(자동회신)현재 주인장이 식사중입니다. 나중에 꼼꼼하게 읽고 꼭 답변 드리겠습니다 (@_@)",
    "자는중": "(자동회신)현재 주인장이 자고 있습니다. 나중에 꼼꼼하게 읽고 꼭 답변 드리겠습니다 (@_@)",
    "핸드폰을 못 받음": "(자동회신)현재 주인장이 학교에서 핸드폰을 돌려받지 못했습니다. 나중에 꼼꼼하게 읽고 꼭 답변 드리겠습니다 (@_@)"
}

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
