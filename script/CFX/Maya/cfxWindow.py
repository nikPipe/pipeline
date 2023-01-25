
from collections import OrderedDict


from pipeline.widget.sample import mayaWindow
from pipeline.widget.sample import mainWindow
for each in [mayaWindow, mainWindow]:
    reload(each)





def cfx_window():
    window = mainWindow.SAMPLE_QMainWindow()

    fileName = 'File'
    #window.createAct(name='New', shortcut='Ctrl+N', toolTip='Create New Scene', callback=self.on_file_new))
    editName = 'Edit'
    helpName = 'Help'

    dic_val = OrderedDict([
        (fileName, {}),
        (editName, {}),
        (helpName, {}),
        ])


    val = mayaWindow.mayaWindow_sample(window = window, title='CFX', menubarDic=dic_val)
    val.show()


'''
from pipeline.script.CFX.Maya import cfxWindow
cfxWindow.cfx_window()

'''