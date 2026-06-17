#STUDENT MANAGEMENT SYSTEM--
class Sdetails():
    dt=[]
    def __init__(self, name, ID, marks):
        self.name=name
        self.ID=ID
        self.marks=marks
        Sdetails.dt.append({"name":self.name, "ID":self.ID, "marks":self.marks})
        self.save_to_excel()
        
    def display(self, name, ID, marks):
        if name== None and ID==None and marks==None:
            print("error")
            return
        elif ID==None and marks==None:
            return self.name
        elif marks==None:
            return self.name, self.ID
        else:
            return self.name, self.ID, self.marks
    def save_to_excel(self, filename="students.xlsx"):
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.append(["Name", "ID", "Marks"])
        for student in Sdetails.dt:
            ws.append([
                student["name"],
                student["ID"],
                student["marks"]
                ])
            wb.save(filename)
    @classmethod
    def get_student(cls, ID):
        for student in cls.dt:
            if student["ID"] == ID:
                return student
        return "Student not found"
    @classmethod
    def search_by_name(cls, name):
        students = [student for student in cls.dt
                    if student["name"].lower() == name.lower()]
        if not students:
            return "Student not found"
        if len(students) == 1:
            return students[0]
        print("Multiple students found:")
        for student in students:
            print(f"ID: {student['ID']}, Marks: {student['marks']}")
        ID = int(input("Enter the ID of the student you want to view: "))
        for student in students:
            if student["ID"] == ID:
                return student
        return "Invalid ID"
    @classmethod
    def highest_marks(cls):
        if not cls.dt:
            return "No student records found"
        topper = max(cls.dt, key=lambda student: student["marks"])
        return topper    
    @classmethod
    def delete_student(cls, ID):
        for student in cls.dt:
            if student["ID"] == ID:
                cls.dt.remove(student)
                return "Student deleted successfully"
        return "Student not found"
    @classmethod
    def view_all_students(cls):
        if not cls.dt:
            return "No students found"
        return cls.dt
    @classmethod
    def total_students(cls):
        return len(cls.dt)
while True:
    print("\n----- STUDENT MANAGEMENT SYSTEM -----")
    print("1. Add Student")
    print("2. View Student by ID")
    print("3. Search Student by Name")
    print("4. View Topper")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        ID = int(input("Enter ID: "))
        marks = float(input("Enter Marks: "))
        Sdetails(name, ID, marks)
        print("Student Added Successfully!")
        
    elif choice == "2":
        ID = int(input("Enter Student ID: "))
        print(Sdetails.get_student(ID))

    elif choice == "3":
        name = input("Enter Student Name: ")
        print(Sdetails.search_by_name(name))

    elif choice == "4":
        print(Sdetails.highest_marks())

    elif choice == "5":
        ID = int(input("Enter Student ID to delete: "))
        print(Sdetails.delete_student(ID))
        
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
        