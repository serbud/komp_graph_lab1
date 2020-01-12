import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
imageroute = "temp.jpg"
imageroute2 = "temp5.jpg"
def RGBtoHSL(R,G,B):
    R = R/255
    G = G/255
    B = B/255
    Cmax = max(R,G,B)
    Cmin = min(R,G,B)
    delta = Cmax-Cmin
    L = (Cmin+Cmax)/2
    if delta == 0:
        H = 0
        S = 0
    else:
        S = delta / (1-abs(2*L-1))
        if R == Cmax:
            H = 60*(((G-B)/delta)%6)
        elif G == Cmax:
            H = 60*(((B-R)/delta)+2)
        else:
            H = 60*(((R-G)/delta)+4)
    return H, S, L
def RGBtoHSV(R,G,B):
    R = R/255
    G = G/255
    B = B/255
    Cmax = max(R,G,B)
    Cmin = min(R,G,B)
    delta = Cmax - Cmin
    V = Cmax
    if delta == 0:
        H = 0
        S = 0
    else:
        S = delta / V
        if R == Cmax:
            H = 60*(((G-B)/delta)%6)
        elif G == Cmax:
            H = 60*(((B-R)/delta)+2)
        else:
            H = 60*(((R-G)/delta)+4)
    return H, S, V
def HSLtoRGB(H,S,L):
    C = (1-abs(2*L-1))*S
    X = C * (1-abs((H/60)%2 -1))
    m = L - C/2
    R = 0
    G = 0
    B = 0
    if (H >= 0 and H < 60):
        R = C
        G = X
        B = 0
    elif (H >= 60 and H < 120):
        R = X
        G = C
        B = 0
    elif (H >= 120 and H < 180):
        R = 0
        G = C
        B = X
    elif (H >= 180 and H < 240):
        R = 0
        G = X
        B = C
    elif (H >= 240 and H < 300):
        R = X
        G = 0
        B = C
    elif (H >= 300 and H < 360):
        R = C
        G = 0
        B = X

    R = (R + m) * 255
    G = (G + m) * 255
    B = (B + m) * 255

    return R,G,B
def HSVtoRGB(H,S,V):
    C = V*S
    X = C * (1-abs((H/60)%2 -1))
    m = V - C
    R = 0
    G = 0
    B = 0
    if (H >= 0 and H < 60):
        R = C
        G = X
        B = 0
    elif (H >= 60 and H < 120):
        R = X
        G = C
        B = 0
    elif (H >= 120 and H < 180):
        R = 0
        G = C
        B = X
    elif (H >= 180 and H < 240):
        R = 0
        G = X
        B = C
    elif (H >= 240 and H < 300):
        R = X
        G = 0
        B = C
    elif (H >= 300 and H < 360):
        R = C
        G = 0
        B = X

    R = (R + m) * 255
    G = (G + m) * 255
    B = (B + m) * 255

    return R,G,B


class Example(QWidget):



    def __init__(self):
        super().__init__()
        self.initUI()
        # self.applyChanges()


    def applyChanges1(self):
        global imageroute
        image = Image.open(imageroute)  # Открываем изображение.
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
        width = image.size[0]  # Определяем ширину.
        height = image.size[1]  # Определяем высоту.
        pix = image.load()  # Выгружаем значения пикселей.

        cH = self.hField.text()
        cH = int(cH)
        cS = self.sField.text()
        cS = float(cS)
        cL = self.lField.text()
        cL = float(cL)
        print(cL)
        for i in range(width):
            for j in range(height):
                H, S, L = RGBtoHSL(pix[i, j][0], pix[i, j][1], pix[i, j][2])

                H += cH
                S += cS
                L += cL
                H = H % 360
                if S>1:
                    S=1
                elif S<0:
                    S=0
                if L > 1:
                    L = 1
                elif L < 0:
                    L = 0

                R, G, B = HSLtoRGB(H, S, L)
                draw.point((i, j), (round(R), round(G), round(B)))

        image.save(imageroute2, "JPEG")
        del draw
        # self.imageLabel.deleteLater()
        # self.imageLabel = QLabel(self)
        self.pixmap = QPixmap(imageroute2)
        self.imageLabel.setPixmap(self.pixmap)
        # self.imageLabel.move(320, 320)
        self.show()
        print(self.pixmap.width())
        print("showwwwww")




    def applyChanges2(self):
        global imageroute
        print(2)
        image = Image.open(imageroute)  # Открываем изображение.
        draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования.
        width = image.size[0]  # Определяем ширину.
        height = image.size[1]  # Определяем высоту.
        pix = image.load()  # Выгружаем значения пикселей.

        cH = self.hField.text()
        cH = int(cH)
        cS = self.sField.text()
        cS = float(cS)
        cV = self.lField.text()
        cV = float(cV)
        for i in range(width):
            for j in range(height):
                H, S, V = RGBtoHSV(pix[i, j][0], pix[i, j][1], pix[i, j][2])
                H += cH
                S += cS
                V += cV
                while H>360:
                    H -= 360
                if S>1:
                    S=1
                elif S<0:
                    S=0
                if V > 1:
                    V = 1
                elif V < 0:
                    V = 0

                R, G, B = HSVtoRGB(H, S, V)
                draw.point((i, j), (round(R), round(G), round(B)))

        image.save(imageroute2, "JPEG")
        del draw

        self.pixmap = QPixmap(imageroute2)
        self.imageLabel.setPixmap(self.pixmap)
        self.show()
        print("finish load")




    @pyqtSlot()
    def on_click(self):
        print("call")
        print(self.hField.text())
        self.applyChanges1()

        self.show()

    @pyqtSlot()
    def on_click1(self):

        self.applyChanges2()
        print(1)
        self.show()

    def initUI(self):
        global imageroute
        self.resize(650, 500)
        self.center()

        self.qbtn = QPushButton('HSL', self)
        self.qbtn.clicked.connect(self.on_click)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(50, 170)
        self.qbtn1 = QPushButton('HSV', self)
        self.qbtn1.clicked.connect(self.on_click1)
        self.qbtn1.resize(self.qbtn1.sizeHint())
        self.qbtn1.move(50, 200)
        self.hl = QLabel("H", self)
        self.hl.move(50, 50)
        self.hField = QLineEdit("0", self)
        self.hField.move(70, 50)
        self.sl = QLabel("S", self)
        self.sl.move(50, 80)
        self.sField = QLineEdit("0", self)
        self.sField.move(70, 80)
        self.ll = QLabel("L", self)
        self.ll.move(50, 110)
        self.lField = QLineEdit("0", self)
        self.lField.move(70, 110)
        self.vl = QLabel("V", self)
        self.vl.move(50, 140)
        self.vField = QLineEdit("0", self)
        self.vField.move(70, 140)

        self.imageLabel = QLabel(self)
        self.pixmap = QPixmap(imageroute)
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.move(220, 50)


        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()



    sys.exit(app.exec_())