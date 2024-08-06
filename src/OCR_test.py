import pytesseract
import cv2
from PIL import ImageFont, ImageDraw, Image
from easyocr import Reader
import time
import datetime
import numpy as np

from translator import translate


def ocrtest(path=None):
    image = None
    if path is not None:
        image = cv2.imread(path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    USERNAME = 'user'

    
    langs = ['en']
    reader = Reader(lang_list=langs, gpu=True)

    # 비디오 매 프레임 처리
    cap = cv2.VideoCapture(2)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    resize_width = 1920
    resize_height = 1080

    while True:  # 무한 루프
        start_time = time.time()
        ret, frame = cap.read()  # 두 개의 값을 반환하므로 두 변수 지정

        # frame = cv2.resize(frame, (resize_width, resize_height))

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        background = np.zeros(shape=(resize_height, resize_width, 3), dtype=np.uint8)

        background[:, :, 1] = 255

        if not ret:  # 새로운 프레임을 못받아 왔을 때 braek
            break

        results = reader.readtext(frame_gray, batch_size=8192)

        for result in results:
            start = (int(result[0][0][0]), int(result[0][0][1]))
            end = (int(result[0][2][0]), int(result[0][2][1]))
            back_color = (int(frame[start[1], start[0], 0]), int(frame[start[1], start[0], 1]), int(frame[start[1], start[0], 2]))

            cv2.rectangle(background, start, end, back_color, -1)

            # show_text = translate(result[1])
            show_text = result[1]

            fontpath = "fonts/gulim.ttc"
            font = ImageFont.truetype(fontpath, 20)
            img_pil = Image.fromarray(background)
            draw = ImageDraw.Draw(img_pil)
            _, _, text_width, text_height = font.getbbox(show_text)
            text_color = (255-back_color[0], 255-back_color[1], 255-back_color[2], 0)
            text_pos = start[0] + ((end[0] - start[0]) - text_width)/2, start[1] + ((end[1] - start[1]) - text_height)/2
            draw.text(text_pos, show_text, font=font, fill=text_color)

            background = np.array(img_pil)

        cv2.imshow('frame', background)

        print(str(datetime.timedelta(seconds=time.time() - start_time)))

        # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
        if cv2.waitKey(1) == 27:
            break

    cap.release()  # 사용한 자원 해제
    cv2.destroyAllWindows()


if __name__ == '__main__':
    ocrtest()
    # ocrtest("../data/test_ocr2.png")