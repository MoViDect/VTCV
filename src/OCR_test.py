import pytesseract
import cv2
import matplotlib.pyplot as plt

path = '../data/test_ocr2.png'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# use Tesseract to OCR the image
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ejsfl\AppData\Local\tesseract.exe'


# 비디오 매 프레임 처리
cap = cv2.VideoCapture(0)

while True:  # 무한 루프
    ret, frame = cap.read()  # 두 개의 값을 반환하므로 두 변수 지정

    if not ret:  # 새로운 프레임을 못받아 왔을 때 braek
        break

    # 정지화면에서 윤곽선을 추출
    # edge = cv2.Canny(frame, 50, 150)
    #
    # inversed = ~frame  # 반전

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    # cv2.imshow('edge', edge)

    text = pytesseract.image_to_string(frame, lang='kor+eng+jap', config='--psm 5')
    print(text)

    # 10ms 기다리고 다음 프레임으로 전환, Esc누르면 while 강제 종료
    if cv2.waitKey(10) == 27:
        break

cap.release()  # 사용한 자원 해제
cv2.destroyAllWindows()

