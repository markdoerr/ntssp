# -*- coding: utf8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FormationEditor import *
import Monster;
from PathStroke import *
from Data.Data import *;
from Data.Enemy import *;

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
        
        #init
        self.monsterDialog = None;
        
        #Connections :
        QObject.connect(self.ui.PenWidthSlider, SIGNAL("valueChanged(int)"),self.m_renderer.setPenWidth);
        QObject.connect(self.ui.AddPath,SIGNAL("clicked(bool)"),self.m_renderer.addPath);
        QObject.connect(self.ui.Curve,SIGNAL("clicked(bool)"),self.Curve);
        QObject.connect(self.ui.Line,SIGNAL("clicked(bool)"),self.Line);
        QObject.connect(self.ui.AddChange,SIGNAL("clicked()"),self.MonsterDialog);
        
    def Curve(self):
        self.ui.Line.setChecked(False);
        self.m_renderer.setCurveLine(True);
    def Line(self):
        self.ui.Curve.setChecked(False);
        self.m_renderer.setCurveLine(False);
    def MonsterDialog(self):
        if(self.monsterDialog is None):
            self.monsterDialog = MonsterDialogWindow();
        self.monsterDialog.show();
    
class MonsterDialogWindow(QtGui.QDialog):
    def __init__(self):
        #To DELETE
        Data.getInstance().newFormation();
        QtGui.QDialog.__init__(self);
        #Import UI from Designer
        self.ui = Monster.Ui_Dialog();
        
        #SetupUI
        self.ui.setupUi(self);
        
        self.updateMonsterList();
                
        #Connections :
        QObject.connect(self.ui.add,SIGNAL("clicked(bool)"),self.addMonster);
        QObject.connect(self.ui.change,SIGNAL("clicked(bool)"),self.changeMonster);
        QObject.connect(self.ui.remove,SIGNAL("clicked(bool)"),self.removeMonster);
        
    def updateMonsterList(self):
        #Fill MonsterList
        currentFormation = Data.getInstance().getCurrentFormation();
        if(currentFormation is not None):
            self.ui.listWidget.clear();
            for enemy in currentFormation.enemies:
                self.ui.listWidget.addItem(enemy.toString());
    def changeMonster(self):
        pass;
    def removeMonster(self):
        pass;
    def addMonster(self):
        currentFormation = Data.getInstance().getCurrentFormation();
        currentFormation.enemies.append(Enemy(self.ui.horizontalSlider.value(),self.ui.horizontalSlider_2.value(),(0,0),None));
        self.updateMonsterList();
        