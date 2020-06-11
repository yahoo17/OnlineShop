from flask import Flask,jsonify,session,request
from sqlalchemy import create_engine,Integer
from sqlalchemy.orm import sessionmaker
from models import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SECRET_KEY'] = '123456'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:zxcxzcz123@localhost:3307/mall?charset=utf8' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动

# db = SQLAlchemy(app)
# 初始化数据库连接:

# engine = create_engine('mysql+pymysql://root:zxcxzcz123@localhost:3307/mall?charset=utf8')
engine = create_engine('mysql+pymysql://root:123456@localhost:3307/test?charset=utf8')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# db = SQLAlchemy(app) #实例化


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/get_banner")
def get_banner():
    res =[ {"product_id":1,"picture_src":"https://resource.smartisan.com/resource/fda5c3e61a71c0f883bbd6c76516cd85.png"},{"product_id":2,"picture_src":"https://resource.smartisan.com/resource/w/white25wap.png"},{"product_id":3,"picture_src":"https://resource.smartisan.com/resource/9402b4117bf1c1754dca08b52c98cca0.png"},{"product_id":4,"picture_src":"https://resource.smartisan.com/resource/B/BS2000WAP.png"}]
    res = {"code":200,"res":res}
    return jsonify(res)

@app.route("/get_hot")
def get_hot():
    # pass
    res = [{"id":5,"title":"各色DNA检测套装","description":"千万级基因位点数据解读","picUrl": "https://resource.smartisan.com/resource/9bffe702b1f0aea221b1f18ddf886958.jpg","price":499},{"id":6,"title":"畅呼吸智能空气净化器","description":"超强净化能力，超低噪音","picUrl": "https://resource.smartisan.com/resource/6ff92d05a3bfab4fad489ca04d3eea5a.png","price":1299},{"id":7,"title":"坚果 Pro 2","description":"漂亮得不像实力派","picUrl": "https://resource.smartisan.com/resource/c71ce2297b362f415f1e74d56d867aed.png","price":"1799"}]
    res = {"code":200,"res":res}
    return jsonify(res)

@app.route("/get_category")
def get_category():
    res = [{"id":1,"title":"服装","children":[
      {
        "id":2,"title":"内裤","picUrl": "https://yanxuan.nosdn.127.net/8f8e33740f959f78228ea66ded5a2d34.png"
      },
      {
        "id":3,"title":"内衣","picUrl": "https://yanxuan.nosdn.127.net/cd9abb6017e8d0c31d04a6e93fa16c4d.png"
      },
      {
        "id":4,"title":"袜子","picUrl": "https://yanxuan.nosdn.127.net/c34360cc88e0f086676680591b737d06.png"
      },
      {
        "id":5,"title":"T恤","picUrl": "https://yanxuan.nosdn.127.net/f79dc8718c0f42c3736138e2205ce6ad.png"
      }
    ]},{"id":6,"title":"餐厨","children":[
      {
        "id":7,"title":"锅具","picUrl": "https://yanxuan.nosdn.127.net/b5cb8e8abc7d7dd20711de9bf4c2f3fa.png"
      },
      {
        "id":8,"title":"杯壶","picUrl": "https://yanxuan.nosdn.127.net/7b39e972b2905741b50946463a8c75d0.png"
      }
    ]}]
    res = {"code":200,"res":res}
    return jsonify(res)


@app.route("/add_cart",methods=['POST'])
def add_cart():
    print(request.form)
    # insert into 对应用户的购物车表中
    # print(request.form['order_id'])
    res = {"code":200}
    return jsonify(res)

@app.route("/query_cart",methods=['POST'])
def query_cart():
    print("用户"+request.form['user_id']+"正在查询他的购物车信息！")
    res = [{
        "id": 1,
        "checked": False,
        "picUrl": 'https://resource.smartisan.com/resource/71432ad30288fb860a4389881069b874.png',
        "title": '畅呼吸智能空气净化器',
        "spec": '标准版 白色',
        "count": 1,
        "maxNum": 99,
        "price": 1299.00
      },
      {
        "id": 2,
        "checked": True,
        "picUrl": 'https://yanxuan.nosdn.127.net/e9cecc7cb24a8d7745da1c99b87dde08.png',
        "title": '丛林系列·缝线笔记本 4本装',
        "spec": '丛林系列',
        "count": 1,
        "maxNum": 99,
        "price": 29.00
      }]
    res = {"code":200,"res":res}
    return jsonify(res)

