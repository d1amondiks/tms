from sqlalchemy import create_engine, Table, Column, Integer, String, \
    MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()
metadata = MetaData()
user = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String, nullable=False),
              Column('fullname', String),
              Column('password', String)
              )

# for t in metadata.sorted_tables:
#   print(t.name)
# for c in user.primary_key:
#    print(c)
# print (user.metadata)
# print (user.bind)
# users2.create(engine); users2.drop(engine); metadata.create_all(engine); user.c.id.primary_key

Base = declarative_base()
class User(Base):
    __tablename__='users3'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s','%s"')>'%(self.name, self.fullname, self.password)

User.__table__
Base.metadata.create_all(engine)
user2 = User('name','full','no')
user3 = User('name2','full2','no2')
db_session.add(user2)
db_session.add_all
bel = db_session.query(User).filter_by(name='name2')
db_session.commit()
str(users3.id)
print(bel)
