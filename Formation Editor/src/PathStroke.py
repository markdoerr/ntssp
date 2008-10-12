from PyQt4.QtGui import *
from PyQt4.QtCore import *
CurveMode = 0
LineMode = 1
class PathStrokeRenderer(QWidget):
    def __init__(self,parent):
        QWidget.__init__(self,parent)
        self.m_curve=True;
        self.m_colors=[Qt.red,Qt.blue,Qt.black,Qt.magenta,Qt.green,Qt.yellow,Qt.cyan];
        self.m_paths=[];
        self.m_vectorsPath=[];
        self.m_CurrentPoints=[];
        self.m_CurrentVectors=[];
        self.m_Style=[];
        self.m_pointSize = 5;
        self.m_activePoint = -1;
        self.m_capStyle = Qt.FlatCap;
        self.m_joinStyle = Qt.BevelJoin;
        self.m_pathMode = CurveMode;
        self.m_penWidth = 1;
        self.m_penStyle = Qt.SolidLine;
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding);
        self.setFixedSize(800,600)
    def paintEvent(self,e):
        static_image = 0;
        painter = QPainter();
        static_image = QImage(self.size(), QImage.Format_RGB32);
        painter.begin(static_image);

        painter.drawPixmap(240,50,QPixmap(":res/images/demi.png"))
    
    
        painter.setRenderHint(QPainter.Antialiasing);
    
        # client painting
    
        self.paint(painter);
    
        painter.end();
        painter.begin(self);
        painter.drawImage(e.rect(), static_image, e.rect());
    
    def paint(self,painter):

        if (len(self.m_CurrentPoints)==0):
            return;
    
        for j in range(len(self.m_paths)):
            
            CurrentPoints = self.m_paths[j];
            painter.setRenderHint(QPainter.Antialiasing);
        
            painter.setPen(Qt.NoPen);
        
            # Construct the path
            path = QPainterPath();
            path.moveTo(CurrentPoints[0]);
        
            if (self.m_pathMode == LineMode):
                for i in xrange(1,len(CurrentPoints)):
                    path.lineTo(CurrentPoints[i]);
            else:
                i=1;
                while (i + 2 < len(CurrentPoints)):
                    path.cubicTo(CurrentPoints[i], CurrentPoints[i+1], CurrentPoints[i+2]);
                    i += 3;
                while (i < len(CurrentPoints)) :
                    path.lineTo(CurrentPoints[i]);
                    i+=1;
        
        
            # Draw the path
            lg = self.m_colors[j%len(self.m_colors)];
            if(self.m_Style[j]):
                # The "custom" pen
                if (self.m_penStyle == Qt.NoPen):
                    stroker = QPainterPathStroker();
                    stroker.setWidth(self.m_penWidth);
                    stroker.setJoinStyle(self.m_joinStyle);
                    stroker.setCapStyle(self.m_capStyle);
        
                    dashes = [];
                    space = 4.0;
                    dashes.append(1 << space);
                    dashes.append(3 << space)
                    dashes.append(9 << space)
                    dashes.append(27 << space)
                    dashes.append(9 << space)
                    dashes.append(3 << space);
                    stroker.setDashPattern(dashes);
                    stroke = stroker.createStroke(path);
                    painter.fillPath(stroke, lg);
        
                else:
                    pen = QPen(lg, self.m_penWidth, self.m_penStyle, self.m_capStyle, self.m_joinStyle);
                    painter.strokePath(path, pen);
        
            # Draw the control points
            painter.setPen(QColor(50, 100, 120, 200));
            painter.setBrush(QColor(50, 100, 120, 120));
            for i in xrange(0,len(CurrentPoints)):
                pos = CurrentPoints[i];
                painter.drawEllipse(QRectF(pos.x() - self.m_pointSize,pos.y() - self.m_pointSize,self.m_pointSize*2, self.m_pointSize*2));
            if(not self.m_Style[j]):
                painter.setPen(lg);
            else:
                painter.setPen(QPen(Qt.black, 0, Qt.SolidLine));
            painter.setBrush(Qt.NoBrush);
            painter.drawPolyline(QPolygonF(CurrentPoints));

    def initializePoints(self):
        count = 1;
        #self.m_CurrentPoints=[];
        #self.m_CurrentVectors=[];
    
        m = QMatrix();
        rot = 360 / count;
        center = QPointF(self.width() / 2, self.height() / 2);
        vm = QMatrix();
        vm.shear(2, -1);
        vm.scale(3, 3);
    
        for i in xrange(0,count):
            self.m_CurrentVectors.append(QPointF(0.1,0.25) * (m * vm));
            self.m_CurrentPoints.append(QPointF(0, 100) * m + center);
            m.rotate(rot);
    
    def addPoint(self,pos):
        point = QPointF(pos)
        line = QLineF(self.m_CurrentPoints[-1],point)
        self.m_CurrentPoints.append(line.pointAt(1.0/3.0));
        self.m_CurrentPoints.append(line.pointAt(2.0/3.0));
        self.m_CurrentPoints.append(point)
        self.update();
    def addPath(self):
        count = 1;
        Points=[];
        Vectors=[];
    
        m = QMatrix();
        rot = 360 / count;
        center = QPointF(self.width() / 2, self.height() / 2);
        vm = QMatrix();
        vm.shear(2, -1);
        vm.scale(3, 3);
    
        for i in xrange(0,count):
            Vectors.append(QPointF(0.1,0.25) * (m * vm));
            Points.append(QPointF(0, 100) * m + center);
            m.rotate(rot);
        
        self.m_paths.append(Points);
        self.m_vectorsPath.append(Vectors);
        self.m_Style.append(self.m_curve);
        if(len(self.m_CurrentPoints) == 0):
            self.m_CurrentPoints=Points;
            self.m_CurrentVectors=Vectors;
        self.repaint();
    def setCurveLine(self,checked):
        self.m_curve=checked;
    def updatePoints(self):
        pad = 10.0;
        left = pad;
        right = self.width() - pad;
        top = pad;
        bottom = self.height() - pad;
    
        for j in xrange(0,len(self.m_paths)):
            CurrentPoints = self.m_paths[j];
            CurrentVectors= self.m_vectorsPath[j];
            for i in xrange(0,len(CurrentPoints)):
                if (i == self.m_activePoint):
                    continue;
        
                pos = CurrentPoints[i];
                vec = CurrentVectors[i];
                pos += vec;
                if (pos.x() < left or pos.x() > right):
                    vec.setX(-vec.x());
                    if(pos.x() < left):
                        pos.setX(left);
                    else:
                        pos.setX(right)
                if (pos.y() < top or pos.y() > bottom):
                    vec.setY(-vec.y());
                    if(pos.y() < top):
                        pos.setX(top);
                    else:
                        pos.setX(bottom)
                CurrentPoints[i] = pos;
                CurrentVectors[i] = vec;
            self.update();

    def mousePressEvent(self,e):
        self.m_activePoint = -1;
        distance = -1;
        for j in xrange(0,len(self.m_paths)):
            CurrentPoints = self.m_paths[j];
            CurrentVectors= self.m_vectorsPath[j];
            for i in xrange(0,len(CurrentPoints)):
                d = QLineF(QPointF(e.pos()), CurrentPoints[i]).length();
                if ((distance < 0 and d < 8 * self.m_pointSize) or d < distance):
                    distance = d;
                    self.m_activePoint = i;
                    self.m_CurrentPoints = CurrentPoints;
                    self.m_CurrentVectors =CurrentVectors;           
        if (self.m_activePoint != -1):
            self.mouseMoveEvent(e);
    
    def mouseDoubleClickEvent(self,e):
        self.addPoint(e.pos())

    def mouseMoveEvent(self,e):
        if (self.m_activePoint >= 0 and self.m_activePoint < len(self.m_CurrentPoints)):
            self.m_CurrentPoints[self.m_activePoint] = QPointF(e.pos());
            self.update();

    def mouseReleaseEvent(self,e):
        self.m_activePoint = -1;

    def setPenWidth(self,penWidth):
        self.m_penWidth = penWidth / 10.0; 
        self.update();

    def setFlatCap(self):
        self.m_capStyle = Qt.FlatCap; 
        self.update();
    
    def setSquareCap(self):
        self.m_capStyle = Qt.SquareCap; 
        self.update();
    
    def setRoundCap(self):
        self.m_capStyle = Qt.RoundCap; 
        self.update();

    def setBevelJoin(self):
        self.m_joinStyle = Qt.BevelJoin;
        self.update();
        
    def setMiterJoin(self):
        self.m_joinStyle = Qt.MiterJoin;
        self.update();
    
    def setRoundJoin(self):
        self.m_joinStyle = Qt.RoundJoin;
        self.update();

    def setCurveMode(self):
        self.m_pathMode = CurveMode;
        self.update();
        
    def setLineMode(self):
        self.m_pathMode = LineMode;
        self.update();

    def setSolidLine(self):
        self.m_penStyle = Qt.SolidLine;
        self.update();
        
    def setDashLine(self):
        self.m_penStyle = Qt.DashLine;
        self.update();
        
    def setDotLine(self):
        self.m_penStyle = Qt.DotLine; 
        self.update();
        
    def setDashDotLine(self):
        self.m_penStyle = Qt.DashDotLine;
        self.update();
        
    def setDashDotDotLine(self):
        self.m_penStyle = Qt.DashDotDotLine;
        self.update();
        
    def setCustomDashLine(self):
        self.m_penStyle = Qt.NoPen; 
        self.update();
        
class PathStrokeWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Path Stroking");
        
        #Setting up palette.
        pal = self.palette()
        self.setPalette(pal);
    
        # Widget construction and property setting
        self.m_renderer = PathStrokeRenderer(self);
    
        mainGroup = QGroupBox(self);
        mainGroup.setFixedWidth(180);
        mainGroup.setTitle("Path Stroking");
    
        capGroup = QGroupBox(mainGroup);
        flatCap = QRadioButton(capGroup);
        squareCap = QRadioButton(capGroup);
        roundCap = QRadioButton(capGroup);
        capGroup.setTitle("Cap Style");
        flatCap.setText("Flat Cap");
        squareCap.setText("Square Cap");
        roundCap.setText("Round Cap");
    
        joinGroup = QGroupBox(mainGroup);
        bevelJoin = QRadioButton(joinGroup);
        miterJoin = QRadioButton(joinGroup);
        roundJoin = QRadioButton(joinGroup);
        joinGroup.setTitle("Join Style");
        bevelJoin.setText("Bevel Join");
        miterJoin.setText("Miter Join");
        roundJoin.setText("Round Join");
    
        styleGroup = QGroupBox(mainGroup);
        solidLine = QRadioButton(styleGroup);
        dashLine = QRadioButton(styleGroup);
        dotLine = QRadioButton(styleGroup);
        dashDotLine = QRadioButton(styleGroup);
        dashDotDotLine = QRadioButton(styleGroup);
        customDashLine = QRadioButton(styleGroup);
        styleGroup.setTitle("Pen Style");

        line_solid = QPixmap(":res/images/line_solid.png");
        solidLine.setIcon(QIcon(line_solid));
        solidLine.setIconSize(line_solid.size());
        line_dashed = QPixmap(":res/images/line_dashed.png");
        dashLine.setIcon(QIcon(line_dashed));
        dashLine.setIconSize(line_dashed.size());
        line_dotted = QPixmap(":res/images/line_dotted.png");
        dotLine.setIcon(QIcon(line_dotted));
        dotLine.setIconSize(line_dotted.size());
        line_dash_dot = QPixmap(":res/images/line_dash_dot.png");
        dashDotLine.setIcon(QIcon(line_dash_dot));
        dashDotLine.setIconSize(line_dash_dot.size());
        line_dash_dot_dot=QPixmap(":res/images/line_dash_dot_dot.png");
        dashDotDotLine.setIcon(QIcon(line_dash_dot_dot));
        dashDotDotLine.setIconSize(line_dash_dot_dot.size());
        customDashLine.setText("Custom Style");
    
        fixedHeight = bevelJoin.sizeHint().height();
        solidLine.setFixedHeight(fixedHeight);
        dashLine.setFixedHeight(fixedHeight);
        dotLine.setFixedHeight(fixedHeight);
        dashDotLine.setFixedHeight(fixedHeight);
        dashDotDotLine.setFixedHeight(fixedHeight);

    
        pathModeGroup = QGroupBox(mainGroup);
        curveMode = QRadioButton(pathModeGroup);
        lineMode = QRadioButton(pathModeGroup);
        pathModeGroup.setTitle("Path composed of");
        curveMode.setText("Curves");
        lineMode.setText("Lines");
    
        penWidthGroup = QGroupBox(mainGroup);
        penWidth = QSlider(Qt.Horizontal, penWidthGroup);
        penWidth.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed);
        penWidthGroup.setTitle("Pen Width");
        penWidth.setRange(0, 500);
    
        animated = QPushButton(mainGroup);
        animated.setText("Animate");
        animated.setCheckable(True);
    
        showSourceButton = QPushButton(mainGroup);
        showSourceButton.setText("Show Source");

        whatsThisButton = QPushButton(mainGroup);
        whatsThisButton.setText("What's This?");
        whatsThisButton.setCheckable(True);
    
        # Layouting
        viewLayout = QHBoxLayout(self);
        viewLayout.addWidget(self.m_renderer);
        viewLayout.addWidget(mainGroup);
    
        mainGroupLayout = QVBoxLayout(mainGroup);
        mainGroupLayout.setMargin(3);
        mainGroupLayout.addWidget(capGroup);
        mainGroupLayout.addWidget(joinGroup);
        mainGroupLayout.addWidget(styleGroup);
        mainGroupLayout.addWidget(penWidthGroup);
        mainGroupLayout.addWidget(pathModeGroup);
        mainGroupLayout.addWidget(animated);
        mainGroupLayout.addStretch(1);
        mainGroupLayout.addWidget(showSourceButton);
        mainGroupLayout.addWidget(whatsThisButton);
    
        capGroupLayout = QVBoxLayout(capGroup);
        capGroupLayout.addWidget(flatCap);
        capGroupLayout.addWidget(squareCap);
        capGroupLayout.addWidget(roundCap);
    
        joinGroupLayout = QVBoxLayout(joinGroup);
        joinGroupLayout.addWidget(bevelJoin);
        joinGroupLayout.addWidget(miterJoin);
        joinGroupLayout.addWidget(roundJoin);
    
        styleGroupLayout = QVBoxLayout(styleGroup);
        styleGroupLayout.addWidget(solidLine);
        styleGroupLayout.addWidget(dashLine);
        styleGroupLayout.addWidget(dotLine);
        styleGroupLayout.addWidget(dashDotLine);
        styleGroupLayout.addWidget(dashDotDotLine);
        styleGroupLayout.addWidget(customDashLine);
    
        pathModeGroupLayout = QVBoxLayout(pathModeGroup);
        pathModeGroupLayout.addWidget(curveMode);
        pathModeGroupLayout.addWidget(lineMode);
    
        penWidthLayout = QVBoxLayout(penWidthGroup);
        penWidthLayout.addWidget(penWidth);
    
        # Set up connections
        QObject.connect(penWidth, SIGNAL("valueChanged(int)"),self.m_renderer.setPenWidth);
    
        QObject.connect(flatCap, SIGNAL("clicked()"),self.m_renderer.setFlatCap);
        QObject.connect(squareCap, SIGNAL("clicked()"),self.m_renderer.setSquareCap);
        QObject.connect(roundCap, SIGNAL("clicked()"),self.m_renderer.setRoundCap);
    
        QObject.connect(bevelJoin, SIGNAL("clicked()"),self.m_renderer.setBevelJoin);
        QObject.connect(miterJoin, SIGNAL("clicked()"),self.m_renderer.setMiterJoin);
        QObject.connect(roundJoin, SIGNAL("clicked()"),self.m_renderer.setRoundJoin);
    
        QObject.connect(curveMode, SIGNAL("clicked()"),self.m_renderer.setCurveMode);
        QObject.connect(lineMode, SIGNAL("clicked()"),self.m_renderer.setLineMode);
    
        QObject.connect(solidLine, SIGNAL("clicked()"),self.m_renderer.setSolidLine);
        QObject.connect(dashLine, SIGNAL("clicked()"),self.m_renderer.setDashLine);
        QObject.connect(dotLine, SIGNAL("clicked()"),self.m_renderer.setDotLine);
        QObject.connect(dashDotLine, SIGNAL("clicked()"),self.m_renderer.setDashDotLine);
        QObject.connect(dashDotDotLine, SIGNAL("clicked()"),self.m_renderer.setDashDotDotLine);
        QObject.connect(customDashLine, SIGNAL("clicked()"),self.m_renderer.setCustomDashLine);
        
    
        # Set the defaults
        animated.setChecked(True);
        flatCap.setChecked(True);
        bevelJoin.setChecked(True);
        penWidth.setValue(50);
        curveMode.setChecked(True);
        solidLine.setChecked(True);


