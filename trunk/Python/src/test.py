# -*- coding: utf8 -*-
import sys
from Application.App import *

def main(arg):
    app = App.getSingleton()
    app.mainLoop()
    
if __name__ == '__main__':
    # Import Psyco if available
    main(sys.argv)

