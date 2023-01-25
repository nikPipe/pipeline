
from collections import OrderedDict


from pipeline.widget.sample import mayaWindow
from pipeline.widget.sample import mainWindow
for each in [mayaWindow, mainWindow]:
    reload(each)


def cfx_window():
    window = mainWindow.SAMPLE_QMainWindow()
    dic_val = OrderedDict([])
    mayaWindow_ = mayaWindow.mayaWindow_sample(window = window, title='CFX', menubarDic=dic_val)
    mayaWindow_.show()

def widget_def():
    '''

    :return:
    '''

    pass


'''
from pipeline.script.CFX.Maya import cfxWindow
cfxWindow.cfx_window()
'''