class Student:

    def __init__(self, student_name, student_email, student_age,
                 student_course, student_marks, student_status,
                 student_roll_number):

        self.student_name = student_name
        self.student_email = student_email
        self.student_age = student_age
        self.student_course = student_course
        self.student_marks = student_marks
        self.student_status = student_status
        self.student_roll_number = student_roll_number

        self.college_name = "Sri Indu College of Engineering and Technology"

    def check_marks(self):
        print("Student Marks:", self.student_marks)

    def print_details(self):
        print("Student Name:", self.student_name)
        print("Student Email:", self.student_email)
        print("Student Age:", self.student_age)
        print("Student Course:", self.student_course)
        print("Student Marks:", self.student_marks)
        print("Student Status:", self.student_status)
        print("Student Roll Number:", self.student_roll_number)
        print("College Name:", self.college_name)

    def update_email(self, new_email):
        self.student_email = new_email
        self.print_details()

    def update_marks(self, new_marks):
        if new_marks < 0 or new_marks > 100:
            print("Invalid Marks")
        else:
            self.student_marks = new_marks
            self.print_details()

    def update_course(self, new_course):
        self.student_course = new_course
        self.print_details()

    def update_status(self, new_status):
        self.student_status = new_status
        self.print_details()

student = Student(
    "Srinivas",
    "srinivas@gmail.com",
    23,
    "Python Full Stack",
    85,
    "Active",
    "S101"
)

student.check_marks()

print("**" * 10)

student.print_details()

print("**" * 10)

student.update_email("srinivas123@gmail.com")

print("**" * 10)

student.update_marks(90)

print("**" * 10)


student.update_course("Python Full Stack with AI")

print("**" * 10)


student.update_status("Completed")

print("**" * 10)