# from database import db_session
# from model import User


from model2 import User,db

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
        return "error method"  

    def change_userInfo(self,id,name,email):

        # user=User.query.lter(User.id=='id').first()
        # user=User.query.filter_by()
        # a.id=id
        # db_session.commit()
        return dict(method='change',id=id,username=name,email=email,status='success')
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
    

    def add_user(self,userName,email):
        u=User(userName,email)
        # db_session.add(u)
        # db_session.commit()
        db.session.add(u)
        db.session.commit()
        return dict(method='add',status='success')

    def del_user(self,id):
        # users = User.query.all()
        # admin=User.query()

        return dict(method='del',id='1',username='yanhao',email='123456',status='success')

  
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


   
    

    
