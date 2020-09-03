from basic import db,User
from datetime import date
print("bshfkfhks")

db.create_all()

john = User('John',20,date(1998,6,10),'Male')

print(john.id)

db.session.add(john)

db.session.commit()
print(john.id)
print(john)

