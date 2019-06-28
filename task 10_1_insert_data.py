from venv.tcl.task10_1 import Task3
from venv.tcl.models_task10 import Shops, Departments, Items


# drop table or all tables .
Task3('first.db').drop_table(Items)
Task3('first.db').drop_all_tables()
# create tables
Task3('first.db').create_tables()
# Clear data in table items
Task3('first.db').clear_data_Items()
# show info in Tables
for instance in Task3('first.db').session.query(Items). \
            filter(Items.name == 'Table'). \
            order_by(Items.id):
    print(instance.id, instance.name, instance.department.sphere,
          instance.department.shop.name)
Task3('first.db').show_item_info('Plate2')
# deleting info from tables
Task3('first.db').delete_daata_item(Items, 5)
Task3('first.db').delete_data_item('Plate2')
# get element for its number
x = Task3('first.db').session.query(Items).get(6)
x.name
del_item = Task3('first.db').session.query(Items).filter(Items.name == "Plate")
# change shop name in Shops
Task3('first.db').update_shop_descr('hj', 'Ikea')  # ('Ikea', 'hj')
# change item description in Items
Task3('first.db').update_items_descr(10, ' ')  # ('Ikea', 'hj')
# show content of tables
for instance in Task3('first.db').session.query(Shops).order_by(Shops.id):
    print(instance.id, instance.name, instance.address, instance.department)
for instance in Task3('first.db').session.query(Departments
                                                ).order_by(Departments.id):
    print(instance.id, instance.sphere, instance.shop.name)
for instance in Task3('first.db').session.query(Items).order_by(Items.id):
    print(instance.id, instance.name, instance.description, instance.price,
          instance.department_id)
# choose items which suit for parametres
for instance in Task3('first.db').session.query(Items).filter(
        Items.department_id == Departments.id).filter(
        Departments.shop_id == Shops.id).filter(
        Departments.sphere == 'Furniture').filter(
        Shops.name == 'Ikea').order_by(Items.id):
    print (instance.id, instance.name)
# Insert data in Tables
# Ins in Shop
Task3('first.db').insert_data_shops('Auchan', None, 250)
Task3('first.db').insert_data_shops('Ikea', 'Street Zirniu', 500)
# Ins in Dep
Task3('first.db').insert_data_deps('Furniture', 250, 1)
Task3('first.db').insert_data_deps('Furniture', 300, 2)
Task3('first.db').insert_data_deps('Dishes', 200, 2)
# Ins in Item
Task3('first.db').insert_data_items('Table', 'Cheap wooden table', 300, 1)
Task3('first.db').insert_data_items('Table', ' ', 750, 2)
Task3('first.db').insert_data_items('Bed', 'Amazing wooden bed', 1200, 2)
Task3('first.db').insert_data_items('Cup', ' ', 10, 3)
Task3('first.db').insert_data_items('Plate', 'Glass Plate', 20, 3)
Task3('first.db').insert_data_items('Plate2', 'fukk Plate', 120, 3)
# Session queries and commits
Task3('first.db').session.add()
Task3('first.db').session.commit()
Task3('first.db').session.query(Shops).all()
Task3('first.db').session.query(Departments).all()
Task3('first.db').session.query(Items).all()
#create session for making operations
session = Task3('first.db').session
session.query(Shops).filter(Shops.name == "Ikea").\
    update({Shops.name: "Ikea_new"})
session.commit()

