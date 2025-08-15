import oracledb as orc

con=orc.connect('system/8767843199@localhost/FREE')

conn=con.cursor()
print('orcle db connect succeffuly')