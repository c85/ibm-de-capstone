# Import libraries required for connecting to mysql
import mysql.connector
# Import libraries required for connecting to DB2
import ibm_db
# Connect to MySQL
# connect to database
connection = mysql.connector.connect(user='root', password='MjQ3MDgtY2NtYXJ0',host='127.0.0.1',database='sales')
# create cursor
cursor = connection.cursor()
# Connect to DB2
# connectction details
dsn_hostname = "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "abc12345"        # e.g. "abc12345"
dsn_pwd = "7dBZ3wWt9XN6$o0J"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_port = "50000"                # e.g. "50000" 
dsn_database = "BLUDB"            # i.e. "BLUDB"
dsn_driver = "{IBM DB2 ODBC DRIVER}" # i.e. "{IBM DB2 ODBC DRIVER}"           
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"              # i.e. "SSL"
# connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)
# create connection
conn = ibm_db.connect(dsn, "", "")
print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

# Find out the last rowid from DB2 data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database.

def get_last_rowid():
    DB2_SQL="SELECT max(rowid) FROM sales_data"
    stmt = ibm_db.exec_immediate(conn, DB2_SQL)
    while ibm_db.fetch_row(stmt) != False:
        return ibm_db.result(stmt, 0)

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

import datetime
new_records_list = []

def get_latest_records(rowid):
    MYSQL=f"SELECT *, 0 as price, " + "'" + "".join(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))) + "'" + f" from sales_data where rowid > {rowid}"
    cursor.execute(MYSQL)
    for row in cursor.fetchall():
        new_records_list.append(row)
    return new_records_list

new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database.

def insert_records():
    # Insert data into DB2
    for i in new_records:
        DB2_SQL = f"INSERT INTO sales_data VALUES{i};"
        stmt = ibm_db.prepare(conn, DB2_SQL)
        ibm_db.execute(stmt)

insert_records()
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
connection.close()
# disconnect from DB2 data warehouse
ibm_db.close(conn)
# End of program
print("End of program")