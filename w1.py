#Python101

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 12:38:06 2018
@author: Fahid
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
    print (sortedWords2)
    assert 1==1

"""
Page 23
List Comparisions
"""

@O.k
def page23_listComparisions():
    pointsOfALine = [(x,y)
                        for x in range(0, 10)
                        for y in range(x+5, 20)]
    print (pointsOfALine)
#TODO
def myGcd(a=1, b=1):
    """calcualte the greatest common divisor"""
    if(b>0):
        x = (a%b)
        return myGcd(b, x)
    else:
        return a    

