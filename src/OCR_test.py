import pytesseract
import cv2
from easyocr import Reader
import time
import datetime

def translate(text):
    kor_text = text
    return kor_text



def ocrtest(path=None):
    image = None
    if path is not None:
        image = cv2.imread(path)
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    USERNAME = 'user'

    # cv2.imshow('image', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # use Tesseract to OCR the image
    # pytesseract.pytesseract.tesseract_cmd = f"C:/Program Files/Tesseract-OCR/tesseract.exe" # for Windows
    # pytesseract.pytesseract.tesseract_cmd = f'C:/Users/{USERNAME}/AppData/Local/tesseract.exe' # for Windows
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.4_1/bin/tesseract' # for mac

    # 비디오 매 프레임 처리
    cap = cv2.VideoCapture(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:  # 무한 루프
        start_time = time.time()
        ret, frame = cap.read()  # 두 개의 값을 반환하므로 두 변수 지정

        if not ret:  # 새로운 프레임을 못받아 왔을 때 braek
            break

        # 정지화면에서 윤곽선을 추출
        # edge = cv2.Canny(frame, 50, 150)
        #
        # inversed = ~frame  # 반전

        # cv2.imshow('inversed', inversed)
        # cv2.imshow('edge', edge)

        langs = ['en']

        print("[INFO] OCR'ing input image...")
        reader = Reader(lang_list=langs, gpu=True)
        results = reader.readtext(frame)

        for result in results:
            # print(f'{result[0][0]} {result[0][1]}')
            cv2.rectangle(frame, (int(result[0][0][0]), int(result[0][0][1])), (int(result[0][2][0]), int(result[0][2][1])), (255, 0, 0), -1)
            cv2.putText(frame, result[1], (int(result[0][0][0]), int(result[0][2][1])), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
            # print(result)


        # texts = pytesseract.image_to_boxes(frame, lang='eng', config='--psm 6 --oem 1')
        # texts = texts.split('\n')
        # texts = list(filter(None, texts))

        # for word in texts:
        #     data = word.split(' ')
        #     if int(data[3]) - int(data[1]) < 150 and int(data[4]) - int(data[2]) < 150:
        #         cv2.rectangle(frame, (int(data[1]), 1080 - int(data[2])), (int(data[3]), 1080 - int(data[4])), (255, 0, 0), -1)
        #         cv2.putText(frame, data[0], (int(data[1]), 1080 - int(data[2])), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)
        # kor_text = translate(text)
        # img = cv2.putText(frame, kor_text, (350, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)

        cv2.imshow('frame', frame)

        print(str(datetime.timedelta(seconds=time.time() - start_time)))

        # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
        if cv2.waitKey(10) == 27:
            break

    cap.release()  # 사용한 자원 해제
    cv2.destroyAllWindows()


if __name__ == '__main__':
    ocrtest()
    # ocrtest("../data/test_ocr2.png")