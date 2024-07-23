# VTCV
Computer Vision, OCR, etc...

Installation [for Windows]
    1. tesseract
        1-1. Download Link : https://digi.bib.uni-mannheim.de/tesseract/
        1-2. "tesseract-ocr-w64-setup-5.4.0.20240606.exe" 으로 다운로드
        1-3. "Install for anyone using this Computer"로 체크 (유저 파라미터를 설정 안하기 위함) 
        1-4. Additional language data (download) 를 + 버튼으로 펼쳐서 Japanese, Korean 체크
        1-5. 경로 확인 : C:\Program Files\Tesseract-OCR
        1-6. 설치 진행 및 완료

    2. python requirements
        해당 repository에 있는 requirements.txt 설치
            numpy==2.0.0
            opencv-python==4.10.0.84
            packaging==24.1
            pillow==10.4.0
            pytesseract==0.3.10

    3. test code 실행
        OCR_test.py를 실행하여 캡쳐 디바이스 혹은 웹캠 화면이 나오는지 확인