import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QComboBox, QPushButton


class MyApp(QWidget):

    def __init__(self, data_queue):
        super().__init__()
        self.initUI()

        self.data_queue = data_queue
        self.vtct_font = "NanumGothic.ttf"
        self.vtct_engine = "Google"

        self.vtct_activate()

    def initUI(self):
        # 위젯 생성
        lbl1 = QLabel('Font', self)
        lbl2 = QLabel('Engine', self)

        cb1 = QComboBox(self)
        cb1.setObjectName("cb_Font")
        cb1.addItem('NanumGothic')
        cb1.addItem('BaeminHanna')
        cb1.addItem('DungGeunMo')
        cb1.addItem('HanSCalli')
        cb1.resize(160, 30)

        cb2 = QComboBox(self)
        cb2.setObjectName("cb_Engine")
        cb2.addItem('Google')
        cb2.addItem('Papago')
        cb2.resize(160, 30)

        pb1 = QPushButton(self)
        pb1.setText("Apply")
        pb1.resize(160, 30)

        # 위젯 위치 설정
        lbl1.move(20, 25)
        lbl2.move(20, 90)
        cb1.move(20, 50)
        cb2.move(20, 115)
        pb1.move(20, 180)

        # 위젯 Event 연결
        cb1.activated[str].connect(self.onComboBoxChanged)
        cb2.activated[str].connect(self.onComboBoxChanged)
        pb1.clicked.connect(self.onApplyClicked)

        # 윈도우 설정
        self.setWindowTitle('VTCT')
        self.setGeometry(500, 1200, 200, 250)
        self.show()

    def vtct_activate(self):
        # print("Font:", self.vtct_font)
        # print("Engine:", self.vtct_engine)
        '''
        TODO: vtct_activate 구현하기~ 폰트랑 엔진은 정해드렸으니         
        '''
        self.data_queue.put((self.vtct_font, self.vtct_engine))

    def onComboBoxChanged(self, text):
        object_name = self.sender().objectName()

        if object_name == "cb_Font":
            self.vtct_font = text + ".ttf"
        elif object_name == "cb_Engine":
            self.vtct_engine = text
        else:
            print("Error")
            return -1

        self.vtct_activate()

    def onApplyClicked(self):
        self.vtct_activate()

    def closeEvent(self, event):
        message = QMessageBox.question(self, "Question", "Are you sure you want to quit?")
        if message == QMessageBox.Yes:
            event.accept()
            sys.exit(app.exec_())
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())


