import sqlite3


def drop_table(input_path, table_name):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    curs.execute("DROP TABLE table_name;")
    conn.commit()


def task_1(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    curs.execute("CREATE TABLE shops (id int PRIMARY KEY, name varchar, \
       address varchar NULLABLE, staff_ammount int);")
    curs.execute("CREATE TABLE departments (id int PRIMARY KEY, sphere varchar, \
       staff_ammount int, shop int, FOREIGN KEY (shop) REFERENCES shops(id));")
    curs.execute("""CREATE TABLE items (id int PRIMARY KEY, name varchar,
         description TEXT NULLABLE, price int, department int,
         FOREIGN KEY (department) REFERENCES departments(id));""")
    conn.commit()


task_1("first.db")


def task_2(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    curs.execute("""INSERT INTO shops (id, name, address, staff_ammount)
       VALUES (1, 'Auchan', "", 250);""")
    curs.execute("""INSERT INTO shops (id, name, address, staff_ammount)
       VALUES (2, 'Ikea', 'Street Zirniu g. 56, Vilnius, Lithuania', 500);""")
    curs.execute("""INSERT INTO departments (id, sphere, staff_ammount, shop)
       VALUES (1, 'Furniture', 250, 1);""")
    curs.execute("""INSERT INTO departments (id, sphere, staff_ammount, shop)
       VALUES (2, 'Furniture', 300, 2);""")
    curs.execute("""INSERT INTO departments (id, sphere, staff_ammount, shop)
       VALUES (3, 'Dishes', 200, 2);""")
    curs.execute("""INSERT INTO items (id, name, description, price, department)
       VALUES (1, 'Table', 'Cheap wooden table', 300, 1);""")
    curs.execute("""INSERT INTO items (id, name, description, price, department)
       VALUES (2, 'Table', '', 750, 2);""")
    curs.execute("""INSERT INTO items (id, name, description, price, department)
       VALUES (3, 'Bed', 'Amazing wooden bed', 1200, 2);""")
    curs.execute("""INSERT INTO items (id, name, description, price, department)
       VALUES (4, 'Cup', '', 10, 3);""")
    curs.execute("""INSERT INTO items (id, name, description, price, department)
       VALUES (5, 'Plate', 'Glass Plate', 20, 3);""")
    conn.commit()


task_2("first.db")


def task_3(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    curs.execute("""SELECT * FROM items WHERE description <> ''""")
    print (curs.fetchall())
    curs.execute("""SELECT DISTINCT sphere FROM departments WHERE
        staff_ammount > 200""")
    print (curs.fetchall())
    curs.execute("""SELECT DISTINCT address FROM shops WHERE address
        LIKE 's%'""")
    print (curs.fetchall())
    curs.execute("""SELECT items.name FROM items, departments WHERE
        items.department = departments.id
        AND departments.sphere = 'Furniture'""")
    print (curs.fetchall())
    curs.execute("""SELECT DISTINCT shops.name FROM shops, departments,
        items WHERE items.department = departments.id
        AND departments.shop = shops.id AND items.description != ''""")
    print (curs.fetchall())
    curs.execute("""SELECT DISTINCT shops.name FROM shops
        INNER JOIN departments ON items.department = departments.id
        INNER JOIN items ON departments.shop = shops.id WHERE 
        items.description != ''""")
    print (curs.fetchall())


task_3("first.db")


def task_3f(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    for items_inf in curs.execute(""" SELECT * FROM items, departments,
    shops WHERE items.department = departments.id AND
     departments.shop = shops.id"""):
        print (str(items_inf[1]) + ' ' + str(items_inf[2]) +
               ' ' + str(items_inf[3]) + ' ' + 'Department_sphere ' +
               str(items_inf[6]) + ' Department_staff_amount ' +
               str(items_inf[7]) + ' ' + ' Shops_name ' +
               str(items_inf[10]) + ' Shops_address ' +
               str(items_inf[11]) + ' Shops_staff_amount ' +
               str(items_inf[12]))


task_3f("first.db")


def task_4(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    curs.execute('SELECT * FROM items')
    print (curs.fetchall())
    curs.execute("""DELETE FROM items where price > 500 AND
                description = ''""")
    curs.execute('SELECT * FROM items')
    print (curs.fetchall())
    # conn.commit()


task_4("first.db")


def task_5(input_path):
    conn = sqlite3.connect(input_path)
    curs = conn.cursor()
    # curs.execute("SELECT * FROM items")
    # print (curs.fetchall())
    curs.execute("""DELETE FROM items WHERE department = (SELECT id FROM
    departments WHERE shop = (SELECT id FROM shops WHERE address = ''))""")
    curs.execute("SELECT * FROM items")
    print (curs.fetchall())
    # conn.commit()


task_5("first.db")
