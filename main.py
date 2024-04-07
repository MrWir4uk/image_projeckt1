from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
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
        self.ui.listWidget.currentRowChanged.connect(self.show_chosen_image)
        self.ui.black_white_btn.clicked.connect(self.do_black_white)
        self.ui.sharpness.clicked.connect(self.do_blur_white)


    def show_image_list(self):
        self.filenames = os.listdir(self.workdir)
        images = []
        for filename in self.filenames:
            if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                images.append(filename)

        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(images)



    def choose_folder(self):
        try:
            self.workdir = QFileDialog.getExistingDirectory()
            self.show_image_list()
        except:
            message = QMessageBox()
            message.setText("Помилка відкриття папки!")
            message.exec_()


    def load_image(self, imagename):
        self.image_name = imagename
        self.image_path = os.path.join(self.workdir, self.image_name)
        self.image = Image.open(self.image_path)

    def show_image(self):
        self.ui.label.hide()
        h = self.ui.label.height()
        w = self.ui.label.width()

        pixmap_image = QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(w,h,Qt.KeepAspectRatio)
        self.ui.label.setPixmap(pixmap_image)
        self.ui.label.show()


    def show_chosen_image(self):
        if self.ui.listWidget.currentRow()>=0:
            self.image_name = self.ui.listWidget.currentItem().text()
            self.load_image(self.image_name)
            self.show_image()

    def save_image(self):

        path = os.path.join(self.workdir, "edited")
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        self.new_path = os.path.join(path, self.image_name)
        self.new_image.save(self.new_path)
        self.image_path = self.new_path

    def do_black_white(self):
        self.new_image = self.image.convert('L')
        self.save_image()
        self.show_image()

    def do_blur_white(self):
        self.new_image = self.image.filter(ImageFilter.BoxBlur(4))
        self.save_image()
        self.show_image()
        self.image_path = self.new_image


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
    
