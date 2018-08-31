#Python101

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:38:06 2018
@author: Fahmid Morshed
"""

from __future__ import division
import re,traceback

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f

@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1

if __name__== "__main__":
  O.report()





""" 
Page 5:
A simple for multiplication table
that uses the string and int concat, commands and prints
"""
@O.k
def page5_multiChart():
    myListOfList = [[1,2],                            #using list of list for practice
                [3,4]]
    print ("Multiplication Table\n\n")
    for k in [0,1]:
        for i in myListOfList[k]:
            print ("Multiplication table for " + str(i) + "\n")                             #Start of multiplication, testing line break
        
            for j in [1,2,3,4,5]:
                print (str(i) + "*" +\
                str(j) + "=" + str(i*j))                          #The chart
            print ("\n")
    assert 1==1
    return

"""
Page 6:
Testing import and numpy library
Used google for assistance
"""
def matchThis(myPattern, stringToMatch):
    
    pattern = re.compile(myPattern, re.IGNORECASE)
    if re.match(pattern, stringToMatch) is not None:
        return True
    return False

@O.k
def page6_match():
    """match a string with a given pattern using the re library that uses another function
    testing on pattern 'abc*' and string 'b'"""
    assert False == matchThis('abc*', 'b')



"""
Page 7:
Arithmatic example. The from __future__ has been used at the
beginning of the file.
"""
divInt = lambda x,y: x//y
divFloat = lambda x,y: x/y
def addFive(x=0):
    """adds 5 to a given number. if the number is not given, it returns 5"""
    return x+5
@O.k
def page7_divideAndAddTest():
    """testing 2 lambda function, 1 regular function and __future__ for arithmatic"""
    assert 2.5 == divFloat(15,6)
    assert 2 == divInt(15,6)
    assert 8 == addFive(3)
    return



"""
Page 8:
Function and lambda
"""

def decideALeapYear(year=2000):
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
@O.k
def page8_leapYearTest():
    """Function use. A leapyear test. default argument is 2000. Also testing on 2001 and 2002"""
    assert True == decideALeapYear()
    assert False == decideALeapYear(2001)
    assert False == decideALeapYear(2002)
    return



"""
Page 9:
Strings
"""
def printCol(col1, col2, col3):
    print (col1 + "\t" + col2 + "\t" + col3)
    return

@O.k
def page9_printChart():
    """String and formatting test. prints a row of a chart. Also testing raw string on assert'"""
    printCol("APPLE", "CHAIR", "DISK")
    printCol("MANGO", "TABLE", "RAM")
    printCol("PEACH", "POT", "CPU")
    assert 7==len(r"HELLO\t")


"""
Page 10:
Exception
"""
@O.k
def page10_exception():
    """Exception handling with try. A simple division function was used"""
    def simpleDivision(x,y):
        try:
            return x/y
        except ZeroDivisionError:
            return "Divided by zero exception"

    assert 2 == simpleDivision(10,5)
    assert "Divided by zero exception" == simpleDivision(10,0)
    return


"""
Page 11 and 12:
Lists
"""
@O.k
def page11_12_list():
    """Testing 7 different operations on 3 different kinds of lists"""
    anIntList = range(5,10)
    aFloatList = [2.5, 2.6]
    aFloatList.extend([1.6])
    aMixedList = [anIntList, aFloatList, "Fahmid", True, 1, 2, 3]
    assert sum(anIntList) == (5+6+7+8+9)
    assert len(aFloatList) == 3
    assert aMixedList[2:] == ["Fahmid", True, 1, 2, 3]
    assert aMixedList[-7][3] == 8
    assert (2.5 in aFloatList) == True
    return


"""
Page 13
Tuples
"""
@O.k
def page13_compare3num():
    """Compare 3 numbers and return them in tuples. 
    Also try to change a tuple and catch the exception"""
    def compareABC(a, b, c):
        if(a>b):
            if(a>c):
                if(b>c):
                    return (a,b,c)
                else:
                    return (a, c, b)
            else:
                return (c, a, b)
        else:
            if(b>c):
                 if(a>c):
                     return (b, a, c)
                 else:
                     return (b, c, a)
            else:
                return (c, b, a)
    
    assert (3, 2, 1) == compareABC(1, 2, 3)  
    assert (3, 2, 1) == compareABC(1, 3, 2) 
              
    myTuple = (1,2)
    def changeTuple():
        try:
            myTuple[1] = 3
            return "Changed"
        except TypeError:
            return "Not Possible"
    assert "Not Possible" ==  changeTuple()



"""
Page 14
Dictonary
"""
@O.k
def page14_gradebook():
    """Dictonary. Testing a simple dictonary for csc791"""
    csc791 = {
            "courseNumber" : 791,
            "courseName" : "CSC791",
            "credit" : 3,
            "instructor" : "Menzies",
            "semister" : "Fall 2018",
            "prerequisits" : [310, 411, 120]
    }
    
    
    csc791Keys = csc791.keys()
    csc791Values = csc791.values()
    
    assert 6==len(csc791)
    assert ("courseName" in csc791) == True
    assert ("Menzies" in csc791Values) == True
    
    for i in csc791Keys:
        print (i + " : "+ str(csc791[i]))
    
    assert 3==(csc791.get("credit", 0))
    return



