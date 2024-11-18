import cv2
import threading
from src.OCR import OCR
from src.qtwindow import MyApp
from PyQt5.QtWidgets import QApplication
import sys
from queue import Queue

    
def main_work(q):
    # 캡쳐장비 불러오기 현재 자신의 상황에 맞춘 번호로 사용
    font, engine = q.get()

    cap = cv2.VideoCapture(2)

    # 캡쳐장비 해상도 설정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    # 캡쳐장비가 열려있는 동안에만 실행
    while cap.isOpened():  
        # 프레임 받아오는 변수
        ret, frame = cap.read() 

        # OCR 실행 함수
        if q.empty() is False:
            font, engine = q.get()

        ocr_frame = OCR(frame, font, engine) 

        # ocr_frame으로 받아온 이미지 출력
        cv2.imshow('frame', ocr_frame) 

        # 1ms 기다리고 다음 프레임으로 전환, Esc 누르면 while 종료
        if cv2.waitKey(1) == 27:
            break


if __name__ == '__main__':
    data_queue = Queue()

    # 창 실행 쓰레딩
    # window_thread = threading.Thread(target=window_work, args=(app))
    # window_thread.start()
    app = QApplication(sys.argv)
    ex = MyApp(data_queue)

    main_thread = threading.Thread(target=main_work, args=(data_queue,))
    main_thread.start()

    # 사용한 자원 해제 및 열려있는 창 종료
    sys.exit(app.exec_()) 
    cv2.destroyAllWindows()

        