# Open and close file automatically in read mode
with open('score-test.txt', 'r') as f:
    lines = f.readlines()

# Let's identify the students who approved "A" and failed "F" the exam
pass_students = []
fail_students = []
for line in lines:
    if int(line.split()[0]) > 70:
        pass_students.append(line.rstrip() + " A")
    else:
        fail_students.append(line.rstrip() + " F")

# Let's now create two files, one for students who approved the exam and the other for 
# students who failed. These files will be added in the gitignore definition to do not upload them.
with open('approve.txt', 'w') as f:
    for student in pass_students:
        f.write(student + "\n")

with open('fail.txt', 'w') as f:
    for student in fail_students:
        f.write(student + "\n")