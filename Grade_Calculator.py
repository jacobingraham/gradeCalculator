import sys
import random
from PyQt5 import QtWidgets,uic
assignments = ["Homework", "Project Assignments", "Exam 1", "Midterm", "Exam 2", "Final Project"]
grades = [0,0,0,0,0,0,0]

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
    FG_Color = "rgb(255,255,255);"
    UI.btnCalculate.setText("Enter")
    if Click_Count == 0:
        UI.lblOutput.setText("Please Enter Grade for: " + assignments[Click_Count])
    if Click_Count < len(assignments) and Click_Count != 0:
        UI.lblOutput.setText("Please Enter Grade for: " + assignments[Click_Count])
    
    
    
    if Click_Count< len(grades):
        grades[Click_Count] = UI.UserGrade.value()


    if Click_Count >= len(assignments):
       finalGrade = grades[1]*.3 +grades[2]*.1 +grades[3]*.15 +grades[4]*.1 +grades[5]*.15 +grades[6]*.2 
       
       if finalGrade >=89.5:
           letter = "A"
           BG_Color = "rgb(51,255,51);"
           UI.lblOutput.setText("Your Final Grade is: "  +letter + " " +str(finalGrade))
           UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")
      
       elif finalGrade >=79.5:
           letter = "B"
           BG_Color = "rgb(51,51,255);"
           UI.lblOutput.setText("Your Final Grade is: "  +letter + " " +str(finalGrade))
           UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")

       
       elif finalGrade >=69.5:
           letter = "C"
           BG_Color = "rgb(255,255,51);"
           UI.lblOutput.setText("Your Final Grade is: "  +letter + " " +str(finalGrade))
           UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")

       elif finalGrade >=59.5:
           letter = "D"
           BG_Color = "rgb(255,153,51);"
           UI.lblOutput.setText("Your Final Grade is: "  +letter + " " +str(finalGrade))
           UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")
           
       else:
           letter = "F"
           BG_Color = "rgb(255,51,51);"
           UI.lblOutput.setText("Your Final Grade is: "  +letter + " " +str(finalGrade))
           UI.lblOutput.setStyleSheet("QLabel {background-color :" + BG_Color + "color : " + FG_Color + "}")







    Click_Count = Click_Count + 1
    

## ----------------------------------------------------------------------------
## demo_gui
##   
## Purpose:
##   Provide a sample progarm to demonstrate basic Python and Qt interaction
##
## ----------------------------------------------------------------------------
App = QtWidgets.QApplication([])
UI=uic.loadUi("grade_calculator_gui.ui")
UI.btnCalculate.setText("Begin")
UI.btnCalculate.clicked.connect(Handle_Click)
UI.actionCalculate.triggered.connect(Handle_Click)
UI.actionQuit.triggered.connect(Quit)

UI.show()
sys.exit(App.exec_())