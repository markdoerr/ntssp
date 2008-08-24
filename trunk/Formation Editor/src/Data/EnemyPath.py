class EffectType:
    Circle = 0;
    Switch = 1;
    Rotate = 2;
    Arc = 3;
    Zero = 4;

class EnemyPath:
    def __init__(self,effect = EffectType.Zero):
        self.effect = effect;

class CirclePath(EnemyPath):
    def __init__(self):
        return;

class SwitchPath(EnemyPath):
    def __init__(self):
        return;

class RotatePath(EnemyPath):
    def __init__(self):
        return;
    
class ArcPath(EnemyPath):
    def __init__(self):
        return;