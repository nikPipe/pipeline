from collections import OrderedDict
from pipeline.widget.sample import mayaWindow
from pipeline.widget.sample import mainWindow
from pipeline.widget.sample import sample_widget_template
for each in [mayaWindow, mainWindow, sample_widget_template]:
    reload(each)


sample_widget_template = sample_widget_template.SAMPLE_WIDGET_TEMPLATE()


class CFXWINDOW:
    def __init__(self):
        self.window_name = 'CFX'
        self.width = 500
        self.height = 800


    def cfx_window_(self):
        #MAINWINDOW
        window = mainWindow.SAMPLE_QMainWindow()

        #CREATE MENU DIC
        menuDic = OrderedDict([

        ])
        self.mayaWindow_ = mayaWindow.mayaWindow_sample(window=window, title=self.window_name, menubarDic=menuDic,
                                                        width=self.width, height=self.height)
        self.mayaWindow_.setCentralWidget(self.widget_def(window=self.mayaWindow_))

        self.mayaWindow_.show(dockable=True)

    def widget_def(self, window):
        '''

        :return:
        '''
        widget = sample_widget_template.widget_def()

        self.create_cfxSetup_widget()


        return widget

    def create_cfxSetup_widget(self):
        '''

        :return:
        '''
        name_label = sample_widget_template.label(set_text='Name')
        name_lineedit = sample_widget_template.line_edit(set_PlaceholderText='specify the object')
        pushButton = sample_widget_template.pushButton(set_text='Create CFX Setup')

        widget = sample_widget_template.grid_layout_set(list_object=[[name_label, name_lineedit], pushButton])

        print(widget)







def cfx_window():
    cfx = CFXWINDOW()
    cfx.cfx_window_()


'''
from pipeline.script.CFX.Maya import cfxWindow
cfxWindow.cfx_window()
'''