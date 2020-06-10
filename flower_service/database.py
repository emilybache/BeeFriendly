from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import String


db_url = 'mysql+pymysql://root:mysqlpwd@localhost:3306/flowerdb'
engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Flower(Base):
    __tablename__ = 'flowers'
    name = Column(String, primary_key=True)
    flowering_months = Column(String)
    description = Column(String)

    @staticmethod
    def get(name):
        return session.query(Flower).get(name)
