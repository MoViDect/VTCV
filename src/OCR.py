import cv2
from PIL import ImageFont, ImageDraw, Image
from easyocr import Reader
import numpy as np

# 번역 부분 Import
from src.translator import translate

# OCR에서 읽을 언어 설정 및 EasyOCR Reader 객체 생성
langs = ['en']
reader = Reader(lang_list=langs, gpu=True) # GPU가 없을 경우 gpu=False로 지정

# OCR 진행 함수
def OCR(frame):
    # 흑백 이미지로 변환 (OCR 처리 속도 향상을 위해서)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # OCR한 글자를 해당 위치에 표시하기 위한 백그라운드 화면 생성
    background = np.zeros(shape=(frame.shape[0], frame.shape[1], 3), dtype=np.uint8)

    # 크로마키 적용을 위한 배경화면 초록색으로 설정
    background[:, :, 1] = 255

    # OCR 진행
    results = reader.readtext(frame_gray, batch_size=8192) # 메모리가 부족할 경우 batch_size 조절

    # OCR 진행 결과를 화면에 표시
    for result in results:
        box_start = (int(result[0][0][0]), int(result[0][0][1])) # 기존의 텍스트가 시작하는 좌표
        box_end = (int(result[0][2][0]), int(result[0][2][1])) # 기존의 텍스트가 끝나는 좌표
        box_back_color = (int(frame[box_start[1], box_start[0], 0]), int(frame[box_start[1], box_start[0], 1]), int(frame[box_start[1], box_start[0], 2])) # 기존의 텍스트가 위치한 배경 색상 추출

        # 백그라운드에서 기존 텍스트 영역을 기존의 색상으로 덮어씌우는 코드
        cv2.rectangle(background, box_start, box_end, box_back_color, -1)

        # 표시할 언어를 번역하는 구간
        show_text = translate(result[1])
        # show_text = result[1]

        fontpath = "The Jamsil OTF 3 Regular.otf" # 폰트 설정
        # font = ImageFont.truetype(fontpath, 20) # 폰트 객체 생성 및 글자 크기 지정
        font = ImageFont.truetype(fontpath, int(result[0][2][1]) - int(result[0][0][1])) # 폰트 객체 생성 및 글자 크기 지정
        img_pil = Image.fromarray(background) # Pillow 이미지로 합성하기 위해 백그라운드 이미지를 Image 객체로 변환
        draw = ImageDraw.Draw(img_pil) # 이미지에 글자를 넣기위한 draw 객체 생성
        _, _, text_width, text_height = font.getbbox(show_text) # 글자의 길이 및 높이를 구하는 함수 (앞의 두 변수는 무시)
        text_color = (255-box_back_color[0], 255-box_back_color[1], 255-box_back_color[2], 0) # 글자 색상 지정 (기존의 박스와 대비되는 색상을 위해서 255에서 박스의 색상을 빼줌)
        text_pos = box_start[0] + ((box_end[0] - box_start[0]) - text_width)/2, box_start[1] + ((box_end[1] - box_start[1]) - text_height)/2 # 텍스트가 기존의 덮어씌운 박스의 중앙에 표시하도록 위치 지정
        draw.text(text_pos, show_text, font=font, fill=text_color) # 이미지에 텍스트 생성

        background = np.array(img_pil) # OpenCV로 출력하기 위해 numpy array로 변환

    #이미지를 다 생성하면 최종 background를 반환한다.
    return background