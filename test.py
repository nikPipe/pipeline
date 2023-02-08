from main import *

print('this is working now')
import sys
import subprocess



import inspect

class MyClass(object):
    a = '12'
    b = '34'
    def myfunc(self):
        return self.a

    def value_no(self, something=[1, 2, 3,], one='assets', two={'one':'one'}):
        '''

        :param something:
        :param one:
        :param two:
        :return:
        '''
        print('sssss')

'''
from datetime import datetime
start_time = datetime.now()
while True:
    current_time = datetime.now()
    if current_time != start_time:
        diff = current_time - start_time

        if diff.seconds > 60:
            print(diff)
            print(current_time)
            print(start_time)
            start_time = current_time

'''
import inspect
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton

import inspect

def get_params_info(obj):
    methods = [
        method for method in dir(obj)
        if callable(getattr(obj, method))
    ]
    for method in methods:
        func = getattr(obj, method)
        sig = inspect.signature(func)
        print(f"Method: {method}")
        print(f"Params: {sig}")

# Example usage
layout = QVBoxLayout()
get_params_info(layout)


'''
from import_module import *
val = inspect.getmembers(MyClass, lambda a:not(inspect.isroutine(a)))
one = inspect.getfullargspec(MyClass.value_no)
Foo = QVBoxLayout
method_list = [func for func in dir(Foo) if callable(getattr(Foo, func))]
dir_val = dir(Foo)
for each in method_list:
    one = inspect.getfullargspec(Foo.each)
'''

'''
from PyQt5.QtWidgets import (QTreeWidget, QTreeWidgetItem, QPushButton, QLabel, QDialog, QVBoxLayout, QApplication, QLineEdit)
from PyQt5.QtCore import pyqtSlot
import sys
class TreeWidgetWithWidgetItems(QDialog):
    def __init__(self):
        super(TreeWidgetWithWidgetItems, self).__init__()
        self.init_ui()
    def init_ui(self):
        # Creating the required widgets
        self.vboxLayout = QVBoxLayout()
        self.treeWidget = QTreeWidget()
        self.label = QLabel("I'm going to inform you about the buttons")
        # Adding the widgets
        self.vboxLayout.addWidget(self.treeWidget)
        self.vboxLayout.addWidget(self.label)
        self.treeWidget.setHeaderLabel("TreeWidget with Buttons")
        self.topLevelItem = QTreeWidgetItem()
        # Creating top level and child widgets
        self.topLevelButton = QPushButton("Top Level Button")
        self.childButton_1 = QPushButton("Child 1")
        self.childButton_2 = QPushButton("Child 2")
        self.childButton_3 = QPushButton("Child 3")
        self.childLineEdit = QLineEdit()
        self.childLineEdit.setPlaceholderText("Add Text Here")


        # Adding the child to the top level item
        self.childItems = []
        for i in range(4):
            self.childItems.append(QTreeWidgetItem())
            self.topLevelItem.addChild(self.childItems[i])
        self.treeWidget.addTopLevelItem(self.topLevelItem)
        self.treeWidget.setItemWidget(self.topLevelItem, 0, self.topLevelButton)
        # Replacing the child items with widgets
        self.treeWidget.setItemWidget(self.childItems[0], 0, self.childButton_1)
        self.treeWidget.setItemWidget(self.childItems[1], 0, self.childButton_2)
        self.treeWidget.setItemWidget(self.childItems[2], 0, self.childButton_3)
        self.treeWidget.setItemWidget(self.childItems[3], 0, self.childLineEdit)
        # Connecting the widgets with corresponding slots
        self.topLevelButton.clicked.connect(self.top_button_clicked)
        self.childButton_1.clicked.connect(self.child_button_1_clicked)
        self.childButton_2.clicked.connect(self.child_button_2_clicked)
        self.childButton_3.clicked.connect(self.child_button_3_clicked)
        self.childLineEdit.textEdited.connect(self.child_lineedit_edited)
        # Setting the layout
        self.setWindowTitle("QTreeWidget with Button Example")
        self.setLayout(self.vboxLayout)


    @pyqtSlot(bool)
    def top_button_clicked(self, clicked):
        self.label.setText("Top Level Button was Clicked")
    @pyqtSlot(bool)
    def child_button_1_clicked(self, clicked):
        self.label.setText("Child button 1 was clicked")
    @pyqtSlot(bool)
    def child_button_2_clicked(self, clicked):
        self.label.setText("Child button 2 was clicked")
    @pyqtSlot(bool)
    def child_button_3_clicked(self, clicked):
        self.label.setText("Child button 3 was clicked")
    @pyqtSlot('QString')
    def child_lineedit_edited(self, edited_text):
        self.label.setText(str(edited_text))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    treeWidgetDialog = TreeWidgetWithWidgetItems()
    treeWidgetDialog.show()
    sys.exit(app.exec_())
'''
'''
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
import sys

def main(): 
    app     = QtWidgets.QApplication(sys.argv)
    tree    = QtWidgets.QTreeWidget()
    headerItem  = QtWidgets.QTreeWidgetItem()
    item    = QtWidgets.QTreeWidgetItem()

    for i in range(3):
        parent = QtWidgets.QTreeWidgetItem(tree)
        parent.setText(0, "Parent {}".format(i))
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        for x in range(5):
            child = QtWidgets.QTreeWidgetItem(parent)
            child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
            child.setText(0, "Child {}".format(x))
            child.setCheckState(0, Qt.Unchecked)
    tree.show() 
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

'''