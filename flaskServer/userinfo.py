from werkzeug.security import generate_password_hash,check_password_hash
class UserInfoController(object):
    # def __new__(cls,*args,**kw):
    #     if not hasattr(cls,'_instance'):
    #         org=super(UserInfoController)
    #         cls._instance=org.__new__(cls,*args,**kw)
    #     return cls._instance
    
    def get_userInfo(self,userID):
        return dict(name='yanhao',password='123456')

    def add_user(self,userID,userName,userPassword):
        return 1

userInfo_instance=UserInfoController()        

class UserInfo(object):
    # def __init__(self,userName,userPassword):
        
    #     self.name=userName
    #     self.password=userPassword

    # property定义读的办法
    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    # password.setter 定义 改的办法
    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)


    @property 
    def name(self):
        return self.name
    
    @name.setter
    def name(self,name):
        self.name=name


   
    

    
