import sqlite3
connect=sqlite3.connect('sql.db')
c=connect.cursor()
sql='''
    create table company
    (id int primary key not null,
    name text not null,
    age int not null,
    address char(50),
    salry real);
'''
c.execute(sql)
connect.commit()