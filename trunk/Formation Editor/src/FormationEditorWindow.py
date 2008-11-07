# -*- coding: utf8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from FormationEditor import *
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
        #Path Group:
        QObject.connect(self.ui.Path_Add,SIGNAL("clicked(bool)"),self.AddPath);
        QObject.connect(self.ui.Path_Delete,SIGNAL("clicked(bool)"),self.DeletePath);
        QObject.connect(self.ui.Curve,SIGNAL("clicked(bool)"),self.Curve);
        QObject.connect(self.ui.Line,SIGNAL("clicked(bool)"),self.Line);
        
        #Pen Width
        QObject.connect(self.ui.PenWidthSlider, SIGNAL("valueChanged(int)"),self.m_renderer.setPenWidth);

        #Global Group:
        QObject.connect(self.ui.Animate,SIGNAL("clicked(bool)"),self.Animate);
        QObject.connect(self.ui.Save, SIGNAL("clicked(bool)"),self.Save);
        
        #Groups Group:
        QObject.connect(self.ui.Groups_Add,SIGNAL("clicked(bool)"),self.AddGroup);
        QObject.connect(self.ui.Groups_Change, SIGNAL("clicked(bool)"),self.ChangeGroup);
        QObject.connect(self.ui.Groups_Delete, SIGNAL("clicked(bool)"),self.DeleteGroup);
        
        #Monsters Group:
        QObject.connect(self.ui.Monsters_Add,SIGNAL("clicked(bool)"),self.AddMonster);
        QObject.connect(self.ui.Monsters_Change, SIGNAL("clicked(bool)"),self.ChangeMonster);
        QObject.connect(self.ui.Monsters_Delete,SIGNAL("clicked(bool)"),self.DeleteMonster);
        QObject.connect(self.ui.Monster_Color,SIGNAL("sliderMoved(int)"),self.MonsterColorChange);
        QObject.connect(self.ui.Monster_Size,SIGNAL("sliderMoved(int)"),self.MonsterSizeChange);
        
        #Association Group:
        QObject.connect(self.ui.Association_Associate,SIGNAL("clicked(bool)"),self.Associate);
        QObject.connect(self.ui.Association_TimeBefore,SIGNAL("sliderMoved(int)"),self.TimeBeforeChange);
        
        #Time Tab:
        QObject.connect(self.ui.Time_OrderUp,SIGNAL("clicked(bool)"),self.TimeOrderCurrentUp);
        QObject.connect(self.ui.Time_OrderDown,SIGNAL("clicked(bool)"),self.TimeOrderCurrentDown);
        QObject.connect(self.ui.Time_OrderGlobalDown,SIGNAL("clicked(bool)"),self.TimeOrderGlobalDown);
        QObject.connect(self.ui.Time_OrderGlobalUp,SIGNAL("clicked(bool)"),self.TimeOrderGlobalUp);
        
    
    #TimeTab:
    def TimeOrderCurrentUp(self):
        pass;
    def TimeOrderCurrentDown(self):
        pass;
    def TimeOrderGlobalUp(self):
        pass;
    def TimeOrderGlobalDown(self):
        pass;
    
    #Association Group:
    def Associate(self):
        group = self.GetGroupSelected(self.ui.Association_GroupsList);
        path = self.GetPathSelected(self.ui.Association_PathsList);
        if(len(group) > 0 and len(path) > 0):
            group[0].AddPath(path[0]);
        self.UpdateGroups();
        self.UpdatePaths();
    def TimeBeforeChange(self,value):
        pass;
    
    #Monsters Group
    def AddMonster(self):
        size = self.ui.Monster_Size.value();
        color = self.ui.Monster_Color.value();
        pos = Point(100,100);
        Data.getInstance().newMonster(color,size, pos);
        self.UpdateMonsters();
    def ChangeMonster(self):
        selected = self.GetMonsterSelectedIndexes();
        if(len(selected) == 1):
            monster = Data.getInstance().getMonster(selected[0]);
            size = self.ui.Monster_Size.value();
            color = self.ui.Monster_Color.value();
            monster.life = color;
            monster.size = size;
            self.UpdateMonsters();
    def DeleteMonster(self):
        selected = self.GetMonsterSelectedIndexes();
        for i in selected :
            Data.getInstance().deleteMonster(i);
        self.UpdateMonsters();
        self.UpdateGroups();
            
    def MonsterColorChange(self,value):
        self.ui.Monster_ColorLabel.setText("Color : " + str(value));
    def MonsterSizeChange(self,value):
        self.ui.Monster_SizeLabel.setText("Size : " + str(value));
    def GetMonsterSelected(self):
        selected = [];
        items = self.ui.Formation_MonstersList.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(Data.getInstance().getMonster(i.row()));
        return selected;
    def GetMonsterSelectedIndexes(self):
        selected = [];
        items = self.ui.Formation_MonstersList.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(i.row());
        return selected;
    def UpdateMonsters(self):
        self.ui.Formation_MonstersList.clear();
        for i in xrange(Data.getInstance().getNbMonster()):
            self.ui.Formation_MonstersList.addTopLevelItem(self.GetMonsterUI(Data.getInstance().getMonster(i)));
    def GetMonsterUI(self,monster):
        item = QTreeWidgetItem();
        item.setText(0,"Monster (" + str(monster.id) + ")");
        item.setText(1,"Life : "+str(monster.life) +", Size : "+str(monster.size))
        return item;    
    
    
    #Groups Group
    def AddGroup(self):
        enemies = self.GetMonsterSelected();
        if(len(enemies) > 0):
            Data.getInstance().newGroup(enemies);
            self.UpdateGroups()
    def GetGroupSelected(self,list):
        selected = [];
        items = list.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(Data.getInstance().getGroup(i.row()));
        return selected;
    def GetGroupSelectedIndexes(self,list):
        selected = [];
        items = list.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(i.row());
        return selected;
    def ChangeGroup(self):
        selected = self.GetGroupSelected(self.ui.Formation_GroupsList);
        if(len(selected) == 1):
            selected[0].enemies = self.GetMonsterSelected();
            self.UpdateGroups();
            
    def DeleteGroup(self):
        selected = self.GetGroupSelectedIndexes(self.ui.Formation_GroupsList);
        for i in selected :
            Data.getInstance().deleteGroup(i);
        self.UpdateGroups();
        self.UpdatePaths();
    def UpdateGroups(self):
        self.ui.Formation_GroupsList.clear();
        self.ui.Association_GroupsList.clear();
        self.ui.Time_GroupsList.clear();
        for i in xrange(Data.getInstance().getNbGroups()):
            item = self.GetGroupUI(Data.getInstance().getGroup(i));
            self.ui.Formation_GroupsList.addTopLevelItem(item);
            item = self.GetGroupUI(Data.getInstance().getGroup(i));
            self.ui.Association_GroupsList.addTopLevelItem(item);
            item = self.GetGroupUI(Data.getInstance().getGroup(i));
            self.ui.Time_GroupsList.addTopLevelItem(item);
    def GetGroupUI(self,group):
        item = QTreeWidgetItem();
        item.setText(0,"Group (" + str(group.id) +")");
        for monster in group.enemies:
           uimonster = self.GetMonsterUI(monster);
           item.addChild(uimonster);
        for path in group.paths:
            g = QTreeWidgetItem();
            g.setText(0,"Path (" + str(path.id) +")");
            item.addChild(g);
        return item;   
    
    #Path Group
    def AddPath(self):
        effectType = self.ui.Path_EffectStyle.currentIndex();
        path = Data.getInstance().newEnemyPath(effectType, 1.0, 1.0);   
        self.m_renderer.currentPath = path;
        self.m_renderer.update(); 
        self.UpdatePaths();
    def DeletePath(self):
        current = self.m_renderer.getCurrentPath();
        Data.getInstance().deleteEnemyPath(current);
        self.m_renderer.update();
        self.UpdatePaths();
        self.UpdateGroups();
    def Curve(self):
        self.ui.Line.setChecked(False);
        self.m_renderer.setCurveLine(True);
    def Line(self):
        self.ui.Curve.setChecked(False);
        self.m_renderer.setCurveLine(False);
    def UpdatePaths(self):
        self.ui.Association_PathsList.clear();
        for i in xrange(Data.getInstance().getNbEnemyPath()):
            item = self.GetPathUI(Data.getInstance().getEnemyPath(i));
            self.ui.Association_PathsList.addTopLevelItem(item);
    def GetPathUI(self,path):
        item = QTreeWidgetItem();
        item.setText(0,"Path (" + str(path.id) +")");
        groups = Data.getInstance().getGroupsForPath(path);
        for group in groups:
            g = QTreeWidgetItem();
            g.setText(0,"Group (" + str(group.id) +")");
            item.addChild(g);
        return item;  
    def GetPathSelected(self,list):
        selected = [];
        items = list.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(Data.getInstance().getEnemyPath(i.row()));
        return selected;
    def GetPathSelectedIndexes(self,list):
        selected = [];
        items = list.selectedIndexes();
        for i in items:
            if(i.column() == 0):
                selected.append(i.row());
        return selected;
    #Pen Width
    def SetPenWidth(self,val):
        pass
    
    #GlobalGroup
    def Animate(self):
        pass
    def Save(self):
        pass
        