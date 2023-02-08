
from pipeline.import_module import *
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin
import tempfile
from pipeline.widget.sample import mainWindow
try:
    from importlib import reload
except:
    pass

for each in [mainWindow]:
    reload(each)


class mayaWindow_sample(MayaQWidgetDockableMixin, QMainWindow):
    def __init__(self, title='SampleWindow', menubarDic={}, statusBar='', widget='',
                 x=0, y=0, width=10, height=10):
        super(mayaWindow_sample, self).__init__()


        #SET WINDOW TITLE
        self.setWindowTitle(title)

        #SET WINDOW WIDGET
        if widget != '':
            self.setCentralWidget(widget)


        self.setGeometry(x, y, width, height)


        #SET STATUS BAR
        self.statusBar().showMessage(statusBar)

        #UPDATE
        self.update()


    def update(self):
        '''

        :return:
        '''
        self.setUserData()



    def setUserData(self):
        '''

        :return:
        '''
        tempDir = tempfile.gettempdir()
        print(tempDir)














