class Patient(object):

    status = 'patient' #class variable 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.conditions = []

    def get_details(self): # A function that belongs to the class Patient prints patient details
        print(f'Patient record: {self.name}, {self.age} years. ' )
        if self.conditions:
            print('conditions: ')
            for info in self.conditions:
                print(f' - {info}')

    def add_info(self, information):
        self.conditions.append(information)

patient1 = Patient('Ugo Ndu', 32)
patient2 = Patient('Laju Otomewo', 32)

patient1.add_info("He just arrived from Nigeria, where he was treated for too much swag")
patient2.add_info("She is in love with patient1")

patient2.get_details()
patient1.get_details()

print('')





# Create a Student class with the listed attributes
class Student(object):
    # Create a class variable called total_students to keep track of the total number of students. Assign it a value of 0.
    total_students = 0
    
    def __init__(self, name, age, major, gpa, year):
        # Define instance attributes here
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.year = year
        Student.total_students += 1  # Increment the total_students count
        
    # Please, modify *only* the text within the curly braces.
    # Any extra spaces or newlines will lead to an *incorrect* answer.
    def get_details(self):
      print(f'''
      Name: {self.name}
      Age: {self.age}
      Major: {self.major}
      GPA: {self.gpa}
      Year: {self.year}
      Total number of students in class: {Student.total_students}''')

# Create an instance of the Student class
student1 = Student(
  name="Aisha Khan",
  age=19, 
  major="Biology", 
  gpa=3.9, 
  year=2
  )

# Output the total number of students
student1.get_details()



print(' ')



"""implementing update_age() and update_major() methods"""

class Student(object):
    """ Class variable to keep track of total students"""
    total_students = 0
    
    def __init__(self, name, age, major, gpa, year):
      self.name = name
      self.age = age
      self.major = major
      self.gpa = gpa
      self.year = year
      
      # Increment the total_students count each time a new Student object is created
      Student.total_students += 1
        
    def get_details(self):
      print(f'''Name: {self.name}
      Age: {self.age}
      Major: {self.major}
      GPA: {self.gpa}
      Year: {self.year}
      Total number of students in class: {self.total_students}''')
      
    def update_age(self):
      self.age += 1
      
    def update_major(self, new_major):
      self.major = new_major
      

# Create an instance of the Student class
student1 = Student(
  name="Aisha Khan", 
  age=19, 
  major="Biology", 
  gpa=3.9, 
  year=2
  )

# Output the total number of students
student1.update_age()
student1.update_major(new_major="Molecular Biology")
student1.get_details()