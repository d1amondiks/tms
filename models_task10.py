from sqlalchemy import Column, Integer, String, \
     ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Shops(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    staff_amount = Column(Integer)
    department = relationship("Departments", backref='shop')

    def __init__(self, name, address, staff_amount):
        self.name = name
        self.address = address
        self.staff_amount = staff_amount

    def __repr__(self):
        return "<Shops('%s','%s','%s')>" % (self.name,
                                            self.address, self.staff_amount)


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    sphere = Column(String)
    staff_amount = Column(Integer)
    shop_id = Column(String, ForeignKey('shops.id'))
    item = relationship("Items", backref='department')

    def __init__(self, sphere, staff_amount, shops_id):
        self.sphere = sphere
        self.staff_amount = staff_amount
        self.shop_id = shops_id

    def __repr__(self):
        return "<Departments('%s','%s','%s')>" % (self.sphere,
                                                  self.staff_amount,
                                                  self.shop_id)


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)
    price = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))

    def __init__(self, name, description, price, department_id):
        self.name = name
        self.description = description
        self.price = price
        self.department_id = department_id

    def __repr__(self):
        return "<Items('%s','%s','%s')>" % (self.name, self.description,
                                            self.price, self.department_id)
