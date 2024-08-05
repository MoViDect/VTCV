# VTCV
Computer Vision, OCR, etc...

## Installation [for Windows]

### 1. CUDA 12.1 (Nvidia GPU가 있는 경우에)

1. Download Link : https://developer.nvidia.com/cuda-12-1-0-download-archive
2. Windows -> x86_64 -> 해당하는 버전 선택 -> exe(local) -> Download (3.1GB) 순서대로 클릭 후 다운로드 진행
3. 다운로드 완료 후 설치 파일(cuda_12.1.0_531.14_windows.exe) 실행
4. OK를 눌러 압축풀기 진행
5. "NVIDIA 소프트웨어 라이센스 계약" 동의 및 계속 클릭
6. "사용자 정의 설치" 선택 후 다음 클릭
7. "사용자 정의 설치 옵션" 에서 CUDA만 체크 후 나머지는 체크 해제하여 다음 클릭
8. 설치 경로 확인 하고 다음 클릭 (특별히 경로를 설정하는건 없음)
9. "CUDA Visual Studio Integration" 에서 "I understand, and wish to continue the installation regardless" 체크 후 NEXT 클릭
10. 설치 진행 및 완료

### 2. python requirements

해당 repository에 있는 requirements.txt 설치

```bash
pip install -r requirements.txt
```

NVIDIA GPU를 사용하는 경우 아래의 requirements_gpu.txt 설치
```bash
pip install -r requirements_gpu.txt
```

Packages

- numpy==2.0.0
- opencv-python==4.10.0.84
- packaging==24.1
- pillow==10.4.0
- googletrans==3.1.0a0
- easyocr==1.7.1
- torch==2.4.0
- torchvision==0.19.0
- torchaudio==2.4.0

### 3. code 실행

- main.py 코드 내에서 cap = cv2.VideoCapture(0)의 숫자를 변경하여 사용하려는 캡쳐장비로 변경
- 한대의 기기만 연결되어 있다면 0으로 설정
- main.py를 실행하여 캡쳐 디바이스 혹은 웹캠 화면이 나오는지 확인