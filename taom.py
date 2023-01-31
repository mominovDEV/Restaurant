from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QPushButton, QLabel, QCheckBox
from PyQt5.QtGui import QFont, QIcon
import sys
class restoran(QWidget):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Restoran®️                                                  Ish vaqti: 10:00 22:00")
        # self.setGeometry(50,50,1000,500)
        self.setFixedSize(880,395)
        self.start()
        self.setWindowIcon(QIcon("C:\\Users\\MARDON\\Downloads\\Telegram Desktop\\oqtepa.jpg"))
    def font(self,obj,x,y):
        obj.setFont(QFont("Times", 15))
        obj.move(x, y)
    def start(self):
        self.nomi = QLabel("RESTORAN",self) #Ekranni urtasidagi
        self.nomi.setFont(QFont("Roman, Times-New Roman",25))
        self.nomi.move(350,30)

        self.taom1 = QLabel("Taomlar ",self)# qatorni tepasoda
        self.font(self.taom1,30,90)
        self.osh = QCheckBox("Osh 🍛",self)
        self.font(self.osh,30,130)
        self.dimlama = QCheckBox("Dimlama 🍲",self)
        self.font(self.dimlama,30,170)
        self.qotirma = QCheckBox("Qotirma 🥮", self)
        self.font(self.qotirma, 30, 210)
        self.norin = QCheckBox("Norin 🥠", self)
        self.font(self.norin, 30, 250)
        self.kabob = QCheckBox("Kabob 🍖", self)
        self.font(self.kabob, 30, 290)

        self.taom2 = QLabel("Taomlar ",self)
        self.font(self.taom2,240,90)
        self.lagmon = QCheckBox("Lag'mon 🍜",self)
        self.font(self.lagmon,240,130)
        self.chuchvara = QCheckBox("Chuchvara 🍲",self)
        self.font(self.chuchvara,240,170)
        self.shorva = QCheckBox("Sho'rva 🥣",self)
        self.font(self.shorva,240,210)
        self.moshxorda = QCheckBox("Moshxo'rda 🍲",self)
        self.font(self.moshxorda,240,250)
        self.ajabsanda = QCheckBox("Ajabsanda 🥧",self)
        self.font(self.ajabsanda,240,290)

        self.ichimlik = QLabel("Ichimliklar ",self)
        self.font(self.ichimlik,450,90)
        self.kofe = QCheckBox("Kofe ☕️", self)
        self.font(self.kofe, 450, 130)
        self.cocacola = QCheckBox("Coca Cola 🍷", self)
        self.font(self.cocacola, 450, 170)
        self.chortoq = QCheckBox("Chortoq 🥂", self)
        self.font(self.chortoq, 450, 210)
        self.fanta = QCheckBox("Fanta 🍸", self)
        self.font(self.fanta, 450, 250)
        self.sharbat = QCheckBox("Tabiiy Sharbat 🍹", self)
        self.font(self.sharbat, 450, 290)
        self.desert = QLabel("Desert", self)
        self.font(self.desert, 680, 90)
        self.meva = QCheckBox("Mevalar 🍏", self)
        self.font(self.meva, 680, 130)
        self.shirinlik = QCheckBox("Shirinlik 🍰", self)
        self.font(self.shirinlik, 680, 170)
        self.chips = QCheckBox("Chips 🥡", self)
        self.font(self.chips, 680, 210)
        self.salat = QCheckBox("Salat 🥦", self)
        self.font(self.salat, 680, 250)
        self.piyoz = QCheckBox("Free 🍟", self)
        self.font(self.piyoz, 680, 290)
        self.hisob = QPushButton("Hisob",self)
        self.font(self.hisob,30,350)
        self.hisob.clicked.connect(self.run)

        self.taomlar1 = QLabel(self)
        self.font(self.taomlar1,30,100)
        self.taomlar2 = QLabel(self)
        self.font(self.taomlar2,250,100)
        self.ichim = QLabel(self)
        self.font(self.ichim,500,100)
        self.des = QLabel(self)
        self.font(self.des,720,100)
        self.jami_hisob = QLabel(self)
        self.font(self.jami_hisob,300,40)
    def run(self):
        hisob = 0
        taom_1 = ""
        self.osh.hide()
        self.dimlama.hide()
        self.qotirma.hide()
        self.norin.hide()
        self.kabob.hide()
        self.taom1.hide()
        if self.osh.isChecked():
            taom_1 += "Osh ⇾ 20000\n\n"
            hisob += 20000
        if self.dimlama.isChecked():
            taom_1 += "Dimlama ⇾ 25000\n\n"
            hisob += 25000
        if self.qotirma.isChecked():
            taom_1 += "Qotirma ⇾ 22000\n\n"
            hisob += 22000
        if self.norin.isChecked():
            taom_1 += "Norin ⇾ 23000\n\n"
            hisob += 23000
        if self.kabob.isChecked():
            taom_1 += "Kabob ⇾ 15000"
            hisob += 15000
        self.taomlar1.setText(f"1-Taomlar ⇒ {hisob}\n\n{taom_1}")
        self.taomlar1.adjustSize()

        self.lagmon.hide()
        self.chuchvara.hide()
        self.shorva.hide()
        self.moshxorda.hide()
        self.ajabsanda.hide()
        self.taom2.hide()
        hisob2 = 0
        taom_2 = ""
        if self.lagmon.isChecked():
            taom_2 += "Lag'mon ⇾ 18000\n\n"
            hisob2 += 18000
        if self.chuchvara.isChecked():
            taom_2 += "Chuchvara ⇾ 15000\n\n"
            hisob2 += 15000
        if self.shorva.isChecked():
            taom_2 += "Sho'rva ⇾ 15000\n\n"
            hisob2 += 15000
        if self.moshxorda.isChecked():
            taom_2 += "Moshxo'rda ⇾ 17000\n\n"
            hisob2 += 17000
        if self.ajabsanda.isChecked():
            taom_2 += "Ajabsanda ⇾ 19000"
            hisob2 += 19000
        self.taomlar2.setText(f"2-Taomlar ⇒ {hisob2}\n\n{taom_2}")
        self.taomlar2.adjustSize()

        self.kofe.hide()
        self.cocacola.hide()
        self.chortoq.hide()
        self.fanta.hide()
        self.sharbat.hide()
        self.ichimlik.hide()
        hisob3 = 0
        ichimli = ""
        if self.kofe.isChecked():
            ichimli += "Kofe ⇾ 5000\n\n"
            hisob3 += 5000
        if self.cocacola.isChecked():
            ichimli += "Coca Cola ⇾ 10000\n\n"
            hisob3 += 10000
        if self.chortoq.isChecked():
            ichimli += "Chortoq ⇾ 9000\n\n"
            hisob3 += 9000
        if self.fanta.isChecked():
            ichimli += "Fanta ⇾ 10000\n\n"
            hisob3 += 10000
        if self.sharbat.isChecked():
            ichimli += "Sharbat ⇾ 8000"
            hisob3 += 8000
        self.ichim.setText(f"Ichimliklar ⇒ {hisob3}\n\n{ichimli}")
        self.ichim.adjustSize()

        self.meva.hide()
        self.shirinlik.hide()
        self.chips.hide()
        self.salat.hide()
        self.piyoz.hide()
        self.desert.hide()
        hisob4 = 0
        dese = ""
        if self.meva.isChecked():
            dese += "Meva ⇾ 8000\n\n"
            hisob4 += 8000
        if self.shirinlik.isChecked():
            dese += "Shirinlik ⇾ 10000\n\n"
            hisob4 += 10000
        if self.chips.isChecked():
            dese += "Chips ⇾ 9000\n\n"
            hisob4 += 9000
        if self.salat.isChecked():
            dese += "Salat ⇾ 7000\n\n"
            hisob4 += 7000
        if self.piyoz.isChecked():
            dese += "Free ⇾ 10000"
            hisob4 += 10000
        self.des.setText(f"Desert ⇒ {hisob4}\n\n{dese}")
        self.des.adjustSize()
        self.nomi.hide()
        self.hisob.hide()

        self.jami_hisob.setText(f"Jami hisob ⟶ {hisob+hisob2+hisob3+hisob4} ✓")
        self.jami_hisob.adjustSize()
app = QApplication(sys.argv)
ob = restoran()
ob.show()
sys.exit(app.exec_())