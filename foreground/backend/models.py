# coding: utf-8
from sqlalchemy import BigInteger, Column, DECIMAL, Date, DateTime, Integer, Table, Time, VARBINARY, text
from sqlalchemy.dialects.mysql import TEXT, TINYINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CmsHelp(Base):
    __tablename__ = 'cms_help'
    __table_args__ = {'comment': '帮助表'}

    id = Column(BigInteger, primary_key=True)
    category_id = Column(BigInteger)
    icon = Column(VARCHAR(500))
    title = Column(VARCHAR(100))
    show_status = Column(Integer)
    create_time = Column(DateTime)
    read_count = Column(Integer)
    content = Column(TEXT)


class CmsHelpCategory(Base):
    __tablename__ = 'cms_help_category'
    __table_args__ = {'comment': '帮助分类表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    icon = Column(VARCHAR(500), comment='分类图标')
    help_count = Column(Integer, comment='专题数量')
    show_status = Column(Integer)
    sort = Column(Integer)


t_cms_member_report = Table(
    'cms_member_report', metadata,
    Column('id', BigInteger),
    Column('report_type', Integer, comment='举报类型：0->商品评价；1->话题内容；2->用户评论'),
    Column('report_member_name', VARCHAR(100), comment='举报人'),
    Column('create_time', DateTime),
    Column('report_object', VARCHAR(100)),
    Column('report_status', Integer, comment='举报状态：0->未处理；1->已处理'),
    Column('handle_status', Integer, comment='处理结果：0->无效；1->有效；2->恶意'),
    Column('note', VARCHAR(200)),
    comment='用户举报表'
)


class CmsPrefrenceArea(Base):
    __tablename__ = 'cms_prefrence_area'
    __table_args__ = {'comment': '优选专区'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(255))
    sub_title = Column(VARCHAR(255))
    pic = Column(VARBINARY(500), comment='展示图片')
    sort = Column(Integer)
    show_status = Column(Integer)


class CmsPrefrenceAreaProductRelation(Base):
    __tablename__ = 'cms_prefrence_area_product_relation'
    __table_args__ = {'comment': '优选专区和产品关系表'}

    id = Column(BigInteger, primary_key=True)
    prefrence_area_id = Column(BigInteger)
    product_id = Column(BigInteger)


class CmsSubject(Base):
    __tablename__ = 'cms_subject'
    __table_args__ = {'comment': '专题表'}

    id = Column(BigInteger, primary_key=True)
    category_id = Column(BigInteger)
    title = Column(VARCHAR(100))
    pic = Column(VARCHAR(500), comment='专题主图')
    product_count = Column(Integer, comment='关联产品数量')
    recommend_status = Column(Integer)
    create_time = Column(DateTime)
    collect_count = Column(Integer)
    read_count = Column(Integer)
    comment_count = Column(Integer)
    album_pics = Column(VARCHAR(1000), comment='画册图片用逗号分割')
    description = Column(VARCHAR(1000))
    show_status = Column(Integer, comment='显示状态：0->不显示；1->显示')
    content = Column(TEXT)
    forward_count = Column(Integer, comment='转发数')
    category_name = Column(VARCHAR(200), comment='专题分类名称')


class CmsSubjectCategory(Base):
    __tablename__ = 'cms_subject_category'
    __table_args__ = {'comment': '专题分类表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    icon = Column(VARCHAR(500), comment='分类图标')
    subject_count = Column(Integer, comment='专题数量')
    show_status = Column(Integer)
    sort = Column(Integer)


class CmsSubjectComment(Base):
    __tablename__ = 'cms_subject_comment'
    __table_args__ = {'comment': '专题评论表'}

    id = Column(BigInteger, primary_key=True)
    subject_id = Column(BigInteger)
    member_nick_name = Column(VARCHAR(255))
    member_icon = Column(VARCHAR(255))
    content = Column(VARCHAR(1000))
    create_time = Column(DateTime)
    show_status = Column(Integer)


class CmsSubjectProductRelation(Base):
    __tablename__ = 'cms_subject_product_relation'
    __table_args__ = {'comment': '专题商品关系表'}

    id = Column(BigInteger, primary_key=True)
    subject_id = Column(BigInteger)
    product_id = Column(BigInteger)


class CmsTopic(Base):
    __tablename__ = 'cms_topic'
    __table_args__ = {'comment': '话题表'}

    id = Column(BigInteger, primary_key=True)
    category_id = Column(BigInteger)
    name = Column(VARCHAR(255))
    create_time = Column(DateTime)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    attend_count = Column(Integer, comment='参与人数')
    attention_count = Column(Integer, comment='关注人数')
    read_count = Column(Integer)
    award_name = Column(VARCHAR(100), comment='奖品名称')
    attend_type = Column(VARCHAR(100), comment='参与方式')
    content = Column(TEXT, comment='话题内容')


class CmsTopicCategory(Base):
    __tablename__ = 'cms_topic_category'
    __table_args__ = {'comment': '话题分类表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    icon = Column(VARCHAR(500), comment='分类图标')
    subject_count = Column(Integer, comment='专题数量')
    show_status = Column(Integer)
    sort = Column(Integer)


class CmsTopicComment(Base):
    __tablename__ = 'cms_topic_comment'
    __table_args__ = {'comment': '专题评论表'}

    id = Column(BigInteger, primary_key=True)
    member_nick_name = Column(VARCHAR(255))
    topic_id = Column(BigInteger)
    member_icon = Column(VARCHAR(255))
    content = Column(VARCHAR(1000))
    create_time = Column(DateTime)
    show_status = Column(Integer)


t_font_banner = Table(
    'font_banner', metadata,
    Column('banner_id', Integer),
    Column('product_id', Integer),
    Column('picture_src', VARCHAR(255)),
    Column('createTime', DateTime),
    Column('display', TINYINT(1))
)


class OmsCartItem(Base):
    __tablename__ = 'oms_cart_item'
    __table_args__ = {'comment': '购物车表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    product_sku_id = Column(BigInteger)
    member_id = Column(BigInteger)
    quantity = Column(Integer, comment='购买数量')
    price = Column(DECIMAL(10, 2), comment='添加到购物车的价格')
    product_pic = Column(VARCHAR(1000), comment='商品主图')
    product_name = Column(VARCHAR(500), comment='商品名称')
    product_sub_title = Column(VARCHAR(500), comment='商品副标题（卖点）')
    product_sku_code = Column(VARCHAR(200), comment='商品sku条码')
    member_nickname = Column(VARCHAR(500), comment='会员昵称')
    create_date = Column(DateTime, comment='创建时间')
    modify_date = Column(DateTime, comment='修改时间')
    delete_status = Column(Integer, server_default=text("'0'"), comment='是否删除')
    product_category_id = Column(BigInteger, comment='商品分类')
    product_brand = Column(VARCHAR(200))
    product_sn = Column(VARCHAR(200))
    product_attr = Column(VARCHAR(500), comment='商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]')


class OmsCompanyAddres(Base):
    __tablename__ = 'oms_company_address'
    __table_args__ = {'comment': '公司收发货地址表'}

    id = Column(BigInteger, primary_key=True)
    address_name = Column(VARCHAR(200), comment='地址名称')
    send_status = Column(Integer, comment='默认发货地址：0->否；1->是')
    receive_status = Column(Integer, comment='是否默认收货地址：0->否；1->是')
    name = Column(VARCHAR(64), comment='收发货人姓名')
    phone = Column(VARCHAR(64), comment='收货人电话')
    province = Column(VARCHAR(64), comment='省/直辖市')
    city = Column(VARCHAR(64), comment='市')
    region = Column(VARCHAR(64), comment='区')
    detail_address = Column(VARCHAR(200), comment='详细地址')


class OmsOrder(Base):
    __tablename__ = 'oms_order'
    __table_args__ = {'comment': '订单表'}

    id = Column(BigInteger, primary_key=True, comment='订单id')
    member_id = Column(BigInteger, nullable=False)
    coupon_id = Column(BigInteger)
    order_sn = Column(VARCHAR(64), comment='订单编号')
    create_time = Column(DateTime, comment='提交时间')
    member_username = Column(VARCHAR(64), comment='用户帐号')
    total_amount = Column(DECIMAL(10, 2), comment='订单总金额')
    pay_amount = Column(DECIMAL(10, 2), comment='应付金额（实际支付金额）')
    freight_amount = Column(DECIMAL(10, 2), comment='运费金额')
    promotion_amount = Column(DECIMAL(10, 2), comment='促销优化金额（促销价、满减、阶梯价）')
    integration_amount = Column(DECIMAL(10, 2), comment='积分抵扣金额')
    coupon_amount = Column(DECIMAL(10, 2), comment='优惠券抵扣金额')
    discount_amount = Column(DECIMAL(10, 2), comment='管理员后台调整订单使用的折扣金额')
    pay_type = Column(Integer, comment='支付方式：0->未支付；1->支付宝；2->微信')
    source_type = Column(Integer, comment='订单来源：0->PC订单；1->app订单')
    status = Column(Integer, comment='订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单')
    order_type = Column(Integer, comment='订单类型：0->正常订单；1->秒杀订单')
    delivery_company = Column(VARCHAR(64), comment='物流公司(配送方式)')
    delivery_sn = Column(VARCHAR(64), comment='物流单号')
    auto_confirm_day = Column(Integer, comment='自动确认时间（天）')
    integration = Column(Integer, comment='可以获得的积分')
    growth = Column(Integer, comment='可以活动的成长值')
    promotion_info = Column(VARCHAR(100), comment='活动信息')
    bill_type = Column(Integer, comment='发票类型：0->不开发票；1->电子发票；2->纸质发票')
    bill_header = Column(VARCHAR(200), comment='发票抬头')
    bill_content = Column(VARCHAR(200), comment='发票内容')
    bill_receiver_phone = Column(VARCHAR(32), comment='收票人电话')
    bill_receiver_email = Column(VARCHAR(64), comment='收票人邮箱')
    receiver_name = Column(VARCHAR(100), nullable=False, comment='收货人姓名')
    receiver_phone = Column(VARCHAR(32), nullable=False, comment='收货人电话')
    receiver_post_code = Column(VARCHAR(32), comment='收货人邮编')
    receiver_province = Column(VARCHAR(32), comment='省份/直辖市')
    receiver_city = Column(VARCHAR(32), comment='城市')
    receiver_region = Column(VARCHAR(32), comment='区')
    receiver_detail_address = Column(VARCHAR(200), comment='详细地址')
    note = Column(VARCHAR(500), comment='订单备注')
    confirm_status = Column(Integer, comment='确认收货状态：0->未确认；1->已确认')
    delete_status = Column(Integer, nullable=False, server_default=text("'0'"), comment='删除状态：0->未删除；1->已删除')
    use_integration = Column(Integer, comment='下单时使用的积分')
    payment_time = Column(DateTime, comment='支付时间')
    delivery_time = Column(DateTime, comment='发货时间')
    receive_time = Column(DateTime, comment='确认收货时间')
    comment_time = Column(DateTime, comment='评价时间')
    modify_time = Column(DateTime, comment='修改时间')


class OmsOrderItem(Base):
    __tablename__ = 'oms_order_item'
    __table_args__ = {'comment': '订单中所包含的商品'}

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, comment='订单id')
    order_sn = Column(VARCHAR(64), comment='订单编号')
    product_id = Column(BigInteger)
    product_pic = Column(VARCHAR(500))
    product_name = Column(VARCHAR(200))
    product_brand = Column(VARCHAR(200))
    product_sn = Column(VARCHAR(64))
    product_price = Column(DECIMAL(10, 2), comment='销售价格')
    product_quantity = Column(Integer, comment='购买数量')
    product_sku_id = Column(BigInteger, comment='商品sku编号')
    product_sku_code = Column(VARCHAR(50), comment='商品sku条码')
    product_category_id = Column(BigInteger, comment='商品分类id')
    promotion_name = Column(VARCHAR(200), comment='商品促销名称')
    promotion_amount = Column(DECIMAL(10, 2), comment='商品促销分解金额')
    coupon_amount = Column(DECIMAL(10, 2), comment='优惠券优惠分解金额')
    integration_amount = Column(DECIMAL(10, 2), comment='积分优惠分解金额')
    real_amount = Column(DECIMAL(10, 2), comment='该商品经过优惠后的分解金额')
    gift_integration = Column(Integer, server_default=text("'0'"))
    gift_growth = Column(Integer, server_default=text("'0'"))
    product_attr = Column(VARCHAR(500), comment='商品销售属性:[{"key":"颜色","value":"颜色"},{"key":"容量","value":"4G"}]')


class OmsOrderOperateHistory(Base):
    __tablename__ = 'oms_order_operate_history'
    __table_args__ = {'comment': '订单操作历史记录'}

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, comment='订单id')
    operate_man = Column(VARCHAR(100), comment='操作人：用户；系统；后台管理员')
    create_time = Column(DateTime, comment='操作时间')
    order_status = Column(Integer, comment='订单状态：0->待付款；1->待发货；2->已发货；3->已完成；4->已关闭；5->无效订单')
    note = Column(VARCHAR(500), comment='备注')


class OmsOrderReturnApply(Base):
    __tablename__ = 'oms_order_return_apply'
    __table_args__ = {'comment': '订单退货申请'}

    id = Column(BigInteger, primary_key=True)
    order_id = Column(BigInteger, comment='订单id')
    company_address_id = Column(BigInteger, comment='收货地址表id')
    product_id = Column(BigInteger, comment='退货商品id')
    order_sn = Column(VARCHAR(64), comment='订单编号')
    create_time = Column(DateTime, comment='申请时间')
    member_username = Column(VARCHAR(64), comment='会员用户名')
    return_amount = Column(DECIMAL(10, 2), comment='退款金额')
    return_name = Column(VARCHAR(100), comment='退货人姓名')
    return_phone = Column(VARCHAR(100), comment='退货人电话')
    status = Column(Integer, comment='申请状态：0->待处理；1->退货中；2->已完成；3->已拒绝')
    handle_time = Column(DateTime, comment='处理时间')
    product_pic = Column(VARCHAR(500), comment='商品图片')
    product_name = Column(VARCHAR(200), comment='商品名称')
    product_brand = Column(VARCHAR(200), comment='商品品牌')
    product_attr = Column(VARCHAR(500), comment='商品销售属性：颜色：红色；尺码：xl;')
    product_count = Column(Integer, comment='退货数量')
    product_price = Column(DECIMAL(10, 2), comment='商品单价')
    product_real_price = Column(DECIMAL(10, 2), comment='商品实际支付单价')
    reason = Column(VARCHAR(200), comment='原因')
    description = Column(VARCHAR(500), comment='描述')
    proof_pics = Column(VARCHAR(1000), comment='凭证图片，以逗号隔开')
    handle_note = Column(VARCHAR(500), comment='处理备注')
    handle_man = Column(VARCHAR(100), comment='处理人员')
    receive_man = Column(VARCHAR(100), comment='收货人')
    receive_time = Column(DateTime, comment='收货时间')
    receive_note = Column(VARCHAR(500), comment='收货备注')


class OmsOrderReturnReason(Base):
    __tablename__ = 'oms_order_return_reason'
    __table_args__ = {'comment': '退货原因表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100), comment='退货类型')
    sort = Column(Integer)
    status = Column(Integer, comment='状态：0->不启用；1->启用')
    create_time = Column(DateTime, comment='添加时间')


class OmsOrderSetting(Base):
    __tablename__ = 'oms_order_setting'
    __table_args__ = {'comment': '订单设置表'}

    id = Column(BigInteger, primary_key=True)
    flash_order_overtime = Column(Integer, comment='秒杀订单超时关闭时间(分)')
    normal_order_overtime = Column(Integer, comment='正常订单超时时间(分)')
    confirm_overtime = Column(Integer, comment='发货后自动确认收货时间（天）')
    finish_overtime = Column(Integer, comment='自动完成交易时间，不能申请售后（天）')
    comment_overtime = Column(Integer, comment='订单完成后自动好评时间（天）')


class PmsAlbum(Base):
    __tablename__ = 'pms_album'
    __table_args__ = {'comment': '相册表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(64))
    cover_pic = Column(VARCHAR(1000))
    pic_count = Column(Integer)
    sort = Column(Integer)
    description = Column(VARCHAR(1000))


class PmsAlbumPic(Base):
    __tablename__ = 'pms_album_pic'
    __table_args__ = {'comment': '画册图片表'}

    id = Column(BigInteger, primary_key=True)
    album_id = Column(BigInteger)
    pic = Column(VARCHAR(1000))


class PmsBrand(Base):
    __tablename__ = 'pms_brand'
    __table_args__ = {'comment': '品牌表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(64))
    first_letter = Column(VARCHAR(8), comment='首字母')
    sort = Column(Integer)
    factory_status = Column(Integer, comment='是否为品牌制造商：0->不是；1->是')
    show_status = Column(Integer)
    product_count = Column(Integer, comment='产品数量')
    product_comment_count = Column(Integer, comment='产品评论数量')
    logo = Column(VARCHAR(255), comment='品牌logo')
    big_pic = Column(VARCHAR(255), comment='专区大图')
    brand_story = Column(TEXT, comment='品牌故事')


class PmsComment(Base):
    __tablename__ = 'pms_comment'
    __table_args__ = {'comment': '商品评价表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    member_nick_name = Column(VARCHAR(255))
    product_name = Column(VARCHAR(255))
    star = Column(Integer, comment='评价星数：0->5')
    member_ip = Column(VARCHAR(64), comment='评价的ip')
    create_time = Column(DateTime)
    show_status = Column(Integer)
    product_attribute = Column(VARCHAR(255), comment='购买时的商品属性')
    collect_couont = Column(Integer)
    read_count = Column(Integer)
    content = Column(TEXT)
    pics = Column(VARCHAR(1000), comment='上传图片地址，以逗号隔开')
    member_icon = Column(VARCHAR(255), comment='评论用户头像')
    replay_count = Column(Integer)


class PmsCommentReplay(Base):
    __tablename__ = 'pms_comment_replay'
    __table_args__ = {'comment': '产品评价回复表'}

    id = Column(BigInteger, primary_key=True)
    comment_id = Column(BigInteger)
    member_nick_name = Column(VARCHAR(255))
    member_icon = Column(VARCHAR(255))
    content = Column(VARCHAR(1000))
    create_time = Column(DateTime)
    type = Column(Integer, comment='评论人员类型；0->会员；1->管理员')


class PmsFeightTemplate(Base):
    __tablename__ = 'pms_feight_template'
    __table_args__ = {'comment': '运费模版'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(64))
    charge_type = Column(Integer, comment='计费类型:0->按重量；1->按件数')
    first_weight = Column(DECIMAL(10, 2), comment='首重kg')
    first_fee = Column(DECIMAL(10, 2), comment='首费（元）')
    continue_weight = Column(DECIMAL(10, 2))
    continme_fee = Column(DECIMAL(10, 2))
    dest = Column(VARCHAR(255), comment='目的地（省、市）')


class PmsMemberPrice(Base):
    __tablename__ = 'pms_member_price'
    __table_args__ = {'comment': '商品会员价格表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    member_level_id = Column(BigInteger)
    member_price = Column(DECIMAL(10, 2), comment='会员价格')
    member_level_name = Column(VARCHAR(100))


class PmsProduct(Base):
    __tablename__ = 'pms_product'
    __table_args__ = {'comment': '商品信息'}

    id = Column(BigInteger, primary_key=True)
    brand_id = Column(BigInteger)
    product_category_id = Column(BigInteger)
    feight_template_id = Column(BigInteger)
    product_attribute_category_id = Column(BigInteger)
    name = Column(VARCHAR(64), nullable=False)
    pic = Column(VARCHAR(255))
    product_sn = Column(VARCHAR(64), nullable=False, comment='货号')
    delete_status = Column(Integer, comment='删除状态：0->未删除；1->已删除')
    publish_status = Column(Integer, comment='上架状态：0->下架；1->上架')
    new_status = Column(Integer, comment='新品状态:0->不是新品；1->新品')
    recommand_status = Column(Integer, comment='推荐状态；0->不推荐；1->推荐')
    verify_status = Column(Integer, comment='审核状态：0->未审核；1->审核通过')
    sort = Column(Integer, comment='排序')
    sale = Column(Integer, comment='销量')
    price = Column(DECIMAL(10, 2))
    promotion_price = Column(DECIMAL(10, 2), comment='促销价格')
    gift_growth = Column(Integer, server_default=text("'0'"), comment='赠送的成长值')
    gift_point = Column(Integer, server_default=text("'0'"), comment='赠送的积分')
    use_point_limit = Column(Integer, comment='限制使用的积分数')
    sub_title = Column(VARCHAR(255), comment='副标题')
    description = Column(TEXT, comment='商品描述')
    original_price = Column(DECIMAL(10, 2), comment='市场价')
    stock = Column(Integer, comment='库存')
    low_stock = Column(Integer, comment='库存预警值')
    unit = Column(VARCHAR(16), comment='单位')
    weight = Column(DECIMAL(10, 2), comment='商品重量，默认为克')
    preview_status = Column(Integer, comment='是否为预告商品：0->不是；1->是')
    service_ids = Column(VARCHAR(64), comment='以逗号分割的产品服务：1->无忧退货；2->快速退款；3->免费包邮')
    keywords = Column(VARCHAR(255))
    note = Column(VARCHAR(255))
    album_pics = Column(VARCHAR(255), comment='画册图片，连产品图片限制为5张，以逗号分割')
    detail_title = Column(VARCHAR(255))
    detail_desc = Column(TEXT)
    detail_html = Column(TEXT, comment='产品详情网页内容')
    detail_mobile_html = Column(TEXT, comment='移动端网页详情')
    promotion_start_time = Column(DateTime, comment='促销开始时间')
    promotion_end_time = Column(DateTime, comment='促销结束时间')
    promotion_per_limit = Column(Integer, comment='活动限购数量')
    promotion_type = Column(Integer, comment='促销类型：0->没有促销使用原价;1->使用促销价；2->使用会员价；3->使用阶梯价格；4->使用满减价格；5->限时购')
    brand_name = Column(VARCHAR(255), comment='品牌名称')
    product_category_name = Column(VARCHAR(255), comment='商品分类名称')


class PmsProductAttribute(Base):
    __tablename__ = 'pms_product_attribute'
    __table_args__ = {'comment': '商品属性参数表'}

    id = Column(BigInteger, primary_key=True)
    product_attribute_category_id = Column(BigInteger)
    name = Column(VARCHAR(64))
    select_type = Column(Integer, comment='属性选择类型：0->唯一；1->单选；2->多选')
    input_type = Column(Integer, comment='属性录入方式：0->手工录入；1->从列表中选取')
    input_list = Column(VARCHAR(255), comment='可选值列表，以逗号隔开')
    sort = Column(Integer, comment='排序字段：最高的可以单独上传图片')
    filter_type = Column(Integer, comment='分类筛选样式：1->普通；1->颜色')
    search_type = Column(Integer, comment='检索类型；0->不需要进行检索；1->关键字检索；2->范围检索')
    related_status = Column(Integer, comment='相同属性产品是否关联；0->不关联；1->关联')
    hand_add_status = Column(Integer, comment='是否支持手动新增；0->不支持；1->支持')
    type = Column(Integer, comment='属性的类型；0->规格；1->参数')


class PmsProductAttributeCategory(Base):
    __tablename__ = 'pms_product_attribute_category'
    __table_args__ = {'comment': '产品属性分类表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(64))
    attribute_count = Column(Integer, server_default=text("'0'"), comment='属性数量')
    param_count = Column(Integer, server_default=text("'0'"), comment='参数数量')


class PmsProductAttributeValue(Base):
    __tablename__ = 'pms_product_attribute_value'
    __table_args__ = {'comment': '存储产品参数信息的表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    product_attribute_id = Column(BigInteger)
    value = Column(VARCHAR(64), comment='手动添加规格或参数的值，参数单值，规格有多个时以逗号隔开')


class PmsProductCategory(Base):
    __tablename__ = 'pms_product_category'
    __table_args__ = {'comment': '产品分类'}

    id = Column(BigInteger, primary_key=True)
    parent_id = Column(BigInteger, comment='上机分类的编号：0表示一级分类')
    name = Column(VARCHAR(64))
    level = Column(Integer, comment='分类级别：0->1级；1->2级')
    product_count = Column(Integer)
    product_unit = Column(VARCHAR(64))
    nav_status = Column(Integer, comment='是否显示在导航栏：0->不显示；1->显示')
    show_status = Column(Integer, comment='显示状态：0->不显示；1->显示')
    sort = Column(Integer)
    icon = Column(VARCHAR(255), comment='图标')
    keywords = Column(VARCHAR(255))
    description = Column(TEXT, comment='描述')


class PmsProductCategoryAttributeRelation(Base):
    __tablename__ = 'pms_product_category_attribute_relation'
    __table_args__ = {'comment': '产品的分类和属性的关系表，用于设置分类筛选条件（只支持一级分类）'}

    id = Column(BigInteger, primary_key=True)
    product_category_id = Column(BigInteger)
    product_attribute_id = Column(BigInteger)


class PmsProductFullReduction(Base):
    __tablename__ = 'pms_product_full_reduction'
    __table_args__ = {'comment': '产品满减表(只针对同商品)'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    full_price = Column(DECIMAL(10, 2))
    reduce_price = Column(DECIMAL(10, 2))


class PmsProductLadder(Base):
    __tablename__ = 'pms_product_ladder'
    __table_args__ = {'comment': '产品阶梯价格表(只针对同商品)'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    count = Column(Integer, comment='满足的商品数量')
    discount = Column(DECIMAL(10, 2), comment='折扣')
    price = Column(DECIMAL(10, 2), comment='折后价格')


class PmsProductOperateLog(Base):
    __tablename__ = 'pms_product_operate_log'

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    price_old = Column(DECIMAL(10, 2))
    price_new = Column(DECIMAL(10, 2))
    sale_price_old = Column(DECIMAL(10, 2))
    sale_price_new = Column(DECIMAL(10, 2))
    gift_point_old = Column(Integer, comment='赠送的积分')
    gift_point_new = Column(Integer)
    use_point_limit_old = Column(Integer)
    use_point_limit_new = Column(Integer)
    operate_man = Column(VARCHAR(64), comment='操作人')
    create_time = Column(DateTime)


class PmsProductVertifyRecord(Base):
    __tablename__ = 'pms_product_vertify_record'
    __table_args__ = {'comment': '商品审核记录'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    create_time = Column(DateTime)
    vertify_man = Column(VARCHAR(64), comment='审核人')
    status = Column(Integer)
    detail = Column(VARCHAR(255), comment='反馈详情')


class PmsSkuStock(Base):
    __tablename__ = 'pms_sku_stock'
    __table_args__ = {'comment': 'sku的库存'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    sku_code = Column(VARCHAR(64), nullable=False, comment='sku编码')
    price = Column(DECIMAL(10, 2))
    stock = Column(Integer, server_default=text("'0'"), comment='库存')
    low_stock = Column(Integer, comment='预警库存')
    pic = Column(VARCHAR(255), comment='展示图片')
    sale = Column(Integer, comment='销量')
    promotion_price = Column(DECIMAL(10, 2), comment='单品促销价格')
    lock_stock = Column(Integer, server_default=text("'0'"), comment='锁定库存')
    sp_data = Column(VARCHAR(500), comment='商品销售属性，json格式')


class SmsCoupon(Base):
    __tablename__ = 'sms_coupon'
    __table_args__ = {'comment': '优惠卷表'}

    id = Column(BigInteger, primary_key=True)
    type = Column(Integer, comment='优惠卷类型；0->全场赠券；1->会员赠券；2->购物赠券；3->注册赠券')
    name = Column(VARCHAR(100))
    platform = Column(Integer, comment='使用平台：0->全部；1->移动；2->PC')
    count = Column(Integer, comment='数量')
    amount = Column(DECIMAL(10, 2), comment='金额')
    per_limit = Column(Integer, comment='每人限领张数')
    min_point = Column(DECIMAL(10, 2), comment='使用门槛；0表示无门槛')
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    use_type = Column(Integer, comment='使用类型：0->全场通用；1->指定分类；2->指定商品')
    note = Column(VARCHAR(200), comment='备注')
    publish_count = Column(Integer, comment='发行数量')
    use_count = Column(Integer, comment='已使用数量')
    receive_count = Column(Integer, comment='领取数量')
    enable_time = Column(DateTime, comment='可以领取的日期')
    code = Column(VARCHAR(64), comment='优惠码')
    member_level = Column(Integer, comment='可领取的会员类型：0->无限时')


class SmsCouponHistory(Base):
    __tablename__ = 'sms_coupon_history'
    __table_args__ = {'comment': '优惠券使用、领取历史表'}

    id = Column(BigInteger, primary_key=True)
    coupon_id = Column(BigInteger, index=True)
    member_id = Column(BigInteger, index=True)
    coupon_code = Column(VARCHAR(64))
    member_nickname = Column(VARCHAR(64), comment='领取人昵称')
    get_type = Column(Integer, comment='获取类型：0->后台赠送；1->主动获取')
    create_time = Column(DateTime)
    use_status = Column(Integer, comment='使用状态：0->未使用；1->已使用；2->已过期')
    use_time = Column(DateTime, comment='使用时间')
    order_id = Column(BigInteger, comment='订单编号')
    order_sn = Column(VARCHAR(100), comment='订单号码')


class SmsCouponProductCategoryRelation(Base):
    __tablename__ = 'sms_coupon_product_category_relation'
    __table_args__ = {'comment': '优惠券和产品分类关系表'}

    id = Column(BigInteger, primary_key=True)
    coupon_id = Column(BigInteger)
    product_category_id = Column(BigInteger)
    product_category_name = Column(VARCHAR(200), comment='产品分类名称')
    parent_category_name = Column(VARCHAR(200), comment='父分类名称')


class SmsCouponProductRelation(Base):
    __tablename__ = 'sms_coupon_product_relation'
    __table_args__ = {'comment': '优惠券和产品的关系表'}

    id = Column(BigInteger, primary_key=True)
    coupon_id = Column(BigInteger)
    product_id = Column(BigInteger)
    product_name = Column(VARCHAR(500), comment='商品名称')
    product_sn = Column(VARCHAR(200), comment='商品编码')


class SmsFlashPromotion(Base):
    __tablename__ = 'sms_flash_promotion'
    __table_args__ = {'comment': '限时购表'}

    id = Column(BigInteger, primary_key=True)
    title = Column(VARCHAR(200))
    start_date = Column(Date, comment='开始日期')
    end_date = Column(Date, comment='结束日期')
    status = Column(Integer, comment='上下线状态')
    create_time = Column(DateTime, comment='秒杀时间段名称')


class SmsFlashPromotionLog(Base):
    __tablename__ = 'sms_flash_promotion_log'
    __table_args__ = {'comment': '限时购通知记录'}

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer)
    product_id = Column(BigInteger)
    member_phone = Column(VARCHAR(64))
    product_name = Column(VARCHAR(100))
    subscribe_time = Column(DateTime, comment='会员订阅时间')
    send_time = Column(DateTime)


class SmsFlashPromotionProductRelation(Base):
    __tablename__ = 'sms_flash_promotion_product_relation'
    __table_args__ = {'comment': '商品限时购与商品关系表'}

    id = Column(BigInteger, primary_key=True, comment='编号')
    flash_promotion_id = Column(BigInteger)
    flash_promotion_session_id = Column(BigInteger, comment='编号')
    product_id = Column(BigInteger)
    flash_promotion_price = Column(DECIMAL(10, 2), comment='限时购价格')
    flash_promotion_count = Column(Integer, comment='限时购数量')
    flash_promotion_limit = Column(Integer, comment='每人限购数量')
    sort = Column(Integer, comment='排序')


class SmsFlashPromotionSession(Base):
    __tablename__ = 'sms_flash_promotion_session'
    __table_args__ = {'comment': '限时购场次表'}

    id = Column(BigInteger, primary_key=True, comment='编号')
    name = Column(VARCHAR(200), comment='场次名称')
    start_time = Column(Time, comment='每日开始时间')
    end_time = Column(Time, comment='每日结束时间')
    status = Column(Integer, comment='启用状态：0->不启用；1->启用')
    create_time = Column(DateTime, comment='创建时间')


class SmsHomeAdvertise(Base):
    __tablename__ = 'sms_home_advertise'
    __table_args__ = {'comment': '首页轮播广告表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    type = Column(Integer, comment='轮播位置：0->PC首页轮播；1->app首页轮播')
    pic = Column(VARCHAR(500))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(Integer, comment='上下线状态：0->下线；1->上线')
    click_count = Column(Integer, comment='点击数')
    order_count = Column(Integer, comment='下单数')
    url = Column(VARCHAR(500), comment='链接地址')
    note = Column(VARCHAR(500), comment='备注')
    sort = Column(Integer, server_default=text("'0'"), comment='排序')


class SmsHomeBrand(Base):
    __tablename__ = 'sms_home_brand'
    __table_args__ = {'comment': '首页推荐品牌表'}

    id = Column(BigInteger, primary_key=True)
    brand_id = Column(BigInteger)
    brand_name = Column(VARCHAR(64))
    recommend_status = Column(Integer)
    sort = Column(Integer)


class SmsHomeNewProduct(Base):
    __tablename__ = 'sms_home_new_product'
    __table_args__ = {'comment': '新鲜好物表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    product_name = Column(VARCHAR(64))
    recommend_status = Column(Integer)
    sort = Column(Integer)


class SmsHomeRecommendProduct(Base):
    __tablename__ = 'sms_home_recommend_product'
    __table_args__ = {'comment': '人气推荐商品表'}

    id = Column(BigInteger, primary_key=True)
    product_id = Column(BigInteger)
    product_name = Column(VARCHAR(64))
    recommend_status = Column(Integer)
    sort = Column(Integer)


class SmsHomeRecommendSubject(Base):
    __tablename__ = 'sms_home_recommend_subject'
    __table_args__ = {'comment': '首页推荐专题表'}

    id = Column(BigInteger, primary_key=True)
    subject_id = Column(BigInteger)
    subject_name = Column(VARCHAR(64))
    recommend_status = Column(Integer)
    sort = Column(Integer)


class UmsAdmin(Base):
    __tablename__ = 'ums_admin'
    __table_args__ = {'comment': '后台用户表'}

    id = Column(BigInteger, primary_key=True)
    username = Column(VARCHAR(64))
    password = Column(VARCHAR(64))
    icon = Column(VARCHAR(500), comment='头像')
    email = Column(VARCHAR(100), comment='邮箱')
    nick_name = Column(VARCHAR(200), comment='昵称')
    note = Column(VARCHAR(500), comment='备注信息')
    create_time = Column(DateTime, comment='创建时间')
    login_time = Column(DateTime, comment='最后登录时间')
    status = Column(Integer, server_default=text("'1'"), comment='帐号启用状态：0->禁用；1->启用')


class UmsAdminLoginLog(Base):
    __tablename__ = 'ums_admin_login_log'
    __table_args__ = {'comment': '后台用户登录日志表'}

    id = Column(BigInteger, primary_key=True)
    admin_id = Column(BigInteger)
    create_time = Column(DateTime)
    ip = Column(VARCHAR(64))
    address = Column(VARCHAR(100))
    user_agent = Column(VARCHAR(100), comment='浏览器登录类型')


class UmsAdminPermissionRelation(Base):
    __tablename__ = 'ums_admin_permission_relation'
    __table_args__ = {'comment': '后台用户和权限关系表(除角色中定义的权限以外的加减权限)'}

    id = Column(BigInteger, primary_key=True)
    admin_id = Column(BigInteger)
    permission_id = Column(BigInteger)
    type = Column(Integer)


class UmsAdminRoleRelation(Base):
    __tablename__ = 'ums_admin_role_relation'
    __table_args__ = {'comment': '后台用户和角色关系表'}

    id = Column(BigInteger, primary_key=True)
    admin_id = Column(BigInteger)
    role_id = Column(BigInteger)


class UmsGrowthChangeHistory(Base):
    __tablename__ = 'ums_growth_change_history'
    __table_args__ = {'comment': '成长值变化历史记录表'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    create_time = Column(DateTime)
    change_type = Column(Integer, comment='改变类型：0->增加；1->减少')
    change_count = Column(Integer, comment='积分改变数量')
    operate_man = Column(VARCHAR(100), comment='操作人员')
    operate_note = Column(VARCHAR(200), comment='操作备注')
    source_type = Column(Integer, comment='积分来源：0->购物；1->管理员修改')


class UmsIntegrationChangeHistory(Base):
    __tablename__ = 'ums_integration_change_history'
    __table_args__ = {'comment': '积分变化历史记录表'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    create_time = Column(DateTime)
    change_type = Column(Integer, comment='改变类型：0->增加；1->减少')
    change_count = Column(Integer, comment='积分改变数量')
    operate_man = Column(VARCHAR(100), comment='操作人员')
    operate_note = Column(VARCHAR(200), comment='操作备注')
    source_type = Column(Integer, comment='积分来源：0->购物；1->管理员修改')


class UmsIntegrationConsumeSetting(Base):
    __tablename__ = 'ums_integration_consume_setting'
    __table_args__ = {'comment': '积分消费设置'}

    id = Column(BigInteger, primary_key=True)
    deduction_per_amount = Column(Integer, comment='每一元需要抵扣的积分数量')
    max_percent_per_order = Column(Integer, comment='每笔订单最高抵用百分比')
    use_unit = Column(Integer, comment='每次使用积分最小单位100')
    coupon_status = Column(Integer, comment='是否可以和优惠券同用；0->不可以；1->可以')


class UmsMember(Base):
    __tablename__ = 'ums_member'
    __table_args__ = {'comment': '会员表'}

    id = Column(BigInteger, primary_key=True)
    member_level_id = Column(BigInteger)
    username = Column(VARCHAR(64), unique=True, comment='用户名')
    password = Column(VARCHAR(64), comment='密码')
    nickname = Column(VARCHAR(64), comment='昵称')
    phone = Column(VARCHAR(64), unique=True, comment='手机号码')
    status = Column(Integer, comment='帐号启用状态:0->禁用；1->启用')
    create_time = Column(DateTime, comment='注册时间')
    icon = Column(VARCHAR(500), comment='头像')
    gender = Column(Integer, comment='性别：0->未知；1->男；2->女')
    birthday = Column(Date, comment='生日')
    city = Column(VARCHAR(64), comment='所做城市')
    job = Column(VARCHAR(100), comment='职业')
    personalized_signature = Column(VARCHAR(200), comment='个性签名')
    source_type = Column(Integer, comment='用户来源')
    integration = Column(Integer, comment='积分')
    growth = Column(Integer, comment='成长值')
    luckey_count = Column(Integer, comment='剩余抽奖次数')
    history_integration = Column(Integer, comment='历史积分数量')


class UmsMemberLevel(Base):
    __tablename__ = 'ums_member_level'
    __table_args__ = {'comment': '会员等级表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    growth_point = Column(Integer)
    default_status = Column(Integer, comment='是否为默认等级：0->不是；1->是')
    free_freight_point = Column(DECIMAL(10, 2), comment='免运费标准')
    comment_growth_point = Column(Integer, comment='每次评价获取的成长值')
    priviledge_free_freight = Column(Integer, comment='是否有免邮特权')
    priviledge_sign_in = Column(Integer, comment='是否有签到特权')
    priviledge_comment = Column(Integer, comment='是否有评论获奖励特权')
    priviledge_promotion = Column(Integer, comment='是否有专享活动特权')
    priviledge_member_price = Column(Integer, comment='是否有会员价格特权')
    priviledge_birthday = Column(Integer, comment='是否有生日特权')
    note = Column(VARCHAR(200))


class UmsMemberLoginLog(Base):
    __tablename__ = 'ums_member_login_log'
    __table_args__ = {'comment': '会员登录记录'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    create_time = Column(DateTime)
    ip = Column(VARCHAR(64))
    city = Column(VARCHAR(64))
    login_type = Column(Integer, comment='登录类型：0->PC；1->android;2->ios;3->小程序')
    province = Column(VARCHAR(64))


class UmsMemberMemberTagRelation(Base):
    __tablename__ = 'ums_member_member_tag_relation'
    __table_args__ = {'comment': '用户和标签关系表'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    tag_id = Column(BigInteger)


class UmsMemberProductCategoryRelation(Base):
    __tablename__ = 'ums_member_product_category_relation'
    __table_args__ = {'comment': '会员与产品分类关系表（用户喜欢的分类）'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    product_category_id = Column(BigInteger)


class UmsMemberReceiveAddres(Base):
    __tablename__ = 'ums_member_receive_address'
    __table_args__ = {'comment': '会员收货地址表'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    name = Column(VARCHAR(100), comment='收货人名称')
    phone_number = Column(VARCHAR(64))
    default_status = Column(Integer, comment='是否为默认')
    post_code = Column(VARCHAR(100), comment='邮政编码')
    province = Column(VARCHAR(100), comment='省份/直辖市')
    city = Column(VARCHAR(100), comment='城市')
    region = Column(VARCHAR(100), comment='区')
    detail_address = Column(VARCHAR(128), comment='详细地址(街道)')


class UmsMemberRuleSetting(Base):
    __tablename__ = 'ums_member_rule_setting'
    __table_args__ = {'comment': '会员积分成长规则表'}

    id = Column(BigInteger, primary_key=True)
    continue_sign_day = Column(Integer, comment='连续签到天数')
    continue_sign_point = Column(Integer, comment='连续签到赠送数量')
    consume_per_point = Column(DECIMAL(10, 2), comment='每消费多少元获取1个点')
    low_order_amount = Column(DECIMAL(10, 2), comment='最低获取点数的订单金额')
    max_point_per_order = Column(Integer, comment='每笔订单最高获取点数')
    type = Column(Integer, comment='类型：0->积分规则；1->成长值规则')


class UmsMemberStatisticsInfo(Base):
    __tablename__ = 'ums_member_statistics_info'
    __table_args__ = {'comment': '会员统计信息'}

    id = Column(BigInteger, primary_key=True)
    member_id = Column(BigInteger)
    consume_amount = Column(DECIMAL(10, 2), comment='累计消费金额')
    order_count = Column(Integer, comment='订单数量')
    coupon_count = Column(Integer, comment='优惠券数量')
    comment_count = Column(Integer, comment='评价数')
    return_order_count = Column(Integer, comment='退货数量')
    login_count = Column(Integer, comment='登录次数')
    attend_count = Column(Integer, comment='关注数量')
    fans_count = Column(Integer, comment='粉丝数量')
    collect_product_count = Column(Integer)
    collect_subject_count = Column(Integer)
    collect_topic_count = Column(Integer)
    collect_comment_count = Column(Integer)
    invite_friend_count = Column(Integer)
    recent_order_time = Column(DateTime, comment='最后一次下订单时间')


class UmsMemberTag(Base):
    __tablename__ = 'ums_member_tag'
    __table_args__ = {'comment': '用户标签表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    finish_order_count = Column(Integer, comment='自动打标签完成订单数量')
    finish_order_amount = Column(DECIMAL(10, 2), comment='自动打标签完成订单金额')


class UmsMemberTask(Base):
    __tablename__ = 'ums_member_task'
    __table_args__ = {'comment': '会员任务表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100))
    growth = Column(Integer, comment='赠送成长值')
    intergration = Column(Integer, comment='赠送积分')
    type = Column(Integer, comment='任务类型：0->新手任务；1->日常任务')


class UmsMenu(Base):
    __tablename__ = 'ums_menu'
    __table_args__ = {'comment': '后台菜单表'}

    id = Column(BigInteger, primary_key=True)
    parent_id = Column(BigInteger, comment='父级ID')
    create_time = Column(DateTime, comment='创建时间')
    title = Column(VARCHAR(100), comment='菜单名称')
    level = Column(Integer, comment='菜单级数')
    sort = Column(Integer, comment='菜单排序')
    name = Column(VARCHAR(100), comment='前端名称')
    icon = Column(VARCHAR(200), comment='前端图标')
    hidden = Column(Integer, comment='前端隐藏')


class UmsPermission(Base):
    __tablename__ = 'ums_permission'
    __table_args__ = {'comment': '后台用户权限表'}

    id = Column(BigInteger, primary_key=True)
    pid = Column(BigInteger, comment='父级权限id')
    name = Column(VARCHAR(100), comment='名称')
    value = Column(VARCHAR(200), comment='权限值')
    icon = Column(VARCHAR(500), comment='图标')
    type = Column(Integer, comment='权限类型：0->目录；1->菜单；2->按钮（接口绑定权限）')
    uri = Column(VARCHAR(200), comment='前端资源路径')
    status = Column(Integer, comment='启用状态；0->禁用；1->启用')
    create_time = Column(DateTime, comment='创建时间')
    sort = Column(Integer, comment='排序')


class UmsResource(Base):
    __tablename__ = 'ums_resource'
    __table_args__ = {'comment': '后台资源表'}

    id = Column(BigInteger, primary_key=True)
    create_time = Column(DateTime, comment='创建时间')
    name = Column(VARCHAR(200), comment='资源名称')
    url = Column(VARCHAR(200), comment='资源URL')
    description = Column(VARCHAR(500), comment='描述')
    category_id = Column(BigInteger, comment='资源分类ID')


class UmsResourceCategory(Base):
    __tablename__ = 'ums_resource_category'
    __table_args__ = {'comment': '资源分类表'}

    id = Column(BigInteger, primary_key=True)
    create_time = Column(DateTime, comment='创建时间')
    name = Column(VARCHAR(200), comment='分类名称')
    sort = Column(Integer, comment='排序')


class UmsRole(Base):
    __tablename__ = 'ums_role'
    __table_args__ = {'comment': '后台用户角色表'}

    id = Column(BigInteger, primary_key=True)
    name = Column(VARCHAR(100), comment='名称')
    description = Column(VARCHAR(500), comment='描述')
    admin_count = Column(Integer, comment='后台用户数量')
    create_time = Column(DateTime, comment='创建时间')
    status = Column(Integer, server_default=text("'1'"), comment='启用状态：0->禁用；1->启用')
    sort = Column(Integer, server_default=text("'0'"))


class UmsRoleMenuRelation(Base):
    __tablename__ = 'ums_role_menu_relation'
    __table_args__ = {'comment': '后台角色菜单关系表'}

    id = Column(BigInteger, primary_key=True)
    role_id = Column(BigInteger, comment='角色ID')
    menu_id = Column(BigInteger, comment='菜单ID')


class UmsRolePermissionRelation(Base):
    __tablename__ = 'ums_role_permission_relation'
    __table_args__ = {'comment': '后台用户角色和权限关系表'}

    id = Column(BigInteger, primary_key=True)
    role_id = Column(BigInteger)
    permission_id = Column(BigInteger)


class UmsRoleResourceRelation(Base):
    __tablename__ = 'ums_role_resource_relation'
    __table_args__ = {'comment': '后台角色资源关系表'}

    id = Column(BigInteger, primary_key=True)
    role_id = Column(BigInteger, comment='角色ID')
    resource_id = Column(BigInteger, comment='资源ID')
