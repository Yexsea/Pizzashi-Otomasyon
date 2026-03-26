import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from ana_menu_ui import Ui_MainWindow as Ui_AnaMenu
from siparis_ver_ui import Ui_MainWindow as UiSiparisVer
from siparis_ara_ui import Ui_MainWindow as UiSiparisAra
from listele_ui import Ui_MainWindow as UiListele
from degistir_ui import Ui_MainWindow as UiDegistir
from sil_ui import Ui_MainWindow as UiSil


siparis_listesi = []

class AnaMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AnaMenu()
        self.ui.setupUi(self)

        self.pencere_siparis_ver = SiparisVer()
        self.pencere_siparis_ara = SiparisAra()
        self.pencere_listele = Listele()
        self.pencere_degistir = Degistir()
        self.pencere_sil = Sil()

        self.ui.ver.clicked.connect(self.pencere_siparis_ver.show)
        self.ui.ara.clicked.connect(self.pencere_siparis_ara.show)
        self.ui.gor.clicked.connect(self.pencere_listele.show)
        self.ui.degis.clicked.connect(self.pencere_degistir.show)
        self.ui.sil.clicked.connect(self.pencere_sil.show)

class SiparisVer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiSiparisVer()
        self.ui.setupUi(self)
        
        self.selected_ingredients = []

        self.ui.kasar.clicked.connect(self.toggle_kasar)
        self.ui.sucuk.clicked.connect(self.toggle_sucuk)
        self.ui.mantar.clicked.connect(self.toggle_mantar)
        self.ui.zeytin.clicked.connect(self.toggle_zeytin)
        self.ui.misir.clicked.connect(self.toggle_misir)
        self.ui.biber.clicked.connect(self.toggle_biber)
        self.ui.kavurma.clicked.connect(self.toggle_kavurma)
        self.ui.pastirma.clicked.connect(self.toggle_pastirma)

        self.ui.pushButton.clicked.connect(self.siparis_ver)

    def toggle_kasar(self):
        if self.ui.kasar.isChecked():
            self.selected_ingredients.append("kasar")
        else:
            self.selected_ingredients.remove("kasar")

    def toggle_sucuk(self):
        if self.ui.sucuk.isChecked():
            self.selected_ingredients.append("sucuk")
        else:
            self.selected_ingredients.remove("sucuk")

    def toggle_mantar(self):
        if self.ui.mantar.isChecked():
            self.selected_ingredients.append("mantar")
        else:
            self.selected_ingredients.remove("mantar")

    def toggle_zeytin(self):
        if self.ui.zeytin.isChecked():
            self.selected_ingredients.append("zeytin")
        else:
            self.selected_ingredients.remove("zeytin")

    def toggle_misir(self):
        if self.ui.misir.isChecked():
            self.selected_ingredients.append("misir")
        else:
            self.selected_ingredients.remove("misir")

    def toggle_biber(self):
        if self.ui.biber.isChecked():
            self.selected_ingredients.append("biber")
        else:
            self.selected_ingredients.remove("biber")

    def toggle_kavurma(self):
        if self.ui.kavurma.isChecked():
            self.selected_ingredients.append("kavurma")
        else:
            self.selected_ingredients.remove("kavurma")

    def toggle_pastirma(self):
        if self.ui.pastirma.isChecked():
            self.selected_ingredients.append("pastirma")
        else:
            self.selected_ingredients.remove("pastirma")

    def siparis_ver(self):
        username = self.ui.username_input.toPlainText()
        print(f"Ad: {username}")
        print(f"Seçilen Malzemeler: {', '.join(self.selected_ingredients)}")
        siparis = {
            "ad": username,
            "malzemeler": self.selected_ingredients.copy()
            }
        siparis_listesi.append(siparis)
        self.close()

class SiparisAra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiSiparisAra()
        self.ui.setupUi(self)
        
       
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Ad", "Malzemeler"])
        
       
        self.ui.textEdit.textChanged.connect(self.arama_yap)
    
    def arama_yap(self):
        aranan_metin = self.ui.textEdit.toPlainText().lower()
        self.ui.tableWidget.setRowCount(0) 
        
        if not aranan_metin:
            return
            
        for siparis in siparis_listesi:
            if aranan_metin in siparis["ad"].lower():
                row_position = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_position)
                
                self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(siparis["ad"]))
                self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(", ".join(siparis["malzemeler"])))

