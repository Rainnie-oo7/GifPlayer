# This Python file uses the following encoding: utf-8
import pygame
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

    def main():
        pygame.init()
        # Setze die Größe des Fensters entsprechend der GIF-Datei
        gif_file = "525px-Euler_s_formula_proof.gif"
        gif = pygame.image.load(gif_file)
        width, height = gif.get_size()
        screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption("GIF-Player")

        clock = pygame.time.Clock()
        is_playing = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        is_playing = not is_playing

            if is_playing:
                screen.blit(gif, (0, 0))

            pygame.display.flip()
            clock.tick(30)  # Hier kannst du die Bildwiederholrate anpassen



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    main()
    sys.exit(app.exec())
