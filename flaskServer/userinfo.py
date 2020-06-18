# from database import db_session
# from model import User


from model2 import User,db
import json
from flask import jsonify
class UserInfoController(object):
    # def __new__(cls,*args,**kw):
    #     if not hasattr(cls,'_instance'):
    #         org=super(UserInfoController)
    #         cls._instance=org.__new__(cls,*args,**kw)
    #     return cls._instance
    # from main import User,db
    def do_crud(self,method,id,name,email):
        if method=="add":
            return self.add_user(name,email)
        elif method=="del":
            return self.del_user(id)
        elif method=="get":
            return self.get_userInfo(id)
        elif method=="change":
            return self.change_userInfo(id,name,email) 
        elif method=="getbyemail":
            return self.get_userInfoByEmail(email)
        elif method=="getall":
            return self.get_all()
        return "error method"  
    def get_all(self):
        stu_list = User.query.all()
        print(type(stu_list))
        return jsonify(all_users_info=[e.serialize() for e in stu_list])
    def change_userInfo(self,id,name,email):

        # # filter_by 和filter这些可以结合用
        # stu = User.query.filter(User.id > 100)
        # for i in stu :
        #     print(i.id, i.name , i.email)

        # stu = User.query.filter(User.id==id)
        # for i in stu :
        #     print(i.id, i.name , i.email)

        # # stu = User.query.filter_by(name = "yanhao").first()

        # stu = User.query.filter_by(name = "yanhao") # select name from User where name= "yanhao"
        # for i in stu :
        #     print(i.id, i.name , i.email)

        # stu.name=name
        # stu.email = email
        
        #方法2
        # stu = User.query.filter(User.id==id)
        # stu.name="chan"
        # db.session.add(stu)
        # db.session.commit()

        #方法1
        update_count = User.query.filter(User.id==id).update({"name":name,"email":email})
        db.session.commit()
        if update_count==1:
            return dict(method='change',id=id,username=name,email=email,status='success')
        else:
            return dict(method='change',id=-1,username=-1,email=-1,status='fail')
    def get_userInfo(self,userID):
        # all_user=db_session.query(User).all()
        stu=User.query.get(userID)
        if(type(stu)==User):
            id=stu.id
            name=stu.name
            email=stu.email
            print(id,name,email)
            return dict(method='get',id=id,username= name ,email= email ,status='success')
        else:
            return dict(method='get',id='-1',username='-1',email='-1',status='fail')
    
    def get_userInfoByEmail(self,email):
        stu = User.query.filter_by(email=email).first()
        # print(type(stu))
        # return "1"
        return dict(id=stu.id,username=stu.name,email=email)

    def add_user(self,userName,email):
        u=User(userName,email)
        # db_session.add(u)
        # db_session.commit()
        db.session.add(u)
        db.session.commit()
        temp = self.get_userInfoByEmail(email)
        temp2 = dict(method='add',status='success')
        return dict(**temp2, **temp )

    def del_user(self,id):
        # users = User.query.all()
        # admin=User.query()
        del_count = User.query.filter(User.id==id).delete()
        if del_count>=1:
            return dict(method='del',id='1',username='yanhao',email='123456',status='success')
        else:
            return dict(method='del',id='-1',username='-1',email='-1',status='fail')
  
userInfo_instance= UserInfoController() 
# class UserInfo(object):
    # def __init__(self,userName,userPassword):
        
    #     self.name=userName
    #     self.password=userPassword

    # property定义读的办法

    # @property
    # def password(self):
    #     raise AttributeError('password is not readable attribute')

    # # password.setter 定义 改的办法
    # @password.setter
    # def password(self,password):
    #     self.password_hash=generate_password_hash(password)
    
    # def verify_password(self,password):
    #     return check_password_hash(self.password_hash,password)


    # @property 
    # def name(self):
    #     return self.name
    
    # @name.setter
    # def name(self,name):
    #     self.name=name


   
    

    
