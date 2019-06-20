from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3
from venv.tcl.models_task10 import Shops, Departments, Items, Base


def task_1(sql_path):
    conn = sqlite3.connect(sql_path)
    curs = conn.cursor()
    curs.execute("SELECT * FROM items")
    print(curs.fetchall())
    curs.execute("""UPDATE items SET price = price + 100 WHERE name
                 LIKE '%e' OR name LIKE 'B%'""")
    curs.execute("SELECT * FROM items")
    print (curs.fetchall())


task_1("first.db")


class Task3(object):
    def __init__(self, sql_path):
        self.sql_path = sql_path
        engine = create_engine("sqlite:///"+sql_path, echo=True)
        Session = sessionmaker(bind=engine)
        self.engine = engine
        self.session = Session()

    def create_tables(self):
        # shops = Shops.__table__
        # departments = Departments.__table__
        # items = Items.__table__
        Base.metadata.create_all(self.engine)

    def insert_data_shops(self, name, address, staff_amount):
        new_shop = Shops(name, address, staff_amount)
        self.session.add(new_shop)
        self.session.commit()
        return self.session.query(Shops).all()

    def insert_data_deps(self, sphere, staff_amount, shops_id):
        new_dep = Departments(sphere, staff_amount, shops_id)
        self.session.add(new_dep)
        self.session.commit()

    def insert_data_items(self, name, description, price, department_id):
        new_item = Items(name, description, price, department_id)
        self.session.add(new_item)
        self.session.commit()

    def update_shop_descr(self, name1, description1):
        self.session.query(Shops).filter(Shops.name == name1).\
            update({Shops.name: description1})
        self.session.commit()

    def update_items_descr(self, price1, description1):
        self.session.query(Items).filter(Items.price == price1).\
            update({Items.description: description1})
        self.session.commit()

    def show_item_info(self, item):
        for instance in self.session.query(Items).\
                filter(Items.name == item).join(Departments).\
                join(Shops).order_by(Items.id):
            print(instance.id, instance.name, instance.department.sphere,
                  instance.department.shop.name)

    def delete_daata_item(self, table, item):
        for d in self.session.query(table).\
                 filter(table.id == item):
            del_item = d
            self.session.delete(del_item)
        self.session.commit()

    def delete_data_item(self, item):
        for d in self.session.query(Items).\
                 filter(Items.name == item):
            del_item = d
            self.session.delete(del_item)
        self.session.commit()

    def clear_data_Items(self):
        for i in self.session.query(Items):
            del_item = i
            self.session.delete(del_item)
        self.session.commit()

    def drop_table(self, table):
        table.__table__.drop(self.engine)

    def drop_all_tables(self):
        Base.metadata.drop_all(bind=self.engine)
