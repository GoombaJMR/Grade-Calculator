def defineWeights(categories, weights):
  for gradeType in range(len(weights)) and range(len(categories)):
    print categories[gradeType] + " weighting"
    weights[gradeType] = float(raw_input("Enter weight (0-1): "))
  return weights

def findQuiz(weights):
  quizTotal = 0
  qui = int(raw_input("# of Quizzes: "))
  for quizNumber in range(qui):
    print "Enter score for quiz " + str(quizNumber+1) + ": "
    quizTotal += float(raw_input("Score: "))
  av = quizTotal/qui
  print "Quiz Average: " + str(av)
  return (av * weights[0])

def findMid(weights):
  midTotal = av = 0
  mid = int(raw_input("# of Midterms: "))
  for midtermNumber in range(mid):
    print "Enter score for midterm " + str(midtermNumber+1) + ": "
    midTotal += float(raw_input("Score: "))
  av = midTotal/mid
  print "Midterm Average: " + str(av)
  return (av * weights[1])
  
def findTest(weights):
  testTotal = av = 0
  tes = int(raw_input("# of Finals: "))
  for testNumber in range(tes):
    print "Enter score for final " + str(testNumber+1) + ": "
    testTotal += float(raw_input("Score: "))
  av = testTotal/tes
  print "Test Average: " + str(av)
  return (av * weights[2])

def calcAvg(quizAverage, midtermAverage, testAverage):
  finalScore = (quizAverage) + (midtermAverage) + (testAverage)
  return finalScore

def startCalculate():
  weights = [0, 0, 0]
  categories = ["Quiz", "Midterm", "Final"]
  quizTotal = midTotal = testTotal = final = 0
  weights = defineWeights(categories, weights)

  print weights

  quizTotal = findQuiz(weights)
  midTotal = findMid(weights)
  testTotal = findTest(weights)
  final = calcAvg(quizTotal, midTotal, testTotal)
  print "Your final score is " + str(final)

def main(): 
  print "--WELCOME TO THE GRADE CALCULATOR--"
  print "----JULIAN M RICE----------2018----"
  startCalculate()

main()