class Listele(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiListele()
        self.ui.setupUi(self)
        
     
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Ad", "Malzemeler"])
        
      
        self.siparisleri_yukle()
    
    def siparisleri_yukle(self):
        self.ui.tableWidget.setRowCount(0) 
        
        for siparis in siparis_listesi:
            row_position = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_position)
            
            self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(siparis["ad"]))
            self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(", ".join(siparis["malzemeler"])))

class Degistir(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiDegistir()
        self.ui.setupUi(self)
        
        self.selected_ingredients = []
        
       
        self.ui.checkBox.stateChanged.connect(self.toggle_kasar)
        self.ui.checkBox_2.stateChanged.connect(self.toggle_sucuk)
        self.ui.checkBox_3.stateChanged.connect(self.toggle_mantar)
        self.ui.checkBox_4.stateChanged.connect(self.toggle_zeytin)
        self.ui.checkBox_5.stateChanged.connect(self.toggle_misir)
        self.ui.checkBox_6.stateChanged.connect(self.toggle_biber)
        self.ui.checkBox_7.stateChanged.connect(self.toggle_kavurma)
        self.ui.checkBox_8.stateChanged.connect(self.toggle_pastirma)
        
       
        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)
        self.ui.pushButton.clicked.connect(self.siparisi_degistir)
    
    def toggle_kasar(self, state):
        if state == 2:  
            self.selected_ingredients.append("kasar")
        else:
            if "kasar" in self.selected_ingredients:
                self.selected_ingredients.remove("kasar")

    def toggle_sucuk(self, state):
        if state == 2:
            self.selected_ingredients.append("sucuk")
        else:
            if "sucuk" in self.selected_ingredients:
                self.selected_ingredients.remove("sucuk")

    def toggle_mantar(self, state):
        if state == 2:
            self.selected_ingredients.append("mantar")
        else:
            if "mantar" in self.selected_ingredients:
                self.selected_ingredients.remove("mantar")

    def toggle_zeytin(self, state):
        if state == 2:
            self.selected_ingredients.append("zeytin")
        else:
            if "zeytin" in self.selected_ingredients:
                self.selected_ingredients.remove("zeytin")

    def toggle_misir(self, state):
        if state == 2:
            self.selected_ingredients.append("misir")
        else:
            if "misir" in self.selected_ingredients:
                self.selected_ingredients.remove("misir")

    def toggle_biber(self, state):
        if state == 2:
            self.selected_ingredients.append("biber")
        else:
            if "biber" in self.selected_ingredients:
                self.selected_ingredients.remove("biber")

    def toggle_kavurma(self, state):
        if state == 2:
            self.selected_ingredients.append("kavurma")
        else:
            if "kavurma" in self.selected_ingredients:
                self.selected_ingredients.remove("kavurma")

    def toggle_pastirma(self, state):
        if state == 2:
            self.selected_ingredients.append("pastirma")
        else:
            if "pastirma" in self.selected_ingredients:
                self.selected_ingredients.remove("pastirma")
    
    def on_ok(self):
        print("OK clicked")
    
    def on_cancel(self):
        print("Cancel clicked")
        self.close()
    
    def siparisi_degistir(self):
        username = self.ui.textEdit.toPlainText()
        print(f"Ad: {username}")
        print(f"Yeni Malzemeler: {', '.join(self.selected_ingredients)}")
        
        
        for siparis in siparis_listesi:
            if siparis["ad"] == username:
                siparis["malzemeler"] = self.selected_ingredients.copy()
                print("Sipariş güncellendi!")
                self.close()
                return
        
        print("Sipariş bulunamadı!")

class Sil(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiSil()
        self.ui.setupUi(self)
        
        
        self.ui.buttonBox.accepted.connect(self.on_ok)
        self.ui.buttonBox.rejected.connect(self.on_cancel)
        self.ui.pushButton.clicked.connect(self.siparisi_sil)
    
    def on_ok(self):
        print("OK clicked")
    
    def on_cancel(self):
        print("Cancel clicked")
        self.close()
    
    def siparisi_sil(self):
        username = self.ui.textEdit.toPlainText()
        print(f"Silinecek Ad: {username}")
        
      
        for i, siparis in enumerate(siparis_listesi):
            if siparis["ad"] == username:
                del siparis_listesi[i]
                print("Sipariş silindi!")
                self.close()
                return
        
        print("Sipariş bulunamadı!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaMenu()
    pencere.show()
    sys.exit(app.exec_())