from pipeline.import_module import *



class SAMPLE_QMainWindow():
    def widget_name(self):
        '''

        :return:
        '''
        print('widget is gong to create')


    def menuBar(self, window, menuBarDic={}):
        '''

        :return:
        '''
        menubar = window.menuBar()
        for each in menuBarDic:
            menu = menubar.addMenu(each)


        '''
        filemenu = menubar.addMenu('File')
        filemenu.addAction(QAction('something', window))
        menubar.addMenu('Edit')
        '''

    def createAct(self, name, shortcut, toolTip, callback):
        '''

        :param name:
        :param shortcut:
        :param toolTip:
        :param callback:
        :return:
        '''
        act = QAction(name, self)
        act.setShortcut(shortcut)
        act.setToolTip(toolTip)
        act.triggered.connect(callback)
        return act


    def createMenu(self, name):
        '''

        :param name:
        :return:
        '''
        menuDic = {}
        menuDic[name] = {}


        return menuDic





