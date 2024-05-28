import cv2
from src.OCR_test import ocrtest

if __name__ == '__main__':
    print(cv2.getVersionString())
    ocrtest("./data/test_ocr2.png")