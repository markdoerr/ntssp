# -*- coding: utf8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FormationEditor import *
from PathStroke import *

class FormationEditorWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self);
        #Import UI from Designer
        self.ui = Ui_MainWindow();
        
        #SetupUI
        self.ui.setupUi(self);
        
        #PathStrokeRender
        self.m_renderer = PathStrokeRenderer(self);
        
        #Add to PreviewArea
        self.ui.PreviewArea.setWidget(self.m_renderer);
        
        #Connections :
        QObject.connect(self.ui.PenWidthSlider, SIGNAL("valueChanged(int)"),self.m_renderer.setPenWidth);
        QObject.connect(self.ui.AddPath,SIGNAL("clicked(bool)"),self.m_renderer.addPath);
        QObject.connect(self.ui.Curve,SIGNAL("clicked(bool)"),self.Curve);
        QObject.connect(self.ui.Line,SIGNAL("clicked(bool)"),self.Line);
        
    def Curve(self):
        self.ui.Line.setChecked(False);
        self.m_renderer.setCurveLine(True);
    def Line(self):
        self.ui.Curve.setChecked(False);
        self.m_renderer.setCurveLine(False);