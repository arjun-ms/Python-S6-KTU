# Create a Student class and initialize it with name and roll number. (7)
# Make methods to :
# l. Display - Display all informations ofthe student.
# 2. setAge - Assign age to student
# 3. setTestMarks - Assign marks of a test to the student.

class Student:
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.age = None
        self.mark = 0

    def setAge(self,age):
        self.age = age
    
    def setTestMarks(self,mark):
        self.mark = mark
        
    def display(self):
        print(f"""
              Name: {self.name}
              Roll No: {self.rollno}
              Age: {self.age}
              Mark: {self.mark}""")
        
s1 = Student("Arjun",29)
s1.setAge(21)
s1.setTestMarks(100)
s1.display()