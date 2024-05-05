import pyautogui
import pyperclip

def send_auto_response(message):
    # 카카오톡 아이콘이 위치한 좌표를 지정합니다.
    kakao_icon_position = (550, 900)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.

    # 카카오톡 아이콘으로 마우스를 이동시킵니다.
    pyautogui.moveTo(kakao_icon_position, duration=0.1)  # 마우스 이동 속도를 높입니다.

    # 마우스를 클릭합니다.
    pyautogui.click()

    # 대화창이 열릴 때까지 잠시 대기합니다.
    pyautogui.sleep(0.1)

    # 대화목록에서 첫 번째 대화를 선택합니다.
    first_chat_position = (600, 220)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.

    # 대화목록으로 마우스를 이동시킵니다.
    pyautogui.moveTo(first_chat_position, duration=0.1)

    # 대화를 선택합니다.
    pyautogui.click()

    # 대화창이 열릴 때까지 잠시 대기합니다.
    pyautogui.sleep(0.1)

    # 좌측으로 스크롤합니다.
    left_scroll_position = (300, 600)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.

    # 스크롤 버튼으로 마우스를 이동시킵니다.
    pyautogui.moveTo(left_scroll_position, duration=0.1)

    # 스크롤합니다.
    pyautogui.click()

    # 대화창이 열릴 때까지 잠시 대기합니다.
    pyautogui.sleep(0.1)

    # 좌측으로 스크롤합니다.
    left_bottom_scroll_position = (300, 750)  # 이 좌표는 예시입니다. 실제 좌표로 수정하세요.

    # 스크롤 버튼으로 마우스를 이동시킵니다.
    pyautogui.moveTo(left_bottom_scroll_position, duration=0.1)

    # 스크롤합니다.
    pyautogui.click()

    # 대화창이 열릴 때까지 잠시 대기합니다.
    pyautogui.sleep(0.1)

    # 메시지를 클립보드에 복사합니다.
    pyperclip.copy(message)

    # 클립보드의 내용을 붙여넣기합니다.
    pyautogui.hotkey('command', 'v')
    pyautogui.sleep(0.1)  # 붙여넣기가 완료될 때까지 잠시 대기합니다.

    # 전송 버튼을 클릭하여 메시지를 전송합니다.
    pyautogui.press('return')

# 메시지를 보낼 내용을 정의합니다.
message = "(자동회신) 주인이 자리에 없습니다."

# 메시지를 보냅니다.
send_auto_response(message)
