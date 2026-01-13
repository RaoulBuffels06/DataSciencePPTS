# 2 Advanced programming Python

## Slide 1
- Advanced programming topics

- 2025-2026

## Slide 2
- What do you know already?

- Basics of Python
- Conditionals – Loops
- Functions
- Collections: List – Tuple – Dictionary – Set
- File I/O: txt, csv, JSON
- OO programming in Java

- 2

## Slide 3
- Scaling up your Python programming skills

- OO programming
- Built-in functions for working with collections
- Lambda functions
- List Comprehensions

- 3

## Slide 4
- OO : Classes

- Class definitions start with the class keyword, which is followed by the name of the class and a colon.
- Class names are written in CapitalizedWords notation by convention.
- Class attributes which are identical for all instances are defined first.
- Every time a new object is created, __init__() sets the initial state of the object by assigning the values of the object’s attributes.
- __init__() can have any number of parameters, but the first parameter will always be a variable called self.
- When a new object is created, the instance is automatically passed to the self parameter.

- 4

- class Flight:
- #class attributes
- airport = "Brussels South"
- #initializer
- def __init__(self, operator, destination):
- self.operator = operator
- self.destination = destination
- #instantiating objects
- a=Flight("Virgin","Amsterdam")
- b=Flight("Ryanair","Berlin")
- print('From', a.airport,"to",a.destination)
- print('From', b.airport,"to",b.destination)

## Slide 5
- OO: Instance methods

- 5

- class Flight:
- #...
- def __str__(self):
- return f"Flight from {self.airport} to {self.destination}"
- def takeoff(self, ready):
- if ready:
- return f"{self} ready for take off"
- else:
- return f"{self} still waiting"

- Instance methods are functions that are defined inside a class and can only be called from an instance of that class.
- An instance method’s first parameter is always self.
- Override of  __str__(self) defines the default output when printing the object.

## Slide 6
- OO: Instance methods

- 6

- #instantiating objects
- a=Flight("Virgin","Amsterdam")
- b=Flight("Ryanair","Berlin")
- print (a)
- print (b)
- print (a.takeoff(False))
- print (b.takeoff(True))

- def __str__(self):
- return f"Flight from {self.airport} to {self.destination}"

- In the takeoff method the object (self) is called so the default output set in __str__() appears

## Slide 7
- OO: Inheritance

- 7

- # CommercialFlight inherits Flight
- class CommercialFlight(Flight):
- def __init__(self, operator, destination, passengers):
- super().__init__(operator, destination)
- self.passengers = passengers
- # instantiating CommercialFlight objects
- c = CommercialFlight("Virgin","Copenhagen",120)
- print(c)

- To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
- The Flight class is extended with the attribute ‘passengers’
- BUT the child's __init__() function overrides the inheritance of the parent's __init__() function.Hence a call to the parent’s __init__() function is required. Via the super() function you can call all the functionality of the parent class.

## Slide 8
- OO: Inheritance

- 8

- # CommercialFlight inherits Flight
- class CommercialFlight(Flight):
- def __init__(self, operator, destination, passengers):
- super().__init__(operator, destination)
- self.passengers = passengers
- # extra function for commercial flights    def startboarding(self, ready):
- if ready:
- return f"{self.passengers} passengers can start boarding on {self}"
- else:
- return f"No boarding yet for {self}"
- # instantiating CommercialFlight objects
- c = CommercialFlight("Virgin","Copenhagen",120)
- print(c.startboarding(True))
- print(c.takeoff(True))

## Slide 9
- Time to practice OO programming

- Exercise 1:  HR Payroll system
- Exercise 1 extra: Abstract classes in Python

- 9

- from abc import ABC, abstractmethod

## Slide 10
- Built-in functions for working with collections

- Enumerate()
- Zip()
- Map()
- Filter()
- Using Lambda functions

- 10

## Slide 11
- Collection-based iteration

- To iterate over a collection, use a for-loop
- To show the index number of each item in the collection, use a counter
- Now each item in the collection is retrieved by index
- The first element in the collection has index number 0

