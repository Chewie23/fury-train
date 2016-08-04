"""
Testing out sqlite3
"""
import sqlite3

sql_db = 'test.sqlite'

#defining name of tables and column
table_1 = 'my_table_1'
table_2 = 'my_table_2'

new_field = 'my_1st_column'
field_type = 'INTEGER'

#connecting to db
conn = sqlite3.connect(sql_db)
c = conn.cursor()

#creating a table with 1 column, as integer type
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_1, nf=new_field, ft=field_type))

conn.commit() #This is to make sure that all changes stick
conn.close() #This is to ensure it gets closed out

