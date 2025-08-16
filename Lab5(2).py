class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        print("Name:", self.name, "| Marks:", self.marks)

s1 = Student("Niki", 92)
s2 = Student("Ravi", 88)
s3 = Student("Kiran", 79)

s1.show_details()
s2.show_details()
s3.show_details()
