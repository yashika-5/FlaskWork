from basic import db,User
from datetime import date

# CREATE
student1 = User('Charlie',22,date(1999,8,5),'Male')
db.session.add(student1)
db.session.commit()

# READ
all_students = User.query.all() # list of student objects in table
print(all_students)
print('\n')

# SELECT BY ID
studentById = User.query.get(1)
if studentById:
    print(studentById.name, studentById.age, studentById.dob)
    print('\n')

else:
    print(f"Student with this id = {studentById} not found\n")

# FILTERS
studentByFilter = User.query.filter_by(name='John')
if studentByFilter:
    print(studentByFilter.all())
    print('\n')
else:
    print(f"student with this name not available" +'\n')

# UPDATE
studentAfterUpdate = User.query.get(1)
studentAfterUpdate.name = 'AfterUpdateYashika'
db.session.add(studentAfterUpdate)
db.session.commit()

# DELETE
studentDelete = User.query.get(4)
if studentDelete:
    db.session.delete(studentDelete)
    db.session.commit()
    print(f'Deleted USer of this id : {studentDelete.id}'+'\n')
else:
    print("Not found student for deletion with this id"+'\n')

# ALL STUDENTS
all_students = User.query.all()
print(all_students)