"""
Page 15
Defaultdic
"""

@O.k
def page15_countGrades():
    """Using defaultdict to count a semester grades"""
    from collections import defaultdict
    
    myMarks = ["A", "A", "B", "A", "C", "B", "D"]
    myCount = defaultdict(int)
    
    for grade in myMarks:
        myCount[grade] += 1
        
    print (myCount)
    assert myCount["A"] == 3
    assert myCount["B"] == 2
    return

"""
Page 16
Counter
"""
@O.k
def page16_counter():
    """Testing counter. A line is split into tokens and used a counter on that"""
    from collections import Counter
    myLine = "I am a boy I have a toy I feel happy when I play with boy joy"
    tokens = myLine.split(" ")
    print (tokens)
    wordCounts = Counter(tokens)
    for word, count in wordCounts.most_common(3):
        print (word, count)
    assert 4==wordCounts.get("I",0)


"""
Page 17
Sets
"""

@O.k
def page17_set():
    """Set. testing a meeting schedule and my busy days using set"""
    myMeetingDates = [1, 15, 2, 5, 5, 9, 11, 18, 22, 17, 15, 18, 22, 27]
    myMeetingDatesSet = set(myMeetingDates)
    numOfDaysIAmBusy = len(myMeetingDatesSet)
    print ("I am busy on:")
    print (myMeetingDatesSet)
    print ("I am busy for " + str(numOfDaysIAmBusy) + " days in this month")
    assert (18 in myMeetingDatesSet) == True
    assert not (30 in myMeetingDatesSet) == True


"""
Page 18
Control Flow
"""

@O.k
def page18_printPrime():
    """Control Flow. A prime printer using while and for loop and boolean logics"""
    def isPrime(num):
        if(num==1 or num==2 or num==3):
            print (num)
            return
        elif (num%2==0):
            return
        else:
            i = 3
            while i < num:
                if(num%i==0):
                    return
                else:
                    i += 2
            print (num)
            return
    
    for j in range(10):
        isPrime(j)
    assert 1==1

"""
Page 19 and 20
Trutiness
"""

@O.k
def page19_20_testTruthiness():
    """Testing some truthiness of some complex structure"""
    assert True == all([{1}, 3, True, "Hi"])
    assert True == any([{}, False, 0, 1])
    assert True == any([0, {}, False, ""]) or any([1])
    assert False == all([1, 2.5, "", True]) or all("hi")
    return

"""
Page 22
Sorting
"""
@O.k
def page22_sortWords():
    """sort a collection on words after filtered using set. 
    First sort was based on word length. 2nd one was just a regular sort"""
    myStr = "I have a dog that looks like a cat and a cat that looks like a fish"
    myWords = myStr.split(" ")
    myWords = set(myWords)
    
    sortedWords = sorted(myWords, key=len, reverse=False)
    print (sortedWords)
    sortedWords2 = sorted(myWords)
    print (len(sortedWords2))
    assert 1==1

"""
Page 23
List Comparisions
"""

@O.k
def page23_listComparisions():
    """Two lists and comparing them with one another. Another odd number lists just to check"""
    
    list1 = [(x1,y1)
                        for x1 in range(0, 10)
                        for y1 in range(x1+5, 20)]
    list2 = [(x2,y2)
                for x2 in range(3, 13)
                for y2 in range(x2+1, 15)]
    listOfOdds = [x for x in range(1,10) if x%2!=0]
    print(listOfOdds)
    print(len(list1))
    print(len(list2))
    assert not list1==list2
    
    
"""
Page 24
Generators and Iterators
"""
@O.k
def page24_generatorLoops():
    """Creating random loops to see how generator and iterator works"""
    def giveNextEvenLazy(n):
        i=1
        while i<n:
            yield i
            i+=2
    list1 = []

    for i in giveNextEvenLazy(10):
        list1.append(i)
        
    list2 = [x for x in range (1, 10) if x%2!=0]
    print (list2)
    assert list1==list2    

"""
Page 25
Randomness
"""
    
@O.k
def page25_random():
    """Card picking using random. 
    Used time as a seed to reflect true randomness.
    First suffled, then split in two, then picked 2 cards from the 1st portion"""
    import random
   
    from datetime import datetime
    random.seed(datetime.now())
   
    deck = [(num, suit)
           for num in range(1,14)
           for suit in ["S" , "H", "D", "C"]]
    
    random.shuffle(deck)
    
    numOfCardsInSplit = random.randrange(1,52)
    
    partialDeck = random.sample(deck, numOfCardsInSplit)
    
    print ("You have " + str(len(partialDeck)) + " cards in your first split.")
    
    
    myPick1 = random.choice(partialDeck)
    deck.remove(myPick1)
   
    print("Your 1st Pick: " + str(myPick1))
    print("Card left: " + str(len(deck)))
    assert 51==len(deck)
   
    myPick2 = random.choice(deck)
    deck.remove(myPick2)
   
    print("Your 2nd Pick: " + str(myPick2))
    print("Card left: " + str(len(deck)))
    assert 50==len(deck)
   

