print('Run Python Programs')
print('Adam')
print('The lyrics of a song \n')

print('Variables')
print(5,3,87)
print(64+32)
sixtyfour=64
thirtytwo=32
print(sixtyfour+thirtytwo)

print('\nStrings')
lucky = 'The word "lucky"'
print(lucky[10:15])
print('The date is %d/%d/%d' % (3, 15, 2021))

print('\nString Replace')
replace='the text to replace'
replacedText = replace.replace('replace','bananas')
print(replacedText)
replacedReplacedText = replacedText.replace('bananas','oranges')
print(replacedReplacedText)
#Yes, a string can be replaced twice
replacedPhrases=replacedText.replace('text to','fruit is')
print(replacedPhrases)
#Replace works on both words and phrases

print('\nString Find')
#String find is not case sensitive
findString = 'find the word you want to find'
index = findString.find('find')
print(index)
#find only finds the first query
inputFindString = input('What word would you like to find?')
inputIndex = findString.find(inputFindString)
print(inputIndex)

print("\nString join")
joinWord1 = 'time'
joinWord2 = 'to join'
joinWord3 = 'strings'
print(f'{joinWord1} {joinWord2} {joinWord3}')
print(f'{joinWord1}_{joinWord2}_{joinWord3}')

print("\nString split")
splitString = "time to stop construction"
print(splitString.split("to"))
#Yes a string can be split on multiple characters
geography = "World,Earth,America,Canada"
print(geography.split(","))
#You can split an article based on phrases, the string in .split can be (theoretically) infinitely long


print("\nRandom numbers")
import random as r
x = r.randrange(0,10)
print(x)
print(r.randrange(0, 10))
print(r.randrange(0, 10))
print(r.randrange(0, 10))
randomList = []
for a in range(100):
  randomList.append(r.randint(0,10))
def countNum(list, x): 
    count = 0
    for element in list: 
        if (element == x): 
            count = count + 1
    return count 
for x in range(10):
  print('{} has occurred {} times'.format(x, countNum(randomList, x))) 

print("\nKeyboard input")
phoneNumber = input("Please enter your phone number: ")
progLanguage = input("What is your preferred programming language?: ")


print("\nIf statements")
ifInput = int(input("Enter an integer between 1-10:"))
if 1 <= ifInput <= 10:
  print("That's a valid number :)")
else:
  print("That's an invalid number :(")

password = input("Please enter your password:")
if password == "password":
  print("correct! Please come in!")
else:
  print("incorrect! Go away now")

print("\nFor loops")
clist = ['Canada','USA','Mexico','Australia']
print("Question 1")
for n in clist:
  print(n)
print("Question 2")
for i in range(100):
  print(i)
print("Question 3")
for x in range(12): 
  for y in range(12):
    print((x +1)*(y+1), end='')
    print(" ",end='')
  print()
print("Question 4")
for i in reversed(range(11)):
  print(i)
print("Question 5")
for i in range(10):
  if (i % 2 == 0):
    print(i)
print("Question 6")
sumHundred = 0
for i in range(100):
  sumHundred += (i+100)
print(sumHundred)
print("\nWhile loops")
clist = ["Canada","USA","Mexico"]
print("Question 1")
i = 0
while i < len(clist):
  print(clist[i])
  i += 1
print("Question 2")
print("While loops will run until a condition becomes false, for loops have a set number of times it will run")
print("Question 3")
print("Yes you can sum numbers in a while loop")
print("Question 4")
print("Yes a for loop can be used inside a while loop")

print("\nFunctions")
print("Question 1")
def sum_list(list):
  total = 0
  for i in range(len(list)):
    total += (list[i])
  print(total)
mylist = [1,2,3,4,5]
sum_list(mylist)
print("Question 2")
print("Yes, functions can be called inside a function")
print("Question 3")
print("Yes, functions can call themselves")
print("Question 4")
print("Variables defined in a function can be used in other functions, but the variables have to be returned")

print("\nLists")
state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
for i in range(len(state_names)):
  print(state_names[i])
