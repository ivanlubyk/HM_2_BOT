
from PyQt5.QtWidgets import  QApplication, QMainWindow, QFileDialog


from  ui.main_window import Ui_MainWindow



from pages_functions.Notes import Notes
from pages_functions.Adress import Adress




class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)

        self.adress_btn = self.ui.pushButton_2
        self.notes_btn = self.ui.pushButton_3
        self.sort_btn = self.ui.pushButton


        self.menu_btn_dict = {self.adress_btn: Adress, self.notes_btn: Notes }

        self.show_Home_window()

        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)


        self.sort_btn.clicked.connect(self.get_file_path)
        self.adress_btn.clicked.connect(self.show_selected_window)
        self.notes_btn.clicked.connect(self.show_selected_window)






    def get_file_path(self):
        fname = QFileDialog.getOpenFileName(self)
        self.sort_btn.setChecked(False)
        print(fname)



    def show_Home_window(self):

        result = self.open_tab_flag(self.adress_btn.text())
        self.set_btn_cheked(self.adress_btn)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_tittle = self.adress_btn.text()
            curIndex = self.ui.tabWidget.addTab(Adress(),tab_tittle)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)









    def show_selected_window(self):
        button = self.sender()

        result = self.open_tab_flag(button.text())
        self.set_btn_cheked(button)

        if result[0]:
            pass
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_tittle = button.text()
            curIndex =self.ui.tabWidget.addTab(self.menu_btn_dict[button](),tab_tittle)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def close_tab(self,index):
        self.ui.tabWidget.removeTab(index)

        if self.ui.tabWidget.count() ==0:
            self.ui.toolBox.setCurrentIndex(0)
            self.show_Home_window()

    def set_btn_cheked(self, btn):
        for button in self.menu_btn_dict.keys():
            if button != btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def open_tab_flag(self, btn_text):
        open_tub_count = self.ui.tabWidget.count()

        for i in range(open_tub_count):
            tab_titlle = self.ui.tabWidget.tabText(i)
            if tab_titlle == btn_text:
                return True, i
            else:
                continue
        return False,


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