@app.route("/get_product/<int:product_id>")
def get_product(product_id):
    # print(product_id)
    # print("商品"+str(product_id)+"正在请求！")
    # 根据product_id确定商品
    
    # 返回：product,sku
    res = {"sku": {
      "show": False, # 显示属性规格
      "noneSku": False, # 有无规格选择
      "quota": 100, # 限购数量
      "productId": 1, # 商品id
      "picUrl": "", # 当前选择图片
      "specText": "", # 所选规格属性
      "specTextNoCount": "", # 所选规格属性 无数量
      "tree": [
        {
          "k": '颜色', # skuKeyName：规格类目名称
          "v": [
            {
              "id": 1, # skuValueId：规格值 id
              "name": '银色', # skuValueName：规格值名称
              "picUrl": 'https://img11.360buyimg.com/n1/s450x450_jfs/t1/62813/33/2131/584186/5d079803E03084b0d/2b4970456b7bf49f.png', # 规格类目图片，只有第一个规格类目可以定义图片
              "selected": False, # 是否选择
              "disabled": False # 禁用
            },
            {
              "id": 2,
              "name": '深空灰色',
              "picUrl": 'https://img14.360buyimg.com/n0/jfs/t1/3/15/4536/138660/5b997bf8Ed72ebce7/819dcf182d743897.jpg',
              "selected": False,
              "disabled": False
            }
          ],
          "ks": 's1' # skuKeyStr：sku 组合列表（下方 list）中当前类目对应的 key 值，value 值会是从属于当前类目的一个规格值 id
        },
        {
          "k": '内存',
          "v": [
            {
              "id": 3,
              "name": '64GB',
              "picUrl": '',
              "selected": False,
              "disabled": False
            },
            {
              "id": 4,
              "name": '256GB',
              "picUrl": '',
              "selected": False,
              "disabled": False
            },
            {
              "id": 5,
              "name": '512GB',
              "picUrl": '',
              "selected": False,
              "disabled": False
            }
          ],
          "ks": 's2'
        }
      ],
      # 所有 sku 的组合列表，比如红色、M 码为一个 sku 组合，红色、S 码为另一个组合
      "list": [
        {
          "id": 1, # skuId，下单时后端需要
          "price": 1.00, # 价格
          "s1": 1, # 规格类目 ks 为 s1 的对应规格值 id
          "s2": 3, # 规格类目 ks 为 s2 的对应规格值 id
          "stockNum": 50 # 当前 sku 组合对应的库存
        },
        {
          "id": 2,
          "price": 2.00,
          "s1": 1,
          "s2": 4,
          "stockNum": 100
        },
        {
          "id": 3,
          "price": 3.00,
          "s1": 1,
          "s2": 5,
          "stockNum": 0
        },
        {
          "id": 4,
          "price": 4.00,
          "s1": 2,
          "s2": 3,
          "stockNum": 100
        },
        {
          "id": 5,
          "price": 5.00,
          "s1": 2,
          "s2": 4,
          "stockNum": 100
        },
        {
          "id": 6,
          "price": 6.00,
          "s1": 2,
          "s2": 5,
          "stockNum": 50
        }
      ],
      # 选择的 sku 组合
      "selectedSku": {
      },
      "count": 1 # 选择的商品数量
    }}
    res['product'] = {
      "id": 0,
      "picUrl": "https://img11.360buyimg.com/n1/s450x450_jfs/t1/62813/33/2131/584186/5d079803E03084b0d/2b4970456b7bf49f.png",# 默认商品图片
      "promotion": 1, # 促销活动 0无 1限时购 2领劵
      "gallery": [{
        "picUrl": "https://img11.360buyimg.com/n1/s450x450_jfs/t1/62813/33/2131/584186/5d079803E03084b0d/2b4970456b7bf49f.png",
        "sortOrder": 1
      },
      {
        "picUrl": "https://img10.360buyimg.com/n1/s450x450_jfs/t1/4176/23/3653/281477/5b9a15d4E97e09d00/887e76e6c525324c.jpg",
        "sortOrder": 2
      },
      {
        "picUrl": "https://img10.360buyimg.com/n1/s450x450_jfs/t1/5967/33/3617/54427/5b9a15d4Ebe8c2aed/99c9c06b72d356f7.jpg",
        "sortOrder": 3
      },
      {
        "picUrl": "https://img10.360buyimg.com/n1/s450x450_jfs/t1/2522/37/3744/128519/5b9a15d4Eb916347a/bef9d7fae9c5d2ae.jpg",
        "sortOrder": 4
      },
      {
        "picUrl": "https://img10.360buyimg.com/n1/s450x450_jfs/t1/1508/30/3667/24431/5b9a15d4E61cd63d4/592747ec9cd8ad81.jpg",
        "sortOrder": 5
      }
      ], # 轮播图
      "title": "Apple iPhone XS Max (A2104)",
      "description": "A12仿生芯片流畅体验，支持双卡！",
      "defaultPrice": 1.00, # 默认显示价格
      "price": 1.00,
      "originPrice": 9588.00,
      "detail": '<div><img src="https://img14.360buyimg.com/cms/jfs/t1/25195/1/9487/388554/5c7f80a5E8b8f8f0c/46818404849d6ec6.jpg"><img src="https://img12.360buyimg.com/cms/jfs/t1/15853/18/9628/325164/5c7f80a5E7172b236/ba9f3f63a83a9b65.jpg"></div>', # 商品详情
      "tags": [{
        "id": 1,
        "title": "商家名称"
      },
      {
        "id": 2,
        "title": "品牌名称"
      }
      ],
      "serviceList": [{
        "id": 1,
        "title": "48小时快速退款",
        "desc": "收到退货包裹并确认无误后，将在48小时内办理退款，退款将原路返回，不同银行处理时间不同，预计1-5个工作日到账。"
      },
      {
        "id": 2,
        "title": "满88元免邮费",
        "desc": "单笔订单金额（不含运费），大陆地区满88元免邮，不满88元收取10元邮费；港澳台地区满500元免邮，不满500元收取30元运费；海外地区以下单页提示运费为准。"
      },
      {
        "id": 3,
        "title": "官方自营品牌",
        "desc": "官方原创生活类电商品牌，所有商品均为官方自营，品质保证。"
      },
      {
        "id": 4,
        "title": "国内部分地区无法配送",
        "desc": "不支持省份: 台湾、香港、澳门、新疆"
      }
      ],
      "comment": {
        "goodCommentRate": 100, #好评率
        "count": 3986, # 评论计数
        "goodComment": {
          "nickname": "Exrick",
          "avatar": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJTqQ5hNKicCNEwW3cATfOTaXk6xMlNEfh1gm0kicPDtJrXwTf5YEqQXYea3m5vsuPyJUXc3U0OicXtA/132",
          "content": "很好，手机很有质感，值得购买。",
          "rate": 5,
          "time": "2019.06.18",
          "spec": "银色 64G",
          "pics": [
            "https://img30.360buyimg.com/shaidan/s616x405_jfs/t1/65005/20/4818/92581/5d2ffdb6Ebcbf3018/35411a583e29d52d.jpg",
            "https://img30.360buyimg.com/shaidan/s616x405_jfs/t1/74460/28/4830/96562/5d2ffdb7Ed5e9ce7a/e764b3daa92a9c67.jpg"
          ]
        } # 精选评论
      },
      "attribute": [{
        "name": "品牌",
        "value": "Apple"
      },
      {
        "name": "颜色",
        "value": "银色、黑色"
      },
      {
        "name": "容量",
        "value": "64G、256G"
      }
      ] # 商品属性
    }
    return jsonify({"code":200,"res":res})




if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)