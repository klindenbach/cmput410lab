1. Python:
– Design and implement a class named “Student” with three methods;
 - __init__(self, name, family)
 - addCourseMark(self, course, mark)
 - average(self)

Then test the class with an instance. The details like member variables are up
to you. For example, you can use lists or dictionaries to implement the class.

You can utilize this code (that uses a dictionary) too:

    class Student:
        courseMarks={}
        name= ""
        def __init__(self, name, family):
            ...
        def addCourseMark(self, course, mark):
            self.courseMarks[course] = mark
        def average(self):
            ...
