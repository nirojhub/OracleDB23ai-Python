import oracledb

conn = oracledb.connect(user="SYS", password="*****", dsn="localhost:1521/FREEPDB1", mode=oracledb.SYSDBA)
with conn.cursor() as cur:
   cur.execute("SELECT * FROM dual")
   res = cur.fetchall()
   print(res)