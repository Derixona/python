student_details = {"Name": "Ada", "Course": "Computer Scienc", "Level" : 100}
#print(help(student_details))


def receive_student(student, students):
    print(help(student))
    print(type(student))
    if student.get("Name") == "":
            print("Student name cant be empty")
                students.append(student)
    return students

student = ["Michael"]
ne = {"Name ": "joh"}
print(receive_student(student,ne))

new_student = [student_details]

new = {"Name": "Michael", "Course": "Mathematics", "Level": 200}
updated = receive_student(new_student, new)
print(updated)