from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gestão Escolar")

        layout = QVBoxLayout()

        self.label = QLabel("Bem-vindo ao Sistema de Gestão Escolar")
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
