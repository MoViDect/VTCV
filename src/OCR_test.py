import pytesseract
import cv2

from src.translator import translate


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
    pytesseract.pytesseract.tesseract_cmd = f"C:/Program Files/Tesseract-OCR/tesseract.exe"
    # pytesseract.pytesseract.tesseract_cmd = f'C:/Users/{USERNAME}/AppData/Local/tesseract.exe' # for Windows
    # pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.4_1/bin/tesseract' # for mac

    # 비디오 매 프레임 처리
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:  # 무한 루프
        ret, frame = cap.read()  # 두 개의 값을 반환하므로 두 변수 지정

        if not ret:  # 새로운 프레임을 못받아 왔을 때 braek
            break

        # 정지화면에서 윤곽선을 추출
        # edge = cv2.Canny(frame, 50, 150)
        #
        # inversed = ~frame  # 반전

        # cv2.imshow('inversed', inversed)
        # cv2.imshow('edge', edge)

        text = pytesseract.image_to_string(frame, lang='eng', config='--psm 4')
        kor_text = translate(text)
        img = cv2.putText(frame, kor_text, (350, 40), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 1)

        cv2.imshow('frame', img)

        # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
        if cv2.waitKey(10) == 27:
            break

    cap.release()  # 사용한 자원 해제
    cv2.destroyAllWindows()


if __name__ == '__main__':
    ocrtest()
    # ocrtest("../data/test_ocr2.png")