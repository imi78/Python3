class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
    
    def calc(self):
        avg = sum (self.scores) / len(self.scores)  # така се вадят стойностите от списъка без цикъл
        # for i in self.scores:
        #     avg += i
        if 90 <= avg <= 100:
            return "O"
        elif 80 <= avg < 90:
            return "E"
        elif 70 <= avg < 80:
            return "A"
        elif 55 <= avg < 70:
            return "P"
        elif 40 <= avg < 55:
            return "D"
        else:
            return "T"
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
# numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
avsc = s.calc()  # call the function here, not directly in print statement
print("Grade:", avsc)