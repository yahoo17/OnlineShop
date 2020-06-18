#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from flask_cors import *            # 解决跨域问题
from userinfo import userInfo_instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8'
# app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:123456@localhost:3306/test?charset=utf8'
                                                        #用户名 密码  服务器的ip  端口号 /数据库的名字  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET KEY"]="woluandade"

# #db是我们操作的对象
# db=SQLAlchemy(app)  
# db.create_all()                                                                                                
# # init_db()
from model2 import db,User
db.init_app(app)



# 解决跨域问题
CORS(app, supports_credentials=True)

@app.route('/test', methods=['GET', 'POST'])
def test():

    if request.method == 'GET':
        return 'you send server a GET request'
    elif request.method == 'POST':
        return "you send server a POST request"


@app.route('/profile', methods=['GET', 'POST'])
def profile():

    # if request.method=='GET':
    #         return 'you send server a GET request'
    # else request.method=='POST':
    #     return "hello world"
    if request.method == 'GET':
        name = request.args.get('name', '')
        if name == 'yanhao':
            return 'you send server a  request for yanhao'
        elif name == 'haoyan':
            return 'you send server a  request for haoyan'
        else:
            return 'you send server a request for other user'
    elif request.method == 'POST':
        # 如果要在POST body里面发消息
        # 需要在POST body里面
        print(request.form)
        name = request.json.get('name')
        if name == 'yanhao':
            return dict(name='yanhao', fans=1000000, info='你给服务器我 发了一条POST,里面有 严灏 所以我给你返回')
        elif name == 'haoyan':
            return dict(name='haoyan', fans=10, info='你给服务器我 发了一条POST,里面有 灏严 所以我给你返回')
        else:
            return '你POST的BODY里 的RAW的JSON里面的name 不是我们已知的name'


@app.route('/', methods=['GET', 'POST'])
def home():
    return "hello world you can visit \n localhost:5000/signin \n localhost:5000/signin/signup "


@app.route('/signin', methods=['GET','POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if (username == '6666' or username=='admin') and (password == '123456'or password == '6666'):
        return dict(state=True)
    else:
        return dict(state=False)
    # return render_template('form.html')

# 登陆 sign in
# @app.route('/signin', methods=['POST'])
# def signin():
#     username = request.form['username']
#     password = request.form['password']
#     if (username == '6666' or username=='admin') and (password == '123456'or password == '6666'):
#         return dict(state=True)
#     else:
#         return dict(state=False)
        # return render_template('signin-ok.html', username=username)
    # return render_template('form.html', message='Bad username or password', username=username)

# 注册 sign up
@app.route('/signup', methods=['POST'])
def signup():
    userid = request.form['id']
    name = request.form['username']
    email = request.form['email']
    u = User(userid,name, email)
    db_session.add(u)
    # db_session.commit()
    # return render_template('signup-ok.html', username=name)
    return dict(method='get',id='1',username='yanhao',email='123456',status='success')
    # dict(method='get',id='1',username='yanhao',email='123456',status='fail')

@app.route('/user', methods=['POST'])
def user():
    method=request.form['method']
    userid = request.form['id']
    name = request.form['username']
    email = request.form['email']  
    return userInfo_instance.do_crud(method,userid,name,email)

@app.route('/user', methods=['GET'])
def get_alluser():
    return userInfo_instance.do_crud('getall',-1,-1,-1)
    # u=User(id = userid,name = name ,email = email)
    # db.session.add(u)
    # db.session.commit()
    # db.session.close()
    # return jsonify({"hello":"kitty"})
    # temp = userInfo_instance.add_user(name,email)
    # return temp
   

    
from flask import jsonify


if __name__ == '__main__':
    app.debug = True
    app.run()
