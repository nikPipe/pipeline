
from pipeline.import_module import *
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

from pipeline.widget.sample import mainWindow
try:
    from importlib import reload
except:
    pass

for each in [mainWindow]:
    reload(each)


class mayaWindow_sample(MayaQWidgetDockableMixin, QMainWindow):
    def __init__(self, window, title='SampleWindow', menubarDic={}):
        super(mayaWindow_sample, self).__init__()

        self.setWindowTitle(title)
        self.window_ = window
        self.window_.menuBar(self, menuBarDic=menubarDic)






