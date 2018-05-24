#!/usr/bin/python

###---------GRADING CALCULATOR FINAL VERSION---------###
###------------------JULIAN M RICE-------------------###
###---------------------MAY 2018---------------------###

#FUNCTION DEFINITIONS---------------------------
def greetings():
  print "--WELCOME TO THE GRADE CALCULATOR v2--"
  print "----JULIAN M RICE-------------2018----"

def createLists(weights, categories):
  "This function creates the grading category names & weights"
  num = int(raw_input("How many grading categories? "))
  for index in range(num):
    weights.append(0)
    categories.append("")
    categories[index] = raw_input("Enter grading category name: ")
    weights[index] = float(raw_input("Enter " + categories[index].upper() + " weighting scale (0-1)"))

def enterGrading(weightNum, categoryNum): 
  "This core functions finds the total amount of grades in a category and finds the average for it"
  gradeTotal = av = 0
  gradeCount = int(raw_input("Enter total "+ categoryNum.upper() + " count: "))
  for gradeNumber in range(gradeCount):
    gradeTotal += float(raw_input(categoryNum.upper() + " score " + str((gradeNumber+1)) + ": "))
  av = gradeTotal/gradeCount
  print categoryNum.upper() + " average: " + str(av)
  return (av * weightNum)

def startCalculate():
  "This is the main flow function"
  index = 0
  weights = []
  categories = []
  grades = []
  createLists(weights, categories)
  for cat in range(len(categories)):
    grades.append(0)
    grades[index] = enterGrading(weights[cat], categories[cat])
    index += 1
  final = sum(grades)
  print "Your final score is " + str(final)

#MAIN FUNCTION---------------------------
def main(): 
  greetings()
  startCalculate()

#STARTING POINT---------------------------
main()
