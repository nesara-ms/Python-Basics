# 1.Looping through list
l = [1,23,45,567,45]
total =  0
for num in l:
    total = total+num
    print("total=",total)

#Doubling each number in a list 
l = [2,6,23,34,45]
dl = []
for num in l:
    dl.append(num*2)
    print(dl)

#Examples
foods = ["pasta","fried rice","biryani"]
for food in foods:
    print(f"i like {food}")

# 2.Looping with dictionaries
student_marks = {"Neha":89,"Sowkya":99,"kushal":90}
for students,marks in student_marks.items():
    print(f"{students}---{marks}")
for students in student_marks:
    print(students)
for marks in student_marks.values():
    print(marks)

# 3.for loop with range()
students = ["Neha","Nesara","Kushal"]
marks = [25,90,100]
student_marks = {}
for index, student in enumerate(students):
    student_marks[student] = marks[index]
print(student_marks)

students = ["Neha","Kushal","Sowkya"]
marks = [25,90,100]
student_marks = {}
for i in range(3):#3 is because of known len of the students, is not thn len(students) can be used.
    student_marks[students[i]] = marks[0]
print(student_marks)