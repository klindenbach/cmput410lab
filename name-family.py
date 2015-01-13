class Student:
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.marks = {}

    def addCourseMark(self, course, mark):
        self.marks[course] = mark

    def average(self):
        sum = 0
        for course in self.marks:
            sum += self.marks[course]
        
        return sum / len(self.marks)

def main():
    s = Student("konrad", "lindenbach")
    s.addCourseMark("CMPUT301", 100)
    s.addCourseMark("CMPUT302", 50)
    s.addCourseMark("CMPUT303", 75)

    print s.average()

if __name__ == "__main__":
    main()

