#
#

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))


    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 10
        self.frames = load_sprite('Kirby',self.num_frames)
        self.image = QLabel()
        self.button = QPushButton("Start")
        self.slide = QSlider(Qt.Orientation.Vertical)
        self.text1 = QLabel("Frames Per Second")
        self.text2 = QLabel("0")

        # Add any other instance variables needed to track information as the program
        # runs here

        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        application_frame = QFrame()

        application_layout = QVBoxLayout()


        image_frame = QFrame()
        image_layout = QHBoxLayout(image_frame)
        text_frame = QFrame()
        text_layout = QHBoxLayout(text_frame)
        button_frame = QFrame()
        button_layout = QVBoxLayout(button_frame)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        file_menu = menubar.addMenu('&File')
        pause_action = QAction('&Pause', self)
        pause_action.triggered.connect(self.pause)
        file_menu.addAction(pause_action)
        exit_action = QAction('&Exit', self)
        exit_action.triggered.connect(self.quit_program)
        file_menu.addAction(exit_action)


        # image = QLabel()
        # self.image.setPixmap(QPixmap(self.frames[1]))
        # sprite = self.frames[1]
        # print(sprite)

        self.image.setPixmap(QPixmap("Kirby/sprite_00.png"))
        # self.image.setPixmap(QPixmap(sprite))
        # self.image.setScaledContents(True)
        # self.image.Scaled(100,100,Qt.AspectRatioMode.KeepAspectRatio)
        image_layout.addWidget(self.image)

        # slide = QSlider()
        self.slide.setRange(0, 100)
        self.slide.setSingleStep(1)
        # self.slide.setTickPosition(TicksAbove)
        self.slide.setTickInterval(12)
        image_layout.addWidget(self.slide)

        self.slide.valueChanged.connect(self.value_changed)
        # self.slide.sliderMoved.connect(self.slider_position)

        # text1 = QLabel("Frames Per Second")
        font = self.text1.font()
        font.setPointSize(15)
        self.text1.setFont(font)
        text_layout.addWidget(self.text1)

        font = self.text2.font()
        font.setPointSize(15)
        self.text2.setFont(font)
        text_layout.addWidget(self.text2)

        text_frame.setLayout(text_layout)
        button_layout.addWidget(text_frame)


        # button = QPushButton("Start")
        self.button.setCheckable(True)
        # self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)

        button_layout.addWidget(self.button)


        image_frame.setLayout(image_layout)

        button_frame.setLayout(button_layout)

        application_layout.addWidget(image_frame)
        application_layout.addWidget(button_frame)

        application_frame.setLayout(application_layout)
        self.setCentralWidget(application_frame)

        self.setFixedSize(QSize(300, 300))



    def quit_program(self):
        self.close()

    def pause(self):
        print("pause")

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        if self.button_is_checked:
            self.button.setText("Stop")
            self.animation()
        else:
            self.button.setText("Start")
            self.image.setPixmap(QPixmap("Kirby/sprite_00.png"))

    def value_changed(self, i):
        self.text2.setText(str(i))

    def slider_position(self, p):
        print("Position", p)

    def animation(self):
        
        self.image.setPixmap(QPixmap("Kirby/sprite_01.png"))
        print("Animation")


    # You will need methods in the class to act as slots to connect to signals


def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()

