from PIL import Image, ImageFilter
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from ui import Ui_MainWindow

import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = None
        self.filename = None
        self.image = None
        self.ui.folder.clicked.connect(self.choose_folder)

    def show_image_list(self):
        self.filename = os.listdir(self.workdir)
        image = []
        for filename in self.filenames:
            if filename.endswith(". png") or filename.endswith(". jpg") or filename.endswith(". jpeg"):
                images.append(filename)

        self.ui.image_list.clear()
        self.ui.image_list.addItems(images)

    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("Помилка відкриття папки!")
            message.exec_()


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()


#python -m PyQt5.uic.pyuic -x untitled.ui -o ui.py

# with Image.open("rabstol_net_fast_and_furious_18_1920x1200.jpg") as original:
#     pic_gray = original.convert('L')
#     pic_gray.save('bw_pic.jpg')
#     pic_gray.show()
#     pic_blur = original.filter(ImageFilter.BLUR)
#     pic_blur.save('blur_pic.jpg')
#     pic_blur.show()
#     pic_up = original.transpose(Image.ROTATE_90)
#     pic_up.save('rabstol_net_fast_and_furious_18_1920x1200.jpg')
#     pic_up.show()
    
