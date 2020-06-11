## 这是本项目整个包的初始化的东西 暂时没用
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy


engine=create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
def init_db():
    import model
    Base.metadata.create_all(bind=engine)