"""
Page 26
Regular Expression
"""

@O.k
def page26_testATimeString():
    """Regular Expression. A very basic date recognizer. 
    It has some flaws, but for just testing purpose, it will work."""
    def isADate(myDate):
        if (re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', myDate) is not None):
            myMonth = myDate[0:2]
            myDay = myDate[3:5]
            myYear = myDate[6:]
            if (int(myMonth) > 12): return False
            if (int(myDay) > 31): return False
            return True
        else:
            return False
    print ("10.10.2018 is a valid date")
    assert True == isADate("10.10.2018")
    print ("Asbbasks is NOT")
    assert False == isADate("Asbbasks")
    print ("15/21/2018 is NOT")
    assert False == isADate("15/21/2018")
    
    
"""
Page 27
Classes
"""    

@O.k
def page27_CourseClass():
    """Just a simple course class to demonstrate the oop. Understanding self and init and repr."""
    class Course:
        def __init__(self, courseName, courseNumber):
            if(courseName==None or courseName==""): raise ValueError("Must have a course name and number")
            if(courseNumber==None or courseNumber==""): raise ValueError("Must have a course name and number")
            
            self.courseName = courseName
            self.courseNumber = courseNumber
            self.instructor = {}
            
        def __repr__(self):
            return "Course Number: " + str(self.courseNumber) +\
                "\nCourse Name: " + self.courseName + "\nInstructor: " + str(self.instructor.keys())
        def editName(self, newName):
            self.courseName = newName
        def addInstructor(self, newInstructor):
            self.instructor[newInstructor] = True
        def removeInstructor(self, instructor):
            del self.instructor[instructor]
            
    
    myCourse = Course("CSC FSS", 791)
    myCourse.addInstructor("Menzies")
    myCourse.addInstructor("Krishna")
    print (myCourse)
    assert 1==1
    

"""
Page 28
Functional Tool
"""

@O.k
def page28_basicMath():
    """Checking basic functools and how it works"""
    from functools import partial
    
    def someWiredFunction(x, y, z):
        return (x+y)**z
    makeZ2 = partial(someWiredFunction, z=2)
    
    assert (someWiredFunction(1,3,2))==(makeZ2(1,3))
    
    
"""
Page 29
Functional Tool, Maps, Reduce 
"""   
@O.k    
def page29_MapsReduceFilter():
    """Checking functools and map, reduce and filter"""
    from functools import partial
    from functools import reduce
    
    evenList = [x for x in range(7) if (x%2==0 and x>0)] #just trying and
    print (evenList)
    
    def powerMe(x, y):
        return x ** y
    power2 = partial(powerMe, y=2)
    
    evenSqrList1 = [power2(x) for x in evenList]
    evenSqrList2 = list(map(power2, evenList))
    
    assert evenSqrList1 == evenSqrList2
    print(evenSqrList1)
    
    continousSqr = reduce(powerMe, evenList)
    print (continousSqr)
    assert ((2**4)**6)==continousSqr
    
    
"""
Page 30
Enumerate
"""
@O.k
def page30_enumerate():
    """Enumerating through a list of words"""
    aSimpleStr = "My name is khan. I eat paan. Not a fan of peter pan."
    aSimpleStr = aSimpleStr.replace(".", "")
    aSimpleStr = aSimpleStr.split(" ")
    print(aSimpleStr)
    for i, word in enumerate(aSimpleStr):
        print(str(i) + ":" + word, end=" ")
    
    assert len(aSimpleStr)==13
    

"""
Page 31
Zip & Arg
"""
@O.k
def page31_zipArg():
    """Testing zip and unzip"""
    list1 = [1, 2, 3, 4]
    list2 = ['Me', 'Ma', 'Mo']
    list3 = {"a", True, "Hi"}
    combinedZip = list(zip(list1, list2, list3))
    print (combinedZip)
    
    list1Unzip, list2Unzip, list3Unzip = zip(*combinedZip)
    print (list(list1Unzip))
    assert list1!=list(list1Unzip)
    print (list(list2Unzip))
    assert list2 == list(list2Unzip)
    print (list(list3Unzip))
    assert list3 == set(list3Unzip)
    
    
"""
Page 32
Args & Kwargs
"""
@O.k
def page32_argsKwargs():
    """testing a args and kwargs for higher dimention function"""
    def sqrIt(f):
        def g(*args, **kwargs):
            return f(*args, **kwargs)**2
        return g
    
    
    def increaseAndMulti(x, y):
        return (x + 1) * y
    
    g = sqrIt(increaseAndMulti)
    print (g(2,4))
    assert (((2+1)*4)**2) == g(2,4)
    




