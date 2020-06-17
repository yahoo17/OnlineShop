from model2 import db,User

stu=User.query.get(10)
id=stu.id
name=stu.name
email=stu.email
print(id,name,email)