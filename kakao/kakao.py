import time
import pyaudio
import numpy as np
import pyautogui
import pyperclip

# 오디오 스트림 설정
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024  # 한 번에 처리할 프레임의 수
SECONDS_PER_CHECK = 1  # 몇 초마다 체크할지

def send_auto_response(message):
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
    
    print("메시지를 성공적으로 전송했습니다.")

def callback(in_data, frame_count, time_info, status):
    global start_time
    if time.time() - start_time >= SECONDS_PER_CHECK:
        audio_data = np.frombuffer(in_data, dtype=np.int16)
        volume = np.sqrt(np.mean(audio_data**2))
        if volume > 80:  # 볼륨 임계값 설정
            print("Detected sound")
            send_auto_response("자동회신: 현재 주인이 자리에 없습니다. 나중에 주인장이 꼼꼼히 읽고 답해드리겠습니다!")
        start_time = time.time()
    return (in_data, pyaudio.paContinue)

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

start_time = time.time()  # 시작 시간 초기화

stream.start_stream()

try:
    while stream.is_active():
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()