- 11

- students = ["Ann","Bert","Chris","Dave"]
- for student in students:
- print(student)

- for i in range(len(students)):
- print (i, students[i])
- for i in range(len(students)):
- print (i+1, students[i])

## Slide 12
- Enumerate() for counting

- A more Pythonic way to add a counter is using the built-in enumerate() function.
- enumerate() gives you back two loop variables:
- The count of the current iteration
- The value of the item at the current iteration
- Just like with a normal for loop, the loop variables can be named whatever you want them to be named.

- 12

- for i, student in enumerate(students):
- print(i, student)
- #By default the index counter starts at 0#To print a natural counting number as an # output for the user, you can use the start #argument for enumerate() to change the starting #count to 1
- for i, student in enumerate(students, start=1):
- print(i, student)

## Slide 13
- Enumerate()

- Enumerate() returns a list of tuples, combining every element in the list with its index.
- Note the two variables i & student: During iteration every tuple is automatically stored in these two variables.
- This principle is called argument unpacking.

- 13

- for i, student in enumerate(students):
- print(i, student)
- #enumerate returns list of tuples
- print(list(enumerate(students)))

## Slide 14
- Zip() for parallel iteration

- To loop over iterables of the same length, use the zip() function.
- Zip() gives you back a loop variable for each iterable.
- The loop variables can be named wathever you want.E.g.
- student for students
- grade for grades

- 14

- students = ["Ann","Bert","Chris","Dave"]grades=["A","B","A","C"]
- # From the Python course in 1ITF
- for i in range(len(students)):
- print(i+1, students[i],grades[i])
- #more Pythonic way to achieve this is by using#built-in zip() function
- for student, grade in zip(students,grades):
- print(student,grade)

## Slide 15
- Zip()

- Python’s zip() function is defined as zip(*iterables).
- The function takes in x iterables as arguments and returns a list of tuples containing elements from each iterable.
- Pay attention to the length of your iterables. When the iterables you pass in as arguments aren’t the same length, the number of elements that zip() puts out will be equal to the length of the shortest iterable.

- 15

- for student, grade in zip(students,grades):
- print(student,grade)
- #zip returns list of tuples
- print(list(zip(students, grades)))

- #in case of unequal length?print(list(zip(students, grades, range(2))))

## Slide 16
- Zip() & Enumerate()

- You can combine zip() and enumerate() by using nested argument unpacking
- In the for loop, you nest zip() inside enumerate(). This means that each time the for loop iterates, enumerate() yields a tuple with the first value as the count and the second value as another tuple containing the elements from the arguments to zip().

- 16

- #parallel iteration with print of counter
- for i,(student, grade) in enumerate(zip(students,grades)):
- print(i,student,grade)

## Slide 17
- Map() for calling functions

- To pass each item in an iterable to a function, you better use map() instead of a traditional for loop
- Map() has 2 arguments:
- the transformation function
- the iterables whose items need to be passed to the function

- 17

- #function to transform grade in mark
- def transform(grade):
- lookup_dict = {"A":8,"B":6,"C":4,"D":2}
- return lookup_dict.get(grade)
- # From the Python course in 1ITF
- marks=[]
- for grade in grades:
- marks.append(transform(grade))
- print(marks)
- #more Pythonic way to call function by using #built-in map()
- marks = list(map(transform,grades))
- print(marks)

## Slide 18
- Map()

- Here you see an example of a function that needs 2 incoming arguments.
- pow() takes two arguments, x and y, and returns x to the power of y.
- In the first iteration, x will be 1, y will be 4, and the result will be 1.
- In the second iteration, x will be 2, y will be 3, and the result will be 8, and so on.
- The final iterable is only as long as the shortest iterable, which is the second one in this case.

- 18

- results = list(map(pow,[1,2,3,4,5],[4,3,2,1]))
- print(results)

- X

- Y

## Slide 19
- Filter() for extracting values from iterables

