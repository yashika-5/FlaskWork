from models import db,Student,Book,College

stud1 = Student("Yashika")
stud2 = Student("Ram")

db.session.add_all([stud1,stud2])
db.session.commit()

print(Student.query.all())

stud1 = Student.query.filter_by(name="Ram").first()

#create college of this stud

college1 = College("SKIT",stud1.id)

# some books of stud

book1 = Book("DBMS",stud1.id)
book2 = Book("MATHS",stud1.id)

db.session.add_all([college1,book1,book2])
db.session.commit()

# Grab this stud after those additions
stud1 = Student.query.filter_by(name='Ram').first()
print(stud1)
