import sqlite3
import pandas as pd
conn = sqlite3.connect(r'E:\scanner\Eastside Fire Alerts\data\data.sqlite3')

cursor = conn.cursor()
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, conn)
        print(table.to_markdown())