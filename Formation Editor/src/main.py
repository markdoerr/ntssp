from PyQt4.QtCore import *
from PathStroke import *
from res import *
def main():
    app = QApplication([]);

    pathStrokeWidget = PathStrokeWidget();
    pathStrokeWidget.show();

    return app.exec_();

main()