- Filter() applies a Boolean-valued function (a function that returns either True or False according to a specific condition) to an iterable and generates a new iterable containing the items that satisfy the Boolean condition.
- Boolean-valued function: passed()
- Iterable to filter: grades
- Output: passed_grades containing only items that satisfy the condition

- 19

- grades=["A","B","A","C"]#function returns true in case of A,B
- def passed(grade):
- return grade in ("A", "B")results = list(map(passed,grades))
- print(results)
- passed_grades =list(filter(passed,grades))
- print(passed_grades)

## Slide 20
- Lambda functions

- A lambda function is an anonymous function, hence a function without a name.
- In Python, an anonymous function is created with the lambda keyword.
- Syntax:
- lambda parameters:expression

- 20

- #Immediately invoked lambda functions
- print((lambda x,y:x+y)(2,3))print((lambda x,y,z=3:x+y+z)(2,3))
- print((lambda *args:sum(args))(1,2,3,4))

## Slide 21
- Lambda functions

- Lambda functions are regularly used with the built-in functions map() and filter()
- We can rewrite the previous examples of map() and filter() without using a predefined function but using a lambda function instead

- 21

- #lambda functions in combination with filter
- grades=["A","B","A","C"]
- passed_grades = list(filter(lambda grade:grade in("A","B"),grades))
- print(passed_grades)#lambda functions in combination with map
- marks = list(map(lambda grade:{"A":8,"B":6,"C":4,"D":2}.get(grade),grades))
- print (marks)

## Slide 22
- List comprehension

- List comprehension in Python is an easy and compact syntax for creating a list from a string or another list.
- It is a very concise way to create a new list by performing an operation on each item in the existing list.
- List comprehension is considerably faster than processing a list using the for loop.
- List comprehension is an alternative for the built-in functions map() and filter()
- Syntax:  [output expression for element in iterable if condition]

- 22

## Slide 23
- List comprehension

- 23

- lst = [x*x for x in range(1,6)]

## Slide 24
- List comprehension

- 24

## Slide 25
- List comprehension

- 25

- #basic list comprehension
- squares = [i**2 for i in range(1,11)]
- print(squares)
- even_numbers = [i for i in range(1,11) if i%2==0]
- print(even_numbers)

- #list comprehension replacing map()
- grades=["A","B","A","C"]
- marks = [{"A":8,"B":6,"C":4,"D":2}.get(grade) for grade in grades]
- print(marks)
- results = ["Pass" if grade in("A","B") else "Fail" for grade in grades]
- print(results)
- #list comprehension replacing filter()
- passed_grades = [grade for grade in grades if grade in ("A","B") ]
- print (passed_grades)

## Slide 26
- Copying list

- Python is very tricky when it comes to copying lists
- Look at the notebook called “deep_vs_shallow_copy.ipynb”!

- 26

## Slide 27
- Descriptive statistics

- Descriptive statistics is about describing and summarizing data. It uses two main approaches:
- The quantitative approach describes and summarizes data numerically.
- The visual approach illustrates data with charts, plots, histograms, and other graphs.
- In this introductory chapter you use Python’s statistics library.  This is the basic built-in Python library for descriptive statistics. You can use it if your datasets are not too large or complex.

- 27

## Slide 28
- Measures of central location

- To analyze the central or middle values of datasets:
- Mean: average
- Median: middle value of data set
- Odd number of data points: middle value is returned
- Even number of data points: average of the 2 middle values is returned
- Mode: the most typical data value in the set

- 28

- import statistics as st
- sample = [1,2,2,2,2,3,3,3,4,4,5,6,7]
- print(st.mean(sample))
- print(st.median(sample))
- print(st.mode(sample))

- 3.3846153846153846
- 3
- 2

## Slide 29
- Time to practice

- Exercise 2 : filter()
- Exercise 3 : map() – Lambda function – List Comprehension
- Exercise 4 : zip() – enumerate() – dict()
- Exercise 5 : OO – zip()
- Exercise 6 : Statistics: detecting outliers

- 29