print("\nM states:")
for i in range(len(state_names)):
  if state_names[i][0] == 'M':
    print(state_names[i])

print("\nList operations")
y = [6,4,2]
y.extend([12,8,4])
print(y)
y[1] = 3
print(y)

print("\nSorting list")
def sortFirst(elem):
    return elem[0]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=sortFirst)
print(x)
def sortSecond(elem):
    return elem[1]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=sortSecond)
print(x)

print("\nRange function")
thousandList = list(range(0, 1000))
print(min(thousandList))
print(max(thousandList))
oddList = []
evenList = []
for i in range(len(thousandList)):
  if thousandList[i] % 2 == 0:
    evenList.append(thousandList[i])
  else:
    oddList.append(thousandList[i])
print(evenList)
print(oddList)

print("\nDictionary")
countries = {'United States' : 'USA', 'Canada' : 'CAN','Mexico':'MEX'}
for i in countries:
  print(i, countries[i])

print("\nRead file")
#file = open("FILE.txt", "r")
#file.read() 
#If the file doesn't exist, it prints: "error message: file not accessible"
#If you create a file with another user and try to open it, you won't be able to

print("\nWrite file")
#file.write('take it easy')
#Write the line open(“text.txt”) to a file
#file.write("open(“text.txt”)")

print("\nNested loops")
for i in range(3):
  for j in range(3):
    print(i,j)
persons = ["John", "Marissa", "Pete", "Dayton"]
for i in range(len(persons)):
  j = i
  while j < len(persons) -1:
    print(f"{persons[i]} meets {persons[j+1]}") 
    j += 1
print("If a normal for loop finishes in n steps O(n), a nested loop has O(n^2)")

print("\nSlices")
pizzas = ["Hawaii","Pepperoni","Fromaggi","Napolitana","Diavoli"]
print(pizzas[3])
string = "Hello World"
print(string[6:11])

print("\nMultiple return")
def abfunc(a,b):
  sumab = a+b
  return a, b, sumab
print(abfunc(1,3))
def fiveVar(a,b):
  one = a * b
  two = one ^ 2
  three = a ^ b
  four = one * two
  five = three ^ four
  return one,two,three,four,five
print(fiveVar(3,5))

print("\nScope")
def variableBalance(balance):
  newBal = balance - 500
  return newBal
intBalance = 10000
new_balance = variableBalance(intBalance)

print("\nTime and date")
from datetime import date
today = date.today()
print("Today's date:", today)

print("\nTry except")
print("Try-except can be used to catch invalid keyboard input")
print("Try-except can catch the error if a file can't be opened")
print("You wouldn't use try-except when dealing with out of memory errors")


print("\nOOP exercises")
print("\nClass")
print("You can have more than one class in a file")
print("Multiple objects can be created from the same class")
print("Objects cannot create classes, they are instances of classes")
class Person:
    "This is a person class"
    def getAge(self): 
        return self._age 
      
    def setAge(self, x): 
        self._age = x 

    def greet(self):
        print('sup dawg')
    
    def location(self):
      print("USA")
Adam = Person()

print("\nGetter and setter")
Adam.setAge(23)
printAdam.getAge())
print("You would use getter and setter methods to ensure encapsulation")

print("\nModules")
import math
print(math.sin(1))
def snake():
    print("==========>~")
import main
main.snake()

print("\nInheritance")
class Class1:
    pass
class Class2:
    pass
class MultiClass(Class1, Class2):
    pass

print("\nStatic method")
print("Yes, a method inside a class can be called without creating an object")
print("Not everybody likes static methods because they don't have acccess to the attributes of an instance of a class. Not good for long term use")

print("\nIterable")
print("An iteratable is a Python object that can be used as a sequence.")
print("Iterable types include all sequence types and some non-sequence types like file objects")

print("\nClassmethod")
print("A class method is a method that is shared among all objects")
print("Static methods aren't bound to a class, class methods are")

print("\nMultiple inheritance")
print("Not all programming languages support multiple inheritance")
print("You would not want to use multiple inheritance to prevent ambiguity")
print("There's no limit to the number of classes you can inherit from")