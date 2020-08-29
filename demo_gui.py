import sys
import random
from PyQt5 import QtWidgets,uic

Click_Count = 0

## ----------------------------------------------------------------------------
## Quit
##   
## Purpose:
##   Quits the application
##
## ----------------------------------------------------------------------------
def Quit():
    App.quit()

## ----------------------------------------------------------------------------
## Handle Click
##   
## Purpose:
##   Process the click event.  Increment the persistant click counter
##   and set the background of the label to a random color
##
## ----------------------------------------------------------------------------
def Handle_Click():
    global Click_Count
    Click_Count = Click_Count + 1

    BG_Color = "rgb(" + str(random.randint(0,255)) + "," + str(random.randint(0,255)) + "," + str(random.randint(0,255)) + ");"
    FG_Color = "rgb(255,255,255);"
    Grade = UI.UserGrade.value()
    UI.lblOutput.setText("Clicked " + str(Click_Count) + " times"+ str(Grade))
    print(str(Grade))
    UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")

## ----------------------------------------------------------------------------
## demo_gui
##   
## Purpose:
##   Provide a sample progarm to demonstrate basic Python and Qt interaction
##
## ----------------------------------------------------------------------------
App = QtWidgets.QApplication([])
UI=uic.loadUi("grade_calculator_gui.ui")

UI.btnCalculate.clicked.connect(Handle_Click)
UI.actionCalculate.triggered.connect(Handle_Click)
UI.actionQuit.triggered.connect(Quit)

UI.show()
sys.exit(App.exec_())