# Object combine data with functions

# y = [1,2,3]
# y.append(6)
# print(y)

# z = {'a':1}

# Class variables and instance variables

class Patient(object):
    """Medical Patient Data"""
    def __init__(self, name, age): #creates variables that contain values
        self.name = name
        self.age = age

patient1 = Patient('Steve Hughes', 48)
patient2 = Patient('Abigail Sandrick', 34)

print(patient1.name, patient1.age)
print(patient2.name, patient2.age)


# Create a Student class with the listed attributes
class Student(object):
  def __init__(self, name, age, major, gpa, year):
    self.name = name 
    self.age = int(age)
    self.major = major
    self.gpa = float(gpa)
    self.year = int(year)

# Create two instances of the Student class
student1 = Student(
  name="Aisha Khan", 
  age=19, 
  major="Biology", 
  gpa=3.9, 
  year=2
  )

student2 = Student(name="Carlos Alvarez", 
  age=21, 
  major="Mechanical Engineering", 
  gpa=3.5, 
  year=3
  )# Create the second instance corresponding to the student Carlos Alvarez

# Output the details of both students. 
# Please, do not modify the print-functions.
print(f'''Student 1:
Name: {student1.name}
Age: {student1.age}
Major: {student1.major}
GPA: {student1.gpa}
Year: {student1.year}''')

print("")

print(f'''Student 2:
Name: {student2.name}
Age: {student2.age}
Major: {student2.major}
GPA: {student2.gpa}
Year: {student2.year}''')


# Class variables
class Student(object):
    total_students = 0 
    """Class variable shared amongst all instances of the class"""
    
    def __init__(self, name, age, major, gpa, year):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.year = year
        Student.total_students += 1 # Increment the total_students count
        
student1 = Student(
  name="Aisha Khan", 
  age=19, 
  major="Biology",
  gpa=3.9, 
  year=2
)

student2 = Student(
  name="Carlos Alvarez", 
  age=21, 
  major="Mechanical Engineering", 
  gpa=3.5, 
  year=3
)

student3 = Student(
  name="Maya Patel", 
  age=18, 
  major="Physics", 
  gpa=3.7, 
  year=1
)

print(f"Total number of students: {Student.total_students}")