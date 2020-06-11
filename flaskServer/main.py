#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from userinfo import *
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.orm import sessionmaker
from database import init_db 

app = Flask(__name__)
init_db()
# engine=create_engine('mysql+pymysql://root:123456@localhost:3307/test?charset=utf8',echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
# app.config['SECRET_KEY'] = '123456'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3307/test?charset=utf8' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True       #设置这一项是每次请求结束后都会自动提交数据库中的变动

# db=SQLAlchemy(app)


# metadata=MetaData(engine)
# DBSession = sessionmaker(bind=engine)

    
@app.route('/test', methods=['GET', 'POST'])
def test():
    
    if request.method=='GET':      
            return 'you send server a GET request'
    elif request.method=='POST':
        return "you send server a POST request"

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    
    # if request.method=='GET':      
    #         return 'you send server a GET request'
    # else request.method=='POST':
    #     return "hello world"
    if request.method=='GET':
        name=request.args.get('name','')
        if name=='yanhao':
            return 'you send server a  request for yanhao'
        elif name=='haoyan':
            return 'you send server a  request for haoyan'
        else:
            return 'you send server a request for other user'
    elif request.method=='POST':
        # 如果要在POST body里面发消息
        ## 需要在POST body里面
        print(request.form)

        name=request.json.get('name')
        if name=='yanhao':
            return dict(name='yanhao',fans=1000000,info='你给服务器我 发了一条POST,里面有 严灏 所以我给你返回')
        elif  name=='haoyan':
            return dict(name='haoyan',fans=10,info='你给服务器我 发了一条POST,里面有 灏严 所以我给你返回')
        else :
            return '你POST的BODY里 的RAW的JSON里面的name 不是我们已知的name'
        

@app.route('/', methods=['GET', 'POST'])
def home():
    return "hello world you can visit /signin /sign"

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

#
@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='6666' and password=='123456':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/user/<id>',methods=['POST','GET'])
def info(id):
    temp=userInfo_instance.get_userInfo(id)
    print(temp)
    return temp





if __name__ == '__main__':
    app.